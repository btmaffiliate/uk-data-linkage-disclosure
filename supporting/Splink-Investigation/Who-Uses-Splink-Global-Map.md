# Who Uses Splink
### A global map of documented adoption of the Ministry of Justice's record-linkage tool

*Public-interest research from publicly available documents only. Compiled 4 June 2026.
Two independent deep-research passes; every claim adversarially fact-checked (50 claims verified
across both passes, 0 survived as false). Confidence flagged on every entry. The count is kept
honest on purpose — a vague "used worldwide" is **not** a confirmed country.*

> **Headline, stated plainly:** documented adoption is **narrow and UK-centric**, not a global
> dragnet. Four countries show any confirmed Splink use; one (the UK) accounts for almost all of it.
> Several major statistics agencies that were specifically checked show **no evidence**, and
> **Statistics Canada is a confirmed non-adopter.** Because Splink is freely downloadable open-source
> software with no user registry, undocumented use certainly exists — but it is, by definition,
> undocumented, and is not asserted here as fact.

---

## CONFIRMED adopters (4 countries)

### 🇬🇧 United Kingdom — the core; deep and operational
| Body | Use | Status | Source |
|---|---|---|---|
| **Ministry of Justice** | Built Splink; links justice datasets; cross-justice person ID (Data First / Core Person Record); real-time court use; pulls PNC numbers for arrest info | Operational | gov.uk ATR records; github.com/moj-analytical-services/splink |
| **Office for National Statistics** | Splink v2.1.4 to dedup the 2021 Census; QA of Census↔DWP master key/encrypted NINo↔HMRC PAYE | Operational | ons.gov.uk 2021-Census→DWP; IJPDS 2245 |
| **NHS England** | Splink pipeline feeding the Personal Demographics Service (Person_ID) | Operational (in build) | nhsengland.github.io data-linkage-hub; IJPDS 3271 |

### 🇦🇺 Australia — one major system *(confirmed, first pass)*
| Body | Use | Status | Source |
|---|---|---|---|
| **Australian Bureau of Statistics** (+ AIHW) | Person Linkage Spine 2025 (Medicare+Centrelink+Tax); National Disability Data Asset spine | Operational | abs.gov.au Person Linkage Spine; IJPDS 2818 |

### 🇺🇸 United States — narrow: one state pilot + evaluators
| Body | Use | Status | Source |
|---|---|---|---|
| **Indiana Department of Health (IDOH)** | Pilot linking COVID cases + vaccination records | **Pilot** | in.gov "Probabilistic Record Linkage with Splink" (Simmons) |
| **US Census Bureau** | *Evaluated* Splink vs in-house BigMatch | **Evaluation only — not operational** | census.gov record-linkage |
| **Florida Cancer Registry** | *Evaluated* Splink | **Evaluation only** | IJPDS 2786 |

### 🇨🇱 Chile — one research study
| Body | Use | Status | Source |
|---|---|---|---|
| **Ministry of Health** (with UCL) | Research: link/dedup migrant records lacking a national ID | **Research study** | IJPDS 2348 |

---

## CONFIRMED NEGATIVE — checked, and NOT an adopter
- 🇨🇦 **Statistics Canada** — the Canadian source discusses the UK's Splink work; it does **not** use Splink. *(statcan.gc.ca 11-522-X; PMC9645056)*

## Searched — NO evidence of Splink adoption found
Stats NZ · Netherlands CBS · Statistics Norway · Statistics Sweden · Statistics Finland ·
Statistics Denmark · Germany Destatis · France INSEE · Spain INE · Italy ISTAT · Eurostat ·
Statistics Poland · Statistics Portugal · Brazil IBGE · South Africa StatsSA · India.
*(Absence of a public record ≠ proof of non-use, but it is not a confirmed adopter.)*

## Excluded
- **Credit scoring / credit bureaus** — UNVERIFIED across both passes. No source. Excluded.
- US Census Bureau ↔ ONS appearing together = the **Fellegi-Sunter method's history** (originated at the US Census Bureau, 1969), **not Splink**.

---

## The honest count
- **Confirmed countries with ANY documented Splink use: 4** — UK (operational, multiple agencies), Australia (one operational system), US (one state pilot + two evaluators), Chile (one research study).
- **Operationally deep: the UK, essentially alone.**
- **Confirmed non-adopter: Canada.** **No evidence: ~16 other agencies checked.**
- **The true footprint is larger but undocumented** (open-source, anonymous downloads ~230k/month) — real, but unprovable per-country, so not named here.

## What this means for the story
The strong, defensible version is **not** "the world is secretly running this on everyone." It's:
*"The UK has built deep, operational, cross-domain citizen linkage on this tool — with no individual
consent or notification — and it is beginning to spread (Australia operationally; pilots and studies
in the US and Chile)."* That is true, sourced, and unkillable. The global-dragnet version is not
supported by the documents and would be the first thing a critic dismantles.

*Method: 2 deep-research passes, 200+ agent calls, 40+ sources, every claim majority-refutation-tested. Negative and null results reported, not hidden.*
