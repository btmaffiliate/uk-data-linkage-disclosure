# The Quiet Joining-Up: How the Ministry of Justice Links Personal Records Across the Justice System with Splink — A Public-Record Investigation

## Methods and sourcing-integrity statement

This report investigates the Ministry of Justice's (MoJ) use of **Splink** — its own open-source probabilistic record-linkage software — to deduplicate and link person-level records across prisons, probation and courts, and the associated Data First research programme, Core Person Record pilot, and a North Essex probation-to-police data-sharing pilot.

**Sourcing rules applied.** Every factual assertion is drawn from a publicly available source with a real, checkable URL. Each item is tagged **[confirmed]** (a public source actually states it), **[inference]** (reasoned from sources, labelled as such), or **[unanswered]** (not in the public record). Where original wording matters it is quoted verbatim. Composite or paraphrased wording is flagged as such and not presented as a verbatim quote. Where a source could not be retrieved directly (HTTP 403/404 anti-bot blocks on ICO, WhatDoTheyKnow, Contracts Finder, Find a Tender and parliament.uk), that limitation is stated and the affected fields are tagged unanswered rather than asserted.

**Splink ≠ Palantir.** Throughout, **Splink** is the MoJ's in-house open-source tool (moj-analytical-services GitHub org; Fellegi-Sunter probabilistic model). **Palantir** is a separate, US-owned vendor. No source located in this investigation links Splink to Palantir; both MoJ Algorithmic Transparency Records state external/third-party supplier involvement is "No." The two are never conflated. Likewise, the MoJ's *predictive* systems (OASys reoffending scoring; the "Homicide Prediction Project"/"Sharing Data to Improve Risk Assessment") are distinct from Splink, which is a *record-linkage* tool — no public source states Splink performs the linkage inside those prediction projects.

**Corrections applied from verification.** Following the verifiers' findings: (1) the MoJ-DfE PNC↔National Pupil Database link is reported as **deterministic** matching, **not** Splink; (2) the ADR UK data-quality study is correctly dated **July 2022** (not 2021); (3) the "deterministic, rule-based" characterisation of the MoJ-DfE link is presented as substance-supported paraphrase, not a single verbatim quote; (4) the Fellegi-Sunter description is attributed to its correct source (the GitHub repo / "joined-up data" GOV.UK page), not misattributed between README and ATR; (5) Census 2021/Cafcass linkage is cited to the ADR UK dataset page; (6) the 2019 origin quote is cited to the GOV.UK Data First guidance / IJPDS paper, not the "future of data-linking-methods" page that does not contain it; (7) the repo-description tagline vs README tagline distinction is noted; (8) the GitHub repo creation date (2019-11-22) is now confirmed via the GitHub API.

---

## Executive summary

**What is confirmed.** The MoJ uses Splink, its own open-source probabilistic record-linkage library (MIT licence; repo created 22 November 2019; based on the Fellegi-Sunter model with parameters estimated by unsupervised Expectation-Maximisation), to deduplicate and link person-level records across the justice system. Two GOV.UK Algorithmic Transparency Records (ATRs) are the most authoritative public sources: "MoJ: Data First (Splink)" (published 17 December 2024) and the broader "MoJ: Splink Master Record" (published 6 October 2025). They name the operational source systems — NOMIS (prison), DELIUS (probation), Common Platform (criminal courts), LIBRA (magistrates'), plus FamilyMan (family courts) and CaseMan (civil courts) for the JustLink product. Matching uses name(s), date of birth, addresses and sentence dates, with additional prison-dedup fields including ethnicity, nationality, birthplace, gender and height/weight. Several applications exist: JustLink (weekly anonymised research linkage), Probation in Court (real-time), the Core Person Record pilot (a real-time cross-justice unique identifier), and a North Essex pilot in which Splink identifies Police National Computer (PNC) numbers for probation supervisees that "are sent to the police each day." DPIAs exist (per use case); Splink was built in-house with no external supplier; Data First is grant-funded by ADR UK/ESRC, not procured; the platform is AWS-hosted.

**What remains unknown.** Despite this comparatively rich disclosure, the load-bearing documents are not public. The actual DPIA texts, Data Sharing Agreements, version histories and DPO sign-off dates are unpublished. Neither ATR cites a specific UK GDPR Article 6 sub-paragraph, an Article 9 condition, or DPA 2018 Schedule 1 paragraph, despite processing ethnicity and criminal-history data. There is **no** published Equality Impact Assessment, **no** Human Rights Act/Article 8 assessment, **no** independent ethics-board sign-off of the linkage models, and **no** published quantified fairness/bias-test results. There is **no** individual privacy notice, opt-out, or tailored subject-access route for affected individuals (prisoners, defendants, probationers); transparency relies on generic charters. The ICO has, on the public record, **never** taken enforcement action on, audited, or published an opinion about Splink/Data First. No automated-decision disclosure has visibly been updated for the Data (Use and Access) Act 2025 regime in force from 5 February 2026. These honest gaps are the substance of the exercise.

---

## 1. Data Categories

### Confirmed facts

**[confirmed] Splink is MoJ's own open-source probabilistic record-linkage library — not Palantir.** It is maintained by the moj-analytical-services GitHub org under an MIT licence; repo created 22 November 2019 (GitHub API `created_at: 2019-11-22T14:27:33Z`). The Master Record states the model is a *"Probabilistic Fellegi-Sunter record linkage model trained using unsupervised learning (the Expectation Maximisation (EM) algorithm)."* The GOV.UK "joined-up data" page states: *"Splink is a PySpark package that implements the Fellegi-Sunter model of record linking, and enables parameters to be estimated using the Expectation Maximisation algorithm."*
Sources: https://github.com/moj-analytical-services/splink ; https://api.github.com/repos/moj-analytical-services/splink ; https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record ; https://www.gov.uk/government/publications/joined-up-data-in-government-the-future-of-data-linking-methods/splink-mojs-open-source-library-for-probabilistic-record-linkage-at-scale (updated 16 July 2021)

**[confirmed] Four core operational source systems feed the linkage:** *"DELIUS (Probation) NOMIS (Prison) Common Platform (Criminal Courts) LIBRA (Magistrates' Court)."* Two further systems — *"FamilyMan (Family Courts) CaseMan (Civil Courts)"* — are used specifically for the JustLink product.
Source: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record (published 6 October 2025)

**[confirmed] Record volumes (pre-deduplication) are large:** LIBRA 19.6m, FamilyMan 20.9m, CaseMan 17.7m, Common Platform 2.9m, NOMIS 2.2m, DELIUS 2.4m. (Verbatim figures include *"LIBRA: 19.6m records Common Platform: 2.9m records NOMIS: 2.2m records DELIUS: 2.4m records."*)
Source: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] Core matching identifiers** are name(s), date of birth, current and past addresses, and sentence date(s): *"Date of Birth - Name(s) - Current and past addresses - Sentence date(s)."*
Source: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] Additional fields used for prison (NOMIS) deduplication include ethnicity and other sensitive identifiers:** *"Ethnicity - Birth place - Nationality - Gender - Person's height and weight."*
Source: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] Data suppliers are internal to MoJ:** *"N/A - all data is internal to MoJ."* The weekly JustLink output is *"a fully anonymised lookup table that contains the links between records"* (the Master Record's stronger wording notes it contains the links "but NOT the personal identifiers").
Source: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] A separate North Essex police pilot uses Splink to identify PNC numbers:** *"Splink is used to identify Police National Computer (PNC) numbers associated with individuals supervised by North Essex Probation Delivery Unit"* — those numbers are sent to police daily.
Source: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] Multiple distinct Splink applications exist,** evidencing expanding scope: JustLink (weekly research linkage), Probation in Court, the Essex police pilot, and the *"Core Person Record... A real-time linkage system that is currently being piloted that aims to create a unique identifier that links together each person across MoJ's criminal data systems (specifically courts, prisons and probation)."*
Source: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] A cross-government MoJ-DfE linked dataset links MoJ criminal-justice data (via PNC) to DfE's National Pupil Database (NPD):** *"Criminal history data from the Police National Computer (PNC) has been linked to education and social care data in England, sourced from the DfE's National Pupil Database (NPD)."*
Source: https://www.gov.uk/guidance/ministry-of-justice-data-first (last updated 14 May 2026)

