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
