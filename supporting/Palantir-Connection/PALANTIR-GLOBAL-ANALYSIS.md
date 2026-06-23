# The Operational Twin Goes Global: Palantir Across Every Country That Runs Splink

*Post 7 in the "Quiet Joining-Up" series. Companion to the UK "Operational Twin" post.*

---

## 1. Executive summary and honest thesis

This series began with a narrow, undismissable observation about the UK: the same state that quietly runs **Splink** — the Ministry of Justice's free, open-source probabilistic record-linkage library used by statisticians to join up citizen records — also runs **Palantir**, a proprietary, paid, operational data-integration and analytics platform, inside policing, immigration, defence and health. In the UK, NHS England is the tightest knot: it is simultaneously a Splink user (research linkage) and the Palantir Federated Data Platform customer (operational direct-care integration) — different tools, different functions, same single body.

This post tests whether that pattern travels. It maps Palantir's documented government footprint across the **ten jurisdictions known to adopt Splink** (UK, US, Germany, Australia, Canada, Chile, the EU, the Gambia, Laos, and UNHCR), using eight adversarially-verified country/body profiles.

**The honest thesis, stated plainly:**

> Splink and Palantir are **not the same tool**, and **there is no evidence anywhere on Earth that Palantir uses, supplies, competes for, or touches Splink.** They are unrelated. What is real, and what this series documents, is a *structural coincidence with teeth*: the same wealthy, capacity-rich governments that run benign statistical linkage (Splink) **also** run Palantir's proprietary **operational** platforms — and they run Palantir most heavily where the stakes are highest (policing, immigration, defence, intelligence). The civil-liberties weight sits almost entirely on the Palantir side. The most operational deployment is the **United States**, Palantir's home market. The only **binding court ruling against a Palantir deployment** anywhere is **Germany's Federal Constitutional Court (2023)** — the "ruled unlawful" parallel to the UK Splink-side adjudications, but on the Palantir side and far heavier.

**The link, classified honestly, by strength:**

- **DIRECT (same body runs both, different tools/functions):** Only the **UK** (NHS England). No second example exists. *(Covered in the companion post; included here only as the benchmark.)*
- **SAME_DOMAIN_SAME_COUNTRY (Palantir present in-country, same broad "joining-up government data" domain, but different body/tool/purpose):** the **United States**.
- **THEMATIC_ADJACENCY (same country/sector and shared record-linkage *theme* only — different body, different data domain, different tool):** **Germany, Australia, Canada, EU institutions, UN/humanitarian.**
- **NONE_FOUND (no Palantir presence at all):** **the Gambia, Laos** (and **Chile**, per the global scorecard pass).

A critical correction applied throughout: several profiles were initially tiered too high. Under adversarial review, **Germany and Canada were downgraded from SAME_DOMAIN_SAME_COUNTRY to THEMATIC_ADJACENCY**, and the **US was downgraded from THEMATIC_ADJACENCY to SAME_DOMAIN_SAME_COUNTRY** (in the US the only true common factor is "US federal data-integration domain"; Splink is essentially *non-operational* there). Where a profile's *own evidence* said "different body, different tool, different domain," the tier must read THEMATIC_ADJACENCY, not SAME_DOMAIN. That discipline is applied below.

---

## 2. Per-country / per-body sections

### United States — `SAME_DOMAIN_SAME_COUNTRY` (Palantir's home turf)

**What Palantir does:** The US is Palantir's largest single government market. Per the **FY2025 10-K**, government was **~54% of $4.5bn FY2025 revenue (~$2.43bn)**, with **~74% of total revenue from US customers.**

> **Correction applied:** An earlier draft claimed "$1.88B of $4.5B from the government segment." That figure has no source and **contradicts the 10-K's own 54% split** (54% of $4.5bn ≈ $2.43bn, not $1.88bn). The unsupported "$1.88B" is removed; the corrected, 10-K-consistent figure is **~$2.43bn**.

Palantir is deeply **operational** across the federal government:

- **ICE / DHS — ImmigrationOS:** ~$30M modification to an existing ICE contract, awarded ~April 2025, prototype due Sept 25 2025, running through Sept 2027; cited as supporting Executive Orders 14159 and 13773. Purpose: near-real-time visibility into the "immigration lifecycle" — identify/apprehend removal-priority individuals, track self-deportations, streamline deportation logistics.
- **DoD/Army — Maven Smart System:** ceiling raised to **~$1.3B through 2029** (from ~$480M), demand-driven increase reported May 23 2025. Battlefield AI/targeting and sensor fusion.
- **Army — TITAN:** **$178.4M OTA**, awarded March 6 2024, 10 AI-enabled ground-station prototypes.
- **Army — Vantage:** ~$458M, four-year, unified data management.
- **Army enterprise agreement:** reported **up to $10B over 10 years** (Aug 2025). *Inline caveat (kept everywhere it appears): this is an "up to"/ceiling figure from trade press, **not obligated spend.***
- **CDC:** **$443M, five-year** consolidated disease-surveillance "Common Operating Picture" contract (announced Dec 2022), uniting HHS Protect / ASPR Engage / Tiberius / DCIPHER.
- **HHS:** Tiberius (vaccine allocation, ~$31M) and HHS Protect (~$24.9M no-bid, April 2020).
- **IRS / federal data consolidation:** reporting (NYT; The Intercept, April 2026) that Palantir is building a "mega-database"/single searchable hub off Trump's **March 20 2025 EO** on inter-agency data sharing, with reported talks with SSA and Dept. of Education. *Hedge retained: the "mega-database" framing is sourced to reporting and a June 17 2025 congressional letter (Wyden, Ocasio-Cortez); **Palantir disputes** that it can "proactively share data across federal government sources" (May 30 2025 blog); no contract value is public; no adjudication.*
- **USCIS (Dec 2025, Fortune):** a new Palantir platform contract at "another federal agency that works with ICE." *Unverified flag added: single-source trade reporting; scope/value not independently confirmed.*

