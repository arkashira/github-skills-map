# TECH_SPEC.md
**Project:** github‑skills‑map  
**Owner:** Axentx – Product Engineering  
**Status:** Draft (ready for engineering kickoff)  
**Last Updated:** 2026‑06‑16  

---  

## 1. Overview  

**github‑skills‑map** is a SaaS platform that visualizes a developer’s recent coding activity and inferred skill set by ingesting public (or authorized private) GitHub data. The service produces an interactive, share‑able “skill map” that can be embedded in resumes, portfolios, or team dashboards.  

Key business goals:  

| Goal | Metric | Target |
|------|--------|--------|
| Validate demand | % of sign‑ups that generate a map | ≥ 30 % within 30 days |
| Monetize | Paid conversions (Pro tier) | ≥ 5 % of free users |
| Retention | Monthly active users (MAU) | ≥ 10 k after 6 mo |

The product must be **privacy‑first**, **scalable**, and **extensible** to support future data sources (e.g., GitLab, Bitbucket).

---  

## 2. Architecture Overview  

```
+-------------------+        +-------------------+        +-------------------+
|   Front‑End SPA   |  HTTPS |   API Gateway     |  gRPC  |   Workers (Kafka)|
| (React + Vite)    | <----> | (FastAPI + Auth) | <----> | (Python, Celery) |
+-------------------+        +-------------------+        +-------------------+
          |                           |                         |
          |                           |                         |
          v                           v                         v
+-------------------+        +-------------------+        +-------------------+
|   CDN (Static)    |        |   PostgreSQL      |        |   Redis Cache     |
| (Cloudflare)      |        |   (TimescaleDB)   |        | (Session/Rate‑lim)|
+-------------------+        +-------------------+        +-------------------+
          |                           |
          v                           v
+-------------------+        +-------------------+
|   Object Store    |        |   GitHub API      |
| (AWS S3 / GCS)    |        | (OAuth2)          |
+-------------------+        +-------------------+
```

* **Front‑End SPA** – React app compiled with Vite, served via CDN.  
* **API Gateway** – FastAPI (Python 3.11) handling REST/GraphQL, JWT auth, rate‑limiting.  
* **Workers** – Celery + RabbitMQ (or Kafka) for asynchronous data collection & skill inference.  
* **Data Store** – PostgreSQL with TimescaleDB extension for time‑series activity logs.  
* **Cache** – Redis for session storage, token revocation lists, and hot skill‑map fragments.  
* **Object Store** – S3‑compatible bucket for generated SVG/PNG maps and user‑uploaded assets.  

All components are containerized (Docker) and orchestrated via Kubernetes (Helm charts provided).  

---  

## 3. Core Components  

| Component | Responsibility | Tech |
|-----------|----------------|------|
| **Web UI** | Interactive map editor, auth flow, dashboard | React, TypeScript, D3.js, TailwindCSS |
| **Auth Service** | OAuth2 with GitHub, optional email/password, JWT issuance | FastAPI, PyJWT, OAuthLib |
| **Ingestion Service** | Pull repos, commits, PRs, issues; store raw events | Celery, GitHub GraphQL API, aiohttp |
| **Skill Engine** | Transform activity → skill scores (language, framework, CI/CD, testing) | Python, scikit‑learn, spaCy, custom TF‑IDF, embeddings (sentence‑transformers) |
| **Map Renderer** | Generate SVG/PNG + interactive D3 graph | Node.js (puppeteer) for server‑side rendering, D3.js client fallback |
| **Analytics** | Track usage, conversion funnels, A/B tests | Postgres, Metabase (optional) |
| **Billing** | Stripe integration for Pro tier | Stripe SDK, FastAPI endpoints |

---  

## 4. Data Model  

### 4.1 Relational Schema (PostgreSQL)

| Table | Columns | Description |
|-------|---------|-------------|
| `users` | `id PK`, `github_id`, `email`, `name`, `avatar_url`, `plan` (free/pro), `created_at`, `last_login` | Core user profile |
| `github_tokens` | `user_id FK`, `access_token`, `refresh_token`, `expires_at` | OAuth tokens (encrypted) |
| `repos` | `id PK`, `user_id FK`, `repo_id`, `name`, `private`, `fork`, `language`, `created_at` | Tracked repositories |
| `events` | `id PK`, `repo_id FK`, `type` (commit, pr, issue), `payload JSONB`, `event_ts TIMESTAMP` | Raw GitHub events |
| `skill_scores` | `user_id FK`, `skill` (enum), `score FLOAT`, `last_updated` | Normalized skill values (0‑100) |
| `maps` | `id PK`, `user_id FK`, `format` (svg/png), `url`, `generated_at` | Generated map assets |
| `billing` | `user_id FK`, `stripe_customer_id`, `plan`, `status`, `renewal_date` | Subscription data |

