# WHO JOINS UP THE WORLD'S RECORDS — A Splink Adopter Master Analysis

### Fourteen adversarially-verified profiles of government and institutional record-linkage built on Splink, tiered by how much can actually be proven.

*Public-interest investigation built entirely from public documents. Each profile was researched, then put through an adversarial verification pass against primary sources; the verifier's corrections are applied here strictly. Where a claim rests only on Splink's own maintainer-curated "Used By" page, this report says so in plain terms. Confidence is flagged throughout, overclaims are corrected openly, and the line between lawful statistical linkage and coercive surveillance is held deliberately. This is not a legal opinion.*

---

## 1. Executive summary — the honest global picture

Splink is a free, open-source probabilistic record-linkage library built and maintained by the **UK Ministry of Justice**. It implements the Fellegi–Sunter model — it scores the probability that two records (across files, or within one file) refer to the same real-world entity. Its mathematics is sound and uncontroversial. Because it is open-source and its maintainers keep a public "Used By" page, the people who adopt it are unusually *visible*. That visibility is the only reason this report can exist; it is a window, not the whole room. Most states that join up citizens' records do so with their **own** tools — the phenomenon is far larger than the one library.

The disciplined finding, after adversarial verification, is that the global adoption picture is **much more modest and more honest than a vendor's logo-wall suggests.** Of the fourteen targets examined, only a handful are *independently* proven to run Splink in production on real population data. The rest dissolve, on inspection, into self-reported listings, methods evaluations on synthetic data, in-development pilots, academic papers, or outright negatives where Splink was benchmarked and rejected.

**The tiered count (after applying every verifier correction):**

**TIER 1 — Independently-verified operational use on real population/administrative data (3):**
- **UK Ministry of Justice** — first-party Algorithmic Transparency Records document genuinely operational, person-identifying linkage (the strongest case in the entire survey).
- **UK Office for National Statistics** — Splink named on ONS's own published methodology pages, with concrete record counts and quality metrics, linking the 2021 Census to tax, benefits and NHS identifiers at near-total population scale.
- **Australian Bureau of Statistics** — ABS's own page states the 2025 Person Linkage Spine "was constructed using Splink"; this is first-party production documentation, not a vendor listing.

**TIER 2 — Operational/used, but attested ONLY by Splink's own "Used By" page (self-reported; the underlying *linkage* is often independently corroborated, but the *Splink tooling* is not) (5):**
- **UK wider public sector** (DfE, CMA, Welsh Revenue Authority, Leicestershire, Westmorland & Furness, council "single view of debt" projects) — the OHID/MoJ BOLD case is genuinely well-sourced *research*, but the operational cluster rests on the Splink page.
- **NHS England** — the live Master Person Service is *deterministic and does NOT use Splink*; the Splink work is in-development. Verifier reclassified this to **RESEARCH/development**.
- **Canada — Ontario MCCSS / ECCC** — the MCCSS social-assistance-to-health linkage is independently verified, but the peer-reviewed paper *does not name Splink*; ECCC rests on the page alone.
- **Germany — Destatis** — a single uncited sentence on Splink's homepage; the verifiable German linkage work uses Fellegi–Sunter on *simulated* data and never names Splink.
- **EU — European Medicines Agency** — one uncited line; verifier downgraded to **ASSERTED** (veterinary data, low civil-liberties weight).

**TIER 3 — Pilot / evaluation / research / academic (4):**
- **AIHW + Australian state/territory linkage units** — **EVALUATION** for AIHW (still on in-house SAS DALI); the state units are **NEGATIVE** (they use ChoiceMaker, DLS3, FEBRL — not Splink).
- **United States — Indiana DoH** — **PILOT** (synthetic-data demo); **Florida Cancer Registry** — **EVALUATION** (simulated data).
- **Lao PDR — Shared Child Health Record** — **RESEARCH** (a Kyoto University methods study on real provincial children's records).
- **Chile — Ministry of Health** — **RESEARCH** (a published IJPDS study linking the immunisation register to school enrolment to estimate migrant coverage).
- **The Gambia — 2024 Census** — verifier downgraded to **ASSERTED** (one uncited line; the census is real, the Splink role is self-attested only).

**TIER 4 — Confirmed NEGATIVES (Splink benchmarked and rejected, or never used):**
- **US Census Bureau** — uses in-house **BigMatch**; states it evaluated Splink and found BigMatch superior.
- **NIH All of Us** — uses **Datavant** tokenisation/PPRL; no Splink.
- **Statistics Canada** — uses its own **G-Link**; no Splink.
- **Australian state linkage units** — own engines, not Splink.

**The one-paragraph version.** A small number of national statistical offices and one justice ministry genuinely run Splink in production at population scale, almost always for statistics, lawfully, and almost never with the individual's knowledge or consent. A larger number *appear* to use it only because they are listed on the maintainer's own page — a listing that is unaudited and, in several checked cases, contradicted by the organisation's own documents (NHS England is deterministic; UNHCR's public code uses fastLink; the Gambia and Destatis listings carry no citation at all). The genuinely sharp civil-liberties stories are **the UK MoJ's slide from research into operational policing-adjacent use**, and **UNHCR's documented sharing of Rohingya data toward repatriation screening** — and even the latter was a different mechanism (biometrics) than the Splink claim. The defensible, undismissable spine of the whole investigation remains the **consent and transparency gap**: lawful by design, person-level by construction, and disclosed to almost nobody.

---

## 2. Per-adopter profiles

Each profile is presented at the tier the verifier settled on, with the verifier's corrections applied and unsupported items dropped.

---

### 2.1 UK Ministry of Justice — TIER 1, OPERATIONAL *(verifier: SOLID)*

**What it is.** The MoJ is both the *developer/maintainer* of Splink and a heavy operational user of it. There are two distinct products that must not be conflated:

- **Data First** — explicitly research/statistics-only. Datasets are de-identified, given a universal person ID, and made available to accredited researchers via the ONS Secure Research Service and SAIL Databank. MoJ's own Algorithmic Transparency Record (ATR `moj-data-first-splink`, 17 Dec 2024) states the data are *"not for operational decision-making"* and *"not integrated into a decision-making process."* Around 40 research projects facilitated; 43 tables across 7 justice domains.
- **Splink Master Record** — genuinely operational and person-identifying. The ATR `moj-splink-master-record` (6 Oct 2025) documents weekly **JustLink** batch linkage across courts/prisons/probation, a real-time **Core Person Record** pilot, use **"to find probation records associated with an individual when they come to court, as part of the process of preparing a case for sentence,"** and a **North Essex pilot** that identifies Police National Computer (PNC) numbers and **"sends them to the police each day to identify if any arrests have occurred."**

