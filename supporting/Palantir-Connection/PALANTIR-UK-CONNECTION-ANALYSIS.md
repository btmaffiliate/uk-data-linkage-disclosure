# The Operational Twin: Palantir and the Joined-Up British State

*A Palantir companion to "The Quiet Joining-Up" · Data & Civil Liberties · June 2026*

*A public-interest analysis built entirely from publicly available government documents, procurement records, Parliamentary debate, court judgments, and journalism. No non-public systems were accessed. Confidence levels and connection tiers are stated for every claim; what is unsupported is flagged and excluded. This document applies the strict discipline of the prior five-part Splink investigation: where the strongest connection is "same department, not the same pipeline," it says exactly that.*

---

## 1. Executive summary and the honest thesis

The prior investigation, *The Quiet Joining-Up*, made a narrow and uncomfortable point: the UK state uses **Splink** — a free, open-source probabilistic record-linkage library built by the **Ministry of Justice** — to stitch previously separate citizen datasets into single, person-level records, lawfully, at population scale, and without individual consent, notification, or opt-out. The capability was shown to be quietly migrating from *statistics* (counting populations) toward *operations* (identifying named individuals in real time). That migration — the **statistics → operations slide** — was the story.

This companion answers the obvious follow-up question, and answers it honestly. **Palantir does not run Splink.** There is no documented technical, contractual, or data-flow connection between Splink and any Palantir platform. The two are different categories of artefact entirely: Splink is an algorithm (a Python library, MIT-licensed, with no network listener, running inside whatever environment an analyst puts it in); Palantir Foundry and Gotham are proprietary, hosted, operational data-integration platforms that ingest, fuse, and *action* live data. The local evidence log is unambiguous: *"There is no documented direct technical or corporate connection between Splink and Palantir,"* and the words "Palantir" and "Foundry" appear nowhere in the Splink repository.

**The central, defensible claim is therefore not "Palantir runs Splink." It is this:**

> Palantir is the **proprietary, operational layer** sitting in the **same government departments**, contracting over the **same citizen datasets**, that Splink links statistically — and Palantir is **precisely where the "statistics → operations" slide lands**. Splink is the open-source, statistical, no-consent, lawful joining-up of citizen records. Palantir is the US-owned, operational, identifiable, real-time integration of citizen records in the very same departments. They are two parallel "joining-up" tracks running through one government, occasionally over the same departments and the same data universe, with **no proven technical bridge between them**.

This is not a weakening of the prior work; it is its completion. The "Palantir blindspot" framing *depends* on the two being distinct. The point is precisely that the British state built its **own** open-source linkage engine (Splink) and escapes the vendor-procurement and foreign-ownership scrutiny aimed at Palantir — while, in the same buildings, on the same data, the operational end-state that the Splink dossier warned linkage could feed toward is **already contracted, live, and US-owned.**

### The three tiers of connection — stated plainly up front

Every vector below is graded against the same vocabulary the prior investigation used, as adjusted by the adversarial verifiers:

- **DIRECT_DOCUMENTED_LINK** — a documented Palantir contract / operational deployment exists. *This tier describes the strength of the Palantir-to-department relationship. It is NEVER used to describe a Splink-to-Palantir link, because none is documented.*
- **SAME_DEPARTMENT_OVERLAP** — Palantir and a Splink-investigation entity sit inside the **same body**, on overlapping subject-matter, via **entirely separate tooling**, with no shared pipeline.
- **THEMATIC_ADJACENCY** — the only shared thing is the trajectory (person-level record-linkage on citizens with no consent/opt-out) and/or co-location in the broad criminal-justice space across *different* departments.