### 4.2 Time‑Series (TimescaleDB)

* Hypertable `activity_series` (`user_id`, `metric`, `value`, `ts`) – used for trend charts (e.g., commits per week).

### 4.3 Cache Keys (Redis)

* `session:{session_id}` → JWT payload (TTL 24h)  
* `rate:{user_id}:{endpoint}` → counter (sliding window)  
* `map:preview:{user_id}` → pre‑rendered SVG (TTL 5 min)

---  

## 5. Key APIs / Interfaces  

All public endpoints are versioned under `/api/v1`.  

### 5.1 Authentication  

| Method | Endpoint | Request | Response |
|--------|----------|---------|----------|
| `GET` | `/auth/github/login` | – | Redirect to GitHub OAuth |
| `GET` | `/auth/github/callback` | `code` query | JWT + refresh token (HTTP‑only cookie) |
| `POST` | `/auth/refresh` | `{refresh_token}` | New JWT |
| `POST` | `/auth/logout` | – | 200 (clears cookies) |

### 5.2 Repository Management  

| Method | Endpoint | Request | Response |
|--------|----------|---------|----------|
| `GET` | `/repos` | – | List of tracked repos |
| `POST` | `/repos` | `{repo_id}` | 202 (ingestion queued) |
| `DELETE` | `/repos/{repo_id}` | – | 204 |

### 5.3 Skill Map  

| Method | Endpoint | Request | Response |
|--------|----------|---------|----------|
| `GET` | `/maps/{user_id}` | – | `{url, format, generated_at}` |
| `POST` | `/maps/generate` | `{options}` | 202 (job id) |
| `GET` | `/maps/job/{job_id}` | – | `{status, result_url}` |

### 5.4 Billing (Pro tier)  

| Method | Endpoint | Request | Response |
|--------|----------|---------|----------|
| `GET` | `/billing/plan` | – | Current plan |
| `POST` | `/billing/checkout` | `{plan_id, payment_method}` | Stripe session URL |
| `POST` | `/billing/webhook` | Stripe event | – (internal) |

### 5.5 Internal Worker Queue  

* **Queue:** `github_ingest` – messages `{user_id, repo_id, since_ts}`  
* **Queue:** `skill_compute` – messages `{user_id}`  

---  

## 6. Technology Stack  

| Layer | Choice | Rationale |
|-------|--------|-----------|
| Front‑End | React 18 + TypeScript + Vite | Fast dev, tree‑shaking, modern ecosystem |
| UI Visualisation | D3.js (v7) + SVG | Precise control over graph layout |
| API Server | FastAPI (Python 3.11) | Async, auto‑generated OpenAPI, high performance |
| Async Workers | Celery 5 + RabbitMQ (or Kafka) | Proven pattern, easy scaling |
| Data Store | PostgreSQL 15 + TimescaleDB | Relational + time‑series, mature tooling |
| Cache | Redis 7 | Low‑latency session & rate‑limit |
| Object Storage | AWS S3 (or GCS) | Durable, CDN‑ready |
| Auth | OAuth2 (GitHub) + JWT | Standard, user‑controlled |
| CI/CD | GitHub Actions + Docker Buildx | Consistent with data source |
| Deployment | Kubernetes 1.28 (EKS / GKE) + Helm | Autoscaling, zero‑downtime upgrades |
| Monitoring | Prometheus + Grafana + Loki | Full observability |
| Logging | Structured JSON (Python `structlog`) | Easy correlation across services |
| Testing | Pytest (backend), Jest + React Testing Library (frontend) | High coverage, CI gate |

---  

## 7. Dependencies  

| Dependency | Version | License |
|------------|---------|---------|
| fastapi | 0.112.0 | MIT |
| uvicorn | 0.30.0 | BSD |
| celery | 5.4.0 | BSD |
| redis-py | 5.0.3 | MIT |
| sqlalchemy | 2.0.30 | MIT |
| psycopg2-binary | 2.9.9 | LGPL‑2.1 |
| timescaledb‑psycopg2 | 0.5.0 | PostgreSQL |
| d3 | 7.9.0 | BSD |
| react | 18.3.0 | MIT |
| tailwindcss | 3.4.0 | MIT |
| stripe | 9.12.0 | MIT |
| scikit‑learn | 1.5.0 | BSD |
| spacy | 3.7.4 | MIT |
| sentence‑transformers | 3.0.1 | Apache‑2.0 |
| puppeteer | 22.6.0 | Apache‑2.0 |

