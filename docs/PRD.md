# Product Requirements Document (PRD)  
**Project:** github-skills-map  
**Owner:** Senior Product/Engineering Lead – Axentx  
**Date:** 2026‑06‑16  

---  

## 1. Overview  

**github-skills-map** is a SaaS platform that transforms a developer’s public GitHub activity into an interactive, visual “skill map.” By mining commits, pull‑requests, issues, and repository metadata, the system infers proficiency levels across programming languages, frameworks, tooling, and domain concepts, then renders them as a dynamic, share‑able diagram.  

The product will be positioned as a **career‑development & hiring‑insight tool** for individual developers, recruiters, hiring managers, and engineering leaders. It will generate revenue through a tiered subscription model (individual, team, enterprise).  

---  

## 2. Problem Statement  

| Stakeholder | Pain Point | Why Existing Solutions Fail |
|-------------|------------|-----------------------------|
| **Developers** | Hard to showcase *real* coding expertise beyond a list of repos. | Résumé / LinkedIn only list projects; no quantitative skill visualization. |
| **Recruiters / Hiring Managers** | Time‑consuming manual review of GitHub profiles; difficulty comparing candidates objectively. | No standardized, visual representation of skill depth or recent activity. |
| **Engineering Leaders** | Need to understand skill distribution within their teams for staffing & up‑skilling. | Internal tools are ad‑hoc spreadsheets; lack of live, data‑driven view. |

**Result:** Missed hiring efficiency, under‑utilized developer branding, and limited data for talent development – all of which translate into measurable revenue loss for hiring platforms and talent agencies.

---  

## 3. Target Users  

| Segment | Primary Persona | Core Needs |
|---------|----------------|------------|
| **Individual Developers** | *“Alex, 2‑year senior front‑end engineer, wants to showcase growth to potential employers.”* | Easy, credible skill visualization; shareable link; privacy controls. |
| **Recruiters / Talent Agencies** | *“Mia, technical recruiter, screens 30+ candidates per week.”* | Rapid comparative skill snapshots; exportable PDFs; API for ATS integration. |
| **Engineering Managers / CTOs** | *“Ravi, engineering manager, plans team skill‑gap analysis.”* | Team‑wide dashboards; role‑based filters; export to internal reporting tools. |
| **Learning Platforms** | *“EduCo, an online bootcamp, wants to certify graduate skill levels.”* | Bulk onboarding, white‑label maps, API for automated certification. |

---  

## 4. Goals & Success Metrics  

| Goal | Success Metric | Target (12 mo) |
|------|----------------|----------------|
| **Validate market demand** | Paid trial conversion rate (free → paid) | ≥ 12 % |
| **Revenue generation** | Monthly Recurring Revenue (MRR) | $75 k |
| **User adoption** | Active users (MAU) | 5 k individual, 500 team accounts |
| **Product quality** | Net‑Promoter Score (NPS) | ≥ 45 |
| **Data accuracy** | Skill‑inference precision vs. manual audit | ≥ 85 % (F1‑score) |
| **Time‑to‑value** | Avg. time from GitHub auth to first map view | ≤ 30 seconds |

---  

## 5. Assumptions  

1. **GitHub public API** (or OAuth‑scoped private access) provides sufficient granularity (commit messages, file diffs, PR reviews) for skill inference.  
2. Developers are willing to link their GitHub accounts in exchange for a free visual résumé.  
3. The **auto**, **instr‑resp**, **messages**, and **system‑user‑assistant** datasets can be leveraged to train/finetune the skill‑inference model (e.g., code‑to‑concept mapping, natural‑language labeling).  
4. Compliance with GDPR, CCPA, and GitHub Terms of Service can be achieved with standard consent flows.  

---  

## 6. Constraints  

| Constraint | Detail |
|------------|--------|
| **Data privacy** | No storage of raw code longer than 30 days; only derived skill vectors retained. |
| **Performance** | Map generation ≤ 2 seconds for accounts with ≤ 10 k commits. |
| **Scalability** | Architecture must support 100 k concurrent users (auto‑scaling containers). |
| **Budget** | Initial MVP development capped at $120 k (incl. model training, UI, infra). |
| **Compliance** | Must pass a third‑party security audit before public launch. |

---  

## 7. Key Features  

Features are grouped into **MVP (Phase 1)** and **Phase 2**. Prioritization follows the **MoSCoW** method.

### 7.1 MVP (Launch within 4 months)

| Feature | Description | MoSCoW | Acceptance Criteria |
|---------|-------------|--------|----------------------|
| **GitHub OAuth onboarding** | Secure OAuth flow; user grants read‑only repo access. | Must | Users can connect/disconnect GitHub; token stored encrypted. |
| **Skill inference engine** | ML pipeline that maps commits/PRs → skill taxonomy (languages, frameworks, tools, concepts). | Must | ≥ 85 % precision on a held‑out audit set of 500 repos. |
| **Interactive skill map UI** |