**[confirmed — critical non-conflation] The original MoJ-DfE PNC↔NPD linkage was DETERMINISTIC (rule-based), NOT Splink.** The ADR UK MoJ-DfE data-quality report states the data was *"re-linked using deterministic methods"* (section 3.2), and a footnote records that the probabilistic Fellegi-Sunter/Splink framework is used *"Outwith the MoJ-DfE project."* The report's published Finding 3 records that *"just under two thirds (64%) of linked individuals matched exactly on all identifiers."* (The combined phrasing "deterministic, rule-based... 64% matched exactly" is a paraphrase/composite of these passages, not one contiguous verbatim sentence.)
Source: "Ministry of Justice – Department for Education linked dataset: Data quality report (Feasibility of evaluating early interventions for violence prevention)," ADR UK feasibility study, **July 2022**: https://www.adruk.org/fileadmin/uploads/adruk/Documents/Feasibility_study_1_MoJ-DfE_linked_dataset_Data_quality_report.pdf

**[confirmed] Datasets have demonstrably been ADDED over time** (Data First "Updates to this page" history): first published 30 June 2020; Crown Court / linked magistrates-Crown August–September 2020; prisoner custodial journey February 2021; probation February 2022; *"14 October 2022 - Splink information added"*; Family Court-Cafcass and cross-justice linking July 2024; *"31 July 2025 - Addition of Data First civil court data catalogue ... 29 July 2025 - Updated some wording to include the new Offender Assessments System (OASys) dataset"*; offender-assessments catalogue 19 December 2025; new MoJ/DfE analytical output 14 May 2026.
Source: https://www.gov.uk/guidance/ministry-of-justice-data-first

**[confirmed] The seven core Data First cross-justice datasets** are magistrates' courts, Crown Court, prisoner custodial journey, probation, offender assessment (OASys), family court and civil court, plus a person-level cross-justice linking table: *"person-level linkage across the seven datasets and also includes a case-level linking table for connecting the magistrates' courts and Crown Court data."*
Source: https://www.gov.uk/guidance/ministry-of-justice-data-first

**[confirmed] Family Court–Cafcass and Census 2021 linkages exist** as a distinct linked dataset (concerning children and families).
Source (corrected per verification): ADR UK, "Data First: Family Court linked to Cafcass and Census 2021 – England and Wales": https://www.adruk.org/data-access/flagship-datasets/data-first-family-court-linked-to-cafcass-and-census-2021-england-and-wales/

### Inferences

**[inference]** The ethnicity field used for NOMIS deduplication is **special-category data** under UK GDPR Article 9; nationality, birthplace and height/weight are sensitive personal identifiers. This Article-9 characterisation is the author's legal reading — neither ATR uses the phrase "special category data" or cites Article 9 (see gaps).

**[inference]** The expansion from a research-only pipeline (JustLink) to real-time operational identifiers (Core Person Record) and police sharing (North Essex) represents a material widening of the linkage's purpose beyond its 2019–2020 research origin, reasoned from the application list in the Master Record versus the earlier Data First framing.

### Gaps for this section

- **[unanswered]** Neither ATR explicitly classifies any field as "special category data" or cites Article 9, despite processing ethnicity, nationality, birthplace and height/weight.
- **[unanswered]** The full per-system field inventory is public only for NOMIS; the matching-field lists for DELIUS, Common Platform, LIBRA, FamilyMan and CaseMan are not enumerated. Whether OASys health/mental-health/substance-misuse items feed any Splink linkage is plausible but unconfirmed.
- **[unanswered]** Whether PNC is a standing input to the core JustLink linkage (vs pilot-only via North Essex and the separate MoJ-DfE share) is ambiguous.
- **[unanswered]** Whether Splink (vs deterministic or other tooling) performed the Cafcass/Census 2021 links is not confirmed from a primary document.
- **[unanswered]** No published production model "settings" (blocking rules / comparison columns) tying specific special-category fields to specific comparison logic was located in a primary MoJ artefact.

---

## 2. Data Protection Impact Assessment (DPIA)

### Confirmed facts

**[confirmed] A DPIA was completed for Data First:** *"A Data Protection Impact Assessment (DPIA) has been completed for the Data First Project, including the creation and sharing of the Data First datasets."* (Section 5.1, original ATR; published 17 December 2024; ATRS v3.0; model version 2023-03-01; single publication, no revision history shown.)
Source: https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink

**[confirmed] Per-use-case DPIAs/screenings:** *"DPIAs/DPIA screenings conducted for each Splink use case"* (Section 5.1, Master Record; published 6 October 2025; ATRS v4.0; Splink v4.0.8 as of June 2025), covering JustLink, Probation in Court, the Core Person Record pilot and the North Essex police pilot.
Source: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] The Data First Privacy Statement (Version 2.0, April 2021) commits to a living DPIA:** *"A Data Protection Impact Assessment (DPIA) will be completed prior to data sharing, to identify and assess risks to individuals' privacy and ensure appropriate protections are in place to minimise them. As the share evolves, so too will the details in the DPIA and DSA report."* It also states *"Each dataset shared between the MoJ and ONS will be subject to a DSA and DPIA."* The "Version 2.0 April 2021" marker belongs to the Privacy Statement, **not** the DPIA.
Source: https://assets.publishing.service.gov.uk/media/6099053bd3bf7f2887b642bd/data-first-privacy-statement.pdf

**[confirmed] DPO approval is documented only for one narrow, separate study:** *"A formal data protection impact assessment (DPIA) was carried out. The DPIA was approved by data protection officers in the MoJ and DHSC."* (Pathways between probation and addiction treatment — methodology annex, published 19 March 2026; also notes a signed MoJ-DHSC DSA and UKHSA Caldicott Guardian authorisation.)
Source: https://www.gov.uk/government/statistics/pathways-between-probation-and-addiction-a-follow-up-study/pathways-between-probation-and-addiction-treatment-in-england-a-follow-up-study-methodology

### Inferences

**[inference]** The Master Record (Oct 2025, broader, multiple use cases) appears to be a later, broader entry than the Data First (Splink) record (Dec 2024, research-dataset focus), created to cover newer deployments — but neither page declares a supersede/archive relationship.

**[inference]** Per-use-case DPIAs were produced as use cases expanded (Core Person Record, North Essex pilot), reasoned from the Privacy Statement's "as the share evolves" language plus the Master Record's "for each Splink use case." No specific updated versions, re-assessment dates, or formal revision of the original Data First DPIA are confirmed.

### Gaps for this section

- **[unanswered]** No full DPIA document is published anywhere located — only its existence is asserted.
- **[unanswered]** No DPIA version history or version numbers are public.
- **[unanswered]** No DPO sign-off date exists for the core Data First DPIA or the Master Record use cases (only the MoJ-DHSC study).
- **[unanswered]** No published source cites UK GDPR Article 35 (DPIA requirement) or Article 36 (prior consultation with the ICO) by number; whether Article 36 consultation occurred for any high-risk use case (e.g. real-time police sharing) is unknown.
- **[unanswered]** A WhatDoTheyKnow FOI thread (request 630081) surfaced a redacted ADR UK/MoJ Data First **Grant Agreement** — not a DPIA. No FOI release of the DPIA itself was found. (https://www.whatdotheyknow.com/request/630081)

---

## 3. Ethical Review

### Confirmed facts

**[confirmed] Downstream research-use proposals are scrutinised by panels that check for ethical issues, under the ONS Five Safes:** *"Each time a researcher wants to use these datasets they are required to complete a research proposal which is scrutinised by various panels ... These reviews ensure the proposal is feasible, addresses evidence gaps and identifies potential ethical issues."* This is ethics review of research **use** of the linked data, not of the linkage **model** itself.
Source: https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink

**[confirmed] Bias is acknowledged as an open, ongoing risk — not a passed audit:** *"Work is ongoing to identify potential sources of bias in the underlying data linkage models (e.g. ethnicity, gender, non-anglicised names), including a dedicated internship programme in conjunction with the Alan Turing Institute."*
Source: https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink

**[confirmed] The Master Record names differential accuracy as a key risk, mitigated by data-quality work (not a fairness gate):** *"Key risk 2: Linkage may be more or less accurate for different groups. Mitigation Differential linkage rates occur when we have poor data quality on peoples' identity and the primary purpose of the Core Person Record project is to improve data quality across all records."* (Risk 1: errors mitigated by "Detailed clerical review.")
Source: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] For Core Person Record only, the MoJ's ethics framework is being self-applied:** *"For Core Person Record, the newest application of Splink, MoJ's new ethics framework is being followed."*
Source: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] The MoJ AI and Data Science Ethics Framework (SAFE-D principles) was published 5 June 2025, co-produced with the Alan Turing Institute.** It describes a *"Data Ethics Team and Champions Network [that] can provide support and guidance"* — not an independent ethics board or mandatory sign-off panel — and does not mention Splink, record linkage or Core Person Record as a worked example.
Source: https://www.gov.uk/government/publications/ministry-of-justice-ai-and-data-science-ethics-framework/introduction-to-the-moj-ai-and-data-science-ethics-framework-text-only ; launch blog: https://mojdigital.blog.gov.uk/2025/06/05/principles-to-practice-launching-the-ministry-of-justice-ai-and-data-science-ethics-framework/

