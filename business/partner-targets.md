```markdown
# partner-targets.md

## Partner Integration Roadmap – github‑skills‑map

| # | SaaS / API | Free‑Tier Limits | Integration Effort | Value‑Add (User Job) | Revenue Potential | Notes |
|---|------------|------------------|--------------------|----------------------|-------------------|-------|
| 1 | **GitHub API (v4 GraphQL)** | 5,000 requests/day (unauthenticated) <br> 5,000,000 requests/month (authenticated) | **S** | *Track recent commits, PRs, issues, and repo stats* – core data source for skill mapping. | **N/A** (core platform) | Must be the first integration; required for all other data. |
| 2 | **GitHub Actions API** | 5,000 actions/month (free tier) | **M** | *Show CI/CD pipeline usage & skill depth* – demonstrates automation proficiency. | **Affiliate** – GitHub offers partner revenue share on Actions usage. | Adds depth to skill graph; requires OAuth scopes. |
| 3 | **CodeSignal API** | 1,000 API calls/month (free) | **M** | *Validate coding skill levels via challenges* – enrich skill scores with external benchmarks. | **Revenue‑share** – CodeSignal offers partner program for challenge integrations. | Requires user login to CodeSignal. |
| 4 | **LeetCode API (unofficial)** | 100 requests/day | **M** | *Show problem‑solving activity* – complements GitHub data for algorithmic skill assessment. | **Affiliate** – LeetCode offers partner links for premium plans. | Unofficial, monitor rate limits. |
| 5 | **LinkedIn API** | 10,000 requests/month (free) | **L** | *Auto‑populate profile & endorsements* – helps users showcase skills on professional network. | **Revenue‑share** – LinkedIn offers referral bonuses for new connections. | Requires OAuth 2.0; GDPR compliance. |
| 6 | **Stack Overflow API** | 10,000 requests/day | **M** | *Pull reputation & tags* – adds community engagement metrics to skill map. | **Affiliate** – Stack Overflow offers partner program for job referrals. | Align with SO’s terms; cache aggressively. |
| 7 | **Zapier Integration** | Unlimited free tier (limited tasks) | **S** | *Automate data sync & notifications* – users can trigger updates via Zapier workflows. | **Revenue‑share** – Zapier pays for each new paid user referred. | Low effort; high reach. |
| 8 | **Auth0 / Okta** | 7,000 active users/month (free) | **S** | *Single Sign‑On & user management* – simplifies onboarding for enterprise customers. | **N/A** – core security; no revenue share. | Must support SAML/OIDC. |

### Roadmap Prioritization

| Phase | Target Integrations | Rationale |
|-------|---------------------|-----------|
| **Q1 2026** | 1, 2, 7 | Core GitHub data + CI/CD visibility + low‑effort automation. |
| **Q2 2026** | 3, 4 | External skill validation & problem‑solving metrics; affiliate revenue streams. |
| **Q3 2026** | 5, 6 | Professional profile enrichment & community reputation; higher value for enterprise. |
| **Q4 2026** | 8 | Enterprise SSO for large teams; no direct revenue but essential for scaling. |

### Key Success Metrics

| Metric | Target |
|--------|--------|
| # of partner integrations live | 8 by Q4 2026 |
| Avg. new users per partner channel | 200/month |
| Revenue from affiliate/revenue‑share | 15% of total subscription revenue |
| Partner‑driven churn rate | <5% |

> **Note**: All integrations must adhere to each provider’s rate limits and data‑privacy policies. Prioritize OAuth scopes that minimize user friction while maximizing data richness.