# Government use of Splink (probabilistic record linkage) on citizen data — sourced tracker

*Public-interest research. Every entry cited and tiered. Last updated: 2026-06-23 (v2 — rebuilt after a 14-target adversarial verification pass).*
*Publicly documented deployments only. No third-party systems accessed.*

> **What changed in v2:** the previous tracker over-counted. After an adversarial verification pass against primary sources, entries are now tiered by how much can actually be proven, several claims were **corrected or removed**, and confirmed negatives are stated plainly. Full write-up: `SPLINK-GLOBAL-MASTER-ANALYSIS.md`.
>
> **Corrections from v1:**
> - **US Defense Health Agency (200M records) — REMOVED.** Refuted 0-3; rested only on Splink's self-reported page and could not be corroborated. Do not cite.
> - **NHS England — DOWNGRADED.** Its *live* Master Person Service is **deterministic**; the Splink work is in development, not operational. Tier as research/development, not operational.
> - **Germany Destatis, EU EMA, Gambia census, UNHCR — flagged self-reported/asserted**, not independently verified.
> - **"Canada" is not monolithic:** Statistics Canada is a NEGATIVE (uses G-Link); *other* Canadian bodies (Ontario MCCSS, ECCC) are self-reported users.

## What Splink is
Open-source Python library for **probabilistic record linkage** (Fellegi–Sunter model), built and maintained by the **UK Ministry of Justice**. Links/dedupes records about the same person across datasets with no shared ID. ~3M+ downloads. The maths is sound; the issue is **governance of cross-domain person-level linkage** — consent, transparency, scope.

---

## TIER 1 — Independently proven, operational on real population data (3)

| Body | Country | What is done with the data | Source |
|---|---|---|---|
| **Ministry of Justice** | 🇬🇧 UK | Production linkage across courts/prisons/probation (DELIUS, NOMIS, Common Platform, LIBRA). Research arm (Data First) is de-identified, "not for operational decision-making." Operational arm (Splink Master Record): real-time Core Person Record, court sentencing-prep record retrieval, daily North Essex PNC→police arrest-check feed. | gov.uk ATR `moj-splink-master-record` (6 Oct 2025), `moj-data-first-splink` (17 Dec 2024); IJPDS 1794 |
| **Office for National Statistics** | 🇬🇧 UK | 2021 Census self-linkage (~58M records); Census↔DWP master key/encrypted NINo↔HMRC PAYE; Census→NHS PDS to assign NHS numbers (precision 99.95%). | ons.gov.uk Census-2021 linkage methodology pages; StatCan-hosted Splink census case study |
| **Australian Bureau of Statistics** | 🇦🇺 AU | 2025 Person Linkage Spine "constructed using Splink" — Medicare + Centrelink/DOMINO + Personal Income Tax. | abs.gov.au Person Linkage Spine; ISI WSC 2025 abstract |

## TIER 2 — Listed only on Splink's own "Used By" page (self-reported, unaudited) (5)
*Real linkage in most cases, but the Splink attribution and/or operational status is not independently verified. Cite as "per Splink's own Used-By page."*