**[confirmed] The Splink team ran an informal internal ethics working session (Jan 2024) and published technical bias work (Aug + Dec 2024) from the Turing internship** — methodological outputs, not ethics-board approvals, EIAs, or human-rights assessments. The Jan 2024 post frames open-sourcing as motivated by *"an ambition to make our data linking software fully transparent, accessible and auditable."*
Sources: https://moj-analytical-services.github.io/splink/blog/2024/01/23/ethics-in-data-linking.html ; https://moj-analytical-services.github.io/splink/blog/2024/08/19/bias-in-data-linking.html ; https://moj-analytical-services.github.io/splink/blog/2024/12/02/bias-in-data-linking-continued.html

### Inferences

**[inference]** Governance of the linkage **model** is internal/self-assessed (MoJ Data Ethics Team / Champions Network; SRO = Chief Data Scientist) plus downstream research-use panels (ONS accredited-researcher route; ADR UK User Representation Panel) — not independently adjudicated by an external ethics board.

### Gaps for this section

- **[unanswered]** No published Equality Impact Assessment specific to Splink/Data First/Core Person Record, despite the likely applicability of the Public Sector Equality Duty (Equality Act 2010, s.149).
- **[unanswered]** No published Human Rights Act / Article 8 ECHR assessment for the linkage.
- **[unanswered]** No evidence of an independent ethics panel/external AI-ethics board reviewing or signing off the Splink models.
- **[unanswered]** No quantified, published fairness/bias test results (e.g. differential match rates by ethnicity, gender, non-anglicised names) for deployed models — the work is described as "ongoing."
- **[unanswered]** The ethics framework post-dates (June 2025) the earlier Data First linkage; there is no published equivalent ethics review for that earlier work.

---

## 4. Governance

### Confirmed facts

**[confirmed] Ownership and senior responsibility.** The Data First (Splink) record is owned by the Ministry of Justice / Data First team (contact datafirst@justice.gov.uk). The Master Record is owned by the *"Data Linking team"* (contact data_linking_team@justice.gov.uk), with the senior responsible owner listed as *"Chief Data Scientist."*
Sources: https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink ; https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] Access is restricted to the data-linking team:** *"The data is accessible only to staff on the data linking team who need access for model development and quality assurance."*
Source: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] Human oversight / clerical review.** *"Human review is typically used during the model training and quality assurance process to quantify accuracy. In use cases where Splink provides a list of possible matches to a human, the human then makes the final decision."* For Data First releases, *"a sample of records and person clusters are manually reviewed to ensure the models have performed as expected."*
Sources: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record ; https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink

**[confirmed] Downstream governance bodies disclosed in the Privacy Statement** include an Academic Advisory Group, an MoJ ethics advisory group and a User Representation Panel: *"To reflect the commitment of Data First to represent and protect the needs and interests of justice system users, a User Representation Panel has also been established."*
Source: https://assets.publishing.service.gov.uk/media/6099053bd3bf7f2887b642bd/data-first-privacy-statement.pdf

**[confirmed] Quality-monitoring controls (Master Record):** *"We have automated processes in place to monitor linkage quality and detect anomalies, and are working to improve these processes to more quickly identify and rectify errors."*
Source: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] ATRS itself is the governing transparency regime.** The Algorithmic Transparency Recording Standard *"[establishes] a standardised way for public sector organisations to publish information about how and why they are using algorithmic tools"* (published 5 January 2023); a scope/exemptions policy making it mandatory for departments and arm's-length bodies was published December 2024.
Source: https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub

### Inferences

**[inference]** Governance is institutionally documented (ownership, SRO, access controls, clerical review, downstream panels) but is predominantly internal/self-assessed for the linkage models themselves; the only external scrutiny named applies to research **use**, not to model deployment or the operational pilots.

### Gaps for this section

- **[unanswered]** No published terms of reference, membership, or minutes for the Academic Advisory Group, MoJ ethics advisory group or User Representation Panel.
- **[unanswered]** No governance/sign-off decision documents or dates for the Core Person Record or North Essex pilots.
- **[unanswered]** No published quantified error rates; both ATRs state clerical review is used to "quantify accuracy" but give no numeric outcomes.

---

## 5. Lawful Basis

### Confirmed facts

**[confirmed] RESEARCH USE — Digital Economy Act 2017 is named as the legal basis:** *"Data First has been developed within the framework established under the Digital Economy Act (DEA) (2017) which enables government to prepare administrative data for the purposes of research, and to provide de-identified versions of those data to researchers and projects accredited by the UK Statistics Authority (UKSA). This is the legal basis for the project and is the framework for ensuring that data is used responsibly, ethically and will not identify individuals."* (The relevant gateway is the research power in DEA 2017, Part 5, Chapter 5.)
Source: https://assets.publishing.service.gov.uk/media/6099053bd3bf7f2887b642bd/data-first-privacy-statement.pdf ; statute: https://www.legislation.gov.uk/ukpga/2017/30/part/5/chapter/5

**[confirmed] OPERATIONAL USE — common-law administration-of-justice powers:** *"MoJ is permitted to process data supplied by the police, the Crown Prosecution Service (CPS), courts and prisons by virtue of its common law powers for the administration of justice."* Sharing occurs only where *"a suitable legal gateway exists,"* in compliance with *"the General Data Protection Regulation (GDPR) and Data Protection Act 2018."*
Source: https://assets.publishing.service.gov.uk/media/6099053bd3bf7f2887b642bd/data-first-privacy-statement.pdf

**[confirmed] Special-category and criminal-history data acknowledged, but no specific Article 9 condition or DPA 2018 Schedule 1 paragraph named:** *"Information classed as 'special category' data under GDPR are sensitive, as is information about criminal histories. MoJ recognises the risk of this information being disclosed and requires additional justifications for processing and sharing this data, in line with GDPR."*
Source: https://assets.publishing.service.gov.uk/media/6099053bd3bf7f2887b642bd/data-first-privacy-statement.pdf

**[confirmed] The detailed lawful basis lives in unpublished DSAs/DPIAs:** the DSA *"establishes a framework for appropriate processing, including the contents and duration of the share, permitted uses of the data, the legal basis and justification for processing, and the protections in place throughout its lifecycle."*
Source: https://assets.publishing.service.gov.uk/media/6099053bd3bf7f2887b642bd/data-first-privacy-statement.pdf

**[confirmed]** Neither ATR cites a specific Article 6 sub-paragraph or Article 9 condition (a direct text search of the Privacy Statement PDF for "article 6", "article 9", "6(1)(e)", "9(2)(j)", "public task", "legitimate interest" returns zero matches).
Sources: https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink ; https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

### Inferences

**[inference]** Common-law administration-of-justice powers (operational) and the DEA research power (research) most plausibly map to **UK GDPR Article 6(1)(e)** (public task / official authority — which must be laid down by domestic law), with the research disclosure additionally engaging an **Article 9(2)(j)** (research/statistics) condition for special-category data. This mapping is **not stated verbatim** by the MoJ; it is a reasoned reading against ICO public-task guidance (https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/public-task/).