**Datasets (Palantir):** IRS taxpayer records, SSA data, Dept. of Education data (reported talks), Medicaid/HHS health data (per EFF, fed into an ICE-used tool — *allegation, in active litigation, not adjudicated*), ICE immigration/visa-overstay data, CDC/HHS pandemic data, DoD/Army sensor/targeting/logistics data.

**The Splink side in the US is essentially negative/non-operational:** the **Census Bureau evaluated Splink against its in-house BigMatch and chose BigMatch**; NIH's **All of Us** uses **Datavant** privacy-preserving record linkage via CLAD, **not Splink**. *(The "Indiana pilot" of Splink referenced in the lead brief was never located in primary sources and is excluded from all findings.)*

**Connection tier — corrected to SAME_DOMAIN_SAME_COUNTRY:** The only documented common factor is the **US federal data-integration domain**. There is **zero** shared body, dataset, tool, contract, or document; Palantir does not use Splink; Splink is operationally absent in the US. The earlier "same broad joining-up trajectory" framing is **the author's inference, not a documented characterization** — flagged as such, not presented as a finding.

**Adjudications:** No US court or regulator has issued a final ruling holding Palantir's federal data use unlawful. **EPIC v. ICE** was a FOIA suit settled ~Jan 2020 (attorneys' fees recovered) — transparency litigation, not a substantive ruling. **EFF** litigation/amicus activity (2025–26) over DOGE/OPM access, IRS taxpayer data, and a State/DHS mass-surveillance program is **ongoing**, no final adjudication against Palantir.

---

### Germany — `THEMATIC_ADJACENCY` (but home to the one genuine Tier-1 ruling)

**What Palantir does:** Palantir **Gotham** powers automated cross-database police data-analysis in multiple German states — Hesse **"hessenDATA"** (since 2017), North Rhine-Westphalia **"DAR"** (~2019/20), Bavaria **"VeRA"** (operational 2024), and Baden-Württemberg (**contract signed March 2025, ~€25M** under a price-binding clause that otherwise would have ~doubled to €50M, reportedly no exit clause — **deployment only from Q2 2026, i.e. contracted, not yet live**). 2025 reporting (heise) indicates use has broadened to minor crimes.

> **Corrections applied:** (1) The Hesse **"€0.01 nominal purchase order / true price secret"** figure is uncorroborated secondary reporting with no primary procurement citation — flagged unverified, not stated as near-fact. (2) **NRW and Bavaria contract *values* are not cited anywhere** — only the *deployments* are supported; any implied figure is removed. (3) The GFF Bavaria/VeRA constitutional complaint was filed **23 July 2025** (not "2024/2025"). (4) Baden-Württemberg is **prospective**, not a live system.

**The landmark adjudication — the "ruled unlawful" parallel on the Palantir side:**

> **Bundesverfassungsgericht (Federal Constitutional Court), First Senate, Judgment of 16 February 2023, 1 BvR 1547/19 (Hesse) and 1 BvR 2634/20 (Hamburg).** The Court struck down **§25a(1) 1st alt. HSOG (Hesse)** and **§49(1) 1st alt. HmbPolDVG (Hamburg)** — the automated police data-analysis powers — as **unconstitutional** for violating the **right to informational self-determination** (Art. 2(1) read with Art. 1(1) Basic Law), because the statutes set insufficient intervention thresholds and permitted dragnet "analysis by association" sweeping in unsuspected third parties. **Hamburg's provision was declared void; Hesse's was allowed to continue under restrictive conditions until 30 September 2023.**

