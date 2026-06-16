# STORIES.md
**Project:** github-skills-map  
**Owner:** Axentx Product Team  
**Target Release:** MVP (v0.1) → Full Release (v1.0)  

---  

## Table of Contents
1. [Epics Overview](#epics-overview)  
2. [User Story Backlog](#user-story-backlog)  
   - [Epic 1 – Data Ingestion & Normalisation](#epic-1)  
   - [Epic 2 – Skill Extraction & Scoring](#epic-2)  
   - [Epic 3 – Visualisation & UI](#epic-3)  
   - [Epic 4 – Sharing & Collaboration](#epic-4)  
   - [Epic 5 – Admin & Ops](#epic-5)  
3. [Definition of Done (DoD)](#definition-of-done)  

---  

## Epics Overview
| Epic ID | Title | Description | MVP Priority |
|---------|-------|-------------|--------------|
| **E1** | Data Ingestion & Normalisation | Pull public GitHub activity for a target user, store it in a canonical schema, and keep it up‑to‑date. | High |
| **E2** | Skill Extraction & Scoring | Analyse commits, PRs, issues, and repository metadata to infer programming languages, frameworks, and tooling proficiency scores. | High |
| **E3** | Visualisation & UI | Render an interactive, exportable skill map (graph/tree) that developers can explore and filter. | High |
| **E4** | Sharing & Collaboration | Enable users to share their skill map via a link or embed, and allow peer‑review comments. | Medium |
| **E5** | Admin & Ops | Provide monitoring, rate‑limit handling, and a simple admin dashboard for health checks. | Low |

---  

## User Story Backlog  

### Epic 1 – Data Ingestion & Normalisation  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E1‑US1** | **As a** developer, **I want** to connect my GitHub account via OAuth, **so that** the platform can securely access my public activity. | 1. OAuth flow uses GitHub’s official endpoint.<br>2. User grants `read:user` and `repo` scopes.<br>3. Access token is stored encrypted (AES‑256) and never logged.<br>4. Successful connection shows a “Connected” badge. |
| **E1‑US2** | **As a** system, **I want** to fetch the last 90 days of commits, PRs, and issues for the connected user, **so that** we have a recent activity window. | 1. API calls respect GitHub rate limits (5000 req/hr per token).<br>2. Data is stored in a `github_events` table with fields: `event_id`, `type`, `repo`, `timestamp`, `payload`.<br>3. Duplicate events are deduplicated on `event_id`. |
| **E1‑US3** | **As a** developer, **I want** the platform to refresh my data automatically every 24 h, **so that** my skill map stays current. | 1. Background job runs nightly (configurable).<br>2. New events are appended; old events older than 90 d are purged.<br>3. Job logs success/failure and notifies the user on failure via email. |
| **E1‑US4** | **As a** product owner, **I want** a unified JSON schema for all GitHub event types, **so that** downstream services can rely on a stable contract. | 1. Schema documented in `docs/schema/github_event.json`.<br>2. All ingestion code validates against the schema (using JSON‑Schema validator).<br>3. Invalid payloads are logged and discarded, not stored. |

### Epic 2 – Skill Extraction & Scoring  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E2‑US1** | **As a** developer, **I want** the system to infer the programming languages I use most, **so that** my skill map reflects my primary expertise. | 1. Language detection uses file extensions and GitHub’s `language` field.<br>2. Top 5 languages are displayed with a usage percentage (based on lines changed). |
| **E2‑US2** | **As a** system, **I want** to calculate a proficiency score per language (0‑100), **so that** the visual map can size nodes proportionally. | 1. Score = weighted sum of commits, PRs, and code review activity (weights configurable).<br>2. Scores are normalised across the user’s language set. |
| **E2‑US3** | **As a** developer, **I want** the platform to surface framework/tool tags (e.g., React, Docker), **so that** my broader skill set is visible. | 1. Tags are extracted from `package.json`, `requirements.txt`, Dockerfiles, and CI config files.<br>2. Each tag receives a confidence score (≥ 0.7 to be shown). |
| **E2‑US4** | **As a** product analyst, **I want** an exportable CSV of raw skill metrics, **so that** I can run external analyses. | 1. CSV includes columns: `language`, `score`, `commits`, `prs`, `reviews`, `tags`.<br>2. Export respects the user’s consent (opt‑in flag). |

### Epic 3 – Visualisation & UI  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E3‑US1** | **As a** developer, **I want** an interactive graph where each node is a language/tool, **so that** I can explore my skill landscape. | 1. Graph rendered with D3.js (or equivalent) and is responsive.<br>2. Node size = proficiency score; node colour = primary/secondary skill.<br>3. Hover shows tooltip with detailed metrics. |
| **E3‑US2** | **As a** developer, **I want** to filter the view by time range (30 d, 60 d, 90 d), **so that** I can see recent vs. long‑term trends. | 1. Filter control updates the underlying dataset without page reload.<br>2. URL reflects filter state (`?range=30`). |
| **E3‑US3** | **As a** developer, **I want** to download the skill map as an SVG/PNG, **so that** I can embed it in my résumé or portfolio. | 1. Export button triggers client‑side rendering to SVG and PNG.<br>2. Files are named `github-skills-<username>-<date>.svg`. |
| **E3‑US4** | **As a** accessibility advocate, **I want** the UI to meet WCAG 2.1 AA standards, **so that** all users can use the tool. | 1. Contrast ratio ≥ 4.5:1 for text.<br>2. Keyboard navigation works for all interactive elements.<br>3. ARIA labels present on graph nodes. |

### Epic 4 – Sharing & Collaboration  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E4‑US1** | **As a** developer, **I want** a shareable public link to my skill map, **so that** I can showcase it without exposing my GitHub token. | 1. Link is of the form `https://skills.axentx.com/u/<hash>`.<br>2. Public view is read‑only; no personal data other than the map is exposed.<br>3. Link expires after 30 days unless renewed. |
| **E4‑US2** | **As a** reviewer, **I want** to leave a comment on a shared skill map, **so that** I can give feedback to the owner. | 1. Comment thread appears below the map.<br>2. Commenter must sign‑in with GitHub (OAuth) to post.<br>3. Owner receives email notification of new comments. |
| **E4‑US3** | **As a** developer, **I want** an embed snippet (iframe) for my skill map, **so that** I can place it on personal sites or blogs. | 1. Snippet includes a CSP‑safe iframe URL.<br>2. Height/width are configurable via query parameters. |
| **E4‑US4** | **As a** product manager, **I want** analytics on shared link clicks, **so that** we can measure outreach impact. | 1. Each click increments a counter stored in `share_metrics`.<br>2. Dashboard shows total clicks, unique visitors, and conversion to sign‑ups. |

### Epic 5 – Admin & Ops  

| # | User Story | Acceptance Criteria |
|---|------------|----------------------|
| **E5‑US1** | **As a** system admin, **I want** health‑check endpoints (`/healthz`, `/readyz`), **so that** orchestration tools can monitor service status. | 1. `/healthz` returns 200 if DB and GitHub API client are reachable.<br>2. `/readyz` returns 200 only when background workers are running. |
| **E5‑US2** | **As a** ops engineer, **I want** rate‑limit awareness (GitHub API), **so that** the platform degrades gracefully when limits are hit. | 1. When `X-RateLimit-Remaining` ≤ 100, system backs off with exponential delay.<br>2. Users see a non‑intrusive banner “Data refresh delayed due to GitHub rate limits”. |
| **E5‑US3** | **As a** security officer, **I want** all stored tokens to be encrypted at rest and rotated every 90 days, **so that** we meet compliance. | 1. Tokens encrypted with a KMS‑managed key.<br>2. Scheduler triggers rotation workflow; old tokens are revoked via GitHub API. |
| **E5‑US4** | **As a** product owner, **I want** a simple admin UI to view active users, ingestion job status, and error logs, **so that** we can troubleshoot quickly. | 1. UI lists users with last sync timestamp.<br>2. Job status shows “Success”, “Failed”, or “Running”.<br>3. Clicking an error opens the stack trace with a “Retry” button. |

---  

## Definition of Done (DoD)
- Code written in TypeScript (frontend) & Python (backend) with linting passed.  
- Unit tests ≥ 80 % coverage for new modules; integration tests for each API endpoint.  
- All acceptance criteria verified in the sprint review.  
- Documentation updated (`README.md`, API spec, schema files).  
- Docker images built and pushed to the internal registry with version tags.  
- Deployed to staging; smoke‑tested by QA.  

---  

*End of STORIES.md*