**[inference]** Legitimate interests (Article 6(1)(f)) is not cited and would in any case be unavailable to a public authority for its public-task processing (Article 6 final paragraph: point (f) *"shall not apply to processing carried out by public authorities in the performance of their tasks"*; gdpr-info.eu/art-6-gdpr/). Recorded to close the question, not as a positive finding.

### Gaps for this section

- **[unanswered]** No specific Article 6 sub-paragraph, Article 9(2) condition, or DPA 2018 s.10/s.11/Schedule 1 paragraph is named in any located source; whether an "appropriate policy document" exists is unknown.
- **[unanswered]** The DPIAs and DSAs that the Privacy Statement says actually contain "the legal basis and justification for processing" are unpublished.
- **[unanswered]** Whether the operational/real-time uses (Core Person Record; North Essex PNC sharing) engage the **law-enforcement regime (DPA 2018 Part 3)** rather than UK GDPR Part 2 for some processing is not specified anywhere — a material unresolved distinction.

---

## 6. Transparency

### Confirmed facts

**[confirmed] Organisation-level transparency exists** via two ATRs, the Data First guidance page, and the 12-page Data First Privacy Statement (v2.0, April 2021): *"This document outlines how Data First uses and shares data for research purposes and how this data is kept safe and secure."*
Sources: https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink ; https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record ; https://assets.publishing.service.gov.uk/media/6099053bd3bf7f2887b642bd/data-first-privacy-statement.pdf ; https://www.gov.uk/guidance/ministry-of-justice-data-first

**[confirmed] No Splink-specific notice to individuals; reliance on generic charters:** *"Provisions for using data collected in the course of the department's operations for research and statistical purposes are set out in the department's Personal Information Charter and that of Her Majesty's Courts and Tribunals Service (HMCTS)."* Subject access is by pointer only: *"Information on how to request access to copies of your personal information can be found in the MoJ's personal information charter or HMCTS personal information charter."*
Source: https://assets.publishing.service.gov.uk/media/6099053bd3bf7f2887b642bd/data-first-privacy-statement.pdf

**[confirmed] Research datasets are framed as outside decision-making:** *"The Data First datasets are not integrated into a decision-making process. They are datasets provided to academic researchers to study and identify trends within the justice system."* (Shared de-identified via the ONS Secure Research Service and SAIL Databank under the Five Safes.)
Source: https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink

**[confirmed] MoJ's stated ADM position — human-in-the-loop, no Splink-specific complaints route:** *"In use cases where Splink provides a list of possible matches to a human, the human then makes the final decision"*; and *"There are no complaint procedures specific to Splink itself since it does not directly make decisions about individuals. However, there is a formal complaints procedure for the various parts of the justice system which could be used if something was perceived to have gone wrong."*
Source: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] A genuinely operational, identifiable, real-time use exists — with no stated individual notice/opt-out/rights route:** *"Splink is used to identify Police National Computer (PNC) numbers associated with individuals supervised by North Essex Probation Delivery Unit. Those numbers are sent to the police each day to identify if any arrests have occurred."* (For the operational Core Person Record use, the Master Record notes there is no de-identification because the personal identifiers are essential to the task — i.e. the Five Safes/de-identification model applies to the **research** strand, not this operational matching.)
Source: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] The Data (Use and Access) Act 2025 replaced UK GDPR Article 22 with Articles 22A–22D** (commenced 5 February 2026 via S.I. 2026/82), introducing safeguards for significant automated decisions including a meaningful-human-involvement test, information, human-intervention and contest rights.
Source: https://www.legislation.gov.uk/ukpga/2025/18/section/80 ; ICO guidance: https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/the-data-use-and-access-act-2025-what-does-it-mean-for-organisations/

### Inferences

**[inference]** Whether DUAA 2025's ADM safeguards bite on Splink depends on whether the human "final decision" is genuine/meaningful involvement (Article 22A's "no genuine or meaningful human involvement" test). The MoJ's "human makes the final decision" framing suggests it treats Splink as human-in-the-loop and outside solely-automated rules — but for high-volume daily PNC matching at scale (North Essex), whether per-record review is genuinely meaningful is not evidenced. This is the MoJ's framing, not an independent finding, and could be contested.

### Gaps for this section

- **[unanswered]** No Splink/Data First-specific privacy notice served to affected individuals; no charter names Splink/linkage.
- **[unanswered]** No opt-out or right-to-object mechanism documented (research or operational).
- **[unanswered]** For the North Essex operational use, no published statement on whether/how those identifiable individuals are informed or exercise SAR/objection/contest rights for the linkage and onward police sharing.
- **[unanswered]** No ADM disclosure visibly updated for DUAA 2025 Articles 22A–22D.
- **[unanswered]** The Privacy Statement (April 2021) predates both the North Essex use and DUAA 2025 and may be out of date on individual rights.

---

## 7. Technical Architecture

### Confirmed facts

**[confirmed] Splink is an open-source (MIT) Python probabilistic record-linkage library** on the moj-analytical-services GitHub org. The repo's GitHub description reads *"Fast, accurate and scalable probabilistic data linkage with support for multiple SQL backends"*; the README's own top-line tagline is the shorter *"Fast, accurate and scalable data linkage and deduplication."* (Verifier note: cite the description for the longer phrase, the README for the shorter — they are different on-page locations.)
Source: https://github.com/moj-analytical-services/splink ; README: https://github.com/moj-analytical-services/splink/blob/master/README.md

**[confirmed] Algorithm:** Fellegi-Sunter with EM-estimated parameters. README: *"Splink's linkage algorithm is based on Fellegi-Sunter's model of record linkage, with various customisations to improve accuracy."* Master Record: *"Probabilistic Fellegi-Sunter record linkage model trained using unsupervised learning (the Expectation Maximisation (EM) algorithm)."*
Sources: https://github.com/moj-analytical-services/splink/blob/master/README.md ; https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] Supported SQL backends:** DuckDB (default/fastest, *"recommended for most users for all but the largest linkages"*), Spark (100M+ records), PostgreSQL; Athena/SQLite "minimal levels of support" in the v4 line; the v5 CHANGELOG records *"Dropped Amazon Athena support."*
Sources: https://moj-analytical-services.github.io/splink/topic_guides/splink_fundamentals/backends/backends.html ; https://github.com/moj-analytical-services/splink/blob/master/CHANGELOG.md

**[confirmed] MoJ production pipeline (Splink developer blog, 29 Jan 2026):** Splink + DuckDB run as containerised jobs (Docker images in ECR) on EC2, scaling via many parallel jobs; S3 for artefacts/models; AWS Athena via the Glue catalog for SQL cleaning and *"published lookup tables containing reference IDs linked back to raw system IDs"*; Apache Airflow orchestrates a six-stage weekly flow; trained models persisted as versioned .json artefacts.
Source: https://moj-analytical-services.github.io/splink/blog/2026/01/29/running-splink-in-production.html

**[confirmed] Hosting and security:** *"Ministry of Justice Analytical Platform ... OFFICIAL and OFFICIAL-SENSITIVE"*; controls include *"Two-factor authentication; Data encryption at rest and in transit; Granular access control; Extensive audit tracking"*; follows NCSC Cloud Security Principles. The platform *"serves over 500 data and analytics professionals,"* using *"Amazon Managed Workflows for Apache Airflow (Amazon MWAA), Amazon Athena and Amazon S3."*
Sources: https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record ; https://aws.amazon.com/solutions/case-studies/uk-ministry-of-justice/

**[confirmed] Versions:** Master Record cites deployed Splink v4.0.8 (June 2025); latest stable v4.0.16 (released 11 March 2026; Python ≥3.9,<4.0); v5.0.0.dev pre-release line from December 2025. The Data First research model is dated 2023-03-01 (predates Splink 4).
Sources: https://pypi.org/project/splink/ ; https://api.github.com/repos/moj-analytical-services/splink/releases ; https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink

**[confirmed] Data First model design:** two-layer (per-dataset dedup, then cross-dataset link) with 8 underlying linkage models and connected-components clustering: *"For each dataset, a deduplication model is trained and links are generated ... The second layer trains a model across all datasets to generate links between datasets."*
Source: https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink

**[confirmed] Methodology:** blocking generates candidate pairs and a match score is computed per pair (*"generates pairwise record comparisons using an approach called blocking, and computes a match score for each pair"*); comparison levels use string/distance metrics with configurable term-frequency adjustments and EM-estimated m/u probabilities.
Sources: https://dataingovernment.blog.gov.uk/2022/09/23/splink-fast-accurate-and-scalable-record-linkage/ ; https://moj-analytical-services.github.io/splink/topic_guides/comparisons/term-frequency.html

**[confirmed] Performance claim:** *"Capable of linking a million records on a laptop in around a minute."*
Source: https://github.com/moj-analytical-services/splink/blob/master/README.md

**[confirmed] Ecosystem repos:** the org exposes ~21 public repos including `splink`, `splink_udfs` (C++, MIT), `splink_datasets`, `uk_address_matcher` and `laurium` (LLM structured-extraction; README ties it to the **BOLD — Better Outcomes through Linked Data** project and an "AI for Linked Data" team, contacts AI_for_linked_data@justice.gov.uk / bold@justice.gov.uk).
Sources: https://api.github.com/orgs/moj-analytical-services/repos ; https://github.com/moj-analytical-services/laurium

**[confirmed — dead links]** The splink README's "Related Repositories" section links to `splink_scalaudfs` and `splink_synthetic_data`, both of which now return HTTP 404 (deleted, renamed or made private) — a stale-reference finding.

### Inferences

**[inference]** The MoJ stack is open-source Splink on MoJ's own AWS Analytical Platform — **not** a Palantir product. Every located technical source describes in-house open-source tooling on AWS; no source ties this linkage stack to Palantir.

**[inference]** JustLink and Core Person Record are downstream MoJ products that *consume* the Splink library; their pipeline/orchestration code is not present as a public repo (the terms appear only in ATRS prose, not as repo names).

### Gaps for this section

- **[unanswered]** No published architecture/data-flow diagram located.
- **[unanswered]** Exact Splink version pinned in each live pipeline beyond v4.0.8; the Data First model's exact Splink version is unstated.
- **[unanswered]** EC2 instance types/sizing, VPC/network topology, concurrency limits.
- **[unanswered]** Whether Core Person Record real-time lookups use the same containerised DuckDB engine or a low-latency service variant.
- **[unanswered]** Backup/DR, key-management and data-retention specifics for the operational (non-research) linked tables.
- **[unanswered]** Org-wide code search for "JustLink"/"Core Person Record" inside repo files could not be run (GitHub code-search API requires auth); confirmations come from ATRS, not from grepping repos.

---

## 8. Procurement

### Confirmed facts

**[confirmed] Splink/Data First built in-house, no external supplier.** The Data First (Splink) ATR states *"External supplier involvement: No"*; the Master Record states *"Third party involvement: No."* Splink is open source. Development data is *"stored securely in the department's analytical platform."*
Sources: https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink ; https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record

**[confirmed] Data First is GRANT-funded by ADR UK/ESRC, not procured:** *"a grant of almost £3 million to the Ministry of Justice"* announced 6 March 2020; renewal of *"over £2.3 million"* (announced 3 October 2022); and a £168m ADR UK portfolio for April 2026–March 2031. The underlying grant agreement was *"made on 9 September 2019 between the Economic and Social Research Council (as part of United Kingdom Research and Innovation) and The Ministry of Justice."*
Sources: https://popdatasci.swan.ac.uk/adrukinvestmojdata/ ; https://www.adruk.org/news-publications/news-blogs/renewed-adr-uk-funding-for-groundbreaking-data-first-programme/ ; https://www.ukri.org/news/168m-boost-for-public-data-project-improving-lives-across-the-uk/

**[confirmed] A redacted ADR UK/MoJ Data First Grant Agreement exists in the FOI record** (WhatDoTheyKnow request 630081). The title contains "Redacted" → redactions were applied; specific exemptions cited are not retrievable (host returns 403 to automated fetch).
Source: https://www.whatdotheyknow.com/request/630081

**[confirmed] The MoJ AWS hosting deal** ("Public Cloud Compute Storage and Ancillary Services," supplier Amazon Web Services EMEA; value £23,873,429; term 1 May 2021–30 April 2024; G-Cloud 12 call-off under the AWS One Government Value Agreement) is the department-wide host underpinning the Analytical Platform — **not** scoped specifically to Splink/Data First. The headline figure, dates, framework and OGVA route are independently corroborated by Data Center Dynamics; the primary Contracts Finder/bidstats pages return 403 to automated re-fetch (a human should click through to confirm the pence-level figure).
Sources: https://www.datacenterdynamics.com/en/news/uk-moj-signs-23-million-hosting-deal-with-aws/ ; Contracts Finder ref tender_253864/956718: https://www.contractsfinder.service.gov.uk/Notice/728ea9cc-969e-41df-a3b3-c2e7825d8240

**[confirmed — anti-conflation]** Two near-miss notices are **NOT** MoJ: Find a Tender 2021/S 000-031637 ("Cloud infrastructure, trusted research environment and researcher billing") belongs to **Our Future Health**; Contracts Finder "AWS 2024 3-year Renewal" belongs to the **Competition and Markets Authority**.
Sources: https://www.find-tender.service.gov.uk/Notice/031637-2021 ; https://www.contractsfinder.service.gov.uk/notice/91936239-43e0-414d-99e5-7b44e2d9fd4e

**[confirmed] The only data-linkage procurement notice located is NOT MoJ — it is National Records of Scotland** ("Probabilistic Data Matching for Data Linkage," 2025/S 000-003666), procuring a supplier to replace its on-premise *"Big Match"* solution with *"an Azure based 'Splink' solution."* This is strong evidence that other public bodies adopt MoJ's open-source Splink **via procurement**, while MoJ itself did not procure it.
Source: https://www.find-tender.service.gov.uk/Notice/003666-2025

**[confirmed — negative]** Programmatic OCDS search of Contracts Finder (award stage, keyword "data linkage") returned **no** MoJ/HMPPS notice on the subject; the only MoJ hit was an unrelated construction job. No Palantir contract appears in any record-linkage notice located.
Source: https://www.contractsfinder.service.gov.uk/Published/Notices/OCDS/Search?stages=award&keyword=data%20linkage

### Inferences

**[inference]** Because the tool is open-source/in-house and the programme is grant-funded, there was **no competitive tender** for the linkage capability itself — consistent with the absence of any award notice.

**[inference]** AWS capacity for the Analytical Platform is most likely consumed via a Crown Commercial Service cloud framework (G-Cloud / OGVA) rather than a Splink-specific notice — but no specific call-off notice was located, so the precise route is unconfirmed.

### Gaps for this section

- **[unanswered]** No notice ring-fences spend specifically to Splink/Data First.
- **[unanswered]** No successor MoJ AWS hosting notice located after the 30 April 2024 expiry.
- **[unanswered]** The unredacted value/terms of the ADR UK/MoJ grant agreement (redacted FOI attachment; 403 to automated fetch).
- **[unanswered]** The winning supplier and value of the NRS Splink-on-Azure notice (003666-2025).
- **[unanswered]** Whether Palantir holds any *unrelated* MoJ contract was outside this category and not investigated; none was found in scope.

---

## 9. Consolidated dated timeline