| Where the documentation is strongest | What it shows |
|---|---|
| **DIRECT documented Palantir link** | Palantir → Cabinet Office (£27m border/customs, Foundry); Palantir → NHS England (FDP, Foundry); Palantir → MoD (Foundry); Palantir → UK police (Nectar/firearms licensing). These are real, operational, verified. |
| **SAME-DEPARTMENT overlap with Splink** | NHS England (Splink Data Linkage Hub **and** Palantir FDP); MoD (ONS Splink Service-Leavers↔Census **and** Palantir Foundry); MoJ (Splink in-house **and** Palantir's 2024 reoffending *pitch*); Cabinet Office/Home Office (Splink-entity departments **and** Palantir border data). |
| **No documented link of any kind** | Splink ↔ Palantir technical/data pipeline. Searched, refuted, excluded. The only indirect connective tissue is **PwC** — Palantir's UK alliance partner — and even PwC is not documented anywhere in the Splink chain. |

The honest verdict, repeated because it is load-bearing: **the strongest Splink-to-Palantir connection found anywhere in this analysis is "same department, not the same pipeline."**

---

## 2. The per-vector analysis

Each vector states: what Palantir does, the datasets, contract values and dates, what is *done* with the data, consent/oversight, controversies, and the **exact tier** of connection to the Splink entities.

---

### 2.1 NHS — Federated Data Platform + COVID-19 Data Store

**Connection tier to Splink: SAME_DEPARTMENT_OVERLAP** — the single strongest overlap in the whole investigation, and still not a pipeline.

**What Palantir does.** Palantir is prime contractor for NHS England's **Federated Data Platform (FDP)**, built on **Palantir Foundry** (not Gotham). The FDP joins previously siloed NHS trust data into a unified **operational direct-care** view: elective waiting-list management, theatre scheduling, Referral-to-Treatment validation, near-real-time bed visibility, discharge planning (the OPTICA tool), vaccination/immunisation, population-health management, and supply-chain optimisation. As of the March 2026 uptake figures, **168 of 214 trusts had signed up (123 live) and 41 of 42 ICBs** were on board — Greater Manchester the sole ICB holdout. It evolved directly from the **2020 COVID-19 Data Store**, the first NHS Foundry deployment.

**Datasets.** Elective waiting lists, RTT pathways, theatre/surgery scheduling, inpatient/outpatient records, bed occupancy, discharge data (OPTICA), vaccination data, population-health datasets, supply-chain/logistics data; COVID-era feeds (test/case data, hospital occupancy, ventilator stock, 999/111 calls). Identifiable patient-level data is held at trust level and de-identified (IQVIA) when shared nationally.

**Contract values and dates.** FDP **awarded 21 November 2023**; **up to £330m over seven years** — but this is a *non-committed forecast ceiling*; the Contracts Finder initial value to Palantir was nearer **~£182m**, so the accurate phrasing is *"up to £330m."* Year-one investment at least £25.6m. **Corrected contract structure (per verifier):** this is **not** a flat "Nov 2023–Feb 2027" deal. It is a **3+2+1+1 incremental structure** — a committed initial term of roughly three years (first decision point ~March 2027), with a **break clause available from February 2027**, and a maximum term to **~March 2031**. February 2027 is when the break clause becomes available, *not* a hard end date. The DHSC/Parliament extension decision in 2026/27 concerns triggering the first extension past the committed term. Consortium: **Palantir (prime) with Accenture, PwC, NECS and Carnall Farrar.** COVID-19 Data Store: original ~£1 emergency Foundry deal (March 2020), extended via a **£23m two-year contract** commencing 12 December 2020 to December 2022 (Faculty's parallel contract **~£1m**, softened from the unsourced "£930,000").

**What is done with the data.** This is **OPERATIONAL direct care** in NHS England's framing — live waiting-list triage, bed management, discharge, "prioritising those with the most urgent needs." *Honesty marker:* whether FDP processing is genuinely "direct care" — and therefore exempt from the national data opt-out — is the **contested legal question** at the heart of the Foxglove litigation. Treat NHS England's "direct care" classification as a **contested claim, not settled fact.**

**Consent and oversight.** The **national data opt-out does not apply** to the FDP, because NHS England classifies its use as direct care (the opt-out covers only secondary uses — planning/research). The result: **individual patients cannot opt out** of having identifiable data processed in the Palantir-run platform; only their hospital/trust can decline to adopt it (e.g. Greater Manchester ICB). No individual consent or notification is documented — **mirroring the Splink investigation's central finding** (lawful statutory/direct-care basis, no individual consent or opt-out). Oversight: the **National Data Guardian (Dr Nicola Byrne) issued a statement on 3 June 2026** after the "Not With My NHS Data" campaign, confirming that the DPIA said identifiable-data access would be limited to NHS staff, but that **external Palantir contractor staff (three engineers, in a new "admin" role) also have access to identifiable patient data in the NDIT environment** — and that NHS England conceded a DPIA error. An internal NHS briefing reportedly warned the change risked "loss of public confidence."

**Controversies and litigation.**
- 2021: openDemocracy/Foxglove judicial review over the **£23m** COVID Data Store deal; **government conceded April 2021**, committing not to expand Palantir use to non-Covid purposes without public consultation.
- November 2023: Foxglove (with Just Treatment, the Doctors' Association UK, the National Pensioners Convention) launched legal action arguing there is **no lawful basis** to proceed with the FDP without new primary legislation.
- Good Law Project pre-action letter over heavy redactions (~three-quarters) of the published FDP contract.
- Mid-2026: the "admin role" identifiable-data access triggered the **"Not With My NHS Data"** campaign and the NDG intervention.
- 3 June 2026: the cross-party Commons **Science, Innovation and Technology Committee called for termination** of the NHS FDP contract, recommending use of the February 2027 break clause.
- Vendor-level distrust over Palantir's ICE/border, defence (Gotham), and Peter Thiel ties; re-identification risk of "de-identified" data raised by MP David Davis.

**The exact tier and why.** NHS England runs a **named, documented, Splink-based probabilistic linkage workstream** — the NHS England Data Science **"Data Linkage Hub"** (`nhsengland.github.io/datascience/our_work/data-linkage-hub`), implementing a Splink model on administrative data. This is a **first-party NHS source**, stronger than the original profile's hedge that NHS-England-as-Splink-adopter "rests on Splink's own use-cases page." **Crucially, the Data Linkage Hub source makes no reference whatsoever to Palantir, Foundry, or the FDP.** That is the decisive fact: it *corroborates* the honest thesis rather than refuting it. Two distinct layers co-reside in one body — Splink for statistical/research-grade linkage; Palantir/FDP for operational direct care — with **no documented data flow, contract, or technical integration connecting them.** Tier: **SAME_DEPARTMENT_OVERLAP**, not DIRECT. The shared theme (citizen data joined up without individual consent) is the through-line; the concrete tie is co-location in NHS England only.

---

### 2.2 Ministry of Defence — Palantir Foundry

**Connection tier to Splink: SAME_DEPARTMENT_OVERLAP** — co-residence in the MoD, no proven shared pipeline.

**What Palantir does.** Foundry is the MoD's underlying **"data fabric"** / ontology layer: it digests disparate MoD data sources, harmonises them, and maps them to an ontology (objects, properties, relationships) to support scenario planning, hypothesis testing, and decision-making from headquarters to the front line, NATO-interoperable. The **Royal Navy** uses Foundry for operational planning, logistics and fleet/maintenance availability ("Palantir Foundry is critical to the Royal Navy's transformation"). No-code/low-code app builders let MoD personnel build tools on the integrated data.

**Datasets.** MoD operational/Defence data across operational domains (capability, logistics, personnel, planning — specifics classified); Royal Navy operational/logistics/fleet data; MoD personnel data. *Splink-side, NOT Palantir:* the MoD Service Leavers Database and Compensation and Pensions System (linked by ONS to the 2011 Census); Veterans Card applicant data.

**Contract values and dates.**
- **£75m three-year Enterprise Agreement, announced 21 December 2022** (including the Foundry ontology and the Royal Navy work) — confirmed verbatim against PRNewswire.
- **September 2025 strategic partnership**: framework worth **up to £750m over five years**, with Palantir committing to **invest £1.5bn in the UK** (an *investment commitment, not contracted MoD spend*) and base its European defence arm in London (~350 jobs) — confirmed against GOV.UK and corroborating outlets.
- **£240.6m three-year follow-on enterprise agreement, directly awarded 30 December 2025, term starting 1 April 2026, awarded WITHOUT competition** under a defence-and-security exemption — confirmed against The Register (Find a Tender notice 083874-2025).

**Corrections applied (per verifier):**
- The phrase *"critical strategic, tactical and live operational decision making across classifications"* is rendered as a **paraphrase**, attributed to the contract notice / Hansard rather than presented as a verbatim quote from The Register.
- The claim that Foundry was used to "reorganise/streamline personnel during the COVID-19 pandemic" is **unsupported by the cited source and is dropped.**
- The Hadean "£20m … underpinned by Palantir Foundry" line is **flagged as unverified** (cited BusinessWire source could not be fetched) and is not stated as fact.
- The named political-conflict specifics (Mandelson link to the PM's February 2025 Palantir HQ visit; a Labour-donation question) **rest on secondary characterisation of the February 2026 Lords debate and are hedged, not asserted.**

**What is done with the data.** **OPERATIONAL by design** — Foundry supports live operational decision-making, Royal Navy logistics, and NATO-interoperable operations. This is the categorical opposite of the Splink-side MoD work.

**Consent and oversight.** The ONS Service-Leavers↔Census linkage documents **no individual consent/notification/opt-out** (consistent with statutory public-task statistical linkage — again mirroring the Splink finding). Ministers assert **contractual oversight** over Foundry: UK data sovereignty, residency in the UK, no changes without UK consent (February 2026 Lords debate). But **procurement oversight is weak**: the £240.6m award bypassed competition via the defence/security exemption; the Lords debate pressed on excluding British competitors and outsourcing a "sovereign capability."

**Controversies.** No-competition award (British firms reportedly interested but not allowed to compete); **revolving-door concerns** (Palantir hired four former MoD officials in 2025, including ex-policy director **Barnaby Kistruck**, who helped write the Strategic Defence Review and joined Palantir nine days after leaving MoD); vendor-level reputational controversy (Gaza AI-targeting allegations, NHS FDP campaign, UK police trials, German GFF predictive-policing complaints) — attaching to Palantir as a vendor, not to any documented MoD data-misuse finding.

**The exact tier and why.** The MoD is a genuine **Splink-side** entity in two documented ways: (1) **ONS used Splink 2** (the MoJ tool) to probabilistically link the MoD-supplied **Service Leavers Database** (1975–2022; 1,603,782 deduplicated person-records) plus the Compensation and Pensions System geography to the **2011 Census** — a statistical/research product with **649,186 linked records, a 40.5% link rate** (verified verbatim against the ONS methodology page, **which never mentions Palantir or Foundry**); and (2) the **Veterans Card** system uses Splink to verify applicants against historic service records (a discrete operational verification function). The verifier additionally surfaced an **ONS "Veterans' Survey 2022 → Census 2021" Splink linkage** as a further same-department touchpoint. **No source documents Foundry and Splink sharing a pipeline or data flow.** Tier: **SAME_DEPARTMENT_OVERLAP.** Do not assert that veteran/service-leaver linkage runs through Palantir; it does not.

---

### 2.3 Home Office / immigration / borders

**Connection tier: DIRECT_DOCUMENTED_LINK** — *but specifically and only* on the basis of the £27m Cabinet Office border/customs contract and the Nectar policing pilot. The tier is **NOT** justified for Home Office immigration *enforcement*.

**What Palantir does.**
- **Cabinet Office border/customs (£27m, August 2020, no competitive tender):** Palantir integrates and analyses border/customs data for **"risk-based monitoring for the movement of goods and people across the UK border"** (the firm's own pitch language) — facilitated by a **July 2019 introduction from former MI6 chief Sir John Sawers** (Newbridge Advisory) to the Cabinet Office permanent secretary. This is the **closest documented Palantir-to-borders link**, and it is real, operational data processing about people crossing the UK border. *(Detailed under the cross-government vector, §2.5.)*
- **UK policing "Nectar" pilot:** *(detailed under §2.4.)*
- **Immigration ENFORCEMENT (deportation tooling):** documented **only in the US** — ICE's **ImmigrationOS** ($30m, sole-source, awarded April 2025, runs to September 2027). **There is NO UK Home Office equivalent contract on record.** This must not be conflated with a UK deal.

**Honesty marker — the critical distinction.** The much-feared "Palantir runs UK immigration enforcement" claim is **not supported.** The documented UK borders work is **Cabinet Office, not Home Office**; the deportation platform is **US ICE, not UK**. The UK Home-Office-immigration-enforcement link is therefore a **CAPABILITY-and-trajectory concern**, not an existing data flow: Palantir's Foundry↔Gotham interoperability *could*, **if the law changed**, "enable UK government departments such as the Home Office and police to more easily access patient data" (Medact's exact, forward-looking framing). The legislative trigger most often cited is **Reform UK's "Operation Restoring Justice"** pledge of automatic Home Office/NHS/HMRC/DVLA/banks/police data-sharing — sourced to **htworld.co.uk** (which quotes Reform), **not** to Medact.

**Consent and oversight.** No individual consent/notification/opt-out documented; lawful basis asserted as public task. For the Home Office, data-subject rights are curtailed by the **DPA 2018 immigration exemption (Sch 2 para 4)**, ruled an **unlawful GDPR Art 23(2) derogation by the Court of Appeal in 2021** (*R (Open Rights Group & the3million) v SSHD* [2021] EWCA Civ 800) and found **still unlawful** in 2023. Any Palantir-run Home Office immigration platform would inherit a legally contested rights-suspension regime — this is the **same "policy-not-law shortcut"** the prior investigation's Part 3 ("Ruled Unlawful Next Door") identified as the live legal exposure in the immigration regime.

**Corrections applied (per verifier):**
- The aggregate **"34+ contracts across 10+ departments totalling £670m+, exceeding £900m"** is **re-attributed to The Nerve** investigation — *not* to the Novara Media article, which says only "over £500m."
- The **"PX14A6G SEC filing"** reference is **removed** — no cited source supports it.
- The Reform "Operation Restoring Justice" pledge is cited to **htworld**, the "could enable Home Office/police access" quote to **Medact** — kept distinct.
- The "Nectar nine forces initially" phrasing is tightened to a **data-pooling ambition**, not nine signed Nectar customers.

**The exact tier and why.** Two documented, operational, verified UK engagements (Cabinet Office borders; Nectar policing) earn **DIRECT_DOCUMENTED_LINK** for the *Palantir-to-department* relationship. The **Splink relationship** is **PARTIAL OVERLAP, NOT a shared pipeline**: Palantir's borders contract is Cabinet Office (a Splink-investigation department), but no PNC or Splink-linked records are documented flowing into any Palantir platform, and no Palantir Home Office immigration-enforcement contract exists. **Do not manufacture a Splink↔Palantir technical link — none is documented.**

---

### 2.4 UK policing / law enforcement — Palantir "Nectar" + national firearms licensing

**Connection tier to Splink: THEMATIC_ADJACENCY** *(downgraded by the verifier from SAME_DEPARTMENT_OVERLAP — see below).*

**What Palantir does.**
- **Eastern Region "Nectar" pilot** (Bedfordshire + Hertfordshire + Cambridgeshire, with an ambition to pool data from nine forces and "eventually apply it nationally"): integrates dozens of policing databases into a **"single, unified view"** on suspects, victims, witnesses, children and vulnerable people; combines crime records with financial information and intelligence; designed as a real-time data-sharing network to "assist with decision making" and "aid in the prevention, detection and investigation of crimes." It processes **11 categories of special-category data**: race, religion, political opinions, sex life/sexual orientation, health, trade-union membership, philosophical beliefs, plus social-media posts, dating profiles and financial records (per the Bedfordshire DPIA, reported by Bedford Independent / Liberty Investigates).
- **Bedfordshire "Romanian fraud gang" case** (ERSOU, November 2024): Palantir **Foundry** (product family **documented** for this case — chief constable Trevor Rodenhurst) processed ~1.4TB from ~24 seized phones, machine-translated 100,000+ Romanian messages, mapped suspect connections, and flagged ~120 offences, cutting association-charting time ~75%. *(The precise jailing/offence counts are "as reported" pending a primary court/CPS source.)*
- **East Midlands project** (Leicestershire / EMSOU, **~£818,750 reported**): an intelligence/investigation platform fusing data from five forces. The Contracts Finder award notice was **removed from the public record (~2 December 2024)** after Good Law Project inquiries — corroborated via Wayback snapshot; the existence and delisting are **documented** (the value remains "reported," FOI denied). Note: this deployment is **also branded "Nectar emsou,"** so "Nectar = Eastern region" is not a clean geographic signature.
- **National firearms/explosives-precursor/poisons licensing** (announced early June 2026): **~£9m, term up to 10 years (5+5), tender valued ~£17m incl. tax**, run by **BlueLight Commercial on behalf of Police Digital Service** (with NPCC and the Home Office), to hold and manage how all **43 forces in England and Wales** grant/renew/revoke firearms, explosives-precursor and poisons records; initial five-year term from **4 September 2026**; **Accenture and NEC Software** were the losing finalists. A national operational person-level records system.
- **Metropolitan Police (BLOCKED):** a proposed deal — **£25.3m (2026/27) + £24.8m optional extension (~£50m)** — **blocked on 21 May 2026** by the Deputy Mayor for Policing and Crime (MOPAC) over a "clear and serious breach" of procurement rules (single-supplier treatment, no procurement strategy; MOPAC has final sign-off on contracts over £500k). Palantir signalled a legal challenge.

**Important carve-out.** **NDAS (the National Data Analytics Solution, West Midlands Police lead) is Accenture/AWS, NOT Palantir** — and must never be conflated with Palantir's footprint.

**Consent and oversight.** Weak. The Bedfordshire DPIA admits **no individual opt-out** and itself recorded expected public "skepticism or resistance." Lawful basis is law-enforcement processing (DPA 2018 Part 3) — no individual consent sought, **mirroring the Splink finding.** Transparency is actively undermined: the Good Law Project FOI'd 45 forces; **35 refused** on national-security/law-enforcement grounds; Leicestershire delisted its contract. The Commons Science, Innovation and Technology Committee called reliance on Palantir an **"unacceptable point of weakness."**

**The exact tier and why — downgraded.** The original profile rated this SAME_DEPARTMENT_OVERLAP. The verifier **downgrades it to THEMATIC_ADJACENCY**, and the reasoning is decisive: **Splink is a Ministry of Justice tool; Palantir/Nectar is deployed by territorial police forces and Home Office/NPCC/PDS bodies. MoJ and the police/Home Office are *not* the same department** — so there is no "same-department" overlap to claim. The original "striking geographic adjacency" framing (Nectar's Eastern region vs Splink's North Essex PNC→police feed) is **rhetorical inflation and is dropped**: co-location in "the East of England" is coincidence, not connective tissue, and "Nectar emsou" shows Nectar is not an Eastern-region signature. The Gotham-vs-Foundry product naming per force is **inference, not fact** (FOI-refused) — only "Nectar" (the confirmed UK brand) and the documented Foundry use in the Bedfordshire case are stated as product fact. **No document shows PNC or Splink-linked records flowing into Palantir Nectar, and no documented Palantir–PNC integration exists.** The shared theme — operational person-level record-linkage in policing with no individual consent — is real, but appears here via a *second, commercial vendor* in a *different department*. Tier: **THEMATIC_ADJACENCY.**

---

### 2.5 Cross-government — Cabinet Office / ONS / National Data Library

**Connection tier: DIRECT_DOCUMENTED_LINK for Palantir↔Cabinet Office; SAME_DEPARTMENT_OVERLAP for the Splink-adjacent inference.** *(The verifier's central instruction: when this profile is used inside the Splink disclosure, it must lead with the weaker tier.)*

**What Palantir does.**
- **Cabinet Office Border Operations Centre / "border flow" (~£20m ceiling, August 2020, no competitive tender):** Foundry's "Data Connector" extracts and combines live operational data — Phase 1 **Home Office + HMRC**; the feasibility/free-trial set per PublicTechnology named **HMRC, Home Office, Defra, DfT, DVLA, Highways England and Port Health Authorities** — into a dedicated UK Foundry partition on the **AWS London region, for the exclusive use of HMG**, for risk-based monitoring of the throughput of goods and people across the UK border post-Brexit. The data-hosting claim (dedicated partition, AWS London, Palantir barred from processing data outside the UK without Cabinet Office authorisation, encryption at rest/in transit) is **verified verbatim from the contract** — this is the strongest documented data-flow claim in the analysis.
- **Homes for Ukraine (DLUHC/MHCLG):** a Foundry-based platform that let DLUHC, the Home Office and 2,000+ local-authority caseworkers share applicant data. **Corrected to past tense (per verifier):** the Palantir Homes for Ukraine deployment ran ~September 2022–2024 and has since been **replaced by an in-house MHCLG build**, which the department states is "saving millions a year." This is a **wound-down / superseded** deployment, not an ongoing flow.

**Corrections applied (per verifier):**
- **DVLA vs DVSA:** the free-trial ingest set names **DVLA**; "DVSA" appears separately in a phase-2 invitation. The border-flow body list uses **DVLA** for the documented ingest set.
- The **£670m+ government-wide figure is ring-fenced as out-of-scope** for a Cabinet-Office vector (it is dominated by NHS FDP and MoD, which are separate vectors), and attributed to **The Nerve** as an investigative floor.
- "One of the most comprehensive cross-government datasets ever compiled" / "single source of truth" is **attributed to campaigner/journalist framing (openDemocracy/Byline Times)**, not asserted as established fact.

**Contract values and dates.** Border flow: initial 1-yr **£7.85m** + two 1-yr extensions at **£6.125m** each (~£20m ceiling) — only the ceiling is documented; whether extensions were exercised is not confirmed. Homes for Ukraine: 6 months **free**, then 12-month direct award **£4.5m (Sept 2022)**, extended **+£5.5m (Sept 2023)** (~£10m) — confirmed by the **National Audit Office** investigation, which names Palantir explicitly. The government's chief commercial officer **(Gareth Rhys Williams, February 2023)** formally wrote to Palantir noting concern that offering services at zero/nominal cost to gain a commercial foothold cuts against open-competition principles. Palantir named a **Crown Commercial Service supplier April 2021**; **Foundry & AIP on G-Cloud 14** (service definition dated November 2024) — the compliant on-ramp for further cross-government call-offs.

**The decisive negative controls.** This is where the statistics-vs-operations distinction is sharpest at the cross-government level:
- The **ONS Integrated Data Service runs on Google Cloud / BigQuery — NOT Palantir.**
- The **National Fraud Initiative / PSFA data-matching runs on Synectics Solutions — NOT Palantir** (Synectics incumbent since 1996, re-award confirmed).
- The proposed **National Data Library has no named Palantir role** (still pre-procurement; a future role cannot be excluded, only that none is documented now).

So **ONS/Splink = statistical, de-identified, research-only linkage; Palantir/Cabinet Office = operational, identifiable, case-level integration.** Two parallel "joining-up" tracks in the same government, occasionally over the same departments (Home Office, Cabinet Office), with **no proven technical bridge.** Tier for the Splink inference: **SAME_DEPARTMENT_OVERLAP.**

---

### 2.6 Ministry of Justice / prisons / probation

**Connection tier to Splink: SAME_DEPARTMENT_OVERLAP — but the "same department" part is LOBBYING-ONLY, and the operational part is a different body (policing).**

**The central finding is an absence.** **There is NO documented Palantir contract, pilot, or live deployment inside the Ministry of Justice or HMPPS.** That absence is itself the finding, and it survives hostile scrutiny.

**What is documented is lobbying.** In **November 2024**, FOI-released correspondence (The Guardian / Ben Quinn) showed Palantir **lobbied** MoJ ministers — prisons minister James Timpson, Chancellor Rachel Reeves, and others — offering to **score prisoners' reoffending risk**, model recidivism drivers (income, addiction), and optimise prison capacity, and attended a ~30-corporation MoJ surveillance roundtable. The letter to Timpson came ~three weeks after the July 2024 general election; talks reportedly began under the prior government; **ministers largely did not respond and no award followed.** Amnesty International warned of discrimination, privacy breaches and miscarriages of justice.

**Crucially, the MoJ's actual operational reoffending tool is NOT Palantir.** **ARNS** (replacing OASys) profiles **1,300+ people daily**, combining probation/prison caseload data with the **Police National Computer**, and is built **in-house by MoJ / Justice Digital, liaising with Capita** (who support the legacy OASys system — *not* a co-builder of ARNS, per the corrected verifier framing). The Statewatch source naming ARNS **never mentions Palantir.**

**And the gov.uk Splink algorithmic-transparency record names no vendor at all.** Splink is the MoJ's own in-house, open-source library; the North Essex pilot uses Splink to find PNC numbers for individuals supervised by the North Essex Probation Delivery Unit and send them to police daily. **There is no Palantir code in any Splink / Data First / Core Person Record system** — independently corroborated by the local evidence log.

**Corrections applied (per verifier):**
- The **PNC↔Nectar overlap is downgraded to "inferred, not documented"**: Splink (MoJ-side) demonstrably uses PNC numbers per the gov.uk transparency record; Nectar (police-side) is reported only on *force-held* data, and the primary Liberty Investigates source **does not mention PNC**. This single inferential hinge is the only thing that ever elevated the policing overlap above thematic — and it is **not documented for Nectar.**
- The Bedfordshire Romanian case is stated as **Foundry** (documented), dropping the "Foundry/Gotham-family" hedge for that case specifically.
- The Leicestershire ~£800k delisting is **upgraded to a sourced claim** (Wayback + Good Law Project + Leicester Gazette FOI).

**The exact tier and why.** The genuine same-department overlap with Palantir inside the MoJ is **only at the lobbying (non-delivered) level.** Where Palantir actually *operates* in UK criminal justice is **policing — a different body.** Tier: **SAME_DEPARTMENT_OVERLAP**, sitting on the border with THEMATIC_ADJACENCY, and explicitly *not* DIRECT_DOCUMENTED_LINK. The honest headline is the **absence** of any Palantir-MoJ contract.

---

### 2.7 Corporate / governance / national-security dimension

**Connection tier to Splink: SAME_DEPARTMENT_OVERLAP + THEMATIC_ADJACENCY** — and the verifier confirms this should not be upgraded.

**Who controls Palantir.** Palantir Technologies (NYSE: PLTR) is a **US national-security data-integration firm**, founded 2003 by Peter Thiel and Alex Karp with early **CIA In-Q-Tel funding (~$2m, 2004)**. **FY2025 revenue ~$4.5bn, 54% from government** — now **directly confirmed against the FY2025 10-K** (no longer "approximate"). Founder voting control is locked at **~49.99% in perpetuity** via a **tri-class (A/B/F) share structure** and a **Thiel–Karp–Cohen voting trust**, despite the founders holding a minority economic stake (TechCrunch S-1 reporting; 10-K exhibit).

**The UK footprint.** At least **£670m in disclosed UK government contracts across 10+ bodies** — attributed to **The Nerve** as an **investigative floor, not an audited figure**, every time it appears (genuine procurement-transparency gaps mean many contracts are not on Contracts Finder). **Corrected:** the £670m figure **predates the £240.6m MoD December 2025 deal**; the post-MoD documented total now **exceeds ~£900m** per The Nerve's follow-up. The Nerve reports MoD aggregate **~£388m across ~12 contracts/extensions** (so the three line-items £240.6m + £75.2m + £28m are *selected*, not a complete accounting) and NHS-related deals **>£244m across 12 contracts**.

**Corrections applied (per verifier):**
- The COVID Data Store extension figure is stated as the documented, litigated **£23m (December 2020)** — not "no figure initially published."
- **Indra Joshi** is described as **ex-NHSX Director of AI / NHS AI Lab founder, who left NHSX 31 March 2022 and joined Palantir April 2022** — *not* "helped build the COVID-19 datastore," which the verifiable sources do not support.
- **AWE ~£15m** and **Nuclear Propulsion IPT ~£250k** are **single-source (The Nerve), off Contracts Finder, MoD-unconfirmed**, and flagged as such inline — not folded into "disclosed contracts" without attribution.
- The Nerve investigation is dated **February 2026** (Carole Cadwalladr), not January; the AWE figure was "revealed as part of The Nerve's February 2026 reporting."

**The revolving door.** The Nerve found Palantir hired **30+ senior UK officials**, including the AI strategy leaders of both the NHS and the MoD: Indra Joshi (NHS), Harjeet Dhaliwal (NHS England), and from MoD **Barnaby Kistruck** (helped write the Strategic Defence Review, joined nine days after leaving), Laurence Lee, Damian Parmenter, Polly Scully, and ex-armed-forces minister Leo Docherty.

**The exact tier and why.** Palantir genuinely shares **NHS England, Home Office, MoD, and police** as counterparties with the Splink-investigation entities (institutional overlap), and its core capability — joining siloed citizen datasets into a single unified view — is the **proprietary, US-owned, operational commercial analogue** of the open-source government data-linkage work Splink represents (thematic adjacency). But **there is no documented technical pipeline linking Splink to Palantir Foundry/Gotham**, and none should be implied. Tier: **SAME_DEPARTMENT_OVERLAP + THEMATIC_ADJACENCY.** The dominant story here is **governance and civil liberties**: opaque direct awards, a 30+-official revolving door, founder-locked control, and a US national-security vendor positioned to hold integrated UK citizen data.

---

### 2.8 The Splink-vs-Palantir distinction (and whether any data flows between them)

**Connection tier: SAME_DEPARTMENT_OVERLAP, anchored at the MoJ, with strong THEMATIC_ADJACENCY on the statistics→operations gradient.**

This is the analytical crux of the entire document, so it is stated with maximum precision.

**They are different categories of artefact.** Splink is an **open-source probabilistic record-linkage library** — a Python package built by the MoJ, MIT-licensed, running on **DuckDB / Spark / Postgres / Athena / SQLite**. It links records; it is **not** a data platform, has **no network listener**, and runs inside whatever environment an analyst puts it in. Palantir **Foundry/Gotham** are **proprietary, hosted operational data-integration platforms** that ingest, fuse and action live data, with their *own* entity-resolution. A linkage algorithm vs an operational platform.

**There is no documented data flow between them.** No published contract, data-usage agreement, or architecture document ties Splink (or Splink-linked Data First / ONS IDS outputs) to any Palantir platform. **"Palantir" and "Foundry" appear nowhere in the Splink repository**; there are no Palantir contributors or Foundry issues on the repo; Foundry is **not** a Splink backend; and **Foundry's own connector docs reference no Splink integration.** Searches for a Foundry↔Splink integration return only generic Foundry data-integration documentation. *(Note: the "Foundry↔Gotham drag-and-drop interoperability" sometimes cited is an **internal Palantir-product capability**, supported only by the generic Foundry overview page — it is downgraded here to a general data-integration capability and is **not** a Splink linkage.)*

**The only indirect connective tissue is PwC — and even that does not touch Splink.** PwC is **Palantir's formal UK alliance partner** (preferred partners; PwC uses Foundry/AIP) **and** appears as a delivery partner on the NHS FDP. PwC also won crime/intelligence-management technology for the Action Fraud replacement (FCCRAS / NFIB), where a single trade source names Palantir as PwC's "technology alliance partner." **But no source ties Splink to PwC's NFIB build**, and the procurement record names Capita + PwC, not Splink. The "Report Fraud / NFIB includes Palantir Foundry" claim that recurs in search-engine summaries is **NOT in the primary sources and is treated as unverified.**

**The real connection is institutional and trajectory-based.** It is twofold:
1. **Same department (the MoJ anchor):** Splink is the MoJ's own in-house tool (powering Data First and the operational North Essex probation/PNC feed); in 2024 Palantir **pitched the same MoJ** to compute prisoners' reoffending risks over state-held data. They would operate on overlapping subject-matter within one department — via **entirely separate tooling, with no common pipeline, and no Palantir contract awarded.**
2. **Same trajectory (the statistics→operations gradient):** Splink-linked Data First is nominally research-only, yet the same library already runs operationally (courts, daily PNC feeds, the Core Person Record pilot). Palantir's platforms are explicitly **operational and identifiable** (NHS direct care, police real-time fusion, MoD live decisions, Cabinet Office live border flow). **Palantir is the operational pole; Splink/ONS are nearer the statistical pole.** Palantir embodies the operational end-state toward which the Splink dossier warned record-linkage could be pulled.

That is a **thematic and departmental adjacency, not a wired data flow.** Manufacturing a Splink→Palantir data link would be unsupported by the evidence — and, as the evidence log notes, would be the fastest way to discredit the work.

---

## 3. The map

| Department / body | Splink role (statistical/research, open-source, MoJ-built) | Palantir role (operational, proprietary, US-owned) | Connection tier (Splink ↔ Palantir) |
|---|---|---|---|
| **NHS England** | Splink-based **Data Linkage Hub** (probabilistic linkage on admin data; research/business-process) | **FDP on Foundry** (£330m ceiling, Nov 2023; operational direct care: waiting lists, beds, discharge); COVID Data Store (£1 → £23m) | **SAME_DEPARTMENT_OVERLAP** — strongest overlap, no shared pipeline |
| **Ministry of Defence** | **ONS Splink 2** linkage: Service Leavers DB + Comp/Pensions → 2011 Census (statistical); Veterans Card verification | **Foundry "data fabric"** (£75m 2022; up to £750m + £1.5bn invest 2025; £240.6m Dec 2025, no tender) | **SAME_DEPARTMENT_OVERLAP** — co-resident, no shared pipeline |
| **Ministry of Justice / HMPPS** | **Splink in-house** (Data First / XJS; North Essex PNC feed; Core Person Record pilot). Operational tool = **ARNS, in-house, not Palantir** | **No contract.** 2024 **lobbying pitch only** (reoffending-risk scoring) | **SAME_DEPARTMENT_OVERLAP** — but the overlap is **lobbying-only**; operational Palantir is in a different body (policing) |
| **Cabinet Office** | (Splink-investigation department) | **Foundry border/customs** (~£20m, Aug 2020, no tender); Homes for Ukraine (now superseded by in-house build) | **SAME_DEPARTMENT_OVERLAP**; Palantir↔Cabinet Office itself is DIRECT_DOCUMENTED |
| **Home Office** | (Splink-investigation department; DPA 2018 immigration exemption ruled unlawful) | Data ingested via Cabinet Office border flow. **No UK immigration-enforcement contract** (ImmigrationOS is US ICE) | **SAME_DEPARTMENT_OVERLAP** for data; enforcement = **CAPABILITY/trajectory concern only** |
| **UK policing** | **MoJ Splink** North Essex PNC→police feed (MoJ tool used at the policing layer) | **"Nectar"** real-time fusion (Beds/Herts/Cambs; EMSOU ~£818k); national firearms licensing (~£9m); Met deal **blocked** (~£50m) | **THEMATIC_ADJACENCY** — MoJ ≠ police; PNC↔Nectar link **inferred, not documented** |
| **ONS / cross-gov statistical estate** | **Splink** on Census/Business/Demographic indices | **Not Palantir** — ONS IDS on Google Cloud/BigQuery; NFI on Synectics; NDL no named Palantir role | **No link** — decisive negative control |
| **Corporate / governance** | (n/a — Splink is open-source, MIT) | US national-security firm; ~$4.5bn rev (54% govt); founder-locked ~49.99%; £670m+ UK floor (now >£900m); 30+ revolving-door hires | **SAME_DEPARTMENT_OVERLAP + THEMATIC_ADJACENCY** |
| **Splink ↔ Palantir directly** | Algorithm (Python library, no listener) | Operational platform (hosted, proprietary) | **NO documented technical/data link.** Only indirect tissue = PwC (and even PwC ≠ Splink) |

---

## 4. The combined civil-liberties picture

Read the two investigations together and a single shape emerges — **the joined-up operational state, assembled in two layers that the public was never asked about and largely cannot see.**

**Layer one — Splink.** Open-source, statistical, lawful, technically excellent, built by the state itself. It links citizen records across justice, health, tax, and benefits with **no individual consent, no notification, and no opt-out**, because the legal basis is statutory "public task," not consent. It escapes vendor-procurement scrutiny *precisely because* it is not a contract — there is no supplier to FOI, no award notice to redact, no foreign owner to name. It is invisible by construction.

**Layer two — Palantir.** Proprietary, operational, US-owned. It sits in the **same departments** (NHS England, MoD, Home Office data, Cabinet Office, policing), contracts over the **same citizen datasets**, and — unlike Splink — acts on **identifiable individuals in real time**: who gets the next surgery slot, which border movement is flagged, which person is profiled by nine police forces, which military decision is taken at the front line. Where Splink counts, Palantir *does*.

**This is exactly where the "statistics → operations" slide lands.** The prior investigation warned that the same linkage machinery was edging from counting populations toward identifying named individuals operationally. Palantir is not a future warning — it is the operational layer **already contracted and live** in those same departments. The two layers are not wired together. They do not need to be. They are co-located in one government, over one population, and the trajectory of each points at the other.

**And here the two layers differ in one constitutionally significant way: ownership.** Splink is the British state's own code. Palantir is a **US national-security firm** — CIA In-Q-Tel origins, founder voting control locked at ~49.99% in perpetuity in a Thiel–Karp–Cohen trust, a chairman who is a major Trump donor, and an active US ICE deportation contract — now positioned to hold **integrated UK NHS, defence, border, and policing data**. Two MoD systems engineers warned (February 2026) that aggregating cross-government data in one private US vendor is a national-security threat — the **"mosaic effect"**, enabling a profile of the whole population. Ministers' answer is **contractual** sovereignty (UK residency, no changes without UK consent). But contractual control is not constitutional control: it depends on the contract, the vendor, and the political weather in two countries. The Commons Science, Innovation and Technology Committee's June 2026 call to **terminate** the NHS FDP contract, and MOPAC's blocking of the Met deal, are the system beginning — belatedly — to register the stakes.

The civil-liberties summary, stated fairly: the safeguards that exist (Five Safes, accredited-researcher schemes, de-identification, DPIAs) were **built for the statistics use case and are largely internal and researcher-facing.** They do not govern the *prior* question — whether population-scale linkage and operational integration should happen without the individual's knowledge — and they do not address the *foreign-ownership* question at all. The lawful basis is one most citizens have never heard of; the linkage is invisible to the individual; there is no personal right to object; and the operational layer is owned abroad.

---

## 5. Do not overstate — what is NOT supported

The discipline of the prior work was that the unverified line is the line that discredits the rest. The same rule applies here, doubly, because the temptation to draw a single arrow from Splink to Palantir is strong and would be fatal.

**Explicitly NOT supported — exclude:**

1. **Any Splink ↔ Palantir technical or data link.** No contract, no data-usage agreement, no architecture document, no connector, no shared pipeline. "Palantir" and "Foundry" appear nowhere in the Splink repo; Foundry is not a Splink backend; no Palantir contributors on the repo. *"Splink is Palantir"* or *"Palantir runs the MoJ linkage"* is **false and must never be written.** The "Palantir blindspot" framing *depends* on them being distinct.
2. **A Palantir UK Home Office immigration-enforcement contract.** None exists on record. The documented borders work is Cabinet Office; **ImmigrationOS is US ICE, not UK.** The UK enforcement scenario is a capability/trajectory concern contingent on hypothetical future legislation (Reform UK's "Operation Restoring Justice"), **not** an existing data flow.
3. **An NHS→Home Office/police patient-data flow.** This is a campaigner-flagged *risk* ("could enable"), not an operational reality.
4. **The "PX14A6G SEC filing" reference** (Home Office vector) — no source supports it; removed.
5. **The COVID personnel-reorganisation claim** (MoD vector) — unsupported by the cited source; dropped.
6. **The Hadean "£20m … underpinned by Palantir Foundry" integration** — cited source unfetchable; flagged unverified, not asserted.
7. **PNC↔Nectar data sharing** — the primary source does not say Nectar uses PNC; **inferred, not documented.**
8. **The "Foundry↔Gotham drag-and-drop" wording** as documented fact — it is a general internal capability, not a documented cross-domain flow, and is **not** a Splink linkage.

**Tier and attribution disciplines enforced:**
- Policing is **THEMATIC_ADJACENCY**, not SAME_DEPARTMENT_OVERLAP (MoJ ≠ police/Home Office).
- The £670m/£900m/34-contracts aggregate is **The Nerve's** investigative floor (Feb 2026), **not** Novara's; £670m predates the Dec 2025 MoD deal.
- NHS FDP is **"up to £330m"** (ceiling); the committed structure is **3+2+1+1**, break clause Feb 2027, max term ~March 2031 — *not* a flat Nov 2023–Feb 2027 deal.
- NHS "direct care" classification is **contested** (the live Foxglove legal question), not settled.
- Gotham-vs-Foundry naming per police force is **inference** (only "Nectar" and the Bedfordshire-case "Foundry" are documented).
- AWE ~£15m / Nuclear Propulsion ~£250k are **single-source, off Contracts Finder, MoD-unconfirmed.**

**Still uncorroborated (worth chasing, not citable as fact):**
- Whether the NHS FDP contract is extended past the Feb 2027 break clause (Parliament/DHSC decision pending).
- Whether the Cabinet Office border-flow extension years were exercised (only the ~£20m ceiling is documented).
- The complete named list of UK police forces in the Palantir network ("~11 forces" is journalistic).
- Exact Nectar pilot contract values (FOI-refused).
- Whether FDP scope includes GP/social-care records (reported/expected, not confirmed as live ingestion).
- A confirmed Palantir–DWP welfare-data operational deal (implied by trajectory, **not found**; unverified).
- The Romanian-case precise jailing/offence counts (pin to a primary court/CPS source).

---

## 6. Consolidated primary source list

**Splink ↔ Palantir negative-control sources (the load-bearing evidence):**
- Splink repository — `github.com/moj-analytical-services/splink` (MIT; backends DuckDB/Spark/Postgres; no "Palantir"/"Foundry")
- Palantir Foundry data-integration docs — `palantir.com/platforms/foundry/data-integration/` (own connectors; no Splink)
- gov.uk Algorithmic Transparency Records — `moj-splink-master-record`, `moj-data-first-splink` (names no vendor)
- NHS England Data Science **Data Linkage Hub** — `nhsengland.github.io/datascience/our_work/data-linkage-hub` (Splink; no Palantir/Foundry/FDP)
- Local evidence log — `evidence/Splink-Palantir-Connection-Evidence.md`
- PwC–Palantir UK alliance — `pwc.co.uk/services/alliances/insights/pwc-palantir.html`; BusinessWire 2025-11-18

**NHS / FDP:**
- Digital Health — "NHS England awards £330m FDP contract to Palantir" (2023-11-21)
- The Register — "Palantir wins £330M NHS data platform contract" (2023-11-22); "NHS patients can't opt out…" (2026-06-13)
- Foxglove — FDP legal action (2023-11-30); £23m COVID concession (2021-04-01); "7 Key Risks" PDF (2023-06-05)
- CNBC — "Palantir … £1 deal" (2020-06-08); Digital Health — £23m extension (2020-12-14)
- GOV.UK — National Data Guardian statement, "Not With My NHS Data" (2026-06-03)
- NHS England — FDP FAQs / contract explainer; Hansard — NHS FDP (2026-04-16)
- Contracts Finder — Federated Data Platform notice
- Commons Science, Innovation and Technology Committee — termination recommendation (2026-06-03; via Electronics Weekly)

**MoD:**
- PRNewswire — £75m Enterprise Agreement (2022-12-21)
- The Register — £240.6m follow-on / exemption / revolving door (2026-01-28); TechRadar; UKAuthority
- GOV.UK — September 2025 strategic partnership; Find a Tender 083874-2025
- Hansard / ParallelParliament — MoD: Palantir Contracts, House of Lords (2026-02-10/11)
- ONS — "Service Leavers Database linkage to 2011 Census" (Splink 2; no Palantir); ONS Veterans' Survey 2022 → Census 2021

**Home Office / borders / cross-gov:**
- openDemocracy — "Palantir won borders contract after introduction from ex-MI6 boss" (2020/2021)
- PublicTechnology — "£20m 'border flow' contract" (2020-10-28)
- National Audit Office — "Investigation into the Homes for Ukraine scheme" (2023-10-17)
- Byline Times / The Citizens — "Involvement of Palantir and Faculty in the UK Public Sector" (2021-07-30)
- UKAuthority — DLUHC retains Palantir (2023); MHCLG in-house replacement (techmonitor/silicon.co.uk)
- Business Wire — Palantir named CCS supplier (2021-04-21); G-Cloud 14 service definition (2024-11-26)
- ONS — Integrated Data Service (Google Cloud/BigQuery); GOV.UK — National Fraud Initiative (Synectics); National Data Library progress update (2026-01)
- DPA 2018 immigration exemption — *R (ORG & the3million) v SSHD* [2021] EWCA Civ 800; Leigh Day / Open Rights Group (2023); Panopticon (2021-05-26)
- htworld — Reform "Operation Restoring Justice"; Medact — Palantir/NHS briefing (2026)
- American Immigration Council — ICE ImmigrationOS (US, 2025)

**Policing:**
- Liberty Investigates — "real-time surveillance network" / Nectar (2025-06-16)
- Bedford Independent — Bedfordshire DPIA / special-category data (2026)
- The Register — Palantir wins £9m firearms-licensing contract (2026-06-04)
- Computing — "Sadiq Khan blocks Met's £50m AI deal" (2026-05-21); The Register — Met £300m shopping list (2026-05-28)
- Leicester Gazette / leicester.news — Leicestershire/EMSOU; Good Law Project — "police forces dodge questions on Palantir"; Wayback (delisting, 2024-12-02)
- West Yorkshire Police — NDAS privacy notice (NDAS = Accenture/AWS)
- Democracy for Sale — "How UK police are hiding their Palantir work"

**MoJ:**
- The Guardian / Ben Quinn (via inkl) — MoJ reoffending-risk lobbying (2024-11-16); OECD.AI incident (2024-11-13)
- Statewatch — ARNS, 1,300+/day, in-house + PNC (2025-04)
- Tech Policy Press — MoJ ~30-corporation surveillance roundtable (2026)

**Corporate / governance:**
- The Nerve — "£670m+ UK contracts"; "Palantir pipeline: 30+ senior UK officials" (2026-02)
- openDemocracy — four ex-MoD hires; "NHS trusts ordered to share data"; £23m COVID lawsuit
- TechCrunch — tri-class voting structure (2020-08-21); Palantir FY2025 10-K (SEC)
- Healthcare IT News — Indra Joshi joins Palantir; Fast Company — In-Q-Tel/CIA origins
- Privacy International — "All Roads Lead to Palantir" (2021-11); Novara — "How a US spytech firm penetrated the British state" (2026-02-19)
- The Lowdown — FDP controversy/contracts/campaign; Amnesty UK — "No Palantir in our NHS"

**Prior investigation (companion):**
- *The Quiet Joining-Up* — `the-quiet-joining-up.pdf`; *Ruled Unlawful Next Door* — `supporting/Legal-Exposure/`

---

*Tone note for any editor: keep the Splink↔Palantir no-technical-link disclaimer verbatim; lead every Splink-context use of a Palantir profile with the weaker tier; attribute every aggregate figure to The Nerve as an investigative floor; and never, under any editing pressure, upgrade a Splink↔Palantir relationship above THEMATIC_ADJACENCY. The strength of this work is its refusal to manufacture the arrow everyone expects.*
