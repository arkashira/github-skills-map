## Customer Segments
- **Freelance developers (Thailand & APAC)**: 1.2M+ targetable individuals on Upwork/Fiverr; need to differentiate in competitive markets (THB 300–1,500/hr = USD 8–40/hr)
- **Junior-to-mid career engineers (global)**: 4.7M GitHub-active devs with <5 yrs experience seeking job mobility; lack credible skill proof beyond resumes
- **DevRel & community leads (tech firms)**: Teams at startups and mid-tier SaaS companies needing engagement metrics for open-source contributors (budget: THB 120K–600K/yr = USD 3.3K–16.5K/yr)
- **Recruiters in high-velocity tech hubs (Bangkok, Ho Chi Minh, Manila)**: 8,400+ technical hiring managers needing faster signal on candidate activity; current tools are static or outdated

## Value Propositions
- **Auto-generated, real-time skill graphs** from actual GitHub commit history — no manual input required (saves 3–5 hrs/month per dev)
- **Thai-localized export & sharing** for freelancers targeting local and global clients (supports THB-denominated freelance economy)
- **Time-bound activity scoring (30/90/180-day)** to highlight recent relevance — critical for contract roles
- **Embeddable widgets** for portfolios, LinkedIn, personal sites — increases visibility and trust
- **Privacy-first architecture**: On-device analysis option; no persistent storage of credentials or tokens

## Channels
- **GitHub Marketplace integration** — direct install flow; estimated 220K+ monthly visitors (conversion target: 0.8% → 1,760 MAU)
- **Organic SEO + dev.to/Reddit content** — targeting keywords: “show GitHub activity”, “visualize coding skills”, “dev portfolio tool” (est. 40K/mo search volume)
- **Partnerships with Thai coding bootcamps (e.g., DePaul, SunSprint)** — bundled onboarding for grads (reach: 1,200 devs/quarter)
- **API-to-API integration with Fiverr/Upwork via webhook sync** — auto-update profiles when new repos are active (potential 14% conversion lift)

## Customer Relationships
- **Self-serve onboarding** with instant GitHub OAuth → skill map generation (<60 sec flow)
- **Automated weekly digest emails** with updated skill trends and comparison benchmarks (open rate goal: 42%)
- **Community Discord + Thai-language Telegram support group** — moderation by AI agent + human-in-the-loop (target CSAT: 4.6/5)
- **Pro-tier concierge setup** for teams and recruiters (response SLA: <2 hrs during Bangkok business hours)

## Revenue Streams
- **Freemium model**: Free tier (public repos only, 90-day history); Pro at **$5/mo (THB 182)** with private repo support, extended history, team views (target ARPU: $4.20)
- **Team plans**: $15/mo for 5 seats (THB 546) — used by bootcamps, dev shops, remote teams
- **Enterprise API access**: $99/mo (THB 3,600) — for HR platforms and DevRel tools ingesting skill data at scale
- **Affiliate referrals to job boards** (WeWorkRemotely, RemoteOK): $1.50 per qualified click (est. 5% conversion to paid job post)
- **White-label version for universities/bootcamps**: $299/yr (THB 10,900) — includes branding and cohort analytics

## Key Resources
- **GitHub OAuth-integrated backend** with rate limit optimization and caching layer
- **Skill inference engine** trained on 7.8M+ code-instruct pairs (from auto & instr-resp datasets) to map commits to competencies
- **Vectorized user profiles in pgvector** — enables similarity search, trend detection, and anti-duplication logic
- **Thai-English bilingual UI/UX assets** — supports localization without translation lag
- **Live queue in shared BRAIN** — prioritizes users based on engagement signals and market demand

## Key Activities
- **Daily sync of GitHub event streams** across 100K+ seed users to detect skill drift and emergence
- **Model retraining weekly** using new code-activity pairs to maintain accuracy of skill tagging
- **A/B testing UI variants** for shareability (CTA placement, color, export formats)
- **GDPR/CCPA-compliant data handling audits** — monthly automated scans + third-party review
- **Outreach to Thai tech communities** via co-hosted hackathons and visibility challenges

## Key Partners
- **GitHub Education Partner Program** — access to student data and co-marketing
- **Thai Digital Economy Promotion Agency (DEPA)** — grants, validation, and local credibility
- **Bootcamps (SunSprint, DePaul, CodingTH)** — distribution and feedback loop for early adopters
- **Fiverr/Upwork API programs** — official integration status increases trust and usage
- **Cloudflare & Vercel** — edge deployment for low-latency map rendering globally

## Cost Structure
- **Infrastructure**: $320/mo (THB 11,700) — includes Vercel Pro, Supabase, Redis, and vector DB hosting
- **AI inference**: $180/mo (THB 6,600) — fine-tuned embedding models for skill classification
- **Data licensing**: $0 (apache-2.0, cdla) — all training data is permissively licensed
- **Support & moderation**: $400/mo (THB 14,600) — hybrid AI + part-time Thai-speaking agent
- **Marketing & SEO tools**: $150/mo (THB 5,500) — Ahrefs, Grammarly, Canva Pro, Buffer
- **Total estimated burn**: **$1,050/mo (THB 38,400)** — breakeven at 210 Pro users