**Crucial precision (verified against the court's own English judgment text):** the BVerfG judgment **explicitly names Palantir** — it records that the Land Hesse "purchased the 'Gotham' operating system from the software company Palantir" and ran it "under the name hessenDATA." *(Several draft profiles wrongly claimed the ruling "does not name Palantir," or relied only on the press release, which names only "hessenDATA." The full judgment text names Palantir and Gotham. This correction is applied series-wide.)*

**Lawyer's caveat, kept:** the ruling struck down the **enabling state statutes** for inadequate thresholds; it did **not** hold Palantir's software unlawful *per se*. Follow-on **GFF** complaints (Bavaria/VeRA filed 23 July 2025, with Chaos Computer Club support; plus NRW and revised-Hesse challenges) remain **pending**.

**The Splink side is entirely separate:** the **German Federal Statistical Office (Destatis)** is listed verbatim on Splink's official page — it "uses Splink to conduct projects in linking register-based census data."

**Connection tier — corrected to THEMATIC_ADJACENCY:** different body (state police/interior ministries vs. the federal statistics office), different data domain (criminal/security intelligence vs. anonymised census-register statistics), different tool (Gotham vs. open-source Splink), and **no shared data or infrastructure**. The profile's own caveats conceded "same domain/body is NOT met," so SAME_DOMAIN overstated the tie. The honest tier is THEMATIC_ADJACENCY — same country + shared record-linkage *theme* only. **No Splink↔Palantir link exists; the Splink page names neither Palantir nor police.**

---

### Australia — `THEMATIC_ADJACENCY`

**What Palantir does (national-security / law-enforcement / defence domain):**

- **Department of Defence — Foundry:** ~$26M+ cumulative since 2013; **$7.6M one-year limited-tender contract** via AusTender **11 Feb 2026** for the Cyber & Electronic Warfare Division (Defence's biggest Palantir contract to date), plus a ~$7.1M 2024 Foundry contract; reporting of embedded Palantir staff.
- **AUSTRAC:** **$8.1M data-analytics contract (2023)** grown **past $12M via five variations** within ~12 months.
- **ACIC:** criminal-intelligence analytics; a leaked Palantir training manual describes a system holding **~42M data points** on Australians (intercepts, police/government databases, location data), ~$5.7M committed.
- **Nov 2025:** Palantir Foundry + AIP assessed to **IRAP PROTECTED** level, broadening eligible government use.

> **Corrections / hedges applied:** (1) The **ACIC "Gotham" product name** and the **~42M-data-points** figure rest on a **single leaked-manual Crikey story** — explicitly marked single-source/uncorroborated, not stated as a confirmed contracted product. (2) **ASD** as a Palantir customer is "reported, no value/date/use verified." (3) **Victorian Dept. of Justice** is a single advocacy-source claim (Digital Rights Watch), state-level, unverified, outside the federal scope. (4) The **Future Fund equity stake** is "reported between ~$100M and >$160M depending on source." (5) Dollar totals (~$50–60M federal; ~$26M Defence; $5.7M ACIC) carry an inline **"approximate / per secondary reporting (AusTender returned 403 to automated fetch)"** hedge.

**The Splink side:** the **Australian Bureau of Statistics (ABS)** used Splink **for the first time in 2025** to build the **Person Linkage Spine** for **PLIDA** (formerly MADIP), integrating **Medicare** (Services Australia), **DOMINO Centrelink** (DSS) and **Personal Income Tax** (ATO), covering Jan 2006–Jun 2025, for approved-researcher statistical use. *(Splink also underpinned the 2024 National Linkage Spine for the National Disability Data Asset.)*

**Connection tier — THEMATIC_ADJACENCY (confirmed, not upgraded):** Palantir sits in **different bodies** (Defence/AUSTRAC/ACIC/ASD — *not* ABS/ATO/DSS/Services Australia), a **different data domain** (national security/law enforcement vs. de-identified statistical research), and a **different tool**. The profile checked and found **NO Palantir contract with the ABS/ATO/DSS/Services Australia and NO Palantir touch on the Spine/PLIDA** — absent, not merely unsearched. No Australian court has adjudicated Palantir.

---

### Canada — `THEMATIC_ADJACENCY`

**What Palantir does:**

- **DND / CANSOFCOM (JTF2) — Gotham:** sole-source contract from **CAD 14.4M (signed 27 Mar 2020)** expanded to **~CAD 44.4M via 12 amendments** (DND reports ~**CAD 46.8M spent**), preceded by a **CAD 997,434** sole-source pilot (28 Mar 2019). **Kept secret for ~5 years**, surfacing only Sept 2025 after MP questioning. Plus a ~CAD 3.7M **Foundry** evaluation (intermittent 2022–2024).
- **Ontario Provincial Police (OPP) — Gotham:** confirmed Oct 2022; **CAD 36.6M contract re-awarded Oct 2023**; configuration undisclosed; contracts shielded under Ontario's Financial Administration Act exemption (pre-crime / predictive-policing criticism).
- **Federal Supply Arrangement (SLSA):** Palantir added via Carahsoft, **Jan 2024–Jul 2028**, opening licences to all federal departments.

**The adjudication (Canadian, on a Palantir executive):**

> **Conflict of Interest and Ethics Commissioner (Mario Dion), 16 Sept 2020:** ruled Palantir Canada president **David MacNaughton** (former Ambassador to the US) contravened the **Conflict of Interest Act** by pitching Palantir's COVID-19 services to senior officials; **nine officials (incl. Freeland, Bains) ordered to restrict dealings for one year**; MacNaughton consented; no contract resulted.

> **Corrections applied:** (1) The **MCCSS "Social Assistance database 2003–2016 linked to the Registered Persons Database"** study (PMC8900651) used **deterministic/probabilistic "many-to-1 hybrid" methods and did NOT name Splink** — it must be **decoupled** from the Splink attribution. MCCSS remains a Splink user *per the MoJ user list*, but that specific RPDB linkage is **not** a Splink example. (2) The facial-recognition / civilian-social-media-surveillance claim against the military Palantir contract is **SPECULATIVE** — the cited source ties the capability to **Meltwater and Clearview AI**, not to a documented Palantir capability — quarantined to the unverified list, removed from the controversies narrative.

**The Splink side:** **Ontario MCCSS Data Integration Unit** (Splink is its main linkage tool) and **Environment and Climate Change Canada** — social-services and environmental administrative linkage. **Statistics Canada uses its own G-Link / SDLE, not Splink.**

**Connection tier — corrected to THEMATIC_ADJACENCY:** different body (OPP/DND vs. MCCSS/ECCC), different tool (Gotham/Foundry vs. Splink), different data domain (defence/policing vs. social-assistance/environment), **zero dataset/agency/tool overlap**. The only overlap is country and, incidentally, province (Ontario). "Same domain" was contradicted by the profile's own text; the "same-province trajectory" rationale is an unsourced inference and cannot drive the tier. No Palantir presence in MCCSS or ECCC; Palantir does not use Splink.

---

### EU institutions (Europol, Frontex, EMA) — `THEMATIC_ADJACENCY`

**What Palantir does:**

- **EUROPOL — Gotham:** procured as a subcontractor (Capgemini Nederland BV) under a **2012 framework contract**; **€5M initial 2012 contract, ~€7.5M framework total (~€4M spent by June 2020)**; **tested 2016, in continuous operation since mid-2017, used until Q3 2021** before Europol replaced it. Extreme opacity: Europol released **only 2 of 69 requested documents** (trade secrets / public security), and one disclosed record showed Europol **considered legal action against Palantir**.
- **FRONTEX — none found.** Frontex's analytics are reported to rely on Microsoft, not Palantir.
- **EMA — none found** for Palantir. EMA is the *Splink* user.

> **Corrections applied:** (1) **"Social-media posts"** is removed from the Gotham dataset descriptions — the primary source (Monroy/digit.site36) lists **contact lists, radio-cell query tables, travel histories, photos, location data**, not social media. (2) The unsourced **"Dutch authorities hold 45,000+ Palantir documents"** claim is removed. (3) Gotham operational start corrected from "~2016" to **"tested 2016, continuous operation since mid-2017."** (4) The **€5M vs ~€7.5M** split is surfaced inline, not buried.

**The Splink side:** the **European Medicines Agency** is listed verbatim on the Splink page — it "uses Splink to detect duplicate adverse event reports for veterinary medicines" (EudraVigilance Veterinary), a pharmacovigilance/data-quality function.

**A regulator action (not a court ruling):** the **EDPS** order of **3/10 Jan 2022** required Europol to **erase data on individuals with no established criminal link** (6-month filtering window) across its **~4-petabyte** bulk data store. *Hedge kept: sources do **not** establish this was specifically about the Palantir Gotham system; the EDPS also separately objected to Europol's use of Clearview AI (linked to Palantir co-founder Peter Thiel).*

**Connection tier — THEMATIC_ADJACENCY (confirmed):** different EU body (Europol vs. EMA), different data domain (counter-terror/law-enforcement network analysis vs. veterinary pharmacovigilance), different tool. No shared body, dataset, or tool; no Splink↔Palantir link. The BVerfG ruling is a member-state matter, not an EU-institution one.

---

### UN / humanitarian (WFP, UNHCR) — `THEMATIC_ADJACENCY`

**What Palantir does:** Palantir's documented humanitarian footprint is with the **World Food Programme (WFP)**, **not** UNHCR.

- **WFP — Palantir Foundry partnership**, announced **5 Feb 2019**, five-year term, **reported ~$45M** (*not stated in WFP's own press release — reported by press/Privacy International; flagged unconfirmed in primary source*). Unifies WFP's programmatic, operational, supply-chain and beneficiary/partner/supplier/transporter data across ~80 countries (2019 figure) serving ~90 million people. By **June 2026** Privacy International calls Palantir the **"cornerstone of the WFP data ecosystem,"** spanning **120 countries**, warning of partner data integrated into Foundry without informed consent.
- A pre-2019 **"Optimus"** pilot in Iraq claimed **>US$30M** savings (WFP-stated), with a clearly-labelled **~$100M/year-at-scale** projection. *(The looser "$26–30M" lower bound is dropped in favour of the sourced ">$30M.")*

> **Corrections applied:** (1) Pin **"90 million people" to 2019** and **"120 countries" to 2026** — do not present them as simultaneous. (2) The Palantir = hessenDATA identification (in the German adjudication note) is attributed to the **full judgment text / reporting** (the press release names only hessenDATA). (3) "CIA/In-Q-Tel-funded" kept only as **attributed critic framing**.

**The Splink side:** **UNHCR** appears on Splink's user list for probabilistic deduplication of refugee registration lists — **but UNHCR's actual public code (`unhcr-americas/record_linkage`) uses `fastLink` (R), not Splink.** Splink merely *lists* UNHCR.

**Conflation corrected:** the lead's "$45M Building Blocks deal" wrongly merged two separate WFP projects. The **Palantir Foundry analytics deal** and **"Building Blocks"** (WFP's permissioned-blockchain cash-transfer project in Jordan, which integrates UNHCR iris-biometric IDs) are **distinct**. **Building Blocks is not a Palantir product.**

**Connection tier — THEMATIC_ADJACENCY (confirmed):** Palantir at WFP (Foundry) vs. record-linkage at UNHCR (fastLink) — **different UN bodies, different unrelated tools**, sharing only the humanitarian data-aggregation *domain*. Not SAME_DOMAIN_SAME_COUNTRY (these are distinct UN bodies, not one country's institutions); not DIRECT. No Palantir contract at UNHCR; Palantir does not use Splink. **No court or regulator has adjudicated Palantir's WFP work.**

---

### Chile / Latin America — `NONE_FOUND` (Palantir side)

Per the global scorecard pass, **Chile's Splink use is real and benign** — the Ministry of Health + UCL used Splink to link **migrant immunisation records** (probabilistic linkage to improve estimates of migrants' access to services). **No Palantir government footprint in Chile was found** in this research. The connection is therefore **NONE_FOUND** on the Palantir side: a clean negative, with a poorer-country adopter using the free open-source tool for a public-health purpose and zero Palantir entanglement. *(Marked as a search-pass negative, not exhaustive proof of absence.)*

---

### The Gambia / Laos — `NONE_FOUND`

**No evidence of any Palantir presence** — contract, deployment, pilot, partnership, or proposal — was found in **the Gambia** or **Laos** across web search, SEC disclosures, serious journalism, and Palantir's own customer disclosures.

- **The Gambia:** Splink used for **2024 census / post-enumeration deduplication**. No Palantir customer listing, procurement record, or filing references any Gambian body.
- **Laos (Lao PDR):** Splink used to deduplicate **pediatric records in a Shared Child Health Record project** (notable for non-Latin Lao-script matching). No Palantir reference. Mainland low-income SE Asia surveillance (Myanmar, Cambodia) is documented as **Chinese-technology-driven, not Palantir.**

> **Corrections applied:** (1) The WFP open letter was signed by **65 organisations and individuals** (organised by the Responsible Data community), not "~60 civil-society groups." (2) The **NHS FDP** figure: **core platform ~£330M over seven years**, with a **total programme/associated-services envelope reported up to £480M.** (3) The claim that "Palantir government deployments are typically high-visibility and SEC-material at any scale" is re-labelled **analyst inference**, not fact — it is the basis for the high-confidence NONE_FOUND call and must be visible as a judgment, since small donor-funded/sub-contracted engagements are exactly what a search can miss.

**Why the clean negative matters:** the two poorest Splink adopters use a **free, open-source tool** for benign statistical/health linkage with **zero Palantir entanglement** — the polar opposite of the rich-country jurisdictions where Palantir's proprietary operational platforms were deployed and, in Germany, constrained by a constitutional court. **Absence of evidence is not absolute proof of absence**, but for any *material* government deployment, confidence in NONE_FOUND is high.

---

### Global strategy — `SAME_DOMAIN_SAME_COUNTRY` (comparative backbone)

**Financials (SEC / Q4 2025):** FY2025 revenue **~$4.5bn**; **~54% government / ~46% commercial**; full-year government revenue +53% YoY, commercial +60% YoY; US commercial accelerating to triple-digit YoY growth by Q3 2025. Government remains the strategically anchoring segment.

**Strategic pillars:** (1) **US defence anchor** — Maven IDIQ $480M → ~$1.3bn ceiling through 2029; **~$10bn** US Army enterprise agreement (July 2025, *ceiling not obligated spend*). (2) **US immigration** — ImmigrationOS, $30M sole-source / up to $159M through Sep 2027, fusing IRS/SSA/DMV/passport/ALPR data. (3) **NATO** — Maven via NCIA, signed 25 Mar 2025. (4) **Ukraine** — Maven battle-tested (mixed results); Jan 2026 Brave1 Dataroom on Palantir infrastructure. (5) **Israel/IDF** — Jan 2024 "strategic partnership" (see NOT-supported list re Gaza-targeting allegations). (6) **Five Eyes / Europe** — UK (NHS FDP; Lighthouse Reports: **34+ UK state contracts, £670m+ cumulative** — *reputable-journalism aggregates, line items not each re-verified*), Australia, Canada, EU policing (Europol Gotham).

---

## 3. Cross-country scorecard

| Country / body | Splink use (tier) | Palantir gov footprint (tier) | Key adjudication |
|---|---|---|---|
| **United Kingdom** | Pervasive (ONS, NHS England, MoJ Data First, MoD, UKHSA, DfE, etc.) | **DIRECT** — NHS England runs *both* (Splink for research linkage; Foundry FDP for operational care). Different tools/functions, same body. | None binding against Palantir; FOI/political scrutiny only *(see companion post)* |
| **United States** | Pilot/evaluation/**negative** (Census chose BigMatch; All of Us uses Datavant) | **SAME_DOMAIN_SAME_COUNTRY** — Palantir dominant & operational (ICE, DoD, CDC/HHS, IRS) in *different* bodies | None final against Palantir; EPIC FOIA settled 2020; EFF litigation ongoing |
| **Germany** | Destatis (register-census linkage) | **THEMATIC_ADJACENCY** — Gotham in Hesse/NRW/Bavaria police; Baden-Württemberg contracted (Q2 2026) | **BVerfG 16 Feb 2023** — Hesse/Hamburg automated-analysis laws unconstitutional; **Palantir & hessenDATA named in the judgment** *(Tier-1, the flagship ruling)* |
| **Australia** | ABS (Person Linkage Spine / PLIDA, first used 2025) | **THEMATIC_ADJACENCY** — Defence/AUSTRAC/ACIC; *no* Palantir at ABS/ATO/DSS | None in Australia; only the German BVerfG (foreign precedent) |
| **Canada** | Ontario MCCSS; Environment & Climate Change Canada | **THEMATIC_ADJACENCY** — DND/CANSOFCOM ($46.8M, secret 5 yrs); OPP ($36.6M) | **Ethics Commissioner, Sept 2020** — Palantir Canada president breached the Conflict of Interest Act |
| **EU institutions** | European Medicines Agency (veterinary pharmacovigilance dedup) | **THEMATIC_ADJACENCY** — Gotham at Europol (2012–Q3 2021); none at Frontex/EMA | **EDPS Jan 2022** erase-order (Europol bulk data; *not established to be Gotham-specific*) — regulator, not court |
| **UN / humanitarian** | UNHCR (lists Splink; public code uses *fastLink*) | **THEMATIC_ADJACENCY** — Palantir Foundry at WFP (2019, reported ~$45M); none at UNHCR | None against Palantir's humanitarian work |
| **Chile / LatAm** | Min. Health + UCL (migrant immunisation linkage) | **NONE_FOUND** | None |
| **The Gambia** | 2024 census / post-enumeration linkage | **NONE_FOUND** | None |
| **Laos (Lao PDR)** | Child health record deduplication | **NONE_FOUND** | None |

---

## 4. The standout findings

**(a) Germany's Constitutional Court — the "ruled unlawful" parallel, on the Palantir side.** The **BVerfG's 16 February 2023 judgment** (1 BvR 1547/19; 1 BvR 2634/20) is the **only binding court ruling against a Palantir-enabled deployment anywhere in the world.** It struck down Hesse's and Hamburg's automated police data-analysis statutes for violating informational self-determination, voided Hamburg's provision outright, and time-limited Hesse's to 30 Sept 2023. The **judgment text explicitly names Palantir and Gotham/hessenDATA** — a fact that several draft profiles got wrong by relying on the press release. *Honest framing:* the Court invalidated the **enabling statutes** for inadequate thresholds, not Palantir's software *per se*. Yet states keep adopting Gotham (Baden-Württemberg, March 2025), and **GFF's complaint against Bavaria's VeRA (filed 23 July 2025) is pending** — the litigation is live.

**(b) The US federal data-consolidation drive.** Off the **20 March 2025 EO** eliminating inter-agency data silos, Palantir is reported (NYT; Intercept, April 2026) to be building an IRS-centred **"mega-database"** unifying tax, immigration, and Social Security records — the most consequential "joining-up of citizen data" anywhere. *Honest framing:* this is **reporting- and congressional-letter-sourced; Palantir disputes it; no contract value is public; no court has ruled.* It is the loudest version of the series' core anxiety — but it is allegation/reporting, not adjudicated fact.

**(c) The UN/WFP refugee-data controversy.** The 2019 WFP–Palantir Foundry partnership (reported ~$45M, **unconfirmed in WFP's own release**) drew an open letter from **65 organisations and individuals**, and by **2026** Privacy International calls Palantir the **"cornerstone of the WFP data ecosystem"** across 120 countries, warning of partner data flowing into Foundry without informed consent — the aggregation of **vulnerable-population data** inside a US national-security-linked firm. *Honest framing:* the much-cited "refugee data" angle is partly a **conflation** — the *record-linkage* of refugee lists is **UNHCR's** (using fastLink, not even Splink), and **Building Blocks is not Palantir.** Palantir's documented humanitarian footprint is WFP operational/supply-chain data.

---

## 5. The combined civil-liberties + foreign-ownership picture

Two threads converge globally.

**Civil liberties.** The weight sits **overwhelmingly on the Palantir side.** Splink's documented uses are statistical, research, census, health-administration, and humanitarian deduplication — benign joining-up by statistics and research bodies. Palantir's documented uses are **operational**: deportation targeting (US ICE ImmigrationOS), battlefield targeting (Maven, TITAN), police association-mapping (Germany, Europol, OPP), and cross-agency citizen-data consolidation (the US IRS effort). The one constitutional court to rule found the **Palantir-enabled** dragnet a "distinct, serious" interference with informational self-determination. Where Splink has drawn scrutiny, it is transparency/governance scrutiny of statistical linkage; where Palantir has drawn scrutiny, it is over **surveillance, enforcement, and targeting**.

**Foreign ownership / sovereignty.** A recurring, cross-jurisdiction pattern: a **US-headquartered, In-Q-Tel-seeded, Thiel-associated** firm holding **operational** contracts over other nations' citizen, police, defence, and humanitarian data — frequently via **sole-source / limited-tender / secret** procurement (Germany's direct "urgency" award; Australia's limited tenders; Canada's 5-years-secret, 12-amendment CAD 46.8M contract; Europol releasing 2 of 69 documents; Baden-Württemberg's reported no-exit-clause lock-in). This raises dependency and data-sovereignty concerns that are **specific to Palantir's proprietary model** and have **no analogue on the open-source Splink side** — Splink is free, inspectable, and self-hosted.

The combined picture is not "Splink leads to Palantir." It is that **the same well-resourced states pursuing the legitimate, low-risk end of data-linkage (Splink) are, through other arms, also buying the high-risk, foreign-owned, operational end (Palantir)** — and doing so with markedly less transparency.

---

## 6. "Do not overstate" — the explicit NOT-supported and still-uncorroborated lists

**Do NOT overstate. The following are NOT supported by evidence:**

- **No Splink↔Palantir link of any kind.** Palantir does **not** use, supply, integrate with, or compete for Splink. There is **no** documented case of Palantir and Splink in the same agency, dataset, or task **anywhere on Earth.** Every per-country "connection" is *thematic/domain-level at most* — the author's framing of a shared trajectory, **not** a contractual or technical fact.
- **The German ruling did NOT hold Palantir's software unlawful per se** — it struck down the enabling statutes for inadequate thresholds.
- **The US "mega-database" is reporting/allegation**, disputed by Palantir; no public contract value; no adjudication.
- **EFF's ICE-uses-Medicaid-data-via-Palantir report** is an allegation in active litigation, not an adjudicated finding.
- **Israel/Gaza targeting:** claims that Palantir specifically powers IDF "kill lists" / "Lavender" / "Gospel" are **NGO/journalism allegations, not court-confirmed.** Lavender and Gospel are **IDF-attributed systems, not proven Palantir products**; Palantir disputes the characterisation. The Israel MoD contract value ("multi-hundred-million") is reported, not from a primary document.
- **Canada facial-recognition / civilian-social-media surveillance** via the military Palantir contract is **speculative** — the cited capability traces to **Meltwater and Clearview AI**, not a documented Palantir capability.
- **Building Blocks is NOT a Palantir product.** UNHCR's public record-linkage code uses **fastLink, not Splink.**
- The **"Indiana pilot" of Splink** and an **FDA-specific Palantir contract** were **never located** and appear in **no** finding.

**Removed as unsupported (corrections applied):**
- The fabricated **"$1.88B"** US government-segment figure (corrected to ~$2.43bn / 54%).
- The Hesse **"€0.01 nominal purchase order"** as near-fact (uncorroborated; flagged only).
- Implied **NRW/Bavaria Palantir contract values** (uncited).
- **"Social-media posts"** in Europol/Gotham datasets (source lists contact lists, radio-cell tables, travel histories, photos, location data).
- **"Dutch authorities hold 45,000+ Palantir documents"** (no citation).
- The MCCSS **2003–2016 RPDB linkage** as a *Splink* example (that study used deterministic/probabilistic hybrid methods, not Splink).

**Still uncorroborated / single-source (treat with caution):**
- ACIC "Gotham" product name and the **~42M-data-points** figure (single leaked-manual / Crikey).
- USCIS Dec 2025 contract scope/value (single-source Fortune).
- Australia's **ASD** and **Victorian Dept. of Justice** Palantir use (thin/advocacy-sourced).
- Future Fund stake (~$100M to >$160M, varies by source).
- Europol/Palantir exact value (€5M vs ~€7.5M across sources).
- Whether **EDPS Jan 2022** concerned the Gotham system specifically (not established).
- Whether **UNHCR** runs Splink operationally on live registration data (only fastLink is evidenced publicly).
- **Chile/Gambia/Laos** Palantir absence — search-pass negatives, not exhaustive proof.
- Aggregate Australian and UK (£670M / 34-contract) totals — secondary-journalism aggregates.
- Army **$10B** figure — ceiling, not obligated spend.

---

## 7. Consolidated source list

**Primary / official**
- Bundesverfassungsgericht — Judgment of 16 Feb 2023, 1 BvR 1547/19 & 1 BvR 2634/20 (English full text; names Palantir/Gotham/hessenDATA): https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/EN/2023/02/rs20230216_1bvr154719en.html
- BVerfG — Press release (bvg23-018): https://www.bundesverfassungsgericht.de/SharedDocs/Pressemitteilungen/EN/2023/bvg23-018.html
- Palantir FY2025 Form 10-K (54% gov / 74% US, $4.5bn): https://www.sec.gov/Archives/edgar/data/0001321655/000132165526000011/pltr-20251231.htm
- Palantir Q3 2025 earnings 8-K; Q4 2025 investor presentation (investors.palantir.com)
- WFP press release, "Palantir and WFP partner…" (5 Feb 2019): https://www.wfp.org/news/palantir-and-wfp-partner-help-transform-global-humanitarian-delivery
- WFP statement (Medium, 8 Feb 2019)
- EDPS order — erase data with no established criminal link (Jan 2022): https://www.edps.europa.eu/press-publications/press-news/press-releases/2022/edps-orders-europol-erase-data-concerning_en
- European Parliament question E-000951/2022 (Europol/Palantir/Capgemini): https://www.europarl.europa.eu/doceo/document/E-9-2022-000951_EN.html
- ABS — Person Linkage Spine; PLIDA pages (abs.gov.au)
- Destatis — Register census (destatis.de)
- EMA — Veterinary Union Pharmacovigilance Database Best Practice Guide (ema.europa.eu)
- Splink — official MoJ docs / adopter list: https://moj-analytical-services.github.io/splink/index.html
- GOV.UK — MoJ Splink algorithmic-transparency master record
- GFF — Bavaria/VeRA constitutional complaint (23 July 2025): freiheitsrechte.org
- Conflict of Interest and Ethics Commissioner (Canada), MacNaughton ruling, Sept 2020; CBC: https://www.cbc.ca/news/politics/palantir-macnaughton-ethics-1.5726443
- UNHCR-Americas record_linkage repo (uses fastLink): https://github.com/unhcr-americas/record_linkage
- CanadaBuys — Palantir Technologies Canada Inc. contract history; AusTender keyword: Palantir

**Reporting / investigative**
- Axios — ICE pays Palantir $30M / ImmigrationOS (1 May 2025)
- American Immigration Council — ImmigrationOS; ACLU — Palantir deportation roundup
- US Senate Finance Committee — Wyden/Ocasio-Cortez letter (17 June 2025); Nextgov/FCW
- The Intercept — Palantir & IRS "massive-scale" data mining (24 April 2026)
- DefenseScoop — Maven $1.3B (23 May 2025); TITAN $178.4M (6 Mar 2024); NATO/NCIA Maven (Mar 2025)
- AIN — Palantir $10B US Army (4 Aug 2025)
- FedScoop — CDC $443M; HHS Tiberius
- EFF — ICE/Palantir/Medicaid report (Jan 2026)
- EPIC — EPIC v. ICE settlement (Jan 2020); Fortune — USCIS contract (9 Dec 2025)
- heise — Baden-Württemberg ~€25M Palantir (Mar 2025); Palantir for minor crimes
- Ulbricht & Egbert, *Big Data & Society* (2024); LDI NRW; LTO; digit.site36 (Monroy 2020)
- Crikey — ACIC 42m data points (27 Apr 2026); Defence embedding (9 Mar 2026); biggest contract (17 Feb 2026)
- Canberra Times / Defence Connect — $7.6M Defence (Feb 2026); Digital Rights Watch — Palantir in Australia
- The Deep Dive / The Logic / theijf.org — DND CANSOFCOM $46.8M; The Logic / wiretapmedia — OPP $36.6M
- Statewatch (2025) — Europol opaque tech relations; Lighthouse Reports — Palantir in Europe
- Privacy International — WFP ~$45M (2019) and "cornerstone" expansion (17 June 2026); The New Humanitarian; Responsible Data open letter (65 signatories); Elrha case study
- Digital Health — NHS FDP £330M/£480M (Nov 2023); NHS England FDP contract explainer
- State of Surveillance — ImmigrationOS; Business & Human Rights Resource Centre — Israel/Gaza allegations; Palantir–Israel "Battle Tech" PDF (Jan 2024)
- PassBlue — "Palantir, Seemingly Everywhere"; FULCRUM — Myanmar Chinese-tech surveillance

**Splink-side comparators**
- US Census Bureau — record linkage (Splink vs BigMatch context); Datavant / NIH All of Us (CLAD)
- PMC8900651 — Ontario MCCSS social-assistance↔RPDB linkage (deterministic/probabilistic, **not** Splink)
- Statistics Canada — G-Link / SDLE (IJPDS); PMC10929394 — Chile migrant immunisation linkage (Splink)
- MIT Technology Review — WFP Building Blocks + UNHCR biometrics (12 Apr 2018)

---

*Bottom line: Splink and Palantir are different tools, and Palantir does not use Splink. But the same governments that quietly run statistical linkage also run Palantir's proprietary operational platforms — most heavily in the US, most consequentially adjudicated in Germany, and most opaquely procured almost everywhere. The pattern is real; the tier is "same country, different tool" — and where it is exactly that, this post says exactly that.*
