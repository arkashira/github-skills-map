**breakeven.md**  
*Unit economics & break‑even analysis for **github‑skills‑map** (visual GitHub activity/skill profiles)*  

---  

## 1. Cost per Active User (CPU + Storage + Bandwidth)

| Cost Component | Assumptions (per active user / month) | USD / mo |
|----------------|----------------------------------------|----------|
| **Compute** (AWS Fargate / Cloud Run) | • 2 vCPU‑hours for nightly data pull & graph generation  <br>• 0.5 vCPU‑hour for on‑demand API calls | **$2.40** ( $0.12 per vCPU‑hour ) |
| **Storage** (S3 / Cloud‑SQL) | • 50 MB raw GitHub JSON + 10 MB generated SVG/PNG <br>• 60 MB @ $0.023/GB‑mo | **$0.0014** |
| **Bandwidth** (CDN egress) | • 5 MB image delivery + 2 MB API responses ≈ 7 MB <br>• $0.09 per GB | **$0.0006** |
| **Third‑party API** (GitHub GraphQL) | 10 k API calls @ free tier → $0 (within free quota) | **$0.00** |
| **Total Variable Cost / Active User** |  | **≈ $2.40** |

*Rounded to $2.50 per active user to include minor overhead (logging, monitoring).*

---

## 2. Pricing Tiers  

| Tier | Monthly Price (USD) | Core Features | Estimated % of Users |
|------|---------------------|----------------|----------------------|
| **Free** | $0 | • Auto‑import last 30 days <br>• Basic skill tag cloud <br>• Public profile link | 55 % |
| **Pro** | **$9** | • Full 90‑day history <br>• Customizable visual themes <br>• Private profile & embed code <br>• Export PDF/PNG <br>• Email support | 35 % |
| **Team** | **$29** | • Unlimited history & multi‑repo aggregation <br>• Team dashboard & skill heat‑map <br>• SSO / org‑wide permissions <br>• Priority support & SLA <br>• API access for internal tools | 10 % |

*Pricing is positioned slightly below competing “portfolio” tools (e.g., Codemap, GitProfile) to encourage rapid adoption.*

---

## 3. Customer Acquisition Cost (CAC)

| Channel | Cost per Acquisition | Reasoning |
|---------|----------------------|-----------|
| **Content / SEO** (blog, dev‑talks) | $15 – $30 | Low spend, high organic conversion |
| **Paid Social (Twitter/LinkedIn)** | $40 – $60 | Targeted dev ads, 2–3 % CTR |
| **Developer Conferences / Sponsorship** | $70 – $100 | Booth + swag, high‑touch leads |
| **Referral / Affiliate** | $10 – $20 | 10 % referral bonus, low overhead |

**Overall CAC range:** **$20 – $70** (weighted average ≈ $45).  

---

## 4. Lifetime Value (LTV)

Assumptions:  

* Average churn = 5 % per month (typical SaaS for dev tools).  
* Average revenue per paying user (ARPPU) = weighted by tier mix:  

\[
ARPPU = 0.35 \times 9 + 0.10 \times 29 = 3.15 + 2.9 = **$6.05** / mo
\]

* Customer lifetime (in months) = 1 / churn = 20 months.  

\[
LTV = ARPPU \times Lifetime = 6.05 \times 20 = **$121** 
\]

*Subtract CAC to get net LTV:*  

\[
Net\;LTV = 121 - 45 \approx **$76**
\]

Thus each acquired paying user contributes ~\$76 profit over its lifetime.

---

## 5. Break‑Even Users Count  

Break‑even occurs when **Monthly Gross Profit ≥ Fixed Operating Costs**.  

| Item | Monthly Cost |
|------|--------------|
| **Core infra (fixed)** (Fargate base, DB instance, CDN) | $1,200 |
| **Team salaries (1 dev, 0.5 PM, 0.2 QA)** (pro‑rated) | $8,000 |
| **General & admin (office, tools, legal)** | $1,800 |
| **Total Fixed OPEX** | **$11,000** |

### Variable profit per active user  

*Free users generate $0 revenue, $2.5 cost → **‑$2.5** loss each.  
*Paying users (average $6.05 revenue) → profit = $6.05 – $2.5 = **$3.55** per paying user.  

Let **Uₚ** = number of paying users, **U_f** = free users.  
Total active users = Uₚ + U_f.  

Assume typical mix (55 % free, 45 % paying).  

\[
U_f = 0.55 \times U_{total} \\
U_p = 0.45 \times U_{total}
\]

Monthly contribution margin:  

\[
CM = U_p \times 3.55 \;-\; U_f \times 2.5
\]

Set **CM = Fixed OPEX ($11,000)** and solve for **U_total**.

\[
CM = 0.45U_{tot}\times3.55 \;-\;0.55U_{tot}\times2.5 \\
CM = U_{tot}\,(1.5975 - 1.375) = U_{tot}\times0.2225
\]

\[
U_{tot} = \frac{11,000}{0.2225} \approx 49,438 \text{ active users}
\]

**Break‑even active users ≈ 50 k** (≈ 22.5 k paying users, 27.5 k free).  

If we can shift the free‑to‑pay ratio to 70 % paying (e.g., via aggressive conversion), break‑even drops to ~30 k active users.

---

## 6. Path to **$10 K MRR**

Target MRR = $10,000.  

Revenue per tier (assuming the same mix as above):  

*Pro users (35 % of total) → $9 each*  
*Team users (10 % of total) → $29 each*  

Let **N** = total paying users.  

\[
Revenue = 0.35N \times 9 + 0.10N \times 29 = 3.15N + 2.9N = 6.05N
\]

\[
6.05N = 10,000 \;\Rightarrow\; N \approx 1,653 \text{ paying users}
\]

Breakdown:  

| Tier | Users needed | Monthly Rev |
|------|--------------|-------------|
| **Pro** | 1,653 × 0.35 ≈ **579** | 579 × $9 = $5,211 |
| **Team** | 1,653 × 0.10 ≈ **165** | 165 × $29 = $4,785 |
| **Free** (support) | – | – |
| **Total MRR** | – | **$9,996** (≈ $10 K) |

**Thus, ~1.7 k paying users (≈ 4 k total active users with 55 % free) yields $10 K MRR.**  

If conversion improves to 45 % paying, the required active base falls to ~3.8 k users.

---  

### Quick Takeaways  

* Variable cost per active user is low ($2.5), giving a healthy margin on paying tiers ($3.55 profit per paying user).  
* CAC (~$45) is comfortably covered by the net LTV ($76).  
* Break‑even requires ~50 k active users under current free‑to‑pay split; aggressive conversion or upsell to Team tier can halve that number.  
* Reaching $10 K MRR is realistic after acquiring ~1.7 k paying users – a feasible target within 3–6 months of launch with focused content/SEO + developer‑community outreach.  