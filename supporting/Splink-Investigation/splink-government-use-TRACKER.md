# Government use of Splink (probabilistic record linkage) on citizen data — sourced tracker

*Public-interest research. Every entry cited. Last updated: 2026-06-02.*
*This document concerns publicly documented deployments only. No third-party systems accessed.*

## What Splink is

Open-source Python library for **probabilistic record linkage / entity resolution** — links and
deduplicates records about the same person across datasets that share no common ID, using the
Fellegi–Sunter model. Developed and maintained by the **UK Ministry of Justice**. ~230,000+
PyPI downloads/month; "in use across the world." Scales to ~100M records (DuckDB / Spark / Athena).
Repo: github.com/moj-analytical-services/splink

## Why it matters (the civil-liberties hook)

Record linkage is the technical step that turns *siloed* citizen datasets into a *joined* profile
of a person across health, justice, tax, benefits, and defence systems — often without a shared
identifier and **without the citizen's direct knowledge**. The privacy question is not "is the
maths wrong" — it's accurate — it's **the existence and governance of cross-domain person-level
linkage**: consent, purpose limitation, scope creep, and who can re-identify whom.

## CONFIRMED deployments (sourced)

### United Kingdom
| Body | Use | Source |
|---|---|---|
| **Ministry of Justice** | Links persons across courts, prisons, probation (batch + real-time); "Data First" gives researchers a universal cross-justice person ID. Published algorithmic-transparency record. | gov.uk Data First / MoJ Splink Master Record; dataingovernment.blog.gov.uk (2022-09-23) |
| **Office for National Statistics (ONS)** | 2021 Census linkage to itself; Census↔DWP master key / encrypted NINo (96.7% linked, precision ~99.87%); Business Index, Demographic Index. Splink is in ONS's core methods library. | ons.gov.uk "2021 Census linkage to DWP master key and encrypted NINo" |
| **NHS England** | "Implementing a probabilistic linkage model using **Splink**" as the core engine for a new NHS data-linkage service; works with Master Person Service (Person_ID). | nhsengland.github.io/datascience/our_work/data-linkage-hub/ |
| **UK Health Security Agency** | Linked HIV testing data to national health records (A&E opt-out bloodborne-virus testing evaluation). | dataingovernment / case studies |
| **Ministry of Defence** | Veterans Card system verifies applicants against historic service records; service-leavers DB ↔ 2011 Census. | ons.gov.uk "Service leavers database linkage to 2011 Census" |

### Australia
| Body | Use | Source |
|---|---|---|
| **Australian Bureau of Statistics (ABS)** | Built the **2024 National Linkage Spine** underpinning the **National Disability Data Asset**; using Splink for the **2025 Person Linkage Spine**. | abs.gov.au data-linkage materials |

### United States
| Body | Use | Source |
|---|---|---|
| **Defense Health Agency (Dept. of Defense)** | Splink used to de-duplicate hospital records across **200M+ records**. | dataingovernment / case studies |

### Chile
| Body | Use | Source |
|---|---|---|
| Academic / public-health (migrant immunisation access) | Probabilistic linkage to estimate migrant access to immunisation programs. | NCBI PMC10929394 |

## UNVERIFIED — do not publish until sourced
- **Credit scoring / credit bureaus.** No public evidence found. Splink *can* match "financial
  transactions" (per docs), but no credit-scoring deployment is documented. **Flagged, not claimed.**
- **"Many countries."** Confirmed: UK, Australia, US (defence), Chile (academic). Beyond these,
  adoption is asserted ("in use across the world") but specific national deployments need individual
  sourcing before naming.

## Cross-reference: the security finding (kept separate on purpose)
A separate disclosure (`splink-vuln-disclosure-DRAFT.md`) covers an unquoted-SQL-identifier
pattern in Splink 4.0.16. **Do not merge the two narratives.** The privacy concern is about
*governance of lawful linkage*; the bug is about *secure coding in multi-tenant wrappers*. Mixing
them reads as coercion and discredits both.

## Open threads to chase
- ONS cross-government data-linkage review — full list of departments named.
- gov.uk Algorithmic Transparency Recording Standard — all Splink-related records.
- Other national statistics institutes (StatCan, Stats NZ, Eurostat members) — confirm or drop.
- Governance docs: legal basis / DPIAs for each confirmed deployment.

## Sources
- https://github.com/moj-analytical-services/splink
- https://www.gov.uk/government/publications/joined-up-data-in-government-the-future-of-data-linking-methods/splink-mojs-open-source-library-for-probabilistic-record-linkage-at-scale
- https://dataingovernment.blog.gov.uk/2022/09/23/splink-fast-accurate-and-scalable-record-linkage/
- https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink
- https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record
- https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/healthandwellbeing/methodologies/2021censuslinkagetodwpmasterkeyandencryptednino
- https://www.ons.gov.uk/peoplepopulationandcommunity/armedforcescommunity/methodologies/serviceleaversdatabaselinkageto2011census
- https://nhsengland.github.io/datascience/our_work/data-linkage-hub/
- https://www.abs.gov.au/about/our-organisation/australian-statistician/speeches/data-linkage-and-integration-improve-evidence-base-public-policy-lessons-australia
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10929394/
- https://realworlddatascience.net/applied-insights/case-studies/posts/2023/11/22/splink.html
