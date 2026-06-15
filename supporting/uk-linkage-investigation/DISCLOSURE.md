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