- **9 September 2019** — Grant agreement made between ESRC/UKRI and the MoJ funding Data First methodological work. **[confirmed]** https://www.whatdotheyknow.com/request/630081 ; corroborated https://popdatasci.swan.ac.uk/adrukinvestmojdata/
- **2019** — MoJ data-linking team challenged to develop a new linkage methodology, producing Splink (lead developer Robin Linacre). **[confirmed]** https://www.gov.uk/guidance/ministry-of-justice-data-first ; https://ijpds.org/article/view/1794 *(Robin Linacre as lead developer: [inference] from IJPDS authorship and his own site https://www.robinlinacre.com/probabilistic_linkage/ — not stated on the GOV.UK "future of data-linking-methods" page.)*
- **22 November 2019** — moj-analytical-services/splink GitHub repo created (`created_at: 2019-11-22T14:27:33Z`). **[confirmed]** https://api.github.com/repos/moj-analytical-services/splink
- **6 March 2020** — ADR UK announces "almost £3 million" grant to MoJ for Data First. **[confirmed]** https://popdatasci.swan.ac.uk/adrukinvestmojdata/
- **13 March 2020** — First public Splink release on PyPI (v0.1.3). **[confirmed]** https://pypi.org/project/splink/#history
- **30 June 2020** — Magistrates' court dataset becomes the first Data First product deposited in the ONS Secure Research Service; Data First guidance first published. **[confirmed]** https://www.gov.uk/guidance/ministry-of-justice-data-first *(ADR UK news page on the 30 June deposit currently 404s on direct fetch; re-confirm via an archived snapshot or live sibling page.)*
- **August 2020** — Crown Court dataset released. **[confirmed]** ADR UK Data First materials.
- **23 January 2021** — Splink v1.0.0. **[confirmed]** https://pypi.org/project/splink/#history
- **February 2021** — Prisoner custodial journey dataset released. **[confirmed]** ADR UK Data First materials.
- **April 2021** — Data First Privacy Statement v2.0 issued. **[confirmed]** https://assets.publishing.service.gov.uk/media/6099053bd3bf7f2887b642bd/data-first-privacy-statement.pdf
- **1 May 2021** — MoJ AWS hosting deal (G-Cloud 12 / OGVA) commences (to 30 April 2024). **[confirmed]** https://www.datacenterdynamics.com/en/news/uk-moj-signs-23-million-hosting-deal-with-aws/
- **16 July 2021** — GOV.UK "Splink: MoJ's open source library..." page (updated). **[confirmed]** https://www.gov.uk/government/publications/joined-up-data-in-government-the-future-of-data-linking-methods/splink-mojs-open-source-library-for-probabilistic-record-linkage-at-scale
- **7 November 2021** — Splink v2.0.0. **[confirmed]** https://pypi.org/project/splink/#history
- **22 February 2022** — Probation dataset added to Data First. **[confirmed]** https://www.gov.uk/guidance/ministry-of-justice-data-first
- **16 March 2022** — Population Data BC webinar by Robin Linacre on Splink. **[confirmed]** https://www.popdata.bc.ca/events/etu/webinar/splink_Mar16_2022
- **12 July 2022** — Splink v3.0.0. **[confirmed]** https://pypi.org/project/splink/#history
- **July 2022** — ADR UK MoJ-DfE linked-dataset data-quality report published (deterministic matching; 64% exact match). **[confirmed]** https://www.adruk.org/fileadmin/uploads/adruk/Documents/Feasibility_study_1_MoJ-DfE_linked_dataset_Data_quality_report.pdf
- **25 August 2022** — IJPDS paper "Splink: Free software for probabilistic record linkage at scale" published. **[confirmed]** https://ijpds.org/article/view/1794
- **23 September 2022** — "Data in Government" blog post by Robin Linacre. **[confirmed]** https://dataingovernment.blog.gov.uk/2022/09/23/splink-fast-accurate-and-scalable-record-linkage/
- **3 October 2022** — ADR UK renews Data First funding (>£2.3m). **[confirmed]** https://www.adruk.org/news-publications/news-blogs/renewed-adr-uk-funding-for-groundbreaking-data-first-programme/
- **14 October 2022** — "Splink information added" to the Data First guidance page. **[confirmed]** https://www.gov.uk/guidance/ministry-of-justice-data-first
- **5 January 2023** — Algorithmic Transparency Recording Standard Hub published. **[confirmed]** https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub
- **23 January 2024** — Splink team "Ethics in Data Linking" blog (informal working session). **[confirmed]** https://moj-analytical-services.github.io/splink/blog/2024/01/23/ethics-in-data-linking.html
- **4 March 2024** — Written Question UIN 16620 (Kevin Brennan MP) on unique identifiers; answered 7 March 2024 (Mike Freer MP), referencing the "Core Person record" and Splink. **[confirmed via index — verify verbatim]** https://questions-statements.parliament.uk/written-questions/detail/2024-03-04/16620
- **22 July 2024** — Family Court-Cafcass and cross-justice linking added to Data First. **[confirmed]** https://www.gov.uk/guidance/ministry-of-justice-data-first
- **24 July 2024** — Splink v4.0.0 (v3 to maintenance). **[confirmed]** https://pypi.org/project/splink/#history
- **August 2024 & December 2024** — Two technical "Bias in Data Linking" blog posts (Turing internship). **[confirmed]** https://moj-analytical-services.github.io/splink/blog/2024/08/19/bias-in-data-linking.html ; .../2024/12/02/bias-in-data-linking-continued.html
- **17 December 2024** — ATR "MoJ: Data First (Splink)" published (no mention of the North Essex police pilot). **[confirmed]** https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink
- **5 June 2025** — MoJ AI and Data Science Ethics Framework (SAFE-D) published. **[confirmed]** https://www.gov.uk/government/publications/ministry-of-justice-ai-and-data-science-ethics-framework/introduction-to-the-moj-ai-and-data-science-ethics-framework-text-only
- **29 & 31 July 2025** — OASys and civil-court datasets added to Data First. **[confirmed]** https://www.gov.uk/guidance/ministry-of-justice-data-first
- **6 October 2025** — ATR "MoJ: Splink Master Record" published (documents Core Person Record pilot and North Essex PNC-to-police daily sharing; Splink v4.0.8). **[confirmed]** https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record
- **19 December 2025** — Offender-assessments catalogue added; Splink v5.0.0.dev1 pre-release. **[confirmed]** https://www.gov.uk/guidance/ministry-of-justice-data-first ; https://api.github.com/repos/moj-analytical-services/splink/releases
- **29 January 2026** — "Running Splink in Production at the Ministry of Justice" blog (AWS architecture). **[confirmed]** https://moj-analytical-services.github.io/splink/blog/2026/01/29/running-splink-in-production.html
- **5 February 2026** — DUAA 2025 Articles 22A–22D commence (S.I. 2026/82). **[confirmed]** https://www.legislation.gov.uk/ukpga/2025/18/section/80
- **11 March 2026** — Splink v4.0.16 released. **[confirmed]** https://pypi.org/project/splink/#history
- **19 March 2026** — "Pathways between probation and addiction treatment" methodology published (MoJ-DHSC DPIA approved by both DPOs). **[confirmed]** https://www.gov.uk/government/statistics/pathways-between-probation-and-addiction-a-follow-up-study/pathways-between-probation-and-addiction-treatment-in-england-a-follow-up-study-methodology
- **5 April 2026** — Splink v5.0.0.dev3 pre-release. **[confirmed]** https://api.github.com/repos/moj-analytical-services/splink/releases
- **14 May 2026** — New MoJ/DfE analytical output added; Data First guidance last updated. **[confirmed]** https://www.gov.uk/guidance/ministry-of-justice-data-first

---

## 10. Public-record gaps

Each gap below states **why it matters**, the **likely holder**, and a **recommended pursuit route**.

1. **The actual DPIA documents (Data First, Core Person Record, North Essex pilot).** Why it matters: the DPIAs are where the Article 6/9 basis, risk assessment and mitigations actually live; their existence is asserted but never published. Holder: MoJ (Data Linking team). Route: targeted FOI to MoJ via WhatDoTheyKnow citing each named use case; if refused, ICO complaint / internal review.

2. **The Data Sharing Agreements,** especially for the North Essex PNC-to-police sharing. Why it matters: the Privacy Statement says the DSA contains "the legal basis and justification for processing." Holder: MoJ + Essex Police. Route: parallel FOIs to MoJ and Essex Police; Information Rights tribunal if needed.

3. **Specific Article 6 sub-paragraph and Article 9(2) condition + DPA 2018 Schedule 1 paragraph / appropriate-policy-document.** Why it matters: processing of ethnicity and criminal-history data requires a specific Article 9/DPA condition; none is named publicly. Holder: MoJ DPO. Route: FOI for the appropriate policy document; PQ to the Secretary of State for Justice.

4. **Whether operational uses fall under DPA 2018 Part 3 (law enforcement) or Part 2 (UK GDPR).** Why it matters: determines which rights, safeguards and ICO oversight apply to real-time matching and police sharing. Holder: MoJ + Home Office. Route: FOI; ICO clarification request.

5. **Equality Impact Assessment.** Why it matters: the Public Sector Equality Duty (Equality Act 2010 s.149) plausibly applies given differential-accuracy risk by ethnicity/non-anglicised names. Holder: MoJ. Route: FOI; PQ asking whether an EIA was conducted and will be published.

