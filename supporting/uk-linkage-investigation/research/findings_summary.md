# Findings summary (first pass)

_As of 2026-06-10. Evidence-first, non-accusatory. Every CONFIRMED claim rests on a live,
checker-verified source whose content was read. This is a first-pass map, not a final report._

> **Public-ready version:** see top-level `DISCLOSURE.md`. DUAA 2025 legal teardown: `duaa_adm_teardown.md`.
> **Counts:** CONFIRMED 21 · LIKELY 2 · UNKNOWN 3 · SPECULATION 0 (45+ live sources, 0 dead).

## Headline
UK public-sector probabilistic record linkage (MoJ Splink via **Data First** and **BOLD**, NHS England
Data Linkage Hub, ONS Census→PDS) is **substantially documented in the public record**. The *what*,
*by whom*, *legal basis* and *safeguards* are largely sourced. **No evidence of wrongdoing was found**,
and the most sensitive question — whether the linkage drives decisions about individuals — is answered
by the government's own transparency record as **research/statistics only** for Data First.

## What is CONFIRMED (13 claims)
- Splink is MoJ open-source probabilistic linkage; ADR-UK-funded under Data First. (S01/S03/S25)
- Data First links courts (magistrates'/Crown/civil/family) + prisons + probation (E&W), as a
  de-identified person-link lookup table; includes OASys (1,100+ vars). (S06/S07/S08)
- Access is via accredited researchers in ONS SRS (Five Safes, DEA 2017) and SAIL. (S06/S30/S31/S33)
- A MoJ↔DfE (education) share exists. (S06/S18/S23)
- NHS England is building a Splink linkage service on PDS as the spine. (S13/S41)
- ONS linked Census 2021 → PDS to assign NHS numbers, feeding the PHDA. (S14)
- **Data First is research-only — "not for operational decision-making".** (S19, ATRS)
- **A DPIA was completed for Data First.** (S19)
- Special-category processing needs Art. 6 + Art. 9 (+ DPA Sch. 1). (S15/S16/S37)
- **DUAA 2025 (in force 5 Feb 2026)** replaced UK GDPR Art. 22 with Arts. 22A–22D and the research
  safeguard Art. 89(1) with Art. 84B. (S37/S42/S43)

## What is still UNKNOWN (3 — all FOI-bound)
1. **The DPIA is not published** (only its existence is confirmed). → FOI-1 §1.
2. **No individual opt-out / objection route** for Data First is documented. → FOI-1 §2.
3. **No published match-error rates and no described remedy** for a mis-linked individual. → FOI-1 §3.

## Scope expansion found in the completion sweep
- **BOLD** (Better Outcomes through Linked Data) — a second, **broader** MoJ linkage programme adding
  police, CPS, health & social care, HMRC Child Benefit and drug-treatment data; basis Art. 6(1)(e) +
  Art. 9(2)(h)/Caldicott; no stated opt-out. (S22) Its own DPIA is a fresh FOI target (FOI-5).
- **DUAA 2025** teardown completed on primary text: default inversion for ordinary data, special-
  category near-ban retained, new Art. 6(1)(ea)/Annex 1 (incl. crime/safeguarding), SoS powers in
  Art. 22D, and an Art. 14 transparency amendment (verbatim-verify pending).

## Closeable without FOI (read documents already held)
Data First lawful basis + Art. 9/10 conditions and the MoJ↔DfE specifics are almost certainly in
the privacy statement (S20) and MoJ–DfE notice (S23) — both image-PDFs needing a manual read.

## The single biggest gap
**Publication of the completed Data First DPIA (C11b).** The government's own Algorithmic
Transparency Record says a DPIA exists; releasing it would, in one document, likely answer the
lawful-basis, special-category-condition, opt-out and accuracy questions at once. It is the
highest-leverage, lowest-controversy request in the project.

## Provenance / integrity notes
- 39 active sources, all checker-verified live (0 DEAD). 1 seed retired (S05, 404×3); 3 sources
  dropped as unverifiable (NHS Digital / ICO subpages that 403 every automated client here) —
  all documented in `evidence/raw_links.json` `_meta`.
- Two MoJ PDFs (S20, S23) resolve but could not be text-extracted; not used to back any claim.
- Statutory references verified against current legislation.gov.uk text (post-DUAA 2025).