All third‑party libraries are vetted for compatibility with Axentx’s security policy.

---  

## 8. Deployment & Operations  

### 8.1 Container Images  

* **Base:** `python:3.11-slim` for API & workers.  
* **Frontend:** `node:20-alpine` → static assets copied to `nginx:alpine`.  

Images are built via GitHub Actions, scanned with Trivy, and pushed to the company ECR registry.

### 8.2 Helm Chart Structure  

```
github-skills-map/
├─ charts/
│  ├─ api/
│  ├─ worker/
│  ├─ frontend/
│  └─ redis/
├─ values.yaml
└─ Chart.yaml
```

Key values: replica counts, resource limits, autoscaling thresholds, external secrets (GitHub OAuth client secret, Stripe keys).

### 8.3 CI/CD Pipeline  

1. **PR Validation** – lint (ruff, eslint), unit tests, type checking (mypy, tsc).  
2. **Staging Deploy** – on merge to `main`; run integration tests against a staging namespace.  
3. **Canary Release** – 5 % traffic to new version; monitor error rate via Prometheus alerts.  
4. **Production Promote** – full rollout after success criteria.

### 8.4 Observability  

* **Metrics:** request latency, worker queue depth, skill‑engine runtime, map generation time.  
* **Alerts:** 5xx rate > 1 % for >5 min, Redis memory > 80 %, S3 upload failures.  
* **Logs:** centralized in Loki, correlated via `trace_id` (OpenTelemetry).  

### 8.5 Security  

* **OAuth scopes:** `read:user`, `repo` (read‑only).  
* **Secrets:** Managed via AWS Secrets Manager / GCP Secret Manager, injected as env vars.  
* **Data Privacy:** No code is stored; only metadata and aggregated skill scores. Users can revoke access via GitHub → Applications.  
* **Compliance:** GDPR‑ready – data export endpoint `/api/v1/users/{id}/export` and deletion `/delete`.  

---  

## 9. Milestones & Deliverables  

| Milestone | Scope | Duration | Owner |
|-----------|-------|----------|-------|
| **M1 – Foundations** | Repo ingestion pipeline, basic auth, DB schema | 3 wks | Backend Lead |
| **M2 – Skill Engine MVP** | TF‑IDF + language detection, store scores | 4 wks | ML Engineer |
| **M3 – Map Renderer** | Server‑side SVG generation, React D3 viewer | 3 wks | Frontend Lead |
| **M4 – Billing & Pro Tier** | Stripe integration, feature flag gating | 2 wks | Platform Engineer |
| **M5 – QA & Load Test** | End‑to‑end tests, 10k concurrent users simulation | 2 wks | QA Lead |
| **M6 – Public Beta Launch** | Deploy to prod, marketing site, analytics | 1 wk | PM |
| **M7 – Post‑Launch Iteration** | A/B UI tweaks, skill model refinement | Ongoing | Product Team |

---  

## 10. Risks & Mitigations  

| Risk | Impact | Mitigation |
|------|--------|------------|
| GitHub API rate limits (5k req/hr per token) | Ingestion delays for power users | Use conditional requests + ETag, batch queries, fallback to GitHub GraphQL pagination, request higher tier token for enterprise customers |
| Skill inference accuracy | Poor user perception → low conversion | Start with transparent heuristic model, collect user feedback, iterate with supervised fine‑tuning on a labeled subset |
| Data privacy concerns | Legal/regulatory fallout | Full audit logs, easy revocation, data‑minimization, GDPR/CCPA compliance checklist |
| Cost of map rendering at scale | Unexpected OPEX | Cache rendered maps, limit generation frequency, use serverless (AWS Lambda) for burst rendering |

---  

## 11. Glossary  

* **Skill Score** – Normalized 0‑100 value representing proficiency in a specific technology.  
* **Map Job** – Asynchronous task that produces the visual representation.  
* **Pro Tier** – Paid subscription unlocking higher refresh rates, private repo support, and exportable PDFs.  

---  

*Prepared by:* Senior Product/Engineering Lead – Axentx  
*Document ID:* TECH‑SPEC‑GSM‑2026‑06‑16