6. **Human Rights Act / Article 8 ECHR assessment.** Why it matters: large-scale linkage of justice-system personal data engages the right to private life. Holder: MoJ legal. Route: FOI; parliamentary scrutiny (Joint Committee on Human Rights).

7. **Independent ethics-board review and quantified bias-test results.** Why it matters: oversight of the model itself is internal/self-assessed; no pass/fail fairness metrics are published despite acknowledged differential accuracy. Holder: MoJ Data Ethics Team; Alan Turing Institute. Route: FOI for the referenced bias analysis and any ethics-board minutes; request the Turing internship outputs.

8. **Individual transparency: privacy notice, opt-out, tailored SAR/ADM-contest route.** Why it matters: affected individuals (prisoners, defendants, probationers) are not told their records are linked, especially for the operational North Essex use. Holder: MoJ / HMCTS / HMPPS / Essex Police. Route: FOI on how individuals are informed and can object; ICO complaint testing Articles 13/14 and DUAA 2025 ADM safeguards.

9. **Article 35/36 trigger and any ICO prior consultation.** Why it matters: high-risk real-time/police processing may require Article 36 ICO consultation. Holder: MoJ DPO; ICO. Route: FOI to MoJ; FOI/clarification to ICO (noting the ICO public record currently shows nothing on Splink/Data First).

10. **Procurement: post-2024 AWS successor notice; unredacted grant value; NRS Splink supplier/value.** Why it matters: the hosting envelope and funding terms are only partially public. Holder: MoJ Commercial; CCS; National Records of Scotland. Route: Contracts Finder / Find a Tender manual searches (these block automated fetch); FOI for the unredacted grant value; Public Contracts Scotland for the NRS award.

11. **Pilot start/governance dates for Core Person Record and North Essex.** Why it matters: there is no public sign-off date or duration for live operational deployment. Holder: MoJ. Route: FOI; PQ.

12. **Verbatim parliamentary text (UIN 16620, UIN 79552, "Court Reporting Data" debate 10 Feb 2026).** Why it matters: ministerial statements on Splink/Core Person Record are policy-load-bearing but only index-recovered here (parliament.uk returns 403 to automated fetch). Holder: parliament.uk / Hansard. Route: manual browser retrieval to confirm exact wording.

13. **Stale/removed repos `splink_scalaudfs` and `splink_synthetic_data`.** Why it matters: removed history may bear on reproducibility/audit claims. Holder: moj-analytical-services. Route: GitHub Issue or FOI; web.archive.org snapshots.

---

## Consolidated source list

**MoJ / GOV.UK primary records**
- MoJ: Data First (Splink) — ATR (17 Dec 2024): https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink
- MoJ: Splink Master Record — ATR (6 Oct 2025): https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record
- Ministry of Justice: Data First — guidance (last updated 14 May 2026): https://www.gov.uk/guidance/ministry-of-justice-data-first
- Data First: Privacy and data protection (v2.0, April 2021): https://assets.publishing.service.gov.uk/media/6099053bd3bf7f2887b642bd/data-first-privacy-statement.pdf
- Splink: MoJ's open source library... (joined-up data; 16 Jul 2021): https://www.gov.uk/government/publications/joined-up-data-in-government-the-future-of-data-linking-methods/splink-mojs-open-source-library-for-probabilistic-record-linkage-at-scale
- MoJ AI and Data Science Ethics Framework (5 Jun 2025): https://www.gov.uk/government/publications/ministry-of-justice-ai-and-data-science-ethics-framework/introduction-to-the-moj-ai-and-data-science-ethics-framework-text-only
- Ethics framework launch blog: https://mojdigital.blog.gov.uk/2025/06/05/principles-to-practice-launching-the-ministry-of-justice-ai-and-data-science-ethics-framework/
- Pathways between probation and addiction treatment — methodology (19 Mar 2026): https://www.gov.uk/government/statistics/pathways-between-probation-and-addiction-a-follow-up-study/pathways-between-probation-and-addiction-treatment-in-england-a-follow-up-study-methodology
- ATRS Hub: https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub
- Data in Government blog (23 Sep 2022): https://dataingovernment.blog.gov.uk/2022/09/23/splink-fast-accurate-and-scalable-record-linkage/

**Technical / Splink**
- GitHub repo: https://github.com/moj-analytical-services/splink — README: https://github.com/moj-analytical-services/splink/blob/master/README.md — CHANGELOG: https://github.com/moj-analytical-services/splink/blob/master/CHANGELOG.md
- GitHub API (repo metadata / releases): https://api.github.com/repos/moj-analytical-services/splink ; https://api.github.com/repos/moj-analytical-services/splink/releases ; org repos: https://api.github.com/orgs/moj-analytical-services/repos
- PyPI: https://pypi.org/project/splink/
- Backends docs: https://moj-analytical-services.github.io/splink/topic_guides/splink_fundamentals/backends/backends.html
- Term-frequency docs: https://moj-analytical-services.github.io/splink/topic_guides/comparisons/term-frequency.html
- Production blog (29 Jan 2026): https://moj-analytical-services.github.io/splink/blog/2026/01/29/running-splink-in-production.html
- Ethics/bias blogs: https://moj-analytical-services.github.io/splink/blog/2024/01/23/ethics-in-data-linking.html ; .../2024/08/19/bias-in-data-linking.html ; .../2024/12/02/bias-in-data-linking-continued.html
- laurium repo: https://github.com/moj-analytical-services/laurium
- AWS MoJ case study: https://aws.amazon.com/solutions/case-studies/uk-ministry-of-justice/

**ADR UK / academic**
- ADR UK MoJ-DfE data-quality report (Jul 2022): https://www.adruk.org/fileadmin/uploads/adruk/Documents/Feasibility_study_1_MoJ-DfE_linked_dataset_Data_quality_report.pdf
- ADR UK Family Court–Cafcass–Census 2021 dataset: https://www.adruk.org/data-access/flagship-datasets/data-first-family-court-linked-to-cafcass-and-census-2021-england-and-wales/
- ADR UK £3m investment news: https://popdatasci.swan.ac.uk/adrukinvestmojdata/
- ADR UK renewed funding: https://www.adruk.org/news-publications/news-blogs/renewed-adr-uk-funding-for-groundbreaking-data-first-programme/
- UKRI £168m: https://www.ukri.org/news/168m-boost-for-public-data-project-improving-lives-across-the-uk/
- IJPDS Splink paper (25 Aug 2022): https://ijpds.org/article/view/1794
- Robin Linacre site: https://www.robinlinacre.com/probabilistic_linkage/
- Population Data BC webinar (16 Mar 2022): https://www.popdata.bc.ca/events/etu/webinar/splink_Mar16_2022

**Legal / regulatory**
- DEA 2017, Part 5, Chapter 5: https://www.legislation.gov.uk/ukpga/2017/30/part/5/chapter/5
- DUAA 2025, s.80: https://www.legislation.gov.uk/ukpga/2025/18/section/80
- ICO DUAA guidance: https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/the-data-use-and-access-act-2025-what-does-it-mean-for-organisations/
- ICO public-task guidance: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/public-task/
- ICO Data Sharing Code: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/data-sharing-a-code-of-practice/
- UK GDPR Article 6 (reference): https://gdpr-info.eu/art-6-gdpr/

**Procurement / FOI / parliamentary**
- WhatDoTheyKnow request 630081 (redacted Data First grant agreement): https://www.whatdotheyknow.com/request/630081
- Contracts Finder MoJ AWS award: https://www.contractsfinder.service.gov.uk/Notice/728ea9cc-969e-41df-a3b3-c2e7825d8240
- DCD MoJ £23m AWS deal: https://www.datacenterdynamics.com/en/news/uk-moj-signs-23-million-hosting-deal-with-aws/
- NRS Splink-on-Azure notice: https://www.find-tender.service.gov.uk/Notice/003666-2025
- Anti-conflation (Our Future Health): https://www.find-tender.service.gov.uk/Notice/031637-2021
- Anti-conflation (CMA AWS renewal): https://www.contractsfinder.service.gov.uk/notice/91936239-43e0-414d-99e5-7b44e2d9fd4e
- Written Question UIN 16620: https://questions-statements.parliament.uk/written-questions/detail/2024-03-04/16620