| Body | Country | Note | Source |
|---|---|---|---|
| **Wider UK public sector** (DfE, CMA, Welsh Revenue Authority, OHID, Homes England [pilot], DBT [planned], councils: Lewisham/Leicestershire/Gateshead/Richmond/Wandsworth/Westmorland) | 🇬🇧 UK | Free-school-meals auto-enrolment, "single view of debt," SEND records, address matching. OHID/MoJ BOLD probation↔addiction linkage is the best-sourced (research). | Splink Used-By page; OHID/MoJ BOLD methodology |
| **NHS England** | 🇬🇧 UK | **Live spine is deterministic (MPS/Person_ID); Splink is in development.** Tier: research/dev. | nhsengland.github.io data-linkage-hub; IJPDS 3271 |
| **Ontario MCCSS · Environment & Climate Change Canada** | 🇨🇦 CA | MCCSS social-assistance↔health linkage is real but the peer-reviewed paper does not name Splink; ECCC rests on the page alone. | Splink Used-By page; IJPDS 1689 |
| **Destatis** | 🇩🇪 DE | Register-based census — one uncited line on Splink's homepage; no German source corroborates Splink specifically. | Splink homepage (Destatis line) |
| **European Medicines Agency** | 🇪🇺 EU | Veterinary adverse-event dedup — one uncited line; downgraded to ASSERTED. Low civil-liberties weight. | Splink homepage (EMA line) |
| **UNHCR** | 🌍 UN | Dataset dedup — listing only; UNHCR's public linkage code uses **fastLink**, not Splink. (Separate, verified harm: Rohingya data-sharing — but that was biometric, not Splink.) | Splink Used-By page; `unhcr-americas/record_linkage`; HRW (15 Jun 2021) |

## TIER 3 — Pilot / evaluation / research (6)

| Body | Country | Status | Source |
|---|---|---|---|
| **Indiana Dept of Health** | 🇺🇸 US | PILOT — synthetic febrl4 data; productionisation pending | in.gov PDF (29 May 2024) |
| **Florida Cancer Registry** | 🇺🇸 US | EVALUATION — simulated pseudopeople data | IJPDS 2786 |
| **AIHW** | 🇦🇺 AU | EVALUATION — production system is SAS "DALI"; Splink under consideration | ANU/AIHW placement page (2024) |
| **Lao PDR Shared Child Health Record** | 🇱🇦 LA | RESEARCH — methods study on real provincial pediatric records | J. Med. Syst. 49(1):119 (2025) |
| **Chile — Ministry of Health** | 🇨🇱 CL | RESEARCH — migrant immunisation↔school-enrolment linkage | IJPDS 2348 |
| **The Gambia — 2024 Census** | 🇬🇲 GM | ASSERTED — census is real; Splink role self-attested only (uncited) | Splink homepage (Gambia line); UNFPA Gambia census |

## TIER 4 — Confirmed NEGATIVES (Splink benchmarked & rejected, or never used)

| Body | Uses instead | Source |
|---|---|---|
| **US Census Bureau** | **BigMatch** (in-house) — evaluated Splink, found BigMatch superior | census.gov record-linkage |
| **NIH "All of Us"** | **Datavant** tokenisation / PPRL | PMC9645066 |
| **Statistics Canada** | **G-Link** (own system) | statcan.gc.ca 11-522-X |
| **Australian state/territory units** | WA **DLS3**, NSW CHeReL **ChoiceMaker**, SA-NT **FEBRL** | PMC7299493; PMC8142947 |

---

## The honest headline
- **Independently-verified operational Splink use: 3 bodies, 2 countries** (UK — MoJ + ONS; Australia — ABS).
- A **larger self-reported list** (Tier 2) exists because MoJ openly publishes a "Used By" page — a public good *and* a trap: it is unaudited and in several checked cases wrong (NHS England deterministic; UNHCR uses fastLink; Gambia/Destatis uncited).
- The **practice** (joining up citizens' records) is near-universal, but mostly with **other tools** — Splink is just the visible, open-source instance.
- **The defensible spine:** the consent/transparency gap. Lawful by design, person-level by construction, disclosed to almost no one. "It's lawful" is the indictment, not the defence.

## Still uncorroborated — carry as caveats, do not publish as fact
Destatis/EMA/UNHCR Splink use; whether Splink (vs generic Fellegi–Sunter) did the linkage at MCCSS / ONS coverage survey / Gambia / ABS NLS; the exact statutory basis for MoJ's operational uses; whether North Essex PNC feed or Core Person Record has scaled past pilot.

## Cross-reference (kept separate on purpose)
The Splink SQL-identifier security advisory is a *secure-coding* matter, NOT part of the privacy/governance story. Do not merge the narratives.
