# UK Public-Sector Data Linkage, Algorithmic Prediction & the City of London
## FULL DOSSIER — Complete Specification

**Compiled:** 2026-06-10 · **Updated:** 2026-06-11 · **Version:** FULL-SPEC 2.0 · Source-checked (0 dead links).

> **What this is / is not.** A complete transparency dossier from public primary sources, each verified
> live. **It alleges no illegality.** The processing is lawful; the case is *accountability, bias, and
> ethics*. Labels: CONFIRMED / LIKELY / UNKNOWN / SPECULATION. Verify primaries; take a media-law review.

**Central thesis (the spine).** UK public bodies link citizens' administrative records **at scale and
without consent** — lawfully, under public-task and law-enforcement powers — and use that linked data
not only to *match* people but to **profile and predict** them. The matching (MoJ's Splink) is
**probabilistic** and is used operationally, including a **probation→police daily PNC pilot**. Beyond
matching, the same data feeds **prediction systems with documented bias**: the **DWP's anti-fraud AI**
(its own analysis admits statistically significant bias by age/disability/marital status/nationality),
**OASys** reoffending tools (less accurate for Black offenders), and a **MoJ "Homicide Prediction
Project"** built on police + health data that sweeps in victims and witnesses. Much of the analytics
layer runs through a small number of contractors — notably **Palantir/PwC**. The DPIAs largely exist but
are **unpublished**; opt-outs and published error/redress are largely absent. Lawful — and, on the public
record, under-scrutinised.

This dossier consolidates two investigations verbatim. Part A = UK linkage & algorithmic prediction
(MoJ/NHS/ONS/DWP). Part B = City of London Corporation (incl. the Palantir/NFIB thread).


<div style="page-break-before: always;"></div>

# PART A — UK LINKAGE & ALGORITHMIC PREDICTION


<div style="page-break-before: always;"></div>

## A1. Disclosure summary

# UK Public-Sector Record Linkage — Public-Interest Disclosure

**A sourced, evidence-graded account of what is linked, by whom, under what legal basis, with what
safeguards, and what rights citizens have.**

- **Compiled:** 2026-06-10 · **Version:** 1.0
- **Status:** First-pass, fully source-checked. Open for correction.
- **Scope:** MoJ Splink; MoJ *Data First*; MoJ *BOLD*; NHS England *Data Linkage Hub*;
  ONS *Census 2021 → PDS*; and the UK GDPR / DUAA 2025 legal framework.

> **What this document is — and is not.** This is a transparency record assembled entirely from
> **public, primary sources**, each fetched and confirmed live on the access date shown. It **does
> not allege that any body has acted unlawfully.** Where the public record does not answer a
> question, that is marked **UNKNOWN** and turned into a Freedom of Information request — it is not
> filled by inference. Every factual statement carries a status and a source ID resolving to a URL
> in the Appendix. Please correct any error against the cited source.

## How to read the statuses
- **CONFIRMED** — established from a primary/official source, cited and verified live.
- **LIKELY** — strong inference or good secondary source; not yet primary-confirmed.
- **UNKNOWN** — no sourced answer in the public record → an open question / FOI request.
- **SPECULATION** — an explicit, labelled hypothesis. Never presented as fact.

---

## Executive summary

The UK operates several large **probabilistic record-linkage** programmes that join individuals'
records across government using **Splink**, an open-source matching library the Ministry of Justice
built and ADR UK funded. **[CONFIRMED]**

The public record is, in fact, reasonably full on *what* is linked, *by whom*, and *how access is
controlled*. The Ministry of Justice's own **Algorithmic Transparency Record** states the Data First
linkage is for **research and statistics only — "not for operational decision-making"** — and that a
**Data Protection Impact Assessment was completed.** **[CONFIRMED]** No evidence of unlawful conduct
was found, and the most serious concern (that linkage drives automated decisions about individuals)
is, on the government's own record, **not** the case for Data First.

What is **not** in the public record, and what this disclosure asks for, is narrow and specific:

1. **The completed DPIA is not published.** Its existence is officially confirmed; the document is not public.
2. **No individual opt-out or objection route** is documented for the MoJ linkage programmes.
3. **No programme-specific linkage-error rates are published, and no remedy is described** for a
   person who is wrongly linked.

Separately, the **Data (Use and Access) Act 2025** (in force 5 Feb 2026) rewrote the relevant law —
weakening the default protection against automated decisions for ordinary data, while retaining it
for sensitive data, and handing the boundaries of that regime to ministerial regulation. This is a
**policy** development worth public attention; it is **not** evidence of anything about the linkage
programmes, and is presented here as context, with one forward-looking concern explicitly labelled.

---

## 1. The linkage landscape (CONFIRMED unless noted)

- **Splink** is a Ministry of Justice-developed, open-source probabilistic record-linkage library
  (Fellegi–Sunter model, EM-trained), ADR-UK-funded under Data First. *(S01, S03, S25)*
- **Data First** links **seven** cross-justice datasets for England & Wales — magistrates', Crown,
  family and civil courts; prisoner custodial journey; probation; and **offender assessments
  (OASys)** — plus a **MoJ–DfE link** of criminal history to education data. *(S06, S07, S18, S24)*
  OASys carries 1,100+ variables including domestic-violence and sexual-offending assessments. *(S06)*
- The cross-justice product is a Splink-generated **person-link lookup table**, not the underlying
  case records. *(S07, S08)*
- **BOLD (Better Outcomes through Linked Data)** is a second, **broader** MoJ-led programme linking
  police, CPS, courts, prisons, probation, **health & social care, HMRC Child Benefit and
  drug-treatment (NDTMS)** data across many departments. *(S22)*
- **NHS England** is building a Splink-based **Data Linkage Hub**, using the Personal Demographics
  Service as the linkage "spine." *(S13, S41)*
- **ONS** used Splink to link **Census 2021 → PDS**, assigning NHS numbers and feeding the **Public
  Health Data Asset**. *(S14)*
- Access is by **accredited researchers** in de-identified form, via the **ONS Secure Research
  Service** (Five Safes; Digital Economy Act 2017 accreditation) and **SAIL Databank**. *(S06, S11,
  S30, S31, S33)*

## 2. Legal basis and safeguards (what the record shows)

- UK GDPR **special-category** processing requires **both** an Article 6 basis **and** an Article 9
  condition (plus a DPA 2018 Schedule 1 condition where relevant). *(S15, S16, S37 — CONFIRMED)*
- For the sibling **BOLD** programme the stated basis is **Art. 6(1)(e)** ("common law powers for the
  administration of justice") + **Art. 9(2)(h)** (health/social care, under Caldicott and NHS
  IGARD). *(S22 — CONFIRMED)* The equivalent published statement for **Data First** sits in a
  privacy-statement PDF that could not be machine-read for this pass *(S20 — to confirm)*.
- The **research/statistics** Article 9 condition (DPA 2018 Sch. 1 Pt 1 para 4) now references UK
  GDPR **Art. 84B** (formerly Art. 89(1)), per DUAA 2025; that paragraph does not itself require an
  appropriate policy document. *(S37 — CONFIRMED)*
- **Data First use is research-only — "not for operational decision-making"; not integrated into any
  decision-making process** — per the MoJ Algorithmic Transparency Record (v3.0, 17 Dec 2024), which
  also states a **DPIA was completed.** *(S19 — CONFIRMED)*

## 3. The legal backdrop: Data (Use and Access) Act 2025 (context)

Verified against primary text on legislation.gov.uk *(S42–S50)*:

- DUAA 2025 **substituted** UK GDPR Article 22 with new **Articles 22A–22D** (in force 5 Feb 2026). *(S48, S42)*
- For **ordinary** personal data the old prohibition-by-default on solely-automated significant
  decisions becomes **permitted-unless**; for **special-category** data a **near-prohibition is
  retained** (Art. 22B). *(S44 — CONFIRMED)*
- Core safeguards (be informed, make representations, obtain human intervention, contest) are
  **retained** in Art. 22C. *(S45 — CONFIRMED)*
- A new lawful basis, **Art. 6(1)(ea) "recognised legitimate interest"**, draws on an **Annex 1** the
  **Secretary of State may amend by regulations**; Annex 1 categories include national security,
  **crime**, emergencies and safeguarding. *(S47, S49 — CONFIRMED)*
- **Article 22D** lets the **Secretary of State define, by regulation,** what counts as "meaningful
  human involvement" and "significant effect," and modify how the safeguards operate (affirmative
  procedure). *(S46 — CONFIRMED)*
- The indirect-collection transparency duty (**Article 14**) was also amended. *(S50 — LIKELY; verbatim check pending)*

> **Labelled hypothesis (SPECULATION — watch-item, not a claim):** the Art. 22D regulation power and
> the SoS-amendable Annex 1 are *general* levers that could, in future, re-scope automated-decision
> protections across government. There is **no evidence** any such regulation targets the linkage
> programmes. Recorded only as something to monitor (the relevant statutory instruments), explicitly
> not as an assertion of intent.

## 4. The transparency gaps — and the asks (UNKNOWN → FOI)

These are framed as requests for documents and facts, alleging nothing:

1. **Publish the completed Data First DPIA** that the Algorithmic Transparency Record says exists. *(C11b)*
2. **State whether any individual opt-out / objection route exists** for Data First and BOLD, and how
   it is exercised. *(C12)*
3. **Publish linkage-error rates** (false-match / missed-match) and **describe the remedy** for a
   person wrongly linked. *(C14)*
4. **Confirm the lawful basis and Article 9/10 conditions** for Data First and BOLD, and release
   their DPIAs. *(C25, C26; FOI-1, FOI-5)*
5. **Clarify the NHS Data Linkage Hub's status** and whether the National Data Opt-Out applies. *(C08, FOI-2)*
6. **Confirm the ONS Census→PDS legal gateway** and downstream PHDA uses/retention. *(C17, C09, FOI-3)*

Full draft requests to MoJ, NHS England, ONS and ADR UK are in `foi/foi_requests.md`.

## 5. What this disclosure does NOT say

- It does **not** allege any unlawful processing, breach, or bad faith by any body.
- It does **not** claim the linkage drives decisions about individuals — the official record says the
  opposite for Data First.
- It does **not** treat "we could not find X" as "X does not exist" — only as a transparency gap.
- It contains **nothing** that could help re-identify any individual.

## 6. Methodology, verification and limitations

- Every source was fetched and confirmed live; an automated checker (`scripts/source_checker.py`)
  re-verifies the whole register and is run before release. At compilation: **0 dead links.**
- Statutory references were verified against the **current** text on legislation.gov.uk, including
  the DUAA 2025 amendments in force 5 Feb 2026.
- **Limits, stated honestly:** two MoJ PDFs (the Data First privacy statement S20 and the MoJ–DfE
  notice S23) resolve and download but could not be text-extracted by the tools used, so their
  contents do **not** back any claim here and should be read directly. Several NHS Digital / ICO
  pages block automated clients; their points were sourced from accessible equivalents (the dropped
  URLs are logged in `evidence/raw_links.json`). The ONS legal gateway (C17) is **LIKELY**, not
  confirmed. The Article 14 change (C24) needs a verbatim read.
- This compilation was assembled with AI research assistance. **Before formal publication or
  transmission to officials, it should be reviewed by a person and, ideally, a media/data-protection
  lawyer** — not because of any known inaccuracy, but because the stakes warrant it.

---

## Appendix — Source register (verified live 2026-06-10)

Resolves to the machine-readable register in `evidence/raw_links.json` and the table in
`research/sources.md`. Flags: LIVE · STALE? (live, legacy URL) · binary PDF (manual read).

**Splink (core):** S01 repo `github.com/moj-analytical-services/splink` · S02 docs
`moj-analytical-services.github.io/splink` · S03 IJPDS paper `ijpds.org/article/view/1794` ·
S04 org `github.com/moj-analytical-services` · S25 gov.uk blog
`dataingovernment.blog.gov.uk/2022/09/23/splink-fast-accurate-and-scalable-record-linkage/` ·
S26 evaluation tutorial `.../splink/demos/tutorials/07_Evaluation.html`.

**MoJ Data First / BOLD:** S06 ADR annual report `reports.adruk.org/annual-report-2023-2024/...` ·
S07 ONS SRS metadata `ons.metadata.works/browser/dataset?id=58617` · S08 ADR catalogue
`datacatalogue.adruk.org/browser/dataset/58617/1` · S11 HMCTS data access
`gov.uk/guidance/access-hmcts-data-for-research` · S18 Data First landing
`gov.uk/guidance/ministry-of-justice-data-first` · **S19 Algorithmic Transparency Record**
`gov.uk/algorithmic-transparency-records/moj-data-first-splink` · S20 privacy statement (PDF) ·
S21 user guide v8.2 (PDF) · **S22 BOLD privacy notice**
`gov.uk/government/publications/ministry-of-justice-better-outcomes-through-linked-data-bold/...` ·
S23 MoJ–DfE notice (PDF) · S24 criminal-courts landing `gov.uk/government/publications/data-first-criminal-courts-linked-data`.

**ONS / ADR UK / SAIL:** S14 Census→PDS report `ons.gov.uk/.../census2021topersonaldemographicsservicelinkagereport` ·
S30 SRS data-access policy · S31 About the SRS · S32 ADR UK ethics `adruk.org/about-us/ethics-responsibility/` ·
S33 SAIL governance `saildatabank.com/governance/` · S38 ONS special-category for statistics · S39 NSDEC
`uksa.statisticsauthority.gov.uk/.../national-statisticians-data-ethics-advisory-committee/`.

**NHS England:** S13 Data Linkage Hub `nhsengland.github.io/datascience/our_work/data-linkage-hub/` ·
S28 HRA National Data Opt-Out (CAG/s.251) · S40 FDP overarching DPIA
`england.nhs.uk/long-read/overarching-data-protection-impact-assessment-dpia-for-the-federated-data-platform-fdp/` ·
S41 IJPDS NHS pipeline `ijpds.org/article/view/3271`.

**Law (ICO / legislation.gov.uk):** S15–S17 ICO lawful-basis/special-category guidance · S35 ICO DUAA
summary · S36 ICO right-to-be-informed exceptions · **S37 DPA 2018 Sch. 1**
`legislation.gov.uk/ukpga/2018/12/schedule/1` · **S42 DUAA 2025** `legislation.gov.uk/ukpga/2025/18/contents` ·
**S43–S46 UK GDPR Arts. 22A–22D** `legislation.gov.uk/eur/2016/679/article/22A` (…22B/22C/22D) ·
S47 Art. 6 (incl. 6(1)(ea)) · S48 Art. 22 (substituted) · S49 Annex 1 (recognised legitimate
interests) · S50 Art. 14 (as amended).