**ICO enforcement touchpoints (both unrelated to Splink)**
- MoJ SAR-backlog enforcement notice (Jan 2022): https://ico.org.uk/action-weve-taken/enforcement/ministry-of-justice-1/
- MoJ confidential-waste reprimand (May 2023): https://ico.org.uk/action-weve-taken/enforcement/ministry-of-justice-reprimand/

**Distinct predictive systems (NOT Splink) — for non-conflation**
- Statewatch "murder prediction" (8 Apr 2025): https://www.statewatch.org/news/2025/april/uk-ministry-of-justice-secretly-developing-murder-prediction-system/
- Statewatch OASys profiling (9 Apr 2025): https://www.statewatch.org/news/2025/april/uk-over-1-300-people-profiled-daily-by-ministry-of-justice-ai-system-to-predict-re-offending-risk/
- Computer Weekly (25 Apr 2025): https://www.computerweekly.com/news/366623117/UK-MoJ-crime-prediction-algorithms-raise-serious-concerns

*Note on access limitations: ICO, WhatDoTheyKnow, Contracts Finder, Find a Tender and parliament.uk returned HTTP 403/404 to automated retrieval during this investigation. Affected facts were corroborated via search indexing and independent secondary reporting and are tagged accordingly; verbatim confirmation of those specific pages requires manual browser retrieval before quotation in any onward publication.*

---

# Part B — Follow-up questions, derived from the public-record gaps

*Every item below is generated directly from a numbered gap in Section 10 of the report above. Each is tagged with the gap it closes, the department it goes to, and the route. The questions are written to be specific and answerable, so that a refusal or a "we do not hold this" is itself on the record.*

**Keep the tracks separate:** Splink questions → **Ministry of Justice**; the Palantir trial → **Home Office/DHSC** (already begun). These are different systems with no documented link.

---

## B1. Next-round Written Parliamentary Questions to the Ministry of Justice

1. *(Gap 1)* To ask the Secretary of State for Justice whether she will **publish the Data Protection Impact Assessments** referenced in the "Splink Master Record" Algorithmic Transparency Record for (a) the Core Person Record pilot and (b) the North Essex probation-to-police data-sharing pilot.

2. *(Gap 2)* To ask the Secretary of State for Justice whether a **Data Sharing Agreement** governs the daily sharing of Police National Computer numbers with the police under the North Essex pilot, and whether she will place a copy in the Library.

3. *(Gap 3)* To ask the Secretary of State for Justice which **UK GDPR Article 6(1) lawful basis**, which **Article 9(2) condition**, and which **paragraph of Schedule 1 to the Data Protection Act 2018** are relied upon for the processing of ethnicity and criminal-history data in the Splink record-linkage programme, and whether an **appropriate policy document** is in place.

4. *(Gap 4)* To ask the Secretary of State for Justice whether the operational uses of Splink (the Core Person Record and the North Essex police-sharing pilot) are processed under **Part 2 (UK GDPR)** or **Part 3 (law enforcement processing)** of the Data Protection Act 2018.

5. *(Gap 5)* To ask the Secretary of State for Justice whether an **Equality Impact Assessment** has been completed for the Splink record-linkage programme, given the acknowledged risk of differential linkage accuracy by ethnicity and non-anglicised names, and whether it will be published.

6. *(Gap 6)* To ask the Secretary of State for Justice whether a **Human Rights Act / Article 8 ECHR assessment** has been completed for the large-scale linkage of justice-system personal data, and whether it will be published.

7. *(Gap 7)* To ask the Secretary of State for Justice whether the Splink linkage models have been reviewed by an **independent ethics board**, and whether she will publish the **quantified results of any bias or fairness testing** (including differential match rates by ethnicity and gender) for deployed models.

8. *(Gap 8)* To ask the Secretary of State for Justice **how individuals supervised by probation are informed** that their records are linked using Splink and their Police National Computer numbers shared with the police, and what **opt-out, subject-access, and right-to-object** mechanisms are available to them.

9. *(Gap 8)* To ask the Secretary of State for Justice whether the operational uses of Splink constitute **solely automated decision-making** within the meaning of Articles 22A–22D of the UK GDPR (as inserted by the Data (Use and Access) Act 2025), and what safeguards apply.

10. *(Gap 9)* To ask the Secretary of State for Justice whether the **Information Commissioner was consulted under Article 36** of the UK GDPR (prior consultation) before the deployment of any high-risk Splink use case, in particular the real-time Core Person Record and the daily police-sharing pilot.

11. *(Gap 11)* To ask the Secretary of State for Justice on what **date** the Core Person Record pilot and the North Essex probation-to-police pilot each began, what their **planned duration** is, whether they have been **evaluated**, and whether she intends to **extend** them nationally.

12. *(Governance gap)* To ask the Secretary of State for Justice what the **observed false-positive (incorrect match) and false-negative (missed match) rates** are for the operational use of Splink, and what **match-probability threshold** is applied before a link is acted upon.

13. *(Data gap)* To ask the Secretary of State for Justice whether any **special-category data within the Offender Assessment System (OASys)** — including health, mental-health or substance-misuse information — is used in any Splink linkage.

---

## B2. FOI requests (to obtain the documents the WPQs ask to be published)

**To the Ministry of Justice** *(data.access@justice.gov.uk — confirm)*:
- *(Gaps 1, 9)* The full text, version history and DPO sign-off dates of the DPIAs for Data First, the Core Person Record pilot, and the North Essex pilot; and any record of Article 36 ICO prior consultation.
- *(Gap 2)* The Data Sharing Agreement / MoU for the North Essex probation-to-police PNC sharing.
- *(Gap 3)* The "appropriate policy document" for special-category and criminal-offence processing under the Data Protection Act 2018.
- *(Gap 7)* The bias/fairness analyses produced with the Alan Turing Institute, and any ethics-board or Data Ethics Team minutes concerning Splink/Core Person Record.
- *(Gap 10)* The unredacted value and key terms of the ADR UK/MoJ Data First grant agreement (cf. WhatDoTheyKnow request 630081).

**To Essex Police** *(in parallel — they are joint controller for the pilot)*:
- *(Gap 2)* Their copy of the North Essex data-sharing agreement, their DPIA, and the legal basis relied upon for receiving and acting on the daily PNC feed.

**To the ICO** *(Gap 9)*:
- Any correspondence, advice, audit, or prior-consultation record concerning the MoJ Splink/Data First/Core Person Record programme (the public record currently shows none — a nil return is itself significant).

---

## B3. Other routes (for the gaps a WPQ or FOI won't reach)

- *(Gap 6)* **Joint Committee on Human Rights** — a referral on the Article 8 implications of population-scale justice-data linkage moving into operational, real-time use.
- *(Gap 12, verbatim parliamentary text)* **Manual Hansard retrieval** of UIN 16620 (4 Mar 2024), UIN 79552, and the "Court Reporting Data" debate (10 Feb 2026) — needed because parliament.uk blocked automated fetch; confirm exact ministerial wording before quoting.
- *(Gap 10, procurement)* **Public Contracts Scotland** for the National Records of Scotland "Splink-on-Azure" award (003666-2025) — shows another public body procuring the MoJ's open-source tool, useful as comparison; and **Contracts Finder** for any post-April-2024 MoJ AWS hosting successor (manual click-through; the site blocks automated fetch).
- *(Gap 13, stale repos)* A **web.archive.org** retrieval of `splink_scalaudfs` and `splink_synthetic_data` before they were removed, for the reproducibility/audit-trail point.

---

## B4. Sequencing note for the office

1. Table **B1 questions 1–5 and 8** first — DPIAs, the DSA, the Article 6/9 basis, the EIA, and individual transparency. These are the most concrete, the hardest to deflect, and the answers (or refusals) drive everything else.
2. File the **MoJ + Essex Police FOIs** in parallel — a WPQ that declines to publish a DPIA, set against an FOI that produces or withholds it, is the strongest possible record.
3. Use the **answers to question 4** (Part 2 vs Part 3 DPA 2018) to decide whether the matter is one for the ICO under the law-enforcement regime — it determines which rights and oversight apply.
4. Hold the **ICO** ask until at least one WPQ answer is in, so it can be framed against the Department's own words.