**Registers linked.** DELIUS (probation), NOMIS (prisons), Common Platform and LIBRA (criminal/magistrates' courts), FamilyMan (family courts), CaseMan (civil courts), PNC numbers, and — as a *research* cross-domain link via the ONS Secure Research Service — the DfE National Pupil Database joined to PNC criminal-history data.

**Scale.** JustLink pre-deduplication volumes (per the ATR): LIBRA 19.6M, Common Platform 2.9M, NOMIS 2.2M, DELIUS 2.4M, FamilyMan 20.9M, CaseMan 17.7M — roughly 65M+ records combined. *(The earlier framing that coverage "approaches the full population passing through courts/prisons/probation" is the author's inference, not a sourced figure, and is marked as such.)*

**What has actually been done with the data.**
- Assigned a single universal cross-justice person ID to de-identified records for ~40 accredited research projects (Data First), with IJPDS-published outputs (e.g. *Data First: Criminal Courts Linked Data*).
- Weekly JustLink batch linkage producing **"a fully anonymised lookup table that contains the links between records (but NOT the personal identifiers)"** for studying case-progression and reoffending trends.
- Core Person Record pilot that **aims to create a unique identifier** linking the same person across courts/prisons/probation as records are created/updated *(pilot, not confirmed in production)*.
- At court, **retrieves an individual's probation records as part of the process of preparing a case for sentence** *(record retrieval — not a claim that it influences the sentence itself; the earlier "feeds the sentencing process" gloss is dropped)*.
- North Essex pilot: identifies probationers' PNC numbers and sends them to police **daily** to check for arrests.
- Won the **2025 Civil Service Award** for the North Essex Probation Delivery Unit Case Information Dashboard, built on the linkage.

**The disclaimer that must be foregrounded.** The ATR states verbatim: *"There are no complaint procedures specific to Splink itself since it does not directly make decisions about individuals."* MoJ frames Splink as a lookup/matching aid feeding a human process, not an automated decision system. This is the single line a hostile critic will use to attack the operational tier, so it is stated here up front — **and rebutted:** the linkage output directly determines *which named individual's records surface at court* and *which PNC numbers are sent to police each day.* "Does not make the decision" is not the same as "is not operational." It is the input to an operational process about a named person.

**Legal basis.** Not explicitly stated in either ATR. The most likely basis is UK GDPR Art 6(1)(e) public task, with Art 9(2)(g)/Art 10 for criminal-offence data — but this is **inferred, not cited.** Report it as ASSERTED/IMPLICIT. Neither ATR cites the Digital Economy Act 2017 or any specific statutory gateway.

**Consent / notification / opt-out.** None for any use. Data First relies on de-identification plus the Five Safes; the operational uses simply do not tell the individual their records are being linked, and offer no opt-out.

**Governance.** DPIAs per use case; Five Safes; ONS Accredited Researcher scheme; MoJ AI and Data Science Ethics Framework; two published ATRs.

**Function creep.** Real and multi-vector: (1) the *same* engine runs research-only in Data First and person-identifyingly in the Master Record — the boundary is one configuration choice; (2) batch → real-time (Core Person Record); (3) justice → policing (the daily North Essex PNC→police feed). *(The MoJ–DfE National Pupil Database link is RESEARCH/statistical cross-domain creep — accessed only via the ONS Secure Research Service under a privacy statement — NOT operational justice-to-policing creep; the verifier corrected its placement.)* The public engineering blog (29 Jan 2026) describes only the benign batch linkage and omits the PNC/police and court-sentencing uses — so the engineering narrative understates the operational footprint.

**Adjudications.** None found against these specific systems.

**Why this is TIER 1 and not "per Splink's own page":** the operational finding rests on *MoJ's own gov.uk Algorithmic Transparency Records* — first-party admissions, not a vendor self-listing. The North Essex feed and Core Person Record are **pilots**, not confirmed national operations.

---

### 2.2 UK Office for National Statistics — TIER 1, OPERATIONAL *(verifier: SOLID)*

**What it is.** ONS uses Splink in production for three named programmes — the Business Index (former IDBR), the Demographic Index, and the 2021 Census — confirmed on ONS's *own* published methodology pages, not merely the Splink "Used By" listing.

**Registers linked & scale.** Using a hybrid pipeline (deterministic first, then *"a probabilistic data linkage algorithm (Splink) was applied to the non-links"*), ONS joined the **~58.6M-record 2021 Census of England and Wales** to itself (deduplication and coverage estimation) and, at near-total population scale, to:
- the **DWP master key** — 56,673,658 IDs (96.7%);
- **encrypted National Insurance numbers** — 56,716,769 IDs (96.7%) — the key that *enables* HMRC PAYE integration *(this is the linkage to the NINo key; it is not a completed 56.7M PAYE-earnings join — the verifier corrected the earlier phrasing that implied an executed earnings linkage)*;
- the **NHS Personal Demographics Service** — assigning NHS numbers to 55,105,336 census records (95.75%), via "Splink 2."

Census-to-Census-Coverage-Survey matching produced 448,386 person matches at 99.96% precision — **but that step is described as a generic "Fellegi–Sunter probabilistic linkage algorithm" and does NOT name Splink.** Do not state it was Splink. Splink-stage precision on the DWP/NINo linkage was 89.85%; the combined pipeline reached 99.87% precision / 99.86% recall *(figures scoped to that specific methodology page, not programme-wide)*.

**What has actually been done.** Built the lookups above; updated the **Public Health Data Asset** with Census 2021 characteristics; enabled joined health-and-labour-market research; quality-assessed the Statistical Population Dataset; made linked de-identified data available to accredited researchers via the Secure Research Service / Integrated Data Service.

**Legal basis.** Census Act 1920 (as amended by the SRSA 2007); UK GDPR Art 6(1)(c) (legal obligation) and 6(1)(e) (public task). ONS states expressly: **"Consent was not used by ONS as the lawful basis for processing personal data during the 2021 Census."** *(Verifier correction: that quote and the Article 6 detail live on ONS's "Census processing and data protection" page — `/censusprocessinganddataprotection` — not on the "law requiring people to fill in the census" page the original profile cited.)* The IDS/SRS operate under the Digital Economy Act 2017. Disclosure of identifiable data is a criminal offence under SRSA 2007.

**Consent / notification / opt-out.** None. No per-individual consent for downstream linkage to DWP/HMRC/NHS, and no opt-out from being linked. The only "opt-out"-like element is at the access layer (researchers see de-identified data) — which gives the individual no choice over the linkage itself.

**Governance.** Five Safes; DEA-accredited Integrated Data Service; SRSA 2007 criminal-offence protection; de-identification before access. **A full census-level DPIA was completed** (per ONS's own page); *(verifier correction: the earlier blanket "no DPIAs located" was wrong — only the per-linkage DPIAs for the individual Census-to-DWP/HMRC/PDS joins remain unlocated).*

**Operational vs statistical.** Statistical — and ONS is *legally barred* from operational use against individuals (SRSA 2007). But the linkage is person-level identification at near-total population scale, and the outputs feed standing analytical assets. Statistical purpose; operationally identifying at the joining stage.

**Function creep.** Architecturally expansionary by design: the encrypted-NINo and DWP-master-key lookups are persistent keys built to enable future integration; the Demographic Index/SPD are standing infrastructure intended to replace the traditional census with admin-data-based population statistics.

**Adjudications.** None found.

---

### 2.3 Australian Bureau of Statistics — TIER 1, OPERATIONAL *(verifier: MIXED; tier held)*

**What it is.** ABS is a production user of Splink — confirmed first-party on its own Person Linkage Spine page, which states verbatim: *"For the first time in 2025, the Spine was constructed using Splink, a probabilistic linkage tool that estimates the likelihood that records from different sources refer to the same person,"* delivering processing efficiencies *"while maintaining linkage quality comparable to previous deterministic approaches."*

**Registers linked & scale.** Whole-of-Australian-population. The spine is built from three whole-of-population collections — **Medicare Consumer Directory, DOMINO Centrelink data, and Personal Income Tax** — covering January 2006 to June 2025. To this, PLIDA links ~30 datasets / 70,000+ variables (health, education, payments, tax, employment, deaths, aged care, disability). Exact person/record counts are not published (the population-wide spine paper was CAPTCHA-blocked).

**Important corrections from verification.**
- The 2024 **National Linkage Spine / National Disability Data Asset** Splink attribution rests **only** on the Splink "Used By" page. The peer-reviewed IJPDS 2818 paper **does NOT name Splink** — it says only "a combination of ABS's deterministic linkage algorithm and AIHW's probabilistic linkage and machine learning algorithms." So confidence is *high* for the 2025 Person Linkage Spine (first-party ABS documentation) but only *self-reported* for the 2024 NLS/NDDA.
- The earlier claim that ABS "presented at ISI World Statistics Congress 2025" is **dropped** — the located ISI abstract (#2922) is the MoJ Splink-development talk by Robin Linacre, not an ABS presentation.
- ABS is the **"Accredited Data Service Provider"** for PLIDA (not "Integrating Authority," which is older/different terminology).

**What has been done.** Built/maintained the whole-of-population Person Linkage Spine (2025 build with Splink); built PLIDA (formerly MADIP); constructed the National Disability Data Asset; integrated survey data; published methodology in IJPDS.

**Legal basis.** Australian Bureau of Statistics Act 1975 and **Census and Statistics Act 1905** — whose secrecy provisions (s.19) make unauthorised disclosure a criminal offence (120 penalty units or 2 years' imprisonment). Disclosure to ABS is *"authorised by law"* rather than by consent. The Data Availability and Transparency Act 2022 is scoped to the NDDA/some integration projects, not the core PLIDA pages.

**Consent / notification / opt-out.** None. The PLIDA Privacy Statement: agency personal information *"will be disclosed to the ABS for the PLIDA as authorised by law."* Linkage uses name, address, date of birth and government identifiers; direct identifiers are then separated and the data de-identified for access. Individuals are not notified and cannot opt out.

**Operational vs statistical.** Statistical/research only on the documented record. But this is a powerful **re-identifiable population register** held by a Commonwealth body, protected by statute and governance rather than by technical impossibility of re-identification.

**Function creep.** Largely sanctioned-by-design: MADIP → PLIDA rebrand and continual dataset addition; the same Splink-powered spine methodology propagating into the NLS, the NDDA, and the planned 2026 Census Post-Enumeration Survey; cross-jurisdictional linkage widening the linkable graph.

**Adjudications.** None found.

---

### 2.4 UK wider public sector — TIER 2, OPERATIONAL_PER_SPLINK_OWN_PAGE *(verifier: MIXED)*

**What it is.** A heterogeneous set of bodies — DfE, OHID/DHSC, CMA, Homes England, DBT, Welsh Revenue Authority, LOTI, and councils (Lewisham, Leicestershire, Gateshead, Richmond & Wandsworth, Westmorland & Furness) — that share only the Splink engine. They are **not** one coordinated system. Evidentiary strength varies enormously, and the verifier sharply corrected the headline framing.

**The one genuinely well-sourced case — OHID/MoJ BOLD (RESEARCH, not operational).** The Office for Health Improvement and Disparities and MoJ, under the Better Outcomes through Linked Data programme, linked **~40,000 people (38,895 after cleansing)** sentenced to an Alcohol Treatment Requirement or Drug Rehabilitation Requirement (Aug 2018–Mar 2022) in nDelius to the National Drug Treatment Monitoring System, to study whether offenders entered treatment (38.9% engaged). This is confirmed verbatim from gov.uk: *"This model has been incorporated into MOJ's software Splink."* Legal basis: UK GDPR Art 6 public-interest + Art 9 public health. Governance: a DPIA approved by both departments' DPOs, a signed inter-departmental data-sharing agreement, and UKHSA Caldicott Guardian authorisation. Consent: gathered upstream at point of treatment — *"Almost 98% of people provide this consent."* And the explicit non-operational guarantee: **"we did not intend to use the information to affect any specific individual."** *(Verifier correction: the final dataset was **anonymised** per the ICO code with re-identification "remote" — not the "pseudonymisation" the original profile asserted.)* **This case should be published separately as RESEARCH/STATISTICS — it is the only well-evidenced, consented, non-operational deployment in the cluster.**

**The claims the verifier knocked down.**
- **LOTI rough-sleeping tool.** The original profile said it puts named vulnerable rough sleepers in front of "frontline borough teams" for person-level operational action. **Not supported.** LOTI's own page describes a *strategic/aggregate dashboard* to "identify trends and patterns" for "strategic decision makers" — and **does not name Splink at all.** Reclassify as STRATEGIC/AGGREGATE insight pending independent evidence.
- **Lewisham Free School Meals auto-enrolment.** The cited Cities Today article is about **Pupil Premium** (not Free School Meals), mentions only "School Census data on benefits and education" (no council-tax records), and **never mentions Splink.** The ~£1.2m unlocked, 500+ families identified, and "only 3 opted out after a posted opt-out notice" are all real and verified — but as Pupil Premium, and the Splink attribution comes solely from Splink's own page.
- **DBT "Matchbox."** Splink's page says DBT *"plans to use"* Splink; the DBT blog says Matchbox uses Splink to build probabilistic models *but supports alternatives.* So "deployed operationally / built on top of Splink" overstates it, and the quoted phrase *"both analytical and operational use"* is **not in the DBT source** and is dropped. What *is* verified: *"The original data being matched is never sent to the Matchbox server."*
- **Homes England** (~30M Land Registry-to-OS-NGD records in <5 hours on Databricks; "monitor new builds for the 1.5m homes mandate") — traces entirely to Splink's own page. Attribute explicitly to that page, not to an independent source.

**Attested ONLY on Splink's own page (no independent corroboration found):** DfE learner matching, CMA Persons-with-Significant-Control resolution, Welsh Revenue Authority third-party tax linkage ("operational support"), Leicestershire (Education↔Social Care), Westmorland & Furness (SEND dedupe), and the Richmond & Wandsworth / Gateshead "single view of debt" projects. These must be published as self-reported, not established operational fact.

**Legal basis.** Predominantly UK GDPR Art 6(1)(e) public task / public-interest bases under each body's statutory functions. No single overarching statute.

**Consent / notification / opt-out.** Highly inconsistent. Best case: Lewisham posted an opt-out notice (3 of 500+ opted out). OHID/MoJ relied on upstream treatment consent (~98%). Absent/undocumented for the council debt projects, DfE, CMA, WRA, Leicestershire, Westmorland — and, on the corrected reading, the LOTI rough-sleeping work links named records but its documented purpose is strategic.

**Governance.** Strong for BOLD (DPIA/DSA/Caldicott). The Algorithmic Transparency Recording Standard became mandatory across central government from 2025, but **no standalone ATRS record was located** for any of these bodies' Splink use — only MoJ's two records exist.

**Adjudications.** None found.

---

### 2.5 NHS England — TIER 2, reclassified to RESEARCH/development *(verifier: SOLID; tier adjusted)*

**The crucial distinction.** The **live, operational Master Person Service (MPS) does NOT use Splink.** Per NHS England Digital's own page, MPS uses *"a bespoke deterministic linking approach"* across three tracing steps to match each record to the Personal Demographics Service (PDS) "spine" (~80M patient records) or an MPS record bucket, assigning a persistent **Person_ID**. Splink is the engine of a **separate, in-development** probabilistic pipeline being built by NHS England's Data Linkage Hub.

**What the Splink work is.** Per IJPDS abstract 3271 (Laidler, Imaz Blanco & Balasubramanian, 2025), the Splink pipeline links "any health data set" to PDS, reporting *"improved linkage quality by up to 19% in comparison to the existing methodology,"* with status *"building an in-house capability to deliver this methodology at scale"* — i.e. **development, not production.** Splink's own docs say NHS England *"is working on developing an alternative data linkage model using splink as the core engine for a new probabilistic data linkage service"* — a development statement, not a production attestation.

**Why the tier moved.** The original label `OPERATIONAL_PER_SPLINK_OWN_PAGE` overstated it: every source describes the Splink work as in-development. The genuinely operational element (MPS/Person_ID/PDS) is Splink-free. Verifier reclassified the Splink-specific status to **RESEARCH/development.**

**Items dropped:** "and confidence" as one of the mps_diagnostics 10 metadata columns (unverified); the "25 fields" MPS matching schema claim (no citation).

**Registers (operational MPS, deterministic).** PDS (~80M), HES, and any dataset ingested via NHS England Data Processing Services that requests tracing.

**Legal basis.** NHS-number consistent-identifier duty under the **Health and Social Care (Safety and Quality) Act 2015**; secondary uses rely on s251 NHS Act 2006 (CAG approval), DARS/Data Sharing Agreements, UK GDPR Art 6(1)(e) + Art 9(2)(h)/(i)/(j). *(The precise MPS-specific lawful basis could not be quoted — the relevant pages were Cloudflare-blocked — so this is partly inferred.)*

**Consent / notification / opt-out.** Purpose-dependent. The National Data Opt-Out constrains downstream secondary disclosures of confidential information — **not** the linkage/Person_ID assignment itself, which is an infrastructure step individuals are not notified of and cannot opt out of.

**Function creep.** The architecture is inherently expansionary: a single persistent Person_ID applied to "any data set," spanning both research/planning and direct care; the move from deterministic to probabilistic widens which records become linkable. No evidence of cross-domain joining to tax/justice/benefits.

**Adjudications.** None found.

---

### 2.6 Canada — Ontario MCCSS & ECCC — TIER 2, OPERATIONAL_PER_SPLINK_OWN_PAGE *(verifier: MIXED)*

**What it is.** Splink's page says the Data Integration Unit at **Ontario's Ministry of Children, Community and Social Services** uses Splink as its *"main data-integration tool for all intra- and inter-ministerial data-linking projects,"* and that **Environment and Climate Change Canada** uses it "to connect datasets from various administrative and reporting programs."

**The honesty move at the centre of this profile.** For MCCSS, the underlying *linkage* is strongly corroborated independently — but the *Splink tooling* is not. A peer-reviewed IJPDS/ICES paper documents linking the **MCCSS Social Assistance database (2003–2016, 2,736,353 unique member IDs)** to Ontario's **Registered Persons Database** (the health-card registry), achieving an **87.9% link rate (2,405,115 linked)** via 2 deterministic + 14 probabilistic Fellegi–Sunter passes. But **that paper does NOT name Splink anywhere.** So: the linkage is independently verified RESEARCH; the Splink attribution is self-reported only. Publish it as: *"MCCSS links social-assistance to health data without consent (verified); Splink is named as the tool by Splink's own page (self-reported)."*

**Registers.** MCCSS Social Assistance (SAMS); Ontario Registered Persons Database; Developmental Services / Passport data; the linked cohort held at ICES. ECCC: unspecified "administrative and reporting programs" — plausibly the Greenhouse Gas Reporting Program (facility/company data, **not** citizen-level), but this is inference.

**What has been done.** The SA-to-health linkage was created to enable population research on the social determinants of health; the cited paper is a *methodology* paper reporting **no substantive health findings yet.** *(Verifier corrections: the CRDCN holding is a **standalone, unlinked** de-identified SA dataset (2003–2014) — not the pre-built SA-health linked cohort (2003–2016); the year mismatch confirms they are different holdings. And the "linked and then de-identified" quote belongs to the MCCSS Data Integration annual report / data.ontario.ca inventory, not the personal-information-management page originally cited.)*

**Legal basis.** Ontario FIPPA Part III.1 (data-integration provisions) plus **PHIPA s.45**, which permits use of personal health information for analysis/management *without individual consent or research ethics board review* — confirmed verbatim. De-identification applied after linkage: *"all direct personal identifiers ... were removed."*

**Consent / notification / opt-out.** None for the linkage/research use. MCCSS publishes program-level notices of collection, but no specific consent to data integration and no opt-out.

**Operational vs statistical.** Research/statistical and de-identified. **No evidence of operational individual-level decisioning.** The tier token contains "operational" only because Splink's page makes the "main tool" claim; the verified activity is research.

**Statistics Canada is a confirmed NEGATIVE** and must be kept separate: its Social Data Linkage Environment uses **G-Link** (*"linked ... probabilistically using a generalized software tool (G-Link)"*), not Splink.

**Adjudications.** None found. ICES is a PHIPA prescribed entity overseen by Ontario's Information and Privacy Commissioner; no adverse adjudication located.

---

### 2.7 Germany — Destatis — TIER 2, OPERATIONAL_PER_SPLINK_OWN_PAGE *(verifier: MIXED)*

**What it is.** Splink's homepage carries a single vague sentence: *"The German Federal Statistical Office (Destatis) uses Splink to conduct projects in linking register-based census data."* **This is the only source tying Destatis to Splink** — uncited, no project name, no dataset, no scale, no output. No Destatis publication, transparency record, tender or paper corroborates it.

**The verifiable German work (which never attributes itself to Splink).** Destatis's real, substantial record-linkage R&D — the Zensus 2022 register correction, the Zensus 2031 "Methodentest," and microsimulation for a planned national Educational Trajectory Register — uses Fellegi–Sunter probabilistic linkage with an Expectation-Conditional-Maximization algorithm and blocking, on quasi-identifiers (Germany has no universal personal identifier for this). But the published method papers (Destatis WISTA 4/2025; the Schnell group at Duisburg-Essen) run on **microsimulated/synthetic data** and do **not** name Splink. A notable finding from WISTA 4/2025: a *critical linkage bias for female migrants* under Cryptographic Long-term Key methods and probabilistic linkage without place of birth.

**Verifier corrections.**
- The arXiv paper (Ranbaduge/Christen/Schnell) **does cite Splink in its references** — it just does not *use* it as the linkage method. The original "never names Splink" was wrong; correct to "cites Splink but does not implement it."
- The asserted **2023 Constitutional Court register-census proportionality ruling** (and its "freedom-threatening identifier" language) lacks a verifiable citation and should be moved to unverified.
- The cited English Constitutional Court URL (the 2018 `2 BvF 1/15` judgment) returns 404; cite the German source instead. The 2018 ruling itself is real and upheld the register-based census subject to a proportionality test.

**Registers (the census programme, not attributed to Splink).** State population registers (Melderegister); Federal Employment Agency data; education data; tax/land-register data; BKG geodata (the ~22M-address register); the buildings-and-housing census (>20M owners). Future: ~50+ registers to be linked via the tax-ID under the Registermodernisierungsgesetz. *(These are register-census programme datasets and are NOT attributed to Splink; several are planned or microsimulated.)*

**Scale.** Whole resident population (~83M); the arXiv simulation used >130M synthetic records. Splink-specific scale: unknown.

**Legal basis.** Bundesstatistikgesetz; Zensusgesetz 2022; EU Regulation 763/2008; the future Registerzensus on the RegMoG/IDNrG family. GDPR Art 6(1)(c)/(e), Art 9, Art 89.

**Consent / notification / opt-out.** None — census response is a statutory obligation. The wider register-modernisation programme is to offer a *"Datenschutzcockpit"* letting citizens see tax-ID data transfers (for administrative services, not the statistical census).

**Operational vs statistical.** Statistical — and walled off by statistical confidentiality (Statistikgeheimnis, BStatG §16) against operational reuse.

**Function creep.** Material structural *risk*, not confirmed misuse: the tax-ID (Steuer-ID) introduces exactly the persistent single cross-register identifier the Constitutional Court historically called freedom-threatening, shared between statistical and administrative ("once-only") uses.

**Adjudications.** The 1983 *Volkszählungsurteil* (informational self-determination) and the 2018 census judgment are real constitutional context. No regulator action against Destatis's linkage.

---

### 2.8 EU — European Medicines Agency — TIER 2, downgraded to ASSERTED *(verifier: SOLID; tier adjusted)*

**What it is.** Splink's page carries one uncited line: *"The European Medicines Agency uses Splink to detect duplicate adverse event reports for veterinary medicines."* No EMA document, press release, talk, GitHub artefact, or independent source corroborates that Splink (rather than EMA's own documented duplicate-detection algorithm) is in use. EMA's own methodology (GVP Module VI Addendum I on duplicate management) does not mention Splink.

**Why the tier moved.** The label `OPERATIONAL_PER_SPLINK_OWN_PAGE` contains "operational," which a hostile reader could quote as production use. The evidence — one uncited self-listing — supports no operational-status claim. Verifier set it to **ASSERTED.**

**Why the civil-liberties weight is low.** This is **veterinary** pharmacovigilance — EudraVigilance Veterinary (EVVet3) under Regulation (EU) 2019/6. The records concern animal adverse events, and EMA guidance requires reports to be **fully anonymised before recording**, with no owner/veterinarian/person identifiers. So this is a weak example for any citizen-data / cross-domain-profiling argument and should **not** be presented as joining up people's records. *(Verifier dropped the over-specified narrative examples — "pedigree/racehorse names," "referral centres or labs" — as not traceable to the cited guide.)*

**Legal basis.** EU pharmacovigilance law (Reg. 2019/6 for veterinary); data protection under Regulation (EU) 2018/1725 for EMA; not consent-based.

**Consent / opt-out.** Pharmacovigilance reporting is a legal/public-interest obligation; not consent-based. For the veterinary system, anonymisation minimises the human-subject question entirely.

**What is done with the data (method-agnostic, NOT attributable to Splink).** Within-database duplicate detection feeding statistical signal detection and aggregate publication on adrreports.eu/vet. No cross-domain linkage. No function creep.

**Recommendation:** confirm directly with EMA (or via an EDPS/access-to-documents route) before asserting Splink use as fact.

**Adjudications.** None found.

---

### 2.9 AIHW & Australian state/territory linkage units — TIER 3, EVALUATION (AIHW) / NEGATIVE (state units) *(verifier: SOLID)*

**What it is.** For the named target — AIHW plus the state/territory data-linkage units — **Splink is not in production.**
- **AIHW** runs in-house **SAS-based DALI** in production and is *"currently considering replacing"* it with Python-based Splink (per an ANU-hosted 2024 AIHW internship description). **Evaluation only**, on weak single-source evidence.
- **State/territory units are NEGATIVE for Splink:** WA Data Linkage Branch built **DLS3** entirely in-house; CHeReL (NSW/ACT) uses **ChoiceMaker**; SA-NT DataLink uses a **FEBRL**-derived engine. All confirmed.
- The **ABS** is the only Australian Splink adopter (see 2.3), but within *this* composite target its status is the self-reported "Used By" listing.

**Verifier corrections.** Disaggregate the blanket EVALUATION tier: AIHW = EVALUATION (weak single source), state units = NEGATIVE, ABS = OPERATIONAL_PER_SPLINK_OWN_PAGE. Soften "confirmed operational" for ABS to "reported on the maintainer-curated page (corroborated by ABS NDDA/PLIDA pages)." Mark the AIHW dataset enumeration (National Death Index, NDIS, Medicare/PBS, residential aged care) as illustrative/inferred. Treat the Office of the National Data Commissioner NDDA-first-release / DATA Act 2022 citation as **unverified** (the page could not be retrieved).

**Operational vs statistical.** All statistical/research. AIHW linkage exists to enable analysis of service pathways and outcomes; the **separation/distributed model** (identifiers held by a specialist linkage unit; content stays with custodians) governs the state units.

**Legal basis.** AIHW Act 1987 (s.29 confidentiality offence) + Privacy Act 1988 / APPs, relying on the "Required or Authorised by Law" exception plus Ethics Committee approval. State units: jurisdictional linkage/privacy legislation plus HREC approval, typically under consent waivers.

**Consent / notification / opt-out.** Generally none. Protection is structural — separation model, Five Safes, non-identifiable outputs — rather than choice-based. *(Not exhaustively verified that no unit anywhere offers any opt-out.)*

**Function creep.** Limited direct evidence; the trajectory is toward broader, enduring, cross-jurisdictional statistical assets (PLIDA, NDDA, the National Linkage Spine, PHRN cross-border linkage). No statistical-to-operational drift found.

**Adjudications.** None found.

---

### 2.10 United States — Indiana DoH / Florida / Census / All of Us — TIER 3, PILOT (+ two NEGATIVES) *(verifier: SOLID)*

Four US targets, four realities:

**Indiana Department of Health — PILOT.** A 29 May 2024 IDOH Office of Data & Analytics deck ("Probabilistic Record Linkage with Splink," Matt Simmons) shows Splink being *trialled* — motivated by "IDOH – COVID cases and vaccinations" and patient/MPI deduplication — but validated on **synthetic febrl4 data (10,000 records)**, not real Hoosier data. Real-data linkage, Databricks/ARC integration, agency boilerplates and a Master Patient Index are all listed under "Next Steps." *(Verifier correction: the "99%" figure is **match accuracy at a p=.99 threshold** (95.5% for address-based), not "true-match recall" — soften the wording.)* No public evidence of productionisation since mid-2024. Indiana does **not** appear on Splink's own Use Cases page.

**Florida Cancer Registry / FCDS — EVALUATION.** A peer-reviewed IJPDS paper (Alexandersson 2024, art. 2786) and a 2023 FCDS monograph benchmark Splink vs fastLink vs Match\*Pro on **simulated pseudopeople data** (~660,227 simulated matches; Splink 627k TP / 4 FP with SSN, 579k TP / 3 FP without). Splink scored best — but this is a methods comparison, not production, despite FCDS appearing on Splink's page. *(The 2023 monograph could not be independently re-fetched; the IJPDS paper is the reliable source.)*

**US Census Bureau — NEGATIVE.** Production tool is in-house **BigMatch**. The Bureau states verbatim: *"Staff evaluated software packages SPLINK as compared to BigMatch examining the speed, accuracy, and work requirements"* — and concluded BigMatch superior. Splink was benchmarked and rejected. Production matching (e.g. IRS-1040-to-2020-Census) uses BigMatch.

**NIH All of Us — NEGATIVE.** Linkage uses **Datavant** tokenisation/PPRL via the Center for Linkage and Acquisition of Data (CLAD) — *"a HIPAA-compliant privacy-preserving record linkage method (tokenization, provided by Datavant)"* — with **no Splink.** This is the only US target with a genuine informed-consent / withdrawal model — and it does not use Splink. *(Verifier correction: drop "mortality" and "Environmental Justice Index" from its datasets list — the cited source only supports EHR + healthcare claims.)*

**Legal basis.** Indiana: none documented in the deck (correctly reported as absent, not omitted). Census: Title 13 confidentiality (BigMatch). All of Us: informed-consent research cohort under NIH governance + HIPAA-compliant PPRL.

**Consent / opt-out.** Indiana: none mentioned (synthetic demo, no individuals processed). All of Us: broad informed consent with withdrawal.

**Function creep.** Indiana is a watch-item: the deck's stated trajectory (synthetic demo → COVID case+vaccine linkage → MPI → cross-agency "wider agency use") is exactly the statistics-to-operations path — but no realised creep yet.

**Adjudications.** None found.

---

### 2.11 Lao PDR — Shared Child Health Record — TIER 3, RESEARCH *(verifier: SOLID)*

**What it is.** A **methods study**, not an operational government deployment. Sorsavanh et al. (Journal of Medical Systems 49(1):119, 26 Sept 2025), led by **Kyoto University** with Gifu University and the Lao MoH IT team, used Splink (Fellegi–Sunter with Jaro–Winkler) as one of three approaches (deterministic, probabilistic=Splink, hybrid) to de-duplicate **20,433 real pediatric records** from the Shared Child Health Record server for Borikhamxay Province. The hard problem: Lao non-Latin tonal script, phonetic variation, and placeholder names.

**What was done.** Built a manually-verified gold standard (3,191 true matches from 5,740 candidate pairs); ran Splink and a deterministic+probabilistic hybrid; the **hybrid "resolved approximately 2,872 duplicates."** Performance: deterministic recall 67% / F1 76%; probabilistic and hybrid ~90% recall / ~90% F1. Characterised live data-quality gaps: family names missing in 32% of records, parental contact in 13%.

**The underlying SCHR system** is operational (it links immunization + hospital records); the Splink de-duplication is the *research layer* on top. There is no evidence the Splink matching was put into routine operational use.

**Verifier corrections.** Remove or mark **UNVERIFIED** every reference to **"Bahmni"** as the named hospital/EMR system — it appears in *neither* cited paper, which describe a DHIS2-based EMR + Client Registry + Electronic Immunization Registry interoperated via FHIR International Patient Summary. Soften the "Jupyter notebooks on reasonable request" code-availability detail (the verified statement covers *data*, not code).

**Registers.** SCHR server (Borikhamxay, 20,433 records); the DHIS2-based Electronic Immunization Registry; the DHIS2-based EMR/hospital record system via FHIR IPS.

**Scale.** Single-province; ~20,433 records; not national.

**Legal basis.** No statute cited. Lawful basis presented as research ethics: **Lao National Ethics Committee for Health Research approval 033/NECHR (1 Apr 2024)** plus informed consent from legal guardians. No Lao data-protection law referenced. Funding credited only to Kyoto University — **no WHO/Gavi/UNICEF/JICA link to this Splink work** (those donors support Lao's broader DHIS2 immunization infrastructure generally, not this study).

**Consent / opt-out.** Guardian informed consent obtained; no opt-out described, and no statement that guardians were told specifically about the record-linkage/de-duplication purpose (vs generic study consent). In a one-party state with no comprehensive data-protection law, rights protections around children's administrative health data should be treated as minimal/unverified.

**Function creep.** No direct evidence. Latent risk: a de-duplication method validated here could be folded into operational SCHR identity management, moving it from research to operations.

**Adjudications.** None found.

---

### 2.12 Chile — Ministry of Health — TIER 3, RESEARCH *(verifier: SOLID)*

**What it is.** A published IJPDS study (Vol 8 No 2, ADR UK Conference 2023). Two MINSAL analysts (Jorge Pacheco, Jorge Vargas) with Nicolas Libuy of UCL's Centre for Longitudinal Studies used Splink to link and deduplicate the **Chilean National Immunisation Register (~77.9M records)** against the **National School Enrolment database (~68M cumulative records)** to estimate vaccine coverage among **migrant children who lack a Chilean national ID (RUN)** and therefore cannot be matched deterministically. Splink keyed on first/second/last name and date of birth, validated against gold-standard data.

**What was done — a statistical correction.** Of **140,317 enrolled students with no national ID** (drawn from the 2022 annual enrolment cohort of ~3.6M, *not* the 68M cumulative count — the verifier flagged this denominator distinction), **52,524 (37.4%)** were linked to the immunisation register. Including this population corrected national coverage estimates upward by 2 points — from **86% to 88%.** This is aggregate statistics, not operational targeting of migrants. *(Verifier correction: the "5.2M" figure is "immunisation records lacking a national ID," not necessarily all migrants.)*

**Legal basis.** **Not stated** in the conference abstract — no statute, data-sharing agreement, ethics/IRB reference, or consent statement. Chile's data-protection regime (Law 19.628; the new Law 21.719 enacted Dec 2024, after this work) is not cited. Correctly reported as not-stated rather than asserting compliance.

**Consent / notification / opt-out.** Not addressed. No evidence migrant families were told, asked, or offered opt-out; secondary use of pre-existing registers — but this is inferred. *(The "anonymised" descriptor appeared only in an AI search synthesis, never in the primary source — it stays flagged as unverified and must not be promoted to a stated fact; the linkage is inherently individual-level/identifiable.)*

**Operational vs statistical.** Statistical/research. The linked dataset is by construction person-identifiable (it resolves named migrant children across two registers), even though the published output is aggregate.

**Function creep — flagged as context only.** A *separate* Chilean body — the National Migration Service (Servicio Nacional de Migraciones) — published a parallel 2023 IJPDS paper using **deterministic** linkage (not Splink) across police, health, education and migration data to measure irregular migration. That is a different body and is included only to signal that cross-domain migrant linkage is expanding in Chilean government from health-statistics toward migration-measurement uses. It is **not** attributed to MINSAL.

**Adjudications.** None found.

---

### 2.13 The Gambia — 2024 Census — TIER 3, downgraded to ASSERTED *(verifier: MIXED)*

**What it is.** The Gambia Bureau of Statistics conducted The Gambia's **sixth** post-independence census (and first-ever *digital* census) in May/June 2024, recording a population of **2,422,712**, supported by the World Bank, UNFPA, UNECA and Senegal's ANSD. A Post-Enumeration Survey was a documented phase. Splink's homepage states: *"Splink has been used to support the 2024 Gambian census by analysing and linking data from the census and the post-enumeration survey."*

**Why the tier moved to ASSERTED.** The **only** evidence that Splink was used at all is that single self-published homepage line. No GBoS or UNFPA methodology/technical report names Splink, its version, or configuration; the primary census report contains zero mentions of Splink, record linkage, matching, dual-system estimation, or coverage error. A single unaudited vendor self-attestation with no independent corroboration is, by definition, an ASSERTED-tier claim — and the use, even as described, is *statistical*, so labelling it "operational" was doubly misleading.

**Verifier corrections.** The census was the **sixth**, not "seventh" (the cited Preliminary Report says so, listing 1973/1983/1993/2003/2013/2024). The intercensal increase was **~540,000** (1,882,450 → 2,422,712), not "~300,000." The PES-to-census-matching / dual-system-estimation *purpose* is a reasonable inference but is **not in any located source** and must be marked as inference, not attributed fact.

**Registers.** 2024 Census enumeration records; 2024 PES records. Single-domain (census-to-PES).

**Legal basis.** **Statistics Act 2005** (Part V, s.19) — empowers GBoS to conduct the census, imposes statistical confidentiality with criminal penalties, and makes enumeration compulsory. **No contemporaneous data-protection law:** The Gambia's Personal Data Protection and Privacy Act was passed 29 Sept 2025 and assented 7 Nov 2025 — *after* the census. So there were no statutory data-subject rights and no national data-protection authority operative during the census/linkage.

**Consent / opt-out.** No opt-out — enumeration is legally compulsory. Statistical confidentiality, not consent, is the protective mechanism.

**Operational vs statistical.** Statistical only (PES coverage estimation). No cross-domain linkage; no function creep evident.

**The genuinely strong, well-sourced contribution here is the data-rights framing** — population linkage performed under a 2005 statistics-confidentiality regime with *no* contemporaneous data-protection law, compulsory participation, and no opt-out. That survives a hostile read; the Splink-tool claim does not.

**Adjudications.** None found; no DPA existed at the time.

---

### 2.14 UNHCR — TIER 2, OPERATIONAL_PER_SPLINK_OWN_PAGE *(verifier: SOLID)*

**What it is.** Splink's "Used By" page states: *"UNHCR uses Splink to analyse and enhance the quality of datasets by identifying and addressing potential duplicates."* This is a self-reported listing with **no independent corroboration.** Critically, the **one publicly inspectable UNHCR record-linkage artefact** (the `unhcr-americas/record_linkage` GitHub tutorial) uses **fastLink** (an R package), **not Splink** — and explicitly says it focuses on fastLink because it was highlighted at the UN Statistical Commission. No UNHCR methodology document, blog or paper names Splink.

**The two mechanisms must not be conflated.** UNHCR's *primary* operational deduplication is **biometric** (BIMS — fingerprint/iris 1:N matching, integral to registration in *more than 90 country operations* per UNHCR's 2023 blog — *not* the "~93" the original profile twice asserted). The probabilistic linkage (Splink-claimed, fastLink-demonstrated) is a *statistical/data-quality* workflow — building clean survey sampling universes — distinct from the biometric identity register.

**Why the tier is held, not raised.** The only evidence of operational Splink use is UNHCR's own listing; the verified operational deduplication is biometric. So `OPERATIONAL_PER_SPLINK_OWN_PAGE` honestly reflects that operational use rests on the listing, not on independent verification.

**The high-stakes context — verified verbatim.** The civil-liberties stakes here are exceptionally high and not hypothetical, even though they attach to the *surrounding registration apparatus*, not provably to Splink. **Human Rights Watch (15 June 2021)** found UNHCR collected Rohingya biometric and biographic data and shared it via Bangladesh with **Myanmar — the state the refugees had fled** — toward repatriation eligibility, covering **at least ~830,000 names**, *without informed consent* and *without a full DPIA.* Of 24 refugees interviewed, 23 said they were not told their data would be shared with Myanmar; one reported a **pre-checked "yes" consent box on an English-only receipt**; one said *"I could not say no because I needed the Smart Card."* All verified verbatim. This is textbook function creep: protection/aid identity data repurposed for state-to-state repatriation screening.

**Registers.** proGres v4 registration records; BIMS biometric records; field-partner registration lists; the PRIMES ecosystem (proGres, BIMS, RApp, the PING interoperability gateway). Domains: refugee registration, biometric identity, cash assistance, repatriation eligibility, resettlement.

**Scale.** Tens of millions of forcibly displaced people registered; "millions of refugees" in PRIMES (UNHCR self-reporting). Rohingya case: ~830,000 names with biometrics submitted Bangladesh→Myanmar.

**Legal basis.** UNHCR's 2022 General Policy on Personal Data Protection and Privacy. Four grounds for *"legitimate"* (deliberately not *"lawful"*) processing: consent; vital/best interest; mandate; safety/security — so processing can proceed *without* meaningful individual consent. UNHCR operates under the **1946 Convention on the Privileges and Immunities of the UN**, so it is **not subject to GDPR or any national data-protection regulator**, and data-subject redress is "without prejudice and subject to UNHCR's privileges and immunities." *(Verifier note: the "legitimate vs lawful" framing was verified via an analysis of the **2015** policy; the framing carries into 2022, but the 2022 policy text could not be directly fetched.)*

**Consent / notification / opt-out.** Contested and, in the documented Rohingya case, **failed** (above). For the linkage/deduplication work specifically, no evidence individuals are told, asked, or able to opt out.

**Function creep.** Strongly documented — the Rohingya case breaches UNHCR's own Voluntary Repatriation Handbook separation of registration-for-services from repatriation-eligibility assessment.

**Governance.** A UNHCR Data Protection Officer and the 2022 policy — but **no external regulator**, and HRW found only a partial risk assessment, not a full DPIA, before the Rohingya sharing.

**Adjudications.** No enforceable regulatory/court action exists — UN immunities place UNHCR beyond national DPAs and courts. HRW (2021) and ODI/Forced Migration Review published critical findings, but these are not binding rulings.

---

## 3. Cross-cutting patterns

**(a) The move from statistics to operations — real, but rarer than the logo-wall implies.** The genuinely operational, person-identifying use in this survey is concentrated in **one** place: the UK Ministry of Justice (Core Person Record real-time pilot; court record retrieval; the daily North Essex PNC→police feed). Everywhere else, the documented use is statistical/research, or is a pilot/evaluation, or is contradicted by the organisation's own pages (NHS England's live system is deterministic). The structural risk the MoJ case proves is that **the same engine serves both** — Data First (research-only, de-identified, "not for operational decision-making") and the Master Record (operational, person-identifying) are *the same library, one configuration apart.* That portability across the statistics/operations line — not any single deployment — is the finding.

**(b) The consent/opt-out gap is universal and by design.** Across every country and tier, the pattern is identical: linkage proceeds **without consent because the law was written to allow it.** UK (public task; "consent was not used by ONS"); Australia ("authorised by law"; CSA 1905); Canada (PHIPA s.45 — no consent, no ethics review required); Germany (statutory census obligation); Chile (not stated); Gambia (compulsory census, no DP law at all); UNHCR ("legitimate," not "lawful"; consent is one of four substitutable grounds). The protective mechanism is almost never individual choice — it is **statutory confidentiality, de-identification after linkage, and the Five Safes.** The defence "but it's lawful" *is* the indictment: you weren't asked, told, or given a way out, and that was the intent.

**(c) The role of MoJ openly publishing its adopter list.** The single reason this entire map is visible is that the **Ministry of Justice maintains an open-source library with a public "Used By" page.** That transparency is genuinely commendable — and it is also the source of the report's biggest discipline problem. The page is **maintainer-curated, unaudited, and uncited**, and in checked cases it is **wrong or overstated**: NHS England is listed as a user when its live system is deterministic and the Splink work is in development; the Gambia and Destatis entries carry no citation; ECCC, DfE, CMA, WRA and several councils appear with no independent corroboration anywhere. The open list is a public good *and* a trap: it must be read as "organisations that told the maintainers they use or plan to use Splink," not as audited operational fact. Half this report's verification work was distinguishing the two.

**(d) High-stakes cases.** Three deployments carry stakes far above the statistical norm:
- **UNHCR / Rohingya refugees** — the most serious documented harm: data gathered for aid shared toward repatriation screening with the persecuting state, without informed consent, beyond any regulator's reach. (The Splink link is unproven; the harm is verified; the mechanism was biometric.)
- **Lao children** — a methods study on real pediatric records in a one-party state with no data-protection law and only generic guardian consent.
- **Chile / immigration** — linkage explicitly of migrant children who lack national IDs; benign in purpose (measuring vaccine access) but in a government where a *separate* body is already linking migrant records toward migration measurement.

---

## 4. The negatives, stated plainly

To inoculate this report against the charge of finding Splink everywhere it looks, the confirmed negatives are stated as bluntly as the positives:

- **US Census Bureau — NOT Splink.** Production matching uses the in-house **BigMatch**. The Bureau evaluated Splink against BigMatch and concluded **BigMatch is superior**. Splink was benchmarked and rejected.
- **AIHW (Australia) — NOT (yet) Splink.** Production probabilistic linkage runs on the in-house SAS tool **DALI**; Splink is only "under consideration."
- **NIH All of Us (USA) — NOT Splink.** Record linkage uses **Datavant** tokenisation/PPRL via the CLAD center — a different, hash-based approach.
- **Statistics Canada — NOT Splink.** The Social Data Linkage Environment uses StatCan's own **G-Link** (Generalized Record Linkage System).
- **Australian state/territory linkage units — NOT Splink.** WA uses bespoke **DLS3**; CHeReL uses **ChoiceMaker**; SA-NT uses **FEBRL**.

Several "positives" are negatives in disguise once read closely: **NHS England's** operational system is deterministic (Splink is in-development); **Florida Cancer Registry** ran Splink only on *simulated* data; **Indiana** ran it only on *synthetic* data; **UNHCR's** only public linkage code uses *fastLink*.

---

## 5. "Do not overstate" — framing discipline and the still-uncorroborated list

**What this report deliberately does NOT claim:**
- It does **not** claim a global conspiracy or a coordinated system. These are independent bodies sharing one library (and many do not even do that).
- It does **not** claim most of these uses are illegal. Almost all are lawful by statutory design; that is the point, not a gotcha.
- It does **not** equate lawful statistical linkage with coercive surveillance. The line is held: ONS, ABS, Destatis, the Gambia census and the Chile study are statistics; only the MoJ case crosses into operational person-identification, and even there it is framed as a human-reviewed lookup aid (a framing this report rebuts but reports honestly).
- It does **not** treat Splink's "Used By" page as proof. Tier-2 and Gambia/Destatis/EMA claims are explicitly flagged as self-reported or asserted.
- It does **not** present pilots as production: Indiana, Core Person Record, the North Essex feed, and NHS England's Splink pipeline are all pilots/development, not confirmed national operations.

**Items still uncorroborated (carry into any publication as open caveats):**
1. That **Destatis** uses Splink at all — one uncited homepage sentence; no German source corroborates it.
2. That the **EMA** uses Splink — one uncited line; EMA's own dedup methodology omits it.
3. That **UNHCR** uses Splink — listing only; its public code uses fastLink.
4. That **Splink (vs generic tooling) performed the linkage** at MCCSS, ONS's Census Coverage Survey step, the Gambia census, and ABS's 2024 NLS/NDDA — in each case the linkage is real but the *Splink attribution* is self-reported or the source names only "Fellegi–Sunter."
5. The **specific statutory lawful basis** for the MoJ operational uses (inferred public task, not cited).
6. Whether the **North Essex PNC→police feed** or the **Core Person Record** has scaled beyond pilot.
7. Whether **Indiana** has productionised since mid-2024.
8. The asserted **2023 German Constitutional Court** register-census proportionality ruling (no verifiable citation).
9. Exact **record/person counts** for the ABS spine, the Data First de-identified datasets, and the AIHW datasets (inferred).
10. UNHCR's exact biometric-capture granularity ("10 fingerprints," "aged 5+") and the precise country count (source says "more than 90," not "~93").
11. The named hospital/EMR system in the **Lao** SCHR (the "Bahmni" attribution is unsupported and removed).
12. Whether linked individual-level outputs were retained, destroyed, or fed to any operational system in the **Chile** and **Gambia** cases.

---

## 6. Consolidated source list

**Splink (maintainer):** Splink "Used By" / Use Cases page and documentation (`moj-analytical-services.github.io/splink`); GitHub `moj-analytical-services/splink`; "Running Splink in Production at the MoJ" blog (29 Jan 2026); ISI WSC 2025 abstract #2922 (Linacre); GOV.UK "Splink: MoJ's open source library …" (2021/2022).

**UK MoJ:** GOV.UK Algorithmic Transparency Records `moj-splink-master-record` (6 Oct 2025) and `moj-data-first-splink` (17 Dec 2024); MoJ Data First guidance; ADR UK Data First; IJPDS 1794, 1920.

**UK ONS:** 2021 Census linkage to DWP master key & encrypted NINo methodology; Linkage methods for Census 2021; Census 2021 to PDS linkage report; "Census processing and data protection"; Secure Research Service; ADR UK (IDS accreditation); SPD–Demographic Index linkage; ONS Splink case study (`Data-Linkage/Splink-census-linkage`).

**UK NHS England:** Master Person Service page (NHS England Digital); MPS data-linkage algorithm technical details; IJPDS 3271 (Laidler et al.); Data Linkage Hub overview (NHS England Data Science); `NHSDigital/mps_diagnostics`; Health and Social Care (Safety and Quality) Act 2015.

**UK wider sector:** OHID/MoJ "Pathways between probation and addiction treatment" methodology & report (BOLD); Government Analysis Function BOLD spotlight; DBT "Building a reusable data matching product" (digitaltrade.blog.gov.uk); LOTI Rough Sleeping Insights Project; techUK rough-sleeping note; Cities Today (Lewisham Pupil Premium); Data in Government Splink blog (2022); ATRS Hub.

**Australia:** ABS Person Linkage Spine; ABS PLIDA pages (data & legislation; privacy statement); ABS National Disability Data Asset; IJPDS 2818, 1566; CSA 1905 (AustLII s.19); ANU/AIHW internship placement page (DALI); AIHW data-linkage & privacy pages; WA DLS3 (PMC7299493, PMC7477781); CHeReL/ChoiceMaker (PMC8142947); SA-NT DataLink/FEBRL; CVDL (VAHI); Queensland Data Linkage Framework; PHRN profile (PMC7482513); Office of the National Data Commissioner NDDA release *(unverified at fetch time)*.

**Germany:** Splink homepage (Destatis line); Destatis Registerzensus pages; WISTA 6/2022 (Dittrich et al.); WISTA 4/2025 (Weiand); arXiv 2104.09677 (Ranbaduge/Christen/Schnell); BMI RegMoG FAQ; BVerfG 19 Sept 2018 (2 BvF 1/15, German source).

**Canada:** Splink Use Cases (MCCSS/ECCC); IJPDS 1689 / PMC8900651 (Ontario SA-health linkage); ICES publication record; Ontario MCCSS personal-information-management & data.ontario.ca DI inventory; CRDCN holding; Statistics Canada G-Link & SDLE overview; ECCC GHG Reporting Program (context).

**EU:** Splink homepage (EMA line); EMA EudraVigilance Veterinary; adrreports.eu/vet; Veterinary Union Pharmacovigilance Database Best Practice Guide; GVP Module VI Addendum I; EudraVigilance Data Protection Notice (Reg. 2018/1725); EVVET Data Warehouse user manual.

**UNHCR:** Splink "Used By" (UNHCR line); `unhcr-americas/record_linkage` (fastLink); Joint Data Center registration enhancement; UNHCR PRIMES/PING/biometrics blogs; HRW "UN Shared Rohingya Data Without Informed Consent" (15 June 2021); ODI Rohingya analysis; UNHCR General Policy on Personal Data Protection and Privacy 2022 (Refworld); EJIL:Talk! UNHCR data-protection analysis.

**Gambia:** Splink homepage (Gambia line); UNFPA Gambia 2024 Census launch; 2024 Census Preliminary Report (GBoS/UNFPA); UNFPA WCARO digital-census note; GBoS data downloads; Techhive Advisory review of Gambia PDPP Act 2025; The Point (DP bill timeline).

**Laos:** Splink Use Cases (SCHR/Academia); Sorsavanh et al., J. Med. Syst. 49(1):119 (PMC12474658; Springer 10.1007/s10916-025-02260-6); Sorsavanh et al., SHTI240657 (SCHR background); DHIS2 Lao EIR milestone; Gavi Digital Health Information programme (context).

**USA:** IDOH "Probabilistic Record Linkage with Splink" deck (in.gov/mph, 29 May 2024); IJPDS 2786 (Florida/FCDS); FCDS Splink feasibility monograph 2023 *(not independently re-fetched)*; US Census Bureau Record Linkage page (BigMatch); FY2024 CSRM Annual Report; Datavant/CLAD press release; PMC9645066 (All of Us Datavant tokenisation); Splink Use Cases (FCDS, US DHA).

**Chile:** IJPDS 2348 (Libuy, Pacheco, Vargas — immunisation/school linkage); IJPDS Vol 8 No 2 issue listing; Splink homepage (Chile MoH + UCL line); IJPDS 2188 (Harnecker & Mallea, National Migration Service — function-creep context).

*Refuted or self-reported claims are corrected or flagged in-line, as noted throughout. The mathematics of Splink is not in question anywhere in this report; the issue is consent, transparency, scope, and the gap between what a vendor's adopter list claims and what primary sources can prove.*