_Retired/dropped (logged in `raw_links.json` `_meta`): S05 (ADR project page, 404×3); three
NHS Digital/ICO subpages that block automated clients (points carried by accessible equivalents)._


<div style="page-break-before: always;"></div>

## A2. Claims matrix (C01–C36)

# Claims matrix

One atomic assertion per row. Status ∈ {CONFIRMED, LIKELY, UNKNOWN, SPECULATION}.
A claim may be CONFIRMED only if its source is **live-verified** (see `source_check_report.md`)
and the supporting content was actually read. UNKNOWN rows carry no sourced answer and feed
`open_questions.md` / `foi_requests.md`.

> **Statutory baseline (verified 2026-06-10):** UK references are rebased to the **Data (Use and
> Access) Act 2025** (2025 c.18, S42), in force 5 Feb 2026. It replaced UK GDPR **Art. 22** with
> **Arts. 22A–22D** (S43) and renumbered the research safeguard **Art. 89(1) → Art. 84B** (seen in
> the current DPA 2018 Sch. 1 text, S37). "Article 9 + Article 6 both required" is unchanged.

| ID | Claim | Status | Source | Evidence | Confidence | Legal relevance | Follow-up needed |
|----|-------|--------|--------|----------|------------|-----------------|------------------|
| C01 | Splink is a MoJ-developed open-source probabilistic record-linkage library (Fellegi–Sunter, EM-trained). | CONFIRMED | S01, S03, S25 | MoJ repo + IJPDS paper + gov.uk blog. | High | Identifies the linkage technique. | Confirm licence (MIT) + maintained version. |
| C02 | Splink's development was funded by ADR UK under the Data First programme. | CONFIRMED | S03, S18 | IJPDS acknowledgement + gov.uk Data First page. | High | Ties tool to a funded govt programme. | — |
| C03 | Data First comprises 7 cross-justice datasets (magistrates', Crown, family, civil courts; prisoner custodial journey; probation; offender assessments/OASys) for E&W, plus a MoJ–DfE criminal-history × education link. | CONFIRMED | S06, S07, S18, S24 | ADR report + ONS SRS metadata + gov.uk guidance (7 named datasets) + criminal-courts doc. | High | Breadth of cross-domain linkage. | — |
| C04 | The cross-justice dataset is a Splink-generated person-link *lookup table*, not the underlying interaction records. | CONFIRMED | S07, S08 | ONS SRS + ADR catalogue metadata. | Medium-High | Distinguishes identity key from case data. | Verify wording verbatim. |
| C05 | Data First includes OASys data (1,100+ variables, incl. DV / sexual-offending assessments). | CONFIRMED | S06 | ADR UK annual-report description. | Medium-High | OASys fields likely Art. 9 + Art. 10 data. | Confirm field list verbatim (FOI/manual). |
| C06 | Data First data is de-identified and accessed by accredited researchers via ONS SRS (Five Safes; DEA 2017) and SAIL Databank. | CONFIRMED | S06, S11, S30, S31, S33 | ADR + gov.uk + ONS SRS policy + SAIL governance. | High | Five Safes governance; re-identification risk. | — |
| C07 | A MoJ↔DfE (education / National Pupil Database) data-share exists, accessed via ONS SRS. | CONFIRMED | S06, S18, S23 | ADR report + gov.uk page + existence of MoJ-DfE privacy notice (2025-10). | Medium-High | Cross-departmental linkage beyond justice. | Read S23 PDF for datasets + legal gateway. |
| C08 | NHS England is building a Splink-based probabilistic linkage service (Data Linkage Hub), using PDS as the spine. | CONFIRMED | S13, S41 | NHS England Data Science site + IJPDS pipeline paper. | Medium-High | Extends Splink into health data. | Confirm production-vs-pilot (FOI). |
| C09 | ONS used Splink to link Census 2021 → PDS (assigning NHS numbers; feeding the Public Health Data Asset). | CONFIRMED | S14 | ONS Census→PDS methodology report. | High | Health-identifier assignment from a census. | Confirm PHDA downstream use + retention. |
| C10 | UK GDPR special-category processing requires BOTH an Art. 6 basis AND an Art. 9 condition (+ DPA 2018 Sch. 1 where relevant). | CONFIRMED | S15, S16, S37 | ICO guidance + DPA 2018 Sch. 1 text. | High | Core compliance test for OASys / health linkage. | — (DUAA 2025 left the dual test intact). |
| C11 | A DPIA was **completed** for the Data First programme. | CONFIRMED | S19 | Algorithmic Transparency Record states a DPIA was completed. | Medium-High | Art. 35 accountability. | Obtain the DPIA itself (→ C11b). |
| C11b | The Data First DPIA is **published** (in full or redacted form). | UNKNOWN | — | Not located in the public record. | — | Art. 5(2)/35 transparency. | **FOI-1 §1** to MoJ. |
| C12 | A documented individual opt-out from inclusion in Data First linkage. | UNKNOWN | — | Not located. The MoJ Data First guidance page (S18) mentions no opt-out; the sibling BOLD notice (S22) offers none either. NHS NDOO (S28) applies to s.251 research linkage only. | — | Arts. 21/18; sectoral opt-out. | **FOI-1 §2** (MoJ); confirm NDOO scope for NHS Hub. |
| C13 | Data First linkage outputs are used for **research/statistics only — not operational decision-making** about individuals. | CONFIRMED | S19 | ATRS: linkage "not for operational decision-making"; "not integrated into a decision-making process." | Medium-High | Purpose limitation 5(1)(b); Art. 22A. | Confirm no downstream operational re-use (FOI). |
| C14 | Published programme-specific false-positive/negative rates and an individual remedy for mis-linkage. | UNKNOWN | — | Splink *capability* to measure error is documented (S26); ATRS notes manual sample review + bias work (S19); programme-specific published rates/remedy not located. | — | Accuracy 5(1)(d); rectification Art. 16. | **FOI-1 §6**: published rates + correction process. |
| C15 | DUAA 2025 replaced UK GDPR Art. 22 with Arts. 22A–22D (in force 5 Feb 2026). Under Art. 22B, solely-automated significant decisions based wholly/partly on **special-category data are prohibited** (narrow exceptions, e.g. explicit consent); for **ordinary** personal data the former blanket bar is **relaxed** (restricted mainly where relying on the new Art. 6(1)(ea) basis, with Art. 22C safeguards). | CONFIRMED | S42, S43, S44, S35 | Act + UK GDPR Arts. 22A (definitions) & 22B (operative restriction) on legislation.gov.uk; ICO summary. | High | Sensitive (OASys/health) linkage retains strong protection; relaxation is for ordinary data. | Confirm exact 22B exceptions + Art. 6(1)(ea) wording if it becomes load-bearing. |
| C16 | The DPA 2018 Sch. 1 Pt 1 "Research etc." condition now references UK GDPR Art. 84B (formerly Art. 89(1)), per DUAA 2025; para 4 itself does not require an appropriate policy document. | CONFIRMED | S37 | Current revised DPA 2018 Sch. 1 text on legislation.gov.uk. | High | Identifies the live research safeguard + accountability boundary. | — |
| C17 | The ONS Census→PDS linkage relies on the Statistics and Registration Service Act 2007 (with DEA 2017 governing SRS access) as its legal gateway. | LIKELY | (search-derived; not in S14) | Search results cite SRSA 2007 ss.43–44 + DEA 2017, but the S14 methodology report does NOT state the gateway, and the ONS source pages that do are bot-blocked. | Low-Medium | Statutory basis for assigning NHS numbers. | **FOI-3 §2** or browser-verify ONS PDS source pages; do not assert as CONFIRMED. |
| C23 | DUAA 2025's Art. 6(1)(ea) "recognised legitimate interests" (Annex 1) include national security/defence, crime (detect/investigate/prevent; apprehend/prosecute offenders), emergencies, and safeguarding. | CONFIRMED | S49 | UK GDPR Annex 1 on legislation.gov.uk. | High | New lawful-basis categories, several justice/crime-shaped; Annex 1 is SoS-amendable. | Read each Annex 1 condition verbatim. |
| C24 | DUAA 2025 amended UK GDPR Art. 14(5) (transparency where data not obtained from the data subject), reworking the exemptions and adding a "make information available publicly" measure. | LIKELY | S50 | Current Art. 14 text shows DUAA amendment markers; exact restructuring read summarily. | Medium-High | Governs whether linked individuals must be informed — core transparency point. | **VERIFY VERBATIM**; trace effect on research/indirect-collection exemption. |
| C25 | The MoJ also runs BOLD (Better Outcomes through Linked Data), a cross-government linkage programme spanning police, CPS, courts, prisons, probation, health & social care, HMRC Child Benefit, and drug-treatment (NDTMS) data across multiple departments. | CONFIRMED | S22 | BOLD privacy notice (gov.uk). | High | A second, broader linkage programme involving highly sensitive data. | Obtain BOLD DPIA; confirm production status. |
| C26 | BOLD's stated lawful basis is Art. 6(1)(e) (administration of justice) + Art. 9(2)(h) (health/social care, under Caldicott / IGARD), with no explicit opt-out (access rights via formal request only). | CONFIRMED | S22 | BOLD privacy notice. | Medium-High | Shows the MoJ lawful-basis template for linkage; opt-out absent. | Confirm whether Data First uses the same basis (read S20). |
| C18 | DUAA 2025 substituted the old Art. 22 (prohibition-by-default) with a new Section 4A; for **ordinary** personal data the baseline flips to permitted-unless. | CONFIRMED | S48, S44 | legislation.gov.uk substitution note + Art. 22B text. | High | Weakens the default ADM protection for ordinary data. | Confirm consequential edits to Arts. 13–15. |
| C19 | DUAA 2025 added Art. 6(1)(ea) "recognised legitimate interest" (conditions in Annex 1, SoS-amendable). | CONFIRMED | S47 | UK GDPR Art. 6 / Art. 6(5) on legislation.gov.uk. | High | New, partly executive-set lawful basis; trigger for the 22B ordinary-data restriction. | Read Annex 1 conditions verbatim. |
| C20 | Art. 22C retains safeguards for permitted automated significant decisions: information, representations, human intervention, ability to contest. | CONFIRMED | S45 | UK GDPR Art. 22C text. | High | Core ADM safeguards carried over. | — |
| C21 | Art. 22D empowers the Secretary of State, by regulations (affirmative procedure), to define "meaningful human involvement" / "significant effect" and modify how the 22C safeguards operate. | CONFIRMED | S46 | UK GDPR Art. 22D text. | High | Boundaries of the ADM regime are delegated to the executive. | Track any Art. 22D regulations / SIs. |
| C22 | The DUAA ADM reform does **not** newly authorise the linkage programmes to take automated decisions; special-category solely-automated significant decisions remain prohibited (Art. 22B). | CONFIRMED | S19, S44 | ATRS (research-only) + Art. 22B prohibition. | Medium-High | Rebuts any inference the reform "opened a door" for these programmes. | Monitor only (see teardown §6). |

| C27 | Splink is used **operationally** within MoJ (beyond research): the "Splink Master Record" ATR describes a real-time **Core Person Record** (unique IDs across the justice system), **Probation in Court** (retrieving probation records when an individual appears in court), and a **police data-sharing pilot linking to PNC numbers** for arrest-information requests. | CONFIRMED | S51 | MoJ Splink Master Record ATR (gov.uk, 2025-10-06), read 2026-06-10. | High | **Refines C13**: Data First specifically is research-only, but Splink *more broadly* has operational, individual-affecting, police-facing uses. Bears on purpose limitation + (potential) Art. 22A. | Obtain DPIAs for Core Person Record / PNC pilot; confirm whether any solely-automated decision occurs. |
| C28 | MoJ's Splink deployment is described as running on **Apache Spark**; **DuckDB is a backend Splink supports generally** but is not evidenced as MoJ's operational engine. | CONFIRMED | S51, S25 | gov.uk publication names Spark/PySpark; Splink docs list DuckDB/Spark/Athena backends. | Medium | Clarifies the tech stack; corrects any assumption that a specific deployment uses DuckDB. | — |

| C29 | DPIAs (or DPIA screenings) were **conducted for each Splink use case**, but none is published or linked in the transparency record. | CONFIRMED | S51 | Splink Master Record ATR, read 2026-06-10. | High | Art. 35 accountability done; publication is the gap. | **FOI**: release the Core Person Record + Essex-PNC-pilot DPIAs. |
| C30 | The MoJ states Splink **"does not directly make decisions about individuals"**; where it surfaces candidate matches a **human makes the final decision** (human-in-the-loop), with trained staff for manual merges/unmerges. | CONFIRMED | S51 | Splink Master Record ATR. | High | **Art. 22A solely-automated decision-making not engaged** on the MoJ's own account. | Confirm this holds for the daily PNC share specifically. |
| C31 | The **Essex / North Essex Probation PNC pilot** sends PNC numbers to police **daily**; the ATR does **not** state whether a human checks before each share or what police do with the data. | CONFIRMED (daily share) / UNKNOWN (human-check, onward use) | S51 | Splink Master Record ATR. | High (share) | Operational police data flow about supervised individuals. | **FOI**: pre-share human review? onward police use? error handling? |
| C32 | The operational probation↔police linkage likely relies on **DPA 2018 Part 3** (law-enforcement processing), with HMPPS a "competent authority" and MoJ as controller. | LIKELY | S52, S53 | HMPPS/NPS privacy notices (liveness to checker-verify; full text unread). | Medium-High | Part 3 (not UK GDPR) governs; different rights regime. | Confirm verbatim + for the specific use case (FOI). |

| C33 | The DWP's own fairness analysis (Feb 2024) found **statistically significant bias** in its ML tool that flags Universal Credit claimants for fraud — disparity by **age, disability, marital status, nationality** (race/sex not analysed). Human caseworkers review (not solely-automated). | CONFIRMED | S54 | Computer Weekly, read 2026-06-11; 11-page assessment released under FOI to the Public Law Project. | High | Equality Act / Art. 5(1)(a) fairness; algorithmic bias in a benefits context. | Obtain the assessment + the un-analysed characteristics (race/sex) via FOI. |
| C34 | The MoJ is developing a **"Homicide Prediction Project"** to predict who will commit murder, using **PNC + Greater Manchester Police data (100k–500k people)**, MoJ datasets, and **health markers** (mental health, addiction, self-harm, disability); it covers suspects, **victims, witnesses and safeguarding cases**. | CONFIRMED | S55 | Statewatch, read 2026-06-11; obtained the DPIA + GMP data-sharing agreement via FOI. | High | Profiling (Art. 22A-adjacent); special-category health data; proportionality; inclusion of non-suspects. | Obtain the DPIA + data-sharing agreement; confirm current status/scope. |
| C35 | MoJ predictive risk tools (OASys family) have **higher predictive validity for white offenders** than for Black/Asian/Mixed-ethnicity offenders. | LIKELY | S55 (MoJ study to pin) | Cited in Statewatch + secondary reporting; MoJ's own validity study is the primary to cite. | Medium-High | Algorithmic racial bias in justice risk assessment. | Cite the MoJ OASys predictive-validity study directly. |
| C36 | The UK Algorithmic Transparency Recording Standard registry holds **~125 published records** (Apr 2026), mandatory for departments; policing largely exempt (only 2 police records). | CONFIRMED | S56 | gov.uk ATRS registry, read 2026-06-11. | High | Transparency baseline; the policing exemption is itself notable. | Mine the registry for further linkage/profiling tools. |

**Counts (current):** CONFIRMED = 29 · LIKELY = 4 · UNKNOWN = 3 · SPECULATION = 0.
(Phase 0 seed: CONFIRMED 10 / UNKNOWN 4. C15–C22 = DUAA teardown; C23–C26 = BOLD sweep; C27–C32 = Splink Master Record operational uses; C33–C36 = algorithmic decision/prediction systems — DWP bias, MoJ homicide prediction, OASys racial bias, ATRS registry.)

> **C33–C34 are the most concrete findings in this repo.** Unlike the transparency gaps elsewhere, here
> the harm is **documented**: a government body's own analysis admits bias (DWP), and FOI'd primary
> documents describe a homicide-prediction system built on linked police+health data (MoJ). Still lawful;
> the case is bias, proportionality, and prediction-without-consent. See `algorithmic_decision_systems.md`.

> **C27 is the most consequential refinement in this repo.** The earlier headline ("Data First is
> research-only", C13) remains true *for Data First* — but the Splink Master Record ATR shows Splink is
> also deployed operationally on individuals (real-time identity, court record retrieval, a police/PNC
> pilot). That is a sourced, material qualification of the "purely research" reassurance, and it is the
> nearest thing in this project to the operational-use concern — though it is **lawful, published
> government activity**, not evidence of wrongdoing.

> The DUAA teardown is written up in `duaa_adm_teardown.md`. Its one forward-looking concern (the
> Art. 22D / Annex-1 executive powers as a future re-scoping lever) is recorded there as a **labelled
> SPECULATION / watch-item**, deliberately kept out of this matrix as a fact.

> Note on C13: the Algorithmic Transparency Record is an official MoJ self-disclosure. It is strong
> primary evidence of *stated* purpose; "Medium-High" reflects that it is the controller's own
> description, not an independent audit. It is recorded as CONFIRMED for *what the programme states*,
> with the residual operational-reuse question routed to FOI.


<div style="page-break-before: always;"></div>

## A3. Algorithmic decision & prediction systems (DWP bias; MoJ homicide prediction; OASys)

# Algorithmic decision & prediction systems (the on-thesis core)

_Where non-consensual linked data stops being "just matching" and becomes **profiling and prediction**
about individuals — and where documented **bias** appears. Evidence-graded; non-accusatory. These are,
on the public record, lawful — the issue is bias, transparency, and the use of linked data to predict
people's behaviour. CONFIRMED items were read from the cited source._

## C33 — DWP fraud-detection AI: admitted bias (CONFIRMED — S54)
The DWP's **own fairness analysis (Feb 2024)** found a **statistically significant** disparity in how its
machine-learning tool flags **Universal Credit** claimants for fraud investigation — across **age,
disability, marital status and nationality** (race, sex, sexual orientation and religion were **not**
analysed). DWP says caseworkers review (so **not solely-automated**). The 11-page assessment was released
under FOI to the **Public Law Project**. Campaigners call it "hurt first, fix later."
- *Why it matters:* a public body's own analysis admits its anti-fraud AI treats protected groups
  differently — applied to vulnerable claimants, non-consensually. This is documented bias, not a gap.

## C34 — MoJ "Homicide Prediction Project" (CONFIRMED — S55)
The MoJ is/was developing a system to **predict who will commit murder**, using **Police National
Computer + Greater Manchester Police data (100,000–500,000 people)**, MoJ datasets, and **"health
markers"** (mental health, addiction, self-harm, suicide, disability) stated to have *"significant
predictive power."* It covers not only suspects but **victims, witnesses, missing people, and
safeguarding cases**. Bodies named: MoJ, GMP, Met, West Midlands (in discussion), Home Office.
Revealed by **Statewatch via FOI** (DPIA, internal risk assessment, GMP data-sharing agreement obtained).
- *Why it matters:* this is the apex of the thesis — **linked police + health + justice data used to
  profile individuals for future criminality**, sweeping in people who are not even suspects. Lawful,
  FOI-documented, and exactly the "profiling" harm the consent/transparency questions point at.

## C35 — Racial bias in MoJ risk tools (LIKELY — S55, MoJ studies to pin)
MoJ's own research indicates predictive tools (OASys family) have **higher predictive validity for white
offenders than for Black, Asian and Mixed-ethnicity offenders** — i.e. they "work less well for Black
offenders." OASys/OGRS have profiled offenders since ~2001. Critics (Big Brother Watch, RUSI) warn the
inputs reflect "institutionally racist" policing data.
- *Follow-up:* cite the specific MoJ OASys predictive-validity study directly.

## C36 — The disclosed-algorithm catalogue (CONFIRMED — S56)
The UK **Algorithmic Transparency Recording Standard** registry holds **~125 published records** (Apr
2026), now mandatory for government departments. Policing is exempt, but two police records exist
(Hampshire & Thames Valley **DARAT**; West Midlands sexual-convictions analysis). This is the catalogue
to mine for further linkage/profiling tools — and the absence of most policing tools is itself notable.

## How this reframes the whole investigation
The original spine was *non-consensual probabilistic matching feeding police*. These findings sharpen it:
the same non-consensual linked data is used to **profile and predict** — benefit fraud (DWP, admitted
bias), reoffending (OASys, racial bias), and **homicide (the MoJ prediction project)**. That is the
strongest, most concrete public-interest case in this repo, because here the harm is **documented**
(bias analyses, FOI'd DPIAs), not merely a transparency gap. It remains **lawful**; the argument is
**bias, proportionality, and prediction-without-consent** — an ethics/accountability case, well-sourced.


<div style="page-break-before: always;"></div>

## A4. Datasets (DS-01–DS-05)

# Datasets

Per-dataset tracking of probabilistic-linkage programmes.

**Domain legend:** FAM (family courts) · CIV (civil courts) · CRIM (criminal courts) ·
PRIS (prisons) · PROB (probation) · NHS (health) · MH (mental health) · IMM (immigration) ·
EDU (education) · DWP (work & pensions) · LA (local authority).

**Use mode:** RESEARCH (analysis only, de-identified) vs DECISION (affects an individual's
treatment/entitlement). **Rights tracked:** access (Art. 15), correct (Art. 16), restrict
(Art. 18), object (Art. 21), opt-out (sectoral, e.g. National Data Opt-Out).
Each field: value + `[status]` + source.

---

## DS-01 — MoJ Data First, cross-justice linkage
- **Controller / operator:** Ministry of Justice (linkage via Splink). `[CONFIRMED S01,S03]`
- **Domains covered:** CRIM, CIV, FAM, PRIS, PROB. `[CONFIRMED S06,S07]`
- **What is linked:** person-link *lookup table* across justice datasets; OASys assessment
  data (1,100+ vars, incl. DV / sexual-offending). `[CONFIRMED S06,S07,S08]`
- **Special-category / criminal-offence content:** OASys → likely Art. 9 (health/sex life)
  and Art. 10 (offences). `[LIKELY — to verify against field list, S06]`
- **Use mode:** RESEARCH — de-identified, accredited researchers via ONS SRS / SAIL. `[CONFIRMED S06,S11]`
- **Onward sharing:** MoJ↔DfE (EDU) share via ONS SRS. `[CONFIRMED S06]`
- **Individual rights (access/correct/restrict/object/opt-out):** `[UNKNOWN — C12]`
- **DPIA:** a DPIA was **completed** per the Algorithmic Transparency Record. `[CONFIRMED S19 — C11]`;
  whether it is **published** is `[UNKNOWN — C11b]`.
- **False-positive/negative handling & remedy:** Splink can measure error (S26) and ATRS notes
  manual sample review + bias work (S19), but no programme-specific published rates/remedy. `[UNKNOWN — C14]`
- **Decision-vs-research:** ATRS states **research/statistics only — "not for operational
  decision-making"**. `[CONFIRMED S19 — C13]`
- **Source refs:** S06, S07, S08, S11, S18, S19, S20, S21, S22, S23, S24. (S05 retired; S09/S10/S12 superseded.)

## DS-02 — NHS England Data Linkage Hub
- **Controller / operator:** NHS England (Data Science). `[CONFIRMED S13]`
- **Domains covered:** NHS (+ potentially MH, LA — to confirm). `[CONFIRMED NHS S13; others UNKNOWN]`
- **What is linked:** probabilistic linkage service across NHS datasets (Splink-based). `[CONFIRMED S13]`
- **Special-category content:** health data → Art. 9 throughout. `[LIKELY S13]`
- **Use mode:** `[UNKNOWN — production vs pilot — C08]`
- **Individual rights / National Data Opt-Out applicability:** NDOO applies to s.251 research linkage
  but not where another basis applies (S28); applicability to the Hub specifically `[UNKNOWN — C12]`.
- **DPIA / transparency notice published:** Hub-specific `[UNKNOWN — C11b]`; note a **published**
  NHS England DPIA exists for the adjacent **Federated Data Platform** (S40) — relationship to confirm.
- **False-positive/negative handling & remedy:** `[UNKNOWN — C14]`
- **Source refs:** S13, S41 (IJPDS pipeline), S40 (FDP DPIA, adjacent), S28 (NDOO).

## DS-03 — ONS Census 2021 → Personal Demographics Service (PDS) linkage
- **Controller / operator:** Office for National Statistics. `[CONFIRMED S14]`
- **Domains covered:** Census (whole-population) → NHS (identifier). `[CONFIRMED S14]`
- **What is linked:** Census 2021 records to PDS to assign NHS numbers; feeds the
  Public Health Data Asset (PHDA). `[CONFIRMED S14]`
- **Special-category content:** assigns a health identifier; census includes Art. 9 fields. `[LIKELY S14]`
- **Use mode:** RESEARCH / statistics (PHDA). `[LIKELY S14 — confirm downstream]`
- **Legal gateway:** Statistics and Registration Service Act 2007 (ss. 43–44); DEA 2017 for SRS
  access; ONS Art. 9 condition for statistics. `[LIKELY S14, S38 — confirm exact sections — C17]`
- **Individual rights / opt-out:** census-statistics use is an explicit exclusion from the NHS
  NDOO (S28 context); ONS-specific opt-out `[UNKNOWN — C12]`.
- **DPIA published:** `[UNKNOWN — C11b]`
- **Source refs:** S14, S38.

## DS-05 — MoJ BOLD (Better Outcomes through Linked Data)
- **Controller / operator:** Ministry of Justice (BOLD Partnership). `[CONFIRMED S22]`
- **Domains covered:** CRIM, PRIS, PROB, NHS, MH, LA, drug treatment (NDTMS), HMRC Child Benefit;
  departments incl. MoJ, MHCLG, DHSC, Welsh Government, YJB, NHS England, HMPPS, local authorities. `[CONFIRMED S22]`
- **What is linked:** police, CPS, courts, prisons, probation, health & social care, HMRC Child
  Benefit, NDTMS drug-treatment records. `[CONFIRMED S22]`
- **Special-category content:** health/social care under **Art. 9(2)(h)**, Caldicott Principles +
  Caldicott Guardian sign-off + NHS IGARD approval. `[CONFIRMED S22]`
- **Lawful basis:** Art. 6(1)(e) "common law powers for the administration of justice"; consent /
  public-interest / legal-power bases also cited. `[CONFIRMED S22]`
- **Use mode:** RESEARCH / public-good linkage. `[LIKELY S22 — confirm no operational use]`
- **Individual rights / opt-out:** no explicit opt-out; access rights via formal request only. `[CONFIRMED S22]`
- **DPIA published:** `[UNKNOWN — FOI]`
- **Source refs:** S22. **Note:** broader/more sensitive than Data First (adds health, drug-treatment,
  child-benefit, police/CPS) — a primary disclosure target in its own right.

## DS-04 — MoD Veterans' Card (decision-affecting CONTRAST CASE)
- **Why here:** included as an explicit *contrast* — a known decision/entitlement-affecting
  identity-verification context — to keep the research-vs-decision distinction sharp.
  **Not yet sourced in this repo.** `[UNKNOWN — needs primary source before any claim]`
- **Domains:** IMM/identity, veterans' services. `[UNKNOWN]`
- **Use mode:** DECISION (entitlement/eligibility). `[SPECULATION until sourced]`
- **Source refs:** none yet — Phase 2 search target.

---

> Nothing in DS-04 may be stated as fact until a working primary source is recorded in
> `raw_links.json`. It exists now only to anchor the decision-vs-research axis.


<div style="page-break-before: always;"></div>

## A5. DUAA 2025 / automated-decision teardown

# Teardown: DUAA 2025 and the automated-decision regime (UK GDPR Art. 22 → 22A–22D)

_Forensic read of the primary statutory text on legislation.gov.uk, fetched 2026-06-10.
Evidence-first and non-accusatory: this pulls apart **what the law does**, separating
verified text from inference and from labelled hypothesis. It is a teardown of the **law**,
not of any specific programme — see §6 for the (limited) bearing on the linkage targets._

Sources: S42 (Act), S43 (Art 22A), S44 (Art 22B), S45 (Art 22C), S46 (Art 22D),
S47 (Art 6/6(1)(ea)), S48 (Art 22 substitution note), S35 (ICO summary).

## 1. The structural move (CONFIRMED — S48, S42)
The old **Art. 22** ("Automated individual decision-making, including profiling") was not edited
— it was **substituted wholesale** by a new **Chapter 3, Section 4A** = Arts. 22A–22D. In force
19 Jun 2025 (specified purposes) / **5 Feb 2026** (broadly). Consequential changes to Arts. 4, 13,
14, 15 are flagged as still rolling through. So this is a replacement of the architecture, not a tweak.

## 2. The default inversion — the core of it (CONFIRMED — S44, S48)
- **Before:** Art. 22(1) gave a *right not to be subject* to a solely-automated significant
  decision — **prohibition by default**, with narrow exceptions (contract / authorised by law /
  explicit consent).
- **After (ordinary personal data):** Art. 22B does **not** restate that general right. A solely-
  automated significant decision is now **permitted**, and only *restricted* where the processing
  relies on the new **Art. 6(1)(ea)** basis — subject to the Art. 22C safeguards.
- **After (special-category data):** Art. 22B **keeps a near-prohibition** — banned unless explicit
  consent, or contract/legal necessity with an Art. 9(2)(g) substantial-public-interest condition.

**Net:** for *ordinary* data the baseline flips from *"forbidden unless"* to *"allowed unless."*
For *special-category* data the strong bar survives. This is the single most consequential change.

## 3. The new lawful basis that 22B hinges on (CONFIRMED — S47, S49)
Art. **6(1)(ea)** — *"processing is necessary for the purposes of a recognised legitimate
interest."* Per Art. 6(5), it applies only if it meets a condition in **Annex 1**, and the
**Secretary of State may amend Annex 1 by regulations.** So both the trigger for the ordinary-data
ADM restriction (reliance on 6(1)(ea)) **and** the content of that basis are partly executive-set.

**Annex 1 categories (CONFIRMED — S49):** disclosure for an Art. 6(1)(e) public-task purpose;
**national security / public security / defence**; **emergencies** (Civil Contingencies Act 2004);
**crime** ("detecting, investigating or preventing crime", apprehending/prosecuting offenders);
and **safeguarding vulnerable individuals**. Several are justice/crime-shaped — relevant context
for a justice-data ecosystem, though a *lawful basis* is not by itself a power to do anything new.

## 3a. Transparency duty also moved — Art. 14 (LIKELY — S50)
The duty to inform people whose data was obtained **indirectly** (Art. 14 — i.e. essentially everyone
inside a linkage) was **amended by DUAA 2025**. The Art. 14(5) exemptions were reworked (impossible /
disproportionate effort; "likely to render impossible or seriously impair the achievement of the
objectives") with a new "make the information available publicly" measure. The exact fate of the
research/indirect-collection exemption needs **verbatim** confirmation. This is the provision that
governs whether linked individuals must be told at all — directly material to the transparency gap.

## 4. The safeguards that remain (CONFIRMED — S45)
Where a solely-automated significant decision **is** permitted, Art. 22C requires the controller to:
(a) **inform** the data subject; (b) enable them to make **representations**; (c) enable **human
intervention**; (d) enable them to **contest** the decision. These are the familiar Art. 22(3)-style
protections, **carried over**.

## 5. The delegated power — the civil-liberties pressure point (CONFIRMED — S46)
Art. **22D** lets the **Secretary of State by regulations**:
- provide whether there **is or is not "meaningful human involvement"** in a given decision type;
- determine whether a decision has a **"similarly significant effect"**;
- **add to / modify how the 22C safeguards operate**, including defining measures that do **not**
  satisfy them.
Checks: **affirmative resolution** (Parliament must approve), and 22D(4) bars the SoS from directly
amending 22C itself. But the *boundaries* of the whole regime — what counts as "human involvement"
and "significant" — are now **set by ministerial regulation**, not on the face of the Act.

## 6. Bearing on the linkage investigation — honest verdict
- **No new authorisation for the linkage programmes.** Data First is research-only per its
  Algorithmic Transparency Record (S19); it does not take automated decisions about individuals,
  so 22A–22D barely engages it. (CONFIRMED negative finding — S19, S44.)
- **The sensitive material is still protected.** If any programme *did* use special-category data
  (e.g. OASys) for a solely-automated significant decision, Art. 22B **prohibits** it. The reform
  did **not** open that door. (CONFIRMED — S44.)
- **What is a legitimate watch-item (LABELLED HYPOTHESIS — SPECULATION):** the Art. 22D regulation
  power and the SoS-amendable Annex 1 (6(1)(ea)) are *general* levers that could, in future, be used
  to re-scope ADM protections across government — including contexts that touch linked data. There
  is **no evidence** any such regulation targets these programmes; recording this only as a thing to
  monitor, explicitly **not** as a claim of intent. Follow-up: track DUAA commencement/Annex 1 SIs.

## 7. What I have NOT verified (limits)
- The exact wording of the 22B special-category exceptions and the full Annex 1 conditions (read
  summarily, not clause-by-clause) — confirm verbatim before any load-bearing legal use.
- The precise list of consequential amendments to Arts. 13–15 (transparency duties) under DUAA —
  potentially relevant to the Art. 14 "right to be informed" questions in `legal_questions.md`.


<div style="page-break-before: always;"></div>

## A6. Legal questions

# Legal questions (neutral)

Open, non-accusatory questions framed against UK GDPR and the Data Protection Act 2018.
These are *questions to answer with sources*, not allegations. Statutory references must be
checked against current text on legislation.gov.uk before any answer is recorded as CONFIRMED.

> **DUAA 2025 baseline (verified, S37/S42/S43):** in force 5 Feb 2026 — UK GDPR **Art. 22 →
> Arts. 22A–22D** (automated significant decisions), research safeguard **Art. 89(1) → Art. 84B**.
> Questions below are framed in the post-DUAA numbering.

## A. Lawful basis — Article 6
- A1. Which Art. 6(1) basis does each programme rely on for linkage (likely (e) public task)? `[UNKNOWN]`
- A2. Where is that basis published (privacy notice / DPIA)? `[UNKNOWN → C11]`

## B. Special-category & criminal-offence data — Articles 9 & 10
- B1. For OASys-derived fields, which Art. 9(2) condition applies (e.g. (j) research/statistics)? `[UNKNOWN]`
- B2. Which DPA 2018 Sch. 1 condition (and appropriate-policy-document) supports it? `[UNKNOWN]`
- B3. For criminal-offence data (Art. 10), what is the official authority / Sch. 1 basis? `[UNKNOWN]`
- B4. For NHS / Census→PDS health data, which Art. 9 condition is relied on? `[UNKNOWN]`
- B5. Where a research/statistics Art. 9 condition (DPA 2018 Sch. 1 Pt 1 para 4) is used, the safeguard
  is now **Art. 84B** (not Art. 89(1)); para 4 itself needs no appropriate policy document. `[CONFIRMED S37 → C16]`
- Reference: special-category processing needs **both** Art. 6 and Art. 9 (+ Sch. 1). `[CONFIRMED S15,S16,S37 → C10]`

## C. Fairness & transparency — Articles 5(1)(a), 13, 14
- C1. Is there an Art. 14 transparency notice for data obtained indirectly (i.e. not from the
  data subject), and is a research exemption (DPA 2018 s.14 / Art. 14(5)(b)) relied on? `[UNKNOWN]`
- C2. How are data subjects informed their justice/health records are linked? `[UNKNOWN]`

## D. Purpose limitation — Article 5(1)(b)
- D1. Is linkage use confined to the stated research purpose, or re-used for other purposes?
  Data First's ATRS states research/statistics only, "not for operational decision-making"
  `[CONFIRMED for stated purpose, S19 → C13]`; absence of operational *re-use* `[UNKNOWN — FOI]`.

## E. Data minimisation & accuracy — Articles 5(1)(c) & 5(1)(d)
- E1. Are only the fields needed for linkage processed (vs full OASys 1,100+ vars)? `[UNKNOWN]`
- E2. What are the published match-error rates, and how is accuracy assured? `[UNKNOWN → C14]`

## F. Individual rights — Articles 15–22 (incl. opt-out & Art. 22)
- F1. How can an individual exercise access / rectification / restriction / objection over linked data? `[UNKNOWN → C12]`
- F2. Does an opt-out exist (programme-specific or National Data Opt-Out for NHS)? `[UNKNOWN → C12]`
- F3. Do linkage outputs feed any solely-automated significant decision (now **Art. 22A**)? Data First's
  ATRS says outputs are research-only and "not integrated into a decision-making process" `[CONFIRMED S19
  → C13]`, so Art. 22A is unlikely engaged for Data First; verify for NHS Hub / any operational re-use. `[UNKNOWN]`

## G. Accountability — Articles 5(2), 35, 30
- G1. Has a DPIA been completed and (partly) published for each programme (Art. 35)? Data First DPIA
  **completed** per ATRS `[CONFIRMED S19 → C11]`; **publication** `[UNKNOWN → C11b]`. NHS England
  publishes an FDP DPIA `[CONFIRMED S40]` (relationship to the Hub to confirm).
- G2. Is the processing in the controller's Art. 30 Record of Processing Activities? `[UNKNOWN]`

## H. Oversight & litigation
- H1. Any First-tier Tribunal (Information Rights) decisions on Data First FOI requests? `[UNKNOWN — Phase 2 search #18]`
- H2. Any judicial review touching govt administrative-data linkage under UK GDPR? `[UNKNOWN — search #19]`
- H3. Has NSDEC (National Statistician's Data Ethics Advisory Committee) reviewed these? `[UNKNOWN — search #20]`
- H4. What is the Caldicott Guardian / National Data Guardian role for the NHS linkage? `[UNKNOWN]`


<div style="page-break-before: always;"></div>

## A7. Timeline

# Timeline

Dated events relevant to UK public-sector probabilistic linkage. Only dated, sourced events
belong here. Undated items stay in `open_questions.md` until a date is sourced.

| Date | Event | Status | Source | Follow-up |
|------|-------|--------|--------|-----------|
| 2022 | Splink described in peer-reviewed paper (IJPDS v7n3) as MoJ's open-source probabilistic linkage library. | CONFIRMED | S03 | Confirm exact publication month in Phase 2. |
| 2022 | MoJ publishes "Data First: Criminal Courts linked data" documentation. | CONFIRMED (pre-flag STALE?) | S12 | Re-verify URL liveness (legacy gov.uk asset). |
| 2023 | ONS publishes Census 2021 → PDS linkage methodology report. | CONFIRMED | S14 | Confirm exact date; trace PHDA downstream use. |
| 2023–2024 | ADR UK Annual Report documents MoJ Data First Cross-Justice System dataset (E&W). | CONFIRMED | S06 | — |
| 2024 | ONS SRS metadata catalogues Data First dataset 58617. | CONFIRMED | S07 | Confirm catalogue entry date. |
| 2025-08 | gov.uk guidance "Access HMCTS data for research" current/updated. | CONFIRMED | S11 | Confirm "last updated" date string. |
| 2025-10 | MoJ–DfE data-share privacy notice document created. | CONFIRMED | S23 | Read PDF for datasets + legal gateway. |
| 2024-12-17 | MoJ publishes Algorithmic Transparency Record for Data First (Splink) v3.0; states research-only + DPIA completed. | CONFIRMED | S19 | — |
| 2025-06-19 | DUAA 2025 Arts. 22A–22D commence "for specified purposes". | CONFIRMED | S43 | — |
| 2026-02-05 | DUAA 2025 fully in force: UK GDPR Art. 22 → Arts. 22A–22D; Art. 89(1) → Art. 84B. | CONFIRMED | S37, S42, S43 | Rebase all statutory cites. |
| 2026-02-05 | DUAA 2025: Art. 6(1)(ea) + Annex 1 (recognised legitimate interests) in force. | CONFIRMED | S47, S49 | Read Annex 1 verbatim. |
| 2026-02-05 | DUAA 2025 amendments to Art. 14 (indirect-collection transparency) in force. | LIKELY | S50 | Verify verbatim. |
| 2026-03-23 | ICO updates purpose-limitation guidance to reflect DUAA 2025. | LIKELY | S35 | Confirm exact date on page. |
| UNKNOWN | Data First DPIA *published* (completion confirmed; publication not). | UNKNOWN | — | FOI (C11b). |
| UNKNOWN | NHS England Data Linkage Hub production go-live (vs pilot). | UNKNOWN | — | FOI (C08). |

> Several seed sources are undated on-page (Splink repo/docs, ADR UK project page, ICO guidance).
> They are recorded without a timeline date and flagged UNCLEAR for currency.


<div style="page-break-before: always;"></div>

## A8. Open questions

# Open questions (prioritised)

Updated end of Phase 3. Each question is tagged with how it can now be answered:
**[FOI-ONLY]** (no public source exists — needs a statutory request) ·
**[DOC-READ]** (answer likely sits in a source we already hold — read it, no FOI needed) ·
**[VERIFY]** (confirm/upgrade an existing LIKELY claim against primary text).

Priority: **P1** = core to the four project questions; **P2** = important context; **P3** = secondary.

## P1 — the three live UNKNOWNs (the real FOI core)
- **P1-a [FOI-ONLY] — Publish the DPIA.** The Data First Algorithmic Transparency Record (S19,
  17 Dec 2024) states a DPIA **was completed**. The DPIA document itself is not in the public
  record. (C11b) → **FOI-1 §1** to MoJ: release the completed DPIA (redacted if necessary).
- **P1-b [FOI-ONLY] — Individual opt-out / objection.** No documented route for an individual to
  opt out of, or object to, inclusion of their records in Data First linkage. The NHS National Data
  Opt-Out (S28) covers s.251 research linkage, not MoJ research bases or ONS statutory linkage. (C12)
  → **FOI-1 §4** (MoJ) and a scope question to NHS England (NDOO ↔ Data Linkage Hub).
- **P1-c [FOI-ONLY] — Published match-error rates + a remedy.** Splink *can* measure false-positive/
  negative rates (S26) and the ATRS notes manual sample review and bias work (S19), but no
  programme-specific published rates and no described remedy for an individual who is mis-linked. (C14)
  → **FOI-1 §6** (MoJ) and equivalents to NHS England / ONS.

## P1 — now answerable WITHOUT FOI (close these first)
- **P1-d [DOC-READ] — Data First lawful basis (Art. 6) and Art. 9/10 + Sch. 1 conditions.** Almost
  certainly stated in the privacy statement (S20) — but S20 is a binary/image PDF not yet text-read.
  → Read S20 (and BOLD notice S22) before escalating to FOI.
- **P1-e [DOC-READ] — MoJ↔DfE share specifics.** Datasets, purpose and legal gateway are likely in
  the MoJ–DfE privacy notice (S23, created 2025-10) — also a binary PDF needing manual read. (C07)

## P2 — important context
- **P2-a [DOC-READ] — OASys field inventory:** which fields are Art. 9 / Art. 10. Likely in S20 / the
  user guide S21 / dataset metadata S07. (C05)
- **P2-b [FOI-ONLY] — NHS Data Linkage Hub production status** (pilot vs live), datasets, controller,
  and its relationship to the Federated Data Platform DPIA (S40). (C08)
- **P2-c [VERIFY] — ONS Census→PDS legal gateway:** confirm SRSA 2007 ss. 43–44 (and DEA 2017 for SRS)
  verbatim in S14 / PDS source pages. (C17)
- **P2-d [FOI-ONLY] — PHDA downstream:** uses and retention of the linked Public Health Data Asset. (C09)
- **P2-e [VERIFY] — Five Safes / accreditation** controls for ONS SRS (S30/S31) and SAIL (S33).

## P1/P2 — added in the completion sweep
- **[FOI-ONLY] — BOLD DPIA + opt-out + status.** The broader MoJ BOLD programme (health, drug-
  treatment, child-benefit, police/CPS) has no published DPIA or opt-out located. (C25/C26) → FOI-5.
- **[VERIFY] — Art. 14 transparency amendment.** Confirm verbatim how DUAA 2025 reworked Art. 14(5)
  and what remains of the indirect-collection/research exemption (governs whether linked individuals
  must be told). (C24)
- **[VERIFY] — Annex 1 conditions.** Read each Art. 6(1)(ea) "recognised legitimate interest"
  condition verbatim (esp. the crime and safeguarding limbs). (C23)

## P3 — secondary
- **P3-a [VERIFY] — FTT (Information Rights):** confirm absence of any Data First decision via the
  tribunal database directly (Phase 1 found none). (H1)
- **P3-b [VERIFY] — Judicial review:** no JR on these linkages; adjacent precedent exists
  (immigration-exemption challenge; *Delo v IC*). Context only. (H2)
- **P3-c [DOC-READ] — NSDEC** minutes (S39) for any review of justice/health linkage. (H3)
- **P3-d [FOI-ONLY] — DS-04 contrast case:** still needs a sourced decision-affecting example before
  any claim; do not assert.
- **P3-e [VERIFY] — Splink licence + maintained version.** (C01)

---
### Summary: what is now FOI-ONLY vs closeable by reading
- **FOI-ONLY (5):** P1-a (publish DPIA), P1-b (opt-out), P1-c (error rates+remedy), P2-b (NHS Hub
  status), P2-d (PHDA downstream).
- **Closeable by DOC-READ / VERIFY (8):** P1-d, P1-e, P2-a, P2-c, P2-e, P3-a, P3-c, P3-e.

The four-question project framing now reduces to one sentence: *the **what / by whom / legal basis /
safeguards** are largely sourced; the residual gaps are **publication of the DPIA, an individual
opt-out, and published mis-linkage error rates + remedy** — all transparency/recourse questions.*


<div style="page-break-before: always;"></div>

## A9. FOI drafts

# FOI request drafts

Non-accusatory, specific information requests under the Freedom of Information Act 2000
(documents framed as transparency requests for personal-data handling). Tone: neutral
public-interest — each asks for documents/facts, not justifications, and is narrowed
(post-Phase 3) to the genuine gaps so it survives the s.12 cost limit.

> Before sending: confirm the current FOI contact from each body's official page. For MoJ,
> the Data First team address `datafirst@justice.gov.uk` is published (S18) but FOI should go
> via the MoJ FOI route. Cite the specific documents we already have so the request is precise.

---

## FOI-1 — Ministry of Justice (Data First)
**Subject:** Data First linked-data programme — DPIA, opt-out, and linkage accuracy

Context I can already cite: the Algorithmic Transparency Record for "MoJ: Data First (Splink)"
(published 17 December 2024) states that a Data Protection Impact Assessment **was completed** and
that the datasets are for research/statistics and "not for operational decision-making".

1. **Please release the completed DPIA** referenced in that Algorithmic Transparency Record, in
   full or with necessary redactions. (C11b)
2. Please confirm **how an individual can opt out of, or object to, inclusion** of their records in
   Data First linkage, and provide any policy describing that process; if there is no opt-out,
   please confirm that and the basis on which Article 21 objections are handled. (C12)
3. Please provide any **evaluation of linkage accuracy** — published or internal — including
   false-match and missed-match rates for the Data First linkage, and describe the **process for
   correcting an erroneous link** that affects an individual. (C14)
4. Please confirm whether Data First linkage outputs are ever **re-used for any purpose other than
   accredited research/statistics**, including any operational use. (purpose limitation; complements C13)
5. For OASys-derived data, please state the **Article 9 condition and Article 10 / DPA 2018
   Schedule 1 basis**, and provide the appropriate policy document if one applies. (C05, B-block)

> Already sourced (do NOT ask): that Splink is MoJ open-source (S01/S03); the cross-justice scope
> (S06/S07); de-identified SRS/SAIL access (S06/S11/S30/S31/S33); research-only use (S19).

## FOI-2 — NHS England (Data Linkage Hub)
**Subject:** Data Linkage Hub — status, governance, and opt-out scope

1. The current **production status** of the Data Linkage Hub (pilot vs operational), the datasets in
   scope, and the data controller(s). (C08, P2-b)
2. Any **DPIA / transparency notice for the Data Linkage Hub specifically**, and its relationship to
   the published Federated Data Platform DPIA (we already hold the FDP DPIA, S40). (C11b)
3. The **Article 6 basis and Article 9 condition** for the Hub's linkage, and the Caldicott Guardian /
   National Data Guardian role in its governance. (B4, H4)
4. Whether and how the **National Data Opt-Out applies** to processing by the Hub. (C12)
5. Any published **linkage-accuracy metrics** and the **mis-linkage correction process**. (C14)

## FOI-3 — Office for National Statistics
**Subject:** Census 2021 → PDS linkage and the Public Health Data Asset

1. Any **DPIA** for the Census 2021 → PDS linkage and the Public Health Data Asset (PHDA). (C11b)
2. Confirmation of the **legal gateway** (we believe Statistics and Registration Service Act 2007,
   ss. 43–44, with DEA 2017 for SRS access) and the **Article 9 condition** relied on. (C17, B4)
3. Whether and how individuals can **opt out** of this linkage (noting census-statistics use is an
   exclusion from the NHS National Data Opt-Out). (C12)
4. Published **downstream uses and retention period** of the linked PHDA. (C09, P2-d)

## FOI-5 — Ministry of Justice (BOLD)
**Subject:** Better Outcomes through Linked Data (BOLD) — DPIA, scope, opt-out

The BOLD privacy notice (gov.uk) confirms linkage across police, CPS, courts, prisons, probation,
health & social care, HMRC Child Benefit and drug-treatment (NDTMS) data, on an Art. 6(1)(e) +
Art. 9(2)(h) basis, with no stated opt-out.

1. Please release any **DPIA(s)** for BOLD (in full or redacted). (C25)
2. Please confirm BOLD's **current status**, the full list of datasets/departments, and the data
   controller(s). (C25)
3. Please confirm whether an individual can **opt out of or object to** inclusion in BOLD. (C12)
4. Please confirm whether BOLD outputs are **research-only** or inform any decision about an
   individual. (decision-vs-research)
5. Please provide any **linkage-accuracy** evaluation and the **mis-linkage correction** process. (C14)

## FOI-6 — Ministry of Justice (Splink operational use: Core Person Record & PNC pilot)
**Subject:** Operational Splink use — DPIAs, lawful basis, and the probation→police PNC pilot

Context I can cite: the MoJ "Splink Master Record" Algorithmic Transparency Record (published
6 Oct 2025) states DPIAs/DPIA screenings were conducted for each Splink use case; that Splink "does
not directly make decisions about individuals" (human makes the final decision); and that, in a
North Essex pilot, PNC numbers for probation-supervised individuals are sent to police daily.

1. Please **release the DPIA(s)** for (a) the **Core Person Record** and (b) the **North Essex
   Probation → police PNC pilot**, in full or redacted. (C29)
2. Please state the **data controller** and the **lawful basis** for each (UK GDPR and/or DPA 2018
   Part 3 law-enforcement processing), with the Part 3 / Schedule conditions relied on. (C32)
3. For the PNC pilot: is there **human review before each daily share**, what do police do with the
   numbers, and what is the **process to correct a wrongful match** affecting an individual? (C31)
4. Please confirm whether **any solely-automated significant decision** (UK GDPR Art. 22A / DPA Part 3)
   is taken on the basis of a Splink match, and the safeguards. (C30)
5. Please confirm how individuals are **informed** their records are linked across DELIUS/NOMIS/
   Common Platform/LIBRA/FamilyMan/CaseMan (Art. 14 / Part 3 equivalent), and any opt-out/objection. (C12)

> Already sourced — do NOT ask: that Splink is used operationally (Core Person Record, Probation in
> Court, PNC pilot) and that DPIAs were conducted (S51).

## FOI-4 — ADR UK
**Subject:** Governance of the Data First / cross-justice linkage data

1. The **public-benefit and ethics assessment** applied to Data First (beyond the published ethics
   page S32). (P2)
2. Any **DPIA or data-sharing agreement** ADR UK holds for the cross-justice dataset. (C11b)
3. Documentation of the **MoJ↔DfE share** and its legal gateway (complements the MoJ–DfE privacy
   notice S23). (C07)

---

> All four ask for documents and facts, citing what is already public so the scope is tight and the
> tone neutral. The strongest, narrowest single ask is **FOI-1 §1 — release the DPIA that the
> government's own transparency record says exists.** That is the cleanest test of transparency and
> requires no allegation of any kind.


<div style="page-break-before: always;"></div>

## A10. Source table

# Master source table

Flags (re-verified by `scripts/source_checker.py`): **LIVE** · **STALE?** (pre-flagged, re-check) · **UNCLEAR** · **DEAD**.
Type: `splink-core` · `data-first` · `ons-adruk` · `nhs` · `ico-law`.
All "Accessed" = first verification date; re-run the checker to refresh.

| # | Title | Publisher | Pub date | URL | Accessed | Type | Flag |
|---|-------|-----------|----------|-----|----------|------|------|
| S01 | Splink (repository) | MoJ Analytical Services | — | https://github.com/moj-analytical-services/splink | 2026-06-10 | splink-core | LIVE |
| S02 | Splink documentation | MoJ Analytical Services | — | https://moj-analytical-services.github.io/splink/index.html | 2026-06-10 | splink-core | LIVE |
| S03 | Splink: MoJ's open source library for probabilistic record linkage at scale (IJPDS v7n3) | IJPDS | 2022 | https://ijpds.org/article/view/1794 | 2026-06-10 | splink-core | LIVE |
| S04 | MoJ Analytical Services (GitHub org) | Ministry of Justice | — | https://github.com/moj-analytical-services | 2026-06-10 | splink-core | LIVE |
| S05 | Data First overview (ADR UK project page) | ADR UK | — | https://www.adruk.org/our-work/browse-all-projects/data-first-...-169/ | 2026-06-10 | data-first | RETIRED (404 x3; → S18/S32) |
| S06 | MoJ Data First Cross-Justice System (E&W) — Annual Report 2023-24 | ADR UK | 2024 | https://reports.adruk.org/annual-report-2023-2024/our-data/new-and-emerging-datasets/ministry-of-justice-data-first-cross-justice-system-england-and-wales/ | 2026-06-10 | ons-adruk | LIVE |
| S07 | Dataset 58617 metadata | ONS SRS Metadata | 2024 | https://ons.metadata.works/browser/dataset?id=58617 | 2026-06-10 | ons-adruk | LIVE |
| S08 | Dataset 58617 (ADR UK Data Catalogue) | ADR UK | — | https://datacatalogue.adruk.org/browser/dataset/58617/1 | 2026-06-10 | ons-adruk | LIVE |
| S09 | Data First privacy statement | MoJ (gov.uk asset) | — | https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/984511/data-first-privacy-statement.pdf | 2026-06-10 | data-first | STALE? |
| S10 | Data First user guide version 7.0 | MoJ (gov.uk asset) | — | https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1056236/data-first-user-guide-version-7.0.pdf | 2026-06-10 | data-first | STALE? |
| S11 | Access HMCTS data for research | gov.uk | 2025-08 | https://www.gov.uk/guidance/access-hmcts-data-for-research | 2026-06-10 | data-first | LIVE |
| S12 | Data First: Criminal Courts linked data | MoJ (gov.uk asset) | 2022 | https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1058219/data-first-criminal-courts-linked-data.pdf | 2026-06-10 | data-first | STALE? |
| S13 | Data Linkage Hub | NHS England Data Science | — | https://nhsengland.github.io/datascience/our_work/data-linkage-hub/ | 2026-06-10 | nhs | LIVE |
| S14 | Census 2021 to Personal Demographics Service linkage report | ONS | 2023 | https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/healthinequalities/methodologies/census2021topersonaldemographicsservicelinkagereport | 2026-06-10 | ons-adruk | LIVE |
| S15 | Special category data (a guide to lawful basis) | ICO | — | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/special-category-data/ | 2026-06-10 | ico-law | LIVE |
| S16 | What are the rules on special category data? | ICO | — | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/special-category-data/what-are-the-rules-on-special-category-data/ | 2026-06-10 | ico-law | LIVE |
| S17 | A guide to lawful basis | ICO | — | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/a-guide-to-lawful-basis/ | 2026-06-10 | ico-law | LIVE |
| S18 | Ministry of Justice: Data First (landing page) | gov.uk / MoJ | — | https://www.gov.uk/guidance/ministry-of-justice-data-first | 2026-06-10 | data-first | LIVE |
| S19 | MoJ: Data First (Splink) — Algorithmic Transparency Record v3.0 | gov.uk / MoJ | 2024-12-17 | https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink | 2026-06-10 | data-first | LIVE |
| S20 | The Data First Project: Privacy and data protection | MoJ (gov.uk asset) | — | https://assets.publishing.service.gov.uk/media/6099053bd3bf7f2887b642bd/data-first-privacy-statement.pdf | 2026-06-10 | data-first | LIVE (binary PDF — manual read) |
| S21 | Data First Programme: Introductory User Guide v8.2 | MoJ (gov.uk asset) | — | https://assets.publishing.service.gov.uk/media/683863d5c99c4f37ab4e867c/Data_First_User_Guide_Version_8.2.pdf | 2026-06-10 | data-first | LIVE |
| S22 | Better Outcomes through Linked Data (BOLD): Privacy Notice | gov.uk / MoJ | — | https://www.gov.uk/government/publications/ministry-of-justice-better-outcomes-through-linked-data-bold/better-outcomes-through-linked-data-bold-privacy-notice | 2026-06-10 | data-first | LIVE |
| S23 | MoJ-DfE data share: Privacy and Data Protection notice | MoJ / DfE (gov.uk asset) | 2025-10 | https://assets.publishing.service.gov.uk/media/68f2032028f6872f1663efb8/MoJ_DfE_data_privacy_notice__002_.pdf | 2026-06-10 | data-first | LIVE (binary PDF — manual read) |
| S24 | Data First: Criminal Courts Linked Data (landing page) | gov.uk / MoJ | — | https://www.gov.uk/government/publications/data-first-criminal-courts-linked-data | 2026-06-10 | data-first | LIVE |
| S25 | Splink: Fast, accurate and scalable record linkage (blog) | gov.uk / Data in government | 2022-09-23 | https://dataingovernment.blog.gov.uk/2022/09/23/splink-fast-accurate-and-scalable-record-linkage/ | 2026-06-10 | splink-core | LIVE |
| S26 | Splink tutorial: 7. Evaluation (accuracy / error rates) | MoJ Analytical Services | — | https://moj-analytical-services.github.io/splink/demos/tutorials/07_Evaluation.html | 2026-06-10 | splink-core | LIVE |
| S28 | National Data Opt-Out: supplementary info for research orgs (CAG/s.251) | Health Research Authority | — | https://www.hra.nhs.uk/about-us/committees-and-services/confidentiality-advisory-group/national-data-opt-out-supplementary-information-for-research-organisations/ | 2026-06-10 | nhs | LIVE |
| S30 | SRS Research and Data Access Policy | ONS | — | https://www.ons.gov.uk/aboutus/transparencyandgovernance/datastrategy/datapolicies/onsresearchanddataaccesspolicy | 2026-06-10 | ons-adruk | LIVE |
| S31 | About the Secure Research Service (Five Safes; DEA 2017) | ONS | — | https://www.ons.gov.uk/aboutus/whatwedo/statistics/requestingstatistics/secureresearchservice/aboutthesecureresearchservice | 2026-06-10 | ons-adruk | LIVE |
| S32 | Ensuring ADR UK data is used ethically and responsibly | ADR UK | — | https://www.adruk.org/about-us/ethics-responsibility/ | 2026-06-10 | ons-adruk | LIVE |
| S33 | SAIL Databank — Governance | SAIL Databank (Swansea) | — | https://saildatabank.com/governance/ | 2026-06-10 | ons-adruk | LIVE |
| S35 | DUAA 2025: summary of the changes — Data protection | ICO | — | https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/the-data-use-and-access-act-2025-duaa-summary-of-the-changes/data-protection/ | 2026-06-10 | ico-law | LIVE |
| S36 | Right to be informed: are there any exceptions? (Art.14) | ICO | — | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/the-right-to-be-informed/are-there-any-exceptions/ | 2026-06-10 | ico-law | LIVE |
| S37 | Data Protection Act 2018, Schedule 1 (current revised text) | legislation.gov.uk | 2018 | https://www.legislation.gov.uk/ukpga/2018/12/schedule/1 | 2026-06-10 | ico-law | LIVE |
| S38 | Collecting/using special category data for official statistics | ONS | — | https://www.ons.gov.uk/aboutus/transparencyandgovernance/datastrategy/datapolicies/collectingandusingspecialcategorydataforofficialstatisticsandstatisticalresearch | 2026-06-10 | ons-adruk | LIVE |
| S39 | National Statistician's Data Ethics Advisory Committee (NSDEC) | UK Statistics Authority | — | https://uksa.statisticsauthority.gov.uk/the-authority-board/committees/national-statisticians-advisory-committees-and-panels/national-statisticians-data-ethics-advisory-committee/ | 2026-06-10 | ons-adruk | LIVE |
| S40 | Overarching DPIA for the Federated Data Platform (FDP) | NHS England | — | https://www.england.nhs.uk/long-read/overarching-data-protection-impact-assessment-dpia-for-the-federated-data-platform-fdp/ | 2026-06-10 | nhs | LIVE |
| S41 | Probabilistic Linkage Pipeline... in Healthcare (IJPDS) | IJPDS | — | https://ijpds.org/article/view/3271 | 2026-06-10 | nhs | LIVE |
| S42 | Data (Use and Access) Act 2025 (2025 c. 18) | legislation.gov.uk | 2025 | https://www.legislation.gov.uk/ukpga/2025/18/contents | 2026-06-10 | ico-law | LIVE |

> **Phase 0 re-verify findings (2026-06-10):** S05 is **DEAD** (HTTP 404) — replace with the
> current ADR UK Data First URL in Phase 2. S10 **REDIRECTs** to a newer gov.uk asset
> (User Guide v8.2, not v7.0) — update to the canonical media URL in Phase 2. S09 and S12 are
> live but remain `STALE?` (legacy attachment-store PDFs) pending confirmation of currency.
>
> Pub dates shown as "—" are undated on the source page and must be treated as **UNCLEAR** for currency
> (flag for re-check). The three `STALE?` gov.uk assets are legacy attachment-store PDFs whose IDs
> commonly get superseded — Phase 0 re-verifies them before any claim relies on them.
>
> **Phase 2 additions/notes (2026-06-10):** Added S18–S42 (live, checker-verified). Canonical replacements
> for the stale/dead seeds: S20 (privacy statement, current media URL) ⟶ supersedes S09; S21 (User Guide
> v8.2) ⟶ supersedes the S10 v7.0 redirect; S24 (criminal-courts landing page) ⟶ supersedes S12. S05 is
> **RETIRED** (404 on three fetches; see `raw_links.json` `_meta.superseded`). **S20 and S23 are binary/image
> PDFs** — they resolve and download but text could not be auto-extracted, so they must be **read manually**
> before backing any lawful-basis / opt-out / dataset claim. **Three sources were dropped as unverifiable**
> (HTTP 403/404 to every automated client here): two NHS Digital pages (National Data Opt-Out, PDS access)
> and one ICO automated-decisions subpage — see `_meta.unverified_dropped`. Their points are carried by
> accessible sources (HRA S28; ICO DUAA summary S35; legislation S42). **DUAA 2025 (S42)** amends the
> regime: UK GDPR Art.22 → Arts.22A–22D and the research safeguard Art.89(1) → Art.84B, in force 2026-02-05
> (verified in the current DPA 2018 Sch.1 text, S37). Statutory wording is locked in Phase 3.


<div style="page-break-before: always;"></div>

## A11. Source-check report

# Source Check Report

_Generated: 2026-06-11 · max-age-days=90_

| ID | Status | HTTP | Title | Detail |
|----|--------|------|-------|--------|
| S10 | REDIRECT | 200 | Data First user guide version 7.0 | -> https://assets.publishing.service.gov.uk/media/683863d5c99c4f37ab4e867c/Data_First_User_Guide_Version_8.2.pdf; HTTP 200 |
| S55 | REDIRECT | 200 | UK: Ministry of Justice secretly developing 'murder prediction' system | -> https://statewatch.org/news/2025/april/uk-ministry-of-justice-secretly-developing-murder-prediction-system/; HTTP 200 |
| S09 | STALE | 200 | Data First privacy statement | pre-flagged STALE?; HTTP 200 |
| S12 | STALE | 200 | Data First: Criminal Courts linked data | pre-flagged STALE?; HTTP 200 |
| S01 | OK | 200 | Splink (repository) | HTTP 200 |
| S02 | OK | 200 | Splink documentation | HTTP 200 |
| S03 | OK | 200 | Splink: MoJ's open source library for probabilistic record linkage at scale (IJPDS v7n3) | HTTP 200 |
| S04 | OK | 200 | MoJ Analytical Services (GitHub organisation) | HTTP 200 |
| S06 | OK | 200 | MoJ Data First Cross-Justice System (England and Wales) — Annual Report 2023-24 | HTTP 200 |
| S07 | OK | 200 | Dataset 58617 metadata (Data First cross-justice linkage) | HTTP 200 |
| S08 | OK | 200 | Dataset 58617 (ADR UK Data Catalogue) | HTTP 200 |
| S11 | OK | 200 | Access HMCTS data for research | HTTP 200 |
| S13 | OK | 200 | Data Linkage Hub | HTTP 200 |
| S14 | OK | 200 | Census 2021 to Personal Demographics Service linkage report | HTTP 200 |
| S15 | OK | 200 | Special category data (a guide to lawful basis) | HTTP 200 |
| S16 | OK | 200 | What are the rules on special category data? | HTTP 200 |
| S17 | OK | 200 | A guide to lawful basis | HTTP 200 |
| S18 | OK | 200 | Ministry of Justice: Data First (programme landing page) | HTTP 200 |
| S19 | OK | 200 | MoJ: Data First (Splink) — Algorithmic Transparency Recording Standard record (v3.0) | HTTP 200 |
| S20 | OK | 200 | The Data First Project: Privacy and data protection (privacy statement) | HTTP 200 |
| S21 | OK | 200 | The Data First Programme: An Introductory User Guide (v8.2) | HTTP 200 |
| S22 | OK | 200 | Better Outcomes through Linked Data (BOLD): Privacy Notice | HTTP 200 |
| S23 | OK | 200 | MoJ-DfE data share: Privacy and Data Protection notice | HTTP 200 |
| S24 | OK | 200 | Data First: Criminal Courts Linked Data (publication landing page) | HTTP 200 |
| S25 | OK | 200 | Splink: Fast, accurate and scalable record linkage (Data in government blog) | HTTP 200 |
| S26 | OK | 200 | Splink tutorial: 7. Evaluation (linkage accuracy / false positives & negatives) | HTTP 200 |
| S28 | OK | 200 | National Data Opt-Out: supplementary information for research organisations (CAG / s.251) | HTTP 200 |
| S30 | OK | 200 | SRS Research and Data Access Policy | HTTP 200 |
| S31 | OK | 200 | About the Secure Research Service (Five Safes; DEA 2017 accreditation) | HTTP 200 |
| S32 | OK | 200 | Ensuring ADR UK data is used ethically and responsibly | HTTP 200 |
| S33 | OK | 200 | SAIL Databank — Governance | HTTP 200 |
| S35 | OK | 200 | The Data (Use and Access) Act 2025 (DUAA): summary of the changes — Data protection | HTTP 200 |
| S36 | OK | 200 | Right to be informed: are there any exceptions? (Art.14 indirect collection) | HTTP 200 |
| S37 | OK | 200 | Data Protection Act 2018, Schedule 1 (current revised text) | HTTP 200 |
| S38 | OK | 200 | Collecting and using special category data for official statistics and statistical research | HTTP 200 |
| S39 | OK | 200 | National Statistician's Data Ethics Advisory Committee (NSDEC) | HTTP 200 |
| S40 | OK | 200 | Overarching Data Protection Impact Assessment (DPIA) for the Federated Data Platform (FDP) | HTTP 200 |
| S41 | OK | 200 | Probabilistic Linkage Pipeline Improving Linkage Quality and Explainability in Healthcare (IJPDS) | HTTP 200 |
| S42 | OK | 200 | Data (Use and Access) Act 2025 (2025 c. 18) | HTTP 200 |
| S43 | OK | 200 | UK GDPR Article 22A — Automated processing and significant decisions | HTTP 200 |
| S44 | OK | 200 | UK GDPR Article 22B — Restrictions on automated significant decision-making | HTTP 200 |
| S45 | OK | 200 | UK GDPR Article 22C — Safeguards for permitted automated significant decisions | HTTP 200 |
| S46 | OK | 200 | UK GDPR Article 22D — Supplementary / Secretary of State regulation-making power | HTTP 200 |
| S47 | OK | 200 | UK GDPR Article 6 — incl. new point (1)(ea) 'recognised legitimate interest' | HTTP 200 |
| S48 | OK | 200 | UK GDPR Article 22 (substituted) — substitution note | HTTP 200 |
| S49 | OK | 200 | UK GDPR Annex 1 — Recognised legitimate interests (Art. 6(1)(ea)) | HTTP 200 |
| S50 | OK | 200 | UK GDPR Article 14 — information where data not obtained from the data subject (as amended) | HTTP 200 |
| S51 | OK | 200 | MoJ: Splink Master Record — Algorithmic Transparency Record | HTTP 200 |
| S52 | OK | 200 | HMPPS fair processing notice (prisons) | HTTP 200 |
| S53 | OK | 200 | National Probation Service Privacy Notice | HTTP 200 |
| S54 | OK | 200 | DWP 'fairness analysis' reveals bias in AI fraud detection system | HTTP 200 |
| S56 | OK | 200 | Algorithmic Transparency Records (ATRS registry) | HTTP 200 |

**Counts:** `OK=48`, `REDIRECT=2`, `STALE=2`



<div style="page-break-before: always;"></div>

# PART B — THE CITY OF LONDON CORPORATION


<div style="page-break-before: always;"></div>

## B1. Disclosure summary

# The City of London Corporation — Public-Interest Disclosure

**A sourced, evidence-graded account of (1) the Corporation's data-linkage footprint and (2) its
governance & transparency.**

- **Compiled:** 2026-06-10 · **Version:** 1.0 · First pass, source-checked.

> **What this is — and is not.** A transparency record from public sources, each verified live on the
> access date. It **does not allege unlawful conduct.** Unanswered points are marked UNKNOWN and turned
> into Freedom of Information requests, not filled by inference. Statuses: **CONFIRMED** (primary/official,
> read) · **LIKELY** (good secondary, or a live official page whose full text wasn't readable here) ·
> **UNKNOWN** (no sourced answer → FOI) · **SPECULATION** (labelled hypothesis).

## Executive summary
The City of London Corporation is a public authority with two features that draw legitimate public
scrutiny. **(1)** Through the **City of London Police** — the national lead force for fraud — it runs the
**National Fraud Intelligence Bureau (NFIB)**, which **automatically analyses and links** the nation's
fraud and cyber-crime reports and routes intelligence to local forces. **(2)** As a local authority it
is constitutionally unique: a **business-vote franchise**, a centuries-old private fund (**City's Cash**)
that sits **outside Freedom of Information**, and a **Remembrancer** who engages Parliament on the City's
behalf. **No wrongdoing is alleged.** The substance below is well-sourced; the open questions are about
**transparency** — what platform processes national fraud data, and on what basis City's Cash is shielded
from FOI.

## Track 1 — Data-linkage footprint (CONFIRMED unless noted)
- The **City of London Police** is the **national lead force for fraud** and runs the **NFIB** (Home-Office
  funded). *(S01)*
- The NFIB **automatically analyses and compares** fraud/cyber reports, identifies patterns, and sends
  intelligence "packages" to local forces — **automated triage and linking** at national scale. *(S01)*
- **Action Fraud** (2013) was replaced by **Report Fraud** on **4 Dec 2025**. *(S01)*
- City of London Police is the **data controller** for Report Fraud, and **DPIA summaries** (Crime
  Management, Data Migration, Intelligence, Prevention, Victim Services) are reportedly published.
  *(S03 — live page, full text not yet read; LIKELY)*
- **UNKNOWN — the analytics platform/vendor.** Whether Palantir Foundry, Microsoft or others power the
  linking is **not** established by any verified source (a search summary claimed Palantir; the verified
  source names no vendor). → FOI.
- Context: Action Fraud was heavily criticised — a **2019 Times** investigation (handlers misled victims)
  and a **2018 Which?** study (~25% of cases passed to local forces; <4% charged). *(S01)*

## Track 2 — Governance & transparency (CONFIRMED unless noted)
- The Corporation uses a **business-vote franchise** — organisations appoint voters by workforce size —
  **unique among UK local authorities** (such votes abolished elsewhere in 1969); by **2009 ~24,000
  business voters** vastly outnumbered residents. *(S02)*
- **City's Cash** is an **~800-year endowment**, **net assets ~£2.3bn (Mar 2016)** (>£1.3bn first
  disclosed 2012). *(S02)*
- **City's Cash sits outside the Freedom of Information Act 2000** — only the Corporation's public
  functions / the **City Fund** are FOI-covered. *(S05 — live page, full text not yet read; LIKELY)*
- The **Remembrancer** (office since **1571**) monitors and engages Parliament on legislation affecting
  the City and is one of ~20 **parliamentary agents** (with a seat in the Commons under-gallery).
  *(S02 core; S06/S09 for the detail)*

## The transparency asks (UNKNOWN → FOI; allege nothing)
1. **Name the analytics platform** running the national fraud database, and its contract. *(FOI-A §1)*
2. **Release the Report Fraud DPIAs** and state the lawful basis. *(FOI-A §2–3)*
3. **State the basis on which City's Cash is outside FOI**, and publish its latest accounts. *(FOI-B §1–2)*
4. **Is NFIB linking probabilistic, with what accuracy and what remedy** for a wrongful link? *(FOI-A §4)*

## What this does NOT say
- It does **not** allege unlawful processing, surveillance abuse, or corruption.
- It does **not** claim Palantir runs the fraud database — that is explicitly UNKNOWN.
- "Could not find / could not read" ≠ "does not exist" — only a transparency gap.

## Method & limits
All sources verified live by an automated checker (0 dead). Two official pages
(`reportfraud.police.uk`, `cityoflondon.gov.uk`) resolve (HTTP 200) but block the fetch client used
here, so their full text was **not personally read** — claims on them are **LIKELY**, not CONFIRMED,
pending a browser read. Three sources that blocked every client were dropped (logged in the register).
AI-assisted compilation; **review by a person, ideally a media/data-protection lawyer, is advised before
publication or transmission to officials.**

## Source register (verified live 2026-06-10)
- **S01** NFIB — `en.wikipedia.org/wiki/National_Fraud_Intelligence_Bureau` (read)
- **S02** City of London Corporation — `en.wikipedia.org/wiki/City_of_London_Corporation` (read)
- **S03** Report Fraud privacy — `reportfraud.police.uk/privacy-information/` (live, unread)
- **S05** FOI (City of London) — `cityoflondon.gov.uk/about-us/access-to-information/freedom-of-information` (live, unread)
- **S06** Remembrancer's Office — `cityoflondon.gov.uk/about-us/about-the-city-of-london-corporation/remembrancers-office` (live, unread)
- **S07** Business-vote registration — `cityoflondon.gov.uk/about-us/voting-elections/business-vote-registration` (live, unread)
- **S09** "Streets paved with gold" — `thebureauinvestigates.com/stories/2012-07-09/...` (secondary, 2012)


<div style="page-break-before: always;"></div>

## B2. Claims matrix (T1/T2)

# Claims matrix — City of London Corporation

Two tracks: **T1** data-linkage/data-sharing footprint · **T2** governance & transparency.
Status ∈ {CONFIRMED, LIKELY, UNKNOWN, SPECULATION}. CONFIRMED requires a live source whose
content was actually read. Sources flagged `BLOCKED?` (HTTP 403 to our fetch client) yield at most
LIKELY until read in a browser. Non-accusatory: gaps are FOI questions, not allegations.

## Track 1 — Data linkage / data sharing

| ID | Claim | Status | Source | Evidence | Legal relevance | Follow-up |
|----|-------|--------|--------|----------|-----------------|-----------|
| T1-01 | The City of London Police is the **national lead force for fraud** and runs the **National Fraud Intelligence Bureau (NFIB)**, Home-Office funded. | CONFIRMED | S01 (S04,S08 corrob.) | Wikipedia NFIB, read 2026-06-10. | Defines CoLP as a national data controller for fraud data. | — |
| T1-02 | The NFIB **automatically analyses and compares** fraud/cyber reports, identifies crime patterns, and generates intelligence "packages" routed to local forces — i.e. automated triage and **linking**. | CONFIRMED | S01 | Wikipedia NFIB description. | Automated processing / data linking at national scale. | Confirm method (deterministic vs probabilistic). |
| T1-03 | **Action Fraud** (launched 2013) was replaced by **"Report Fraud"** on **4 Dec 2025**. | CONFIRMED | S01 | Wikipedia NFIB. | Continuity of the data asset across systems. | — |
| T1-04 | The City of London Police is the **data controller** for the Report Fraud service. | LIKELY | S03 (BLOCKED?) | Search index of the privacy page; not browser-confirmed here. | Accountability for the processing. | Read S03 in a browser. |
| T1-05 | Multiple **DPIAs** (Crime Management, Data Migration, Intelligence, Prevention, Victim Services) exist for Report Fraud, with **published summaries**. | LIKELY | S03 (BLOCKED?) | Search index lists them. | Art. 35 / DPA 2018 accountability — and unusually, summaries appear public. | Read/obtain the DPIAs (FOI if summaries insufficient). |
| T1-06 | The Action Fraud replacement / NFIB tech (the "FCCRAS", renamed Report Fraud) is delivered by **Capita** (victim management, £50m) and **PwC** (crime & intelligence management); **Palantir** is named (one trade source) as PwC's **"technology alliance partner"** on it. | LIKELY | S11 (+ S13 context) | consultancy.uk names Palantir as PwC's partner on the NFIB tech (read). PwC+Palantir are a formal UK alliance (S13, press release). **BUT corroboration is partial:** Wikipedia names only Capita+PwC (no Palantir); the "Palantir Foundry at the heart of Report Fraud" line is an **unsourced search synthesis**, twice checked, NOT in the actual sources. | Who processes national fraud data, on what platform, under what contract. | **NOT yet publishable as fact.** Need the **procurement award notice** (Find a Tender/Contracts Finder) or PwC/CoLP/Palantir direct confirmation. → FOI to CoLP. |
| T1-09 | Palantir holds an **extensive, documented UK public-sector footprint** beyond the City — incl. the NHS Federated Data Platform (~£330m, under government review), a firearms-licensing system (43 forces), an MoD deal (~£240m), and an FCA data contract; a Met Police deal was **blocked** (2026); and Palantir **pitched reoffending-risk prediction to the MoJ (2024)**. | LIKELY | S12 (+ widely reported) | Multiple secondary sources / parliamentary EDM; context, not yet pinned to primaries here. | Establishes Palantir as a major UK state-data contractor — relevant backdrop to the NFIB link. | Pin each contract to a primary (contract notice / Hansard) before publishing. NOT linked to MoJ Splink/Data First (open-source; no Palantir). |
| T1-07 | Action Fraud was **widely criticised**: a 2019 Times investigation (handlers misled victims) and a 2018 Which? study (~25% of cases passed to local forces; <4% resulted in a charge). | CONFIRMED | S01 | Wikipedia NFIB, citing Times 2019 / Which? 2018. | Context on data quality / outcomes, not a data-protection breach. | Cite the Times/Which? originals directly. |
| T1-08 | The **lawful basis** for Report Fraud processing (likely DPA 2018 Part 3, law-enforcement processing). | UNKNOWN | S03 (BLOCKED?) | Not confirmed from a read source. | Part 3 DPA 2018 vs UK GDPR. | Read S03 / FOI. |

## Track 2 — Governance & transparency

| ID | Claim | Status | Source | Evidence | Legal relevance | Follow-up |
|----|-------|--------|--------|----------|-----------------|-----------|
| T2-01 | The Corporation operates a **business/corporate vote franchise** — organisations appoint voters by workforce size — **unique among UK local authorities** (such votes abolished elsewhere in 1969). | CONFIRMED | S02 (S07 corrob.) | Wikipedia CoL Corporation, read 2026-06-10. | Democratic-legitimacy / franchise question. | — |
| T2-02 | By **2009, business voters (~24,000)** vastly outnumbered residential voters. | CONFIRMED | S02 | Wikipedia CoL Corporation. | Scale of the business franchise. | Confirm current figures. |
| T2-03 | The **City of London (Ward Elections) Act 2002** expanded the business franchise. | LIKELY | S02 (+ search) | Referenced in Wikipedia + search; the Act itself not yet sourced to legislation.gov.uk. | Statutory basis of the franchise. | Cite the Act on legislation.gov.uk. |
| T2-04 | **City's Cash** is an ~800-year endowment; **net assets ~£2.3bn (Mar 2016)**, >£1.3bn first disclosed 2012. | CONFIRMED | S02 | Wikipedia CoL Corporation. | Scale of privately-controlled public-body funds. | Obtain latest City's Cash accounts. |
| T2-05 | **City's Cash / privately-funded activities sit outside the Freedom of Information Act 2000** (only public functions / the City Fund are covered). | LIKELY | S05 (BLOCKED?), S10 | Corporation's own FOI page (search index) + FOI-archive consensus; not browser-confirmed here. | Transparency gap — the core governance question. | Read S05; document refused City's Cash FOIs (S10). |
| T2-06 | The **Remembrancer** is a City chief officer (office dating to 1571) who monitors and engages Parliament on legislation affecting the City, and is one of ~20 **parliamentary agents** (with a seat in the Commons under-gallery). | CONFIRMED (core) / LIKELY (under-gallery + agent detail) | S02 (core), S06 (BLOCKED?), S09 | Wikipedia confirms legislative-liaison role; under-gallery/agent detail from the Corporation's page + secondary. | Institutional lobbying access to Parliament. | Read S06; cite the parliamentary-agents list. |
| T2-07 | The Corporation runs **three financial funds**: City Fund (public/rates, FOI-covered), City's Cash (private endowment), and Bridge House Estates (charity). | LIKELY | (general; verify) | Widely reported; not pinned to a read primary here. | Distinguishes which monies are publicly accountable. | Source each fund to the Corporation's accounts. |

**Counts:** CONFIRMED = 6 · LIKELY = 8 · UNKNOWN = 1 · SPECULATION = 0.
(T1-06 moved UNKNOWN→LIKELY on the consultancy.uk source naming Palantir as PwC's partner; T1-09 added for Palantir's broader UK footprint.)

> Integrity note: the single most "interesting" lead — that Palantir Foundry powers the national fraud
> database — is recorded as **UNKNOWN**, because the source that actually verified (Wikipedia NFIB) does
> **not** name any vendor; the Palantir/Microsoft detail existed only in a search-engine summary. It is a
> sharp FOI target (T1-06), not a claim.


<div style="page-break-before: always;"></div>

## B3. The full Palantir / UK-state-data story

# The full story: Palantir and the UK state's data systems

_Evidence-graded, non-accusatory. This is about **corporate public contracts**, lawfully procured.
Nothing here implicates Peter Thiel (Palantir's co-founder/chairman) in personal wrongdoing; the story
is the **scale and opacity** of one US company's embedding in UK state data, and the scrutiny it is
already drawing. Status: CONFIRMED / LIKELY / UNKNOWN. Secondary-sourced items must be pinned to
primaries (contract notices, Hansard) before publication._

## The thread
Palantir Technologies — a US data-analytics firm with deep US intelligence and defence roots, co-founded
by **Peter Thiel** — has, over a few years, won or partnered on contracts across many of the UK state's
most sensitive data systems. Several are under review or were blocked; much was procured with limited
public scrutiny. That accumulation, not any single deal, is the story.

## The footprint (each item: status + what to pin)
- **PwC–Palantir UK alliance.** Formal "preferred partners" multi-year deal (PwC + BusinessWire press
  releases, Nov 2025). `[LIKELY — corporate press release, not read in full here → verify]`
- **National Fraud Intelligence Bureau / Report Fraud (the City link).** PwC delivers the crime &
  intelligence-management tech; **Palantir named as PwC's "technology alliance partner"** (one trade
  source). Official record names **Capita + PwC** only. `[LIKELY S11 — single source; the "Foundry at
  the heart of it" line is unsourced search synthesis, rejected → get the FCCRAS procurement notice]`
- **NHS Federated Data Platform.** Palantir contract Nov 2023, **~£182m→£330m/7yr**, with
  PwC/Accenture/NECS/Carnall Farrar; reported **"unrestricted access" to identifiable patient data
  (~65m people)** as processor; **under UK government review** with a break clause. `[LIKELY — widely
  reported (TechRadar, The Lowdown, Register); pin to the contract + parliamentary record]`
- **Ministry of Defence.** ~**£240m** data-analytics deal (Dec 2025) for operational decision-making.
  `[LIKELY — reported; pin to notice]`
- **Financial Conduct Authority.** Palantir analysing the FCA data lake (fraud/money-laundering/insider
  trading), ~£30k/week. `[LIKELY — reported]`
- **Firearms licensing.** ~**£9m**, all **43 forces**, ~500k people / ~2m weapons + explosives/poisons
  records. `[LIKELY — reported (Register)]`
- **Metropolitan Police — BLOCKED.** A ~**£25.3m** (+£24.8m extension) Met deal to automate criminal-
  intelligence analysis was **refused** by the deputy mayor (May 2026) over procurement-process
  concerns. `[LIKELY — reported (Computing, Register, MEE)]`
- **MoJ pitch (2024).** Palantir **pitched "reoffending-risk" prediction** for prisons; Amnesty
  International UK objected. A **pitch, not a contract.** `[LIKELY — reported (Novara)]`
- **Scale.** The Nerve (Jan 2026): **34+ contracts, 10+ departments, ~£670m** (incl. Home Office, GDS,
  councils). `[LIKELY — pin]`

## Parliamentary / official scrutiny (corroboration — strengthens the footprint)
- **Commons Science, Innovation & Technology Select Committee (3 Jun 2026)** called on the government to
  **end NHS England's Palantir contract**, calling Palantir "the most concerning example" of reliance on
  a few big tech firms. `[LIKELY — committee; pin to the report]`
- An **Early Day Motion** condemns DHSC over FDP transparency and flags **Lord Mandelson's reported role**
  in helping Palantir win government contracts. `[LIKELY — EDM exists; verify text]`
- The FCCRAS (fraud) programme is a **Home Office major project** with published Accounting-Officer
  assessments and SRO letters on gov.uk — a primary governance trail to pull.

## FCCRAS procurement check (honest result)
Searching the procurement/governance record for the NFIB tech contract returns **Capita (£50m) + PwC**
as the named contractors (CoLP/Home Office records, techmonitor, Sharecast). **Palantir is NOT named in
the procurement record found** — only in the consultancy.uk trade report (as PwC's partner). So the
Palantir↔NFIB link **stays LIKELY/single-source**; the FCCRAS award notice or an FOI is still needed to
confirm Palantir specifically.

## What this story is NOT (the boundaries that keep it honest)
- **Not the MoJ linkage.** Splink / Data First / the cross-justice linkage is **MoJ open-source software
  (on Spark), NOT Palantir.** Do not conflate the two.
- **Two different NHS systems.** The **FDP (Palantir)** is distinct from the **Data Linkage Hub
  (Splink)**. Keep them separate.
- **Not personal wrongdoing.** These are lawful corporate contracts. The critique is *scale, opacity,
  and Palantir's intelligence/ICE associations* — a transparency-and-policy argument, not a crime.
- **Not confirmed at the City.** The NFIB↔Palantir link is **LIKELY (one source)**, not fact.

## To turn this from "story" into "publishable"
1. **FCCRAS procurement award notice** (Find a Tender / Contracts Finder) — names subcontractors.
2. **FOI to City of London Police** — confirm Palantir/platform + contract value.
3. **Pin each contract** above to its primary (contract notice / Hansard / the body's own announcement).
4. **The honest headline:** *"A US intelligence-linked firm has quietly embedded across UK state data —
   health, defence, finance, policing, fraud — much of it under-scrutinised; some now under review."*
   That is true, large, and defensible. "They broke the law" / "get Thiel" is neither.


<div style="page-break-before: always;"></div>

## B4. Track notes

# Track notes

## TRACK 1 — Data linkage / data sharing footprint

### DS-T1 — City of London Police: NFIB & Report Fraud
- **Operator / controller:** City of London Police, national lead force for fraud; runs the **National
  Fraud Intelligence Bureau (NFIB)**, Home-Office funded. `[CONFIRMED S01]`
- **What it does:** national reporting + collation of fraud/cyber reports; systems **automatically
  analyse and compare** reports, assess for crime patterns, and dispatch intelligence **"packages"** to
  local forces — automated triage and **linking** at national scale. `[CONFIRMED S01]`
- **System lineage:** **Action Fraud** (2013) → **Report Fraud** (4 Dec 2025). `[CONFIRMED S01]`
- **Data controller (Report Fraud):** City of London Police. `[LIKELY S03 — live, unread]`
- **DPIAs:** Crime Management, Data Migration, Intelligence, Prevention, Victim Services — **summaries
  reportedly published** on the privacy page. `[LIKELY S03]`
- **Lawful basis:** likely DPA 2018 **Part 3** (law-enforcement processing). `[UNKNOWN — verify S03/FOI]`
- **Analytics platform / vendor:** the Action Fraud replacement / NFIB tech is delivered by **Capita**
  (victim management, £50m) and **PwC** (crime & intelligence management), with **Palantir** named as
  PwC's **"technology alliance partner."** `[LIKELY S11 — single trade-press source; corroborate + FOI T1-06]`
  - **Wider Palantir footprint (context):** NHS Federated Data Platform (~£330m, under review),
    firearms-licensing (43 forces), MoD (~£240m), FCA data; a Met Police deal was **blocked** (2026);
    Palantir **pitched MoJ reoffending-risk prediction (2024)**. `[LIKELY S12 — pin to primaries]`
    **Note:** the MoJ **Splink/Data First** linkage is open-source and is **NOT** Palantir — do not conflate.
- **Track record:** 2019 Times investigation (handlers misled victims); 2018 Which? (~25% of cases
  passed to local forces; <4% charged). `[CONFIRMED S01]` (context on outcomes, not a data breach.)

## TRACK 2 — Governance & transparency

### Business-vote franchise
- Organisations appoint voters by workforce size; a non-residential business vote **abolished elsewhere
  in the UK in 1969**. By 2009, **~24,000 business voters** vastly outnumbered residents — anomalous
  among UK local authorities. `[CONFIRMED S02]` Statutory expansion via the **City of London (Ward
  Elections) Act 2002**. `[LIKELY — source the Act on legislation.gov.uk]`

### City's Cash
- ~800-year endowment; **net assets ~£2.3bn (Mar 2016)**; >£1.3bn first disclosed 2012. `[CONFIRMED S02]`
- Reportedly **outside the Freedom of Information Act 2000** (only the Corporation's public functions /
  the **City Fund** are FOI-covered). `[LIKELY S05 — live, unread]` — the core transparency question.
- Three funds: **City Fund** (public/rates, FOI), **City's Cash** (private endowment), **Bridge House
  Estates** (charity). `[LIKELY — source to the accounts]`

### The Remembrancer
- City chief officer (office dating to **1571**); monitors/engages Parliament on legislation affecting
  the City; one of ~20 **parliamentary agents** (with a seat in the Commons under-gallery).
  `[CONFIRMED core S02 | LIKELY under-gallery/agent detail S06, S09]`

## Legal questions (neutral)
- **L1 (T1):** Which lawful basis (DPA 2018 Part 3 vs UK GDPR) underpins Report Fraud/NFIB, and what
  Art. 9/sensitive-data and Part 3 conditions apply? `[UNKNOWN]`
- **L2 (T1):** Is the NFIB linking deterministic or probabilistic, and is there published accuracy /
  a remedy for wrongful linkage? `[UNKNOWN]`
- **L3 (T1):** What automated processing occurs, and is any decision about an individual taken (UK GDPR
  Art. 22A / DPA Part 3 automated-processing safeguards)? `[UNKNOWN]`
- **L4 (T2):** What is the precise statutory boundary of FOIA coverage for the Corporation, and on what
  basis is City's Cash excluded? `[UNKNOWN — verify S05]`
- **L5 (T2):** What transparency applies to the Remembrancer's parliamentary engagement (lobbying
  registers, records of representations)? `[UNKNOWN]`

## Timeline
| Date | Event | Status | Source |
|------|-------|--------|--------|
| 1571 | Office of Remembrancer established. | LIKELY | S02/S06 |
| 1969 | Non-residential business vote abolished elsewhere in the UK (retained in the City). | CONFIRMED | S02 |
| 2002 | City of London (Ward Elections) Act expands the business franchise. | LIKELY | S02 |
| 2012 | City's Cash value (>£1.3bn) first disclosed. | CONFIRMED | S02 |
| 2013 | Action Fraud launched. | CONFIRMED | S01 |
| 2016-03 | City's Cash net assets ~£2.3bn. | CONFIRMED | S02 |
| 2018 | Which? study: ~25% of cases passed on; <4% charged. | CONFIRMED | S01 |
| 2019 | Times investigation into Action Fraud handling. | CONFIRMED | S01 |
| 2025-12-04 | Action Fraud replaced by Report Fraud. | CONFIRMED | S01 |


<div style="page-break-before: always;"></div>

## B5. Open questions

# Open questions (prioritised)

Tags: **[FOI-ONLY]** no public source · **[DOC-READ]** answer likely in a live page we hold but
couldn't auto-read · **[VERIFY]** confirm/upgrade a LIKELY against primary text.

## P1
- **[FOI-ONLY] T1-06 — Analytics vendor & contract.** What platform powers NFIB/Report Fraud linking
  (Palantir Foundry? Microsoft? other), under what contract and value? The "Palantir" detail was a
  search-summary artefact, unverified — this is a clean FOI to City of London Police.
- **[DOC-READ] T1-04/05/08 — Report Fraud DPIAs, controller, lawful basis.** The privacy page (S03) is
  live but blocks our fetcher; read it in a browser and lift the DPIA summaries + lawful basis verbatim.
- **[DOC-READ] T2-05 — City's Cash & FOI.** Read the Corporation's FOI page (S05) in a browser to
  confirm the exact basis on which City's Cash sits outside FOIA; pair with documented FOI refusals.
- **[FOI-ONLY] T2-05b — City's Cash accounts.** Request the latest City's Cash accounts and a
  breakdown of non-statutory expenditure.

## P2
- **[VERIFY] T2-03 — Ward Elections Act 2002.** Cite the Act on legislation.gov.uk (franchise basis).
- **[VERIFY] T1-07 — Action Fraud criticism.** Pull the Times (2019) and Which? (2018) originals.
- **[VERIFY] T2-06 — Remembrancer.** Read S06 + the parliamentary-agents list for the under-gallery/agent detail.
- **[FOI-ONLY] L2/L3 — Linkage method & automated decisions.** Is NFIB linking probabilistic? Any
  automated decision about an individual, with what safeguards and remedy for wrongful linkage?

## P3
- **[VERIFY] T2-07 — Three funds** (City Fund / City's Cash / Bridge House Estates) sourced to accounts.
- **[FOI-ONLY] L5 — Remembrancer transparency:** records of representations to Parliament / lobbying registers.

### FOI-only vs closeable-by-reading
- **FOI-only (4):** analytics vendor (T1-06); City's Cash accounts (T2-05b); linkage method/automated
  decisions (L2/L3); Remembrancer representations (L5).
- **Closeable by reading (5):** Report Fraud DPIAs/basis (S03), City's Cash FOI basis (S05), Ward
  Elections Act, Action Fraud originals, Remembrancer detail (S06).


<div style="page-break-before: always;"></div>

## B6. FOI drafts

# FOI request drafts (non-accusatory)

Requests for documents/facts under the Freedom of Information Act 2000, framed neutrally and narrowed
to genuine gaps. Confirm current FOI contacts on each body's official page before sending.

---

## FOI-A — City of London Police (NFIB / Report Fraud)
**Subject:** Report Fraud / NFIB — analytics platform, DPIAs, and linkage accuracy

1. Please name the **analytics platform and supplier** used by the NFIB / Report Fraud service to
   triage and link reports, and provide the **contract** (value, term, supplier). (T1-06)
2. Please provide the **Data Protection Impact Assessments** for Report Fraud referenced on the
   privacy page (Crime Management, Data Migration, Intelligence, Prevention, Victim Services), in full
   or redacted. (T1-05)
3. Please state the **lawful basis** for the processing (Data Protection Act 2018 Part 3 and/or UK
   GDPR), and any conditions for sensitive-category data. (T1-08)
4. Please describe whether report **linking is deterministic or probabilistic**, any published
   **accuracy/error rates**, and the **process to correct a wrongful link** affecting an individual. (L2)
5. Please confirm whether any **solely-automated decision** about an individual is taken, and the
   safeguards that apply. (L3)

> Already public — do NOT ask: that CoLP is national lead force and runs NFIB (S01); that Action Fraud
> became Report Fraud on 4 Dec 2025 (S01).

## FOI-B — City of London Corporation (governance / transparency)
**Subject:** City's Cash and the FOI boundary

1. Please confirm the **basis on which City's Cash (and other privately-funded activities) falls outside
   the Freedom of Information Act 2000**, with reference to the relevant designation. (T2-05)
2. Please provide the **latest City's Cash annual accounts** and a breakdown of **non-statutory
   expenditure** for the most recent year. (T2-05b)
3. Please confirm the current split and FOI status of the **City Fund**, **City's Cash**, and **Bridge
   House Estates**. (T2-07)
4. Please provide any **register or records of the Remembrancer's representations** to Parliament/
   Government on behalf of the City in the last 24 months. (L5)

> Already public — do NOT ask: the existence/role of the Remembrancer (S02/S06); the business-vote
> franchise mechanics (S02/S07).

---
> The cleanest single asks: **FOI-A §1** (name the platform running the national fraud database) and
> **FOI-B §1** (state why City's Cash is outside FOI). Both request facts, allege nothing.


<div style="page-break-before: always;"></div>

## B7. Source table

# Master source table

Flags re-verified by `scripts/source_checker.py`. LIVE = HTTP 200. Sources marked
"(live, unread)" returned 200 to the checker but block the fetch client, so their full text
was not personally read; claims on them are graded LIKELY.

| # | Title | Publisher | Pub date | URL | Accessed | Track | Flag |
|---|-------|-----------|----------|-----|----------|-------|------|
| S01 | National Fraud Intelligence Bureau | Wikipedia | — | https://en.wikipedia.org/wiki/National_Fraud_Intelligence_Bureau | 2026-06-10 | T1 | LIVE (read) |
| S02 | City of London Corporation | Wikipedia | — | https://en.wikipedia.org/wiki/City_of_London_Corporation | 2026-06-10 | T2 | LIVE (read) |
| S03 | Report Fraud — Privacy information | City of London Police | — | https://www.reportfraud.police.uk/privacy-information/ | 2026-06-10 | T1 | LIVE (unread) |
| S05 | Freedom of Information Act 2000 (City of London) | City of London Corporation | — | https://www.cityoflondon.gov.uk/about-us/access-to-information/freedom-of-information | 2026-06-10 | T2 | LIVE (unread) |
| S06 | Remembrancer's Office — Working with Parliament | City of London Corporation | — | https://www.cityoflondon.gov.uk/about-us/about-the-city-of-london-corporation/remembrancers-office | 2026-06-10 | T2 | LIVE (unread) |
| S07 | Business/worker vote registration | City of London Corporation | — | https://www.cityoflondon.gov.uk/about-us/voting-elections/business-vote-registration | 2026-06-10 | T2 | LIVE (unread) |
| S09 | Streets paved with gold: the council that works for banks | The Bureau of Investigative Journalism | 2012-07-09 | https://www.thebureauinvestigates.com/stories/2012-07-09/streets-paved-with-gold-the-council-that-works-for-banks | 2026-06-10 | T2 | LIVE (secondary, dated) |

**Dropped as unverifiable (403 to every client here; see `raw_links.json` `_meta`):**
cityoflondon.police.uk National Lead Force; committees.parliament.uk CoLP written evidence;
whatdotheyknow.com City of London FOI archive. Their points are carried by S01 / S05; re-add after a browser read.

> To-source precisely (currently from search/secondary, see open_questions): City of London (Ward
> Elections) Act 2002 on legislation.gov.uk; the Times (2019) and Which? (2018) Action Fraud originals;
> latest City's Cash accounts.


<div style="page-break-before: always;"></div>

## B8. Source-check report

# Source Check Report

_Generated: 2026-06-11 · max-age-days=90_

| ID | Status | HTTP | Title | Detail |
|----|--------|------|-------|--------|
| S09 | UNCLEAR | 200 | Streets paved with gold: the council that works for banks | pre-flagged UNCLEAR; HTTP 200 |
| S12 | UNCLEAR | 200 | Palantir, the controversy, the contracts and the campaign against the FDP | pre-flagged UNCLEAR; HTTP 200 |
| S13 | UNCLEAR | 200 | Palantir and PwC UK sign multi-year deal as preferred partners | pre-flagged UNCLEAR; HTTP 200 |
| S01 | OK | 200 | National Fraud Intelligence Bureau | HTTP 200 |
| S02 | OK | 200 | City of London Corporation | HTTP 200 |
| S03 | OK | 200 | Report Fraud — Privacy information | HTTP 200 |
| S05 | OK | 200 | Freedom of Information Act 2000 (City of London) | HTTP 200 |
| S06 | OK | 200 | Remembrancer's Office — Working with Parliament | HTTP 200 |
| S07 | OK | 200 | Business/worker vote registration | HTTP 200 |
| S11 | OK | 200 | London Police selects Capita and PwC for Action Fraud upgrade work | HTTP 200 |

**Counts:** `OK=7`, `UNCLEAR=3`

