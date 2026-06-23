# Full Tier-Graded Findings — UK Government Data-Linkage Legal Exposure

Backing record for *Ruled Unlawful Next Door*. Three adversarial deep-research passes, ~300 verification agents, 99 sources, 75 claims verified / 4 killed for overreach.

**Tier rubric.** **T1** = ICO enforcement notice / monetary penalty / formal reprimand against the named controller, OR a court ruling that the processing was unlawful (named + dated + cited). **T2** = regulator concern short of enforcement, or a settled / withdrawn judicial review (a settlement, not a ruling). **T3** = criticism without regulatory or judicial adjudication.

## Headline

NO Tier-1 adjudication against any of the four named systems. Every genuine T1 ruling is **adjacent** (Home Office immigration data), not on the linkage systems. Defensible frame: *the same policy-not-law shortcut was struck down next door* — never assert a violation against Data First itself (none exists).

## Per-target verdicts (all "None"; high confidence)

**MoJ Data First — None.** Transparency record documents only a DPIA, the Five Safes, identifier removal and panel oversight; no legal challenge, ICO enforcement, or court ruling.
*Source:* https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink
*Context (unrelated to linkage):* MoJ ICO reprimand May 2023 (confidential waste); £140,000 fine 2011–13 (prisoner spreadsheet emailed to families); Enforcement Notice 18 Jan 2022 over ~7,753 overdue subject-access requests.

**Splink — None.** The open-source probabilistic record-linkage library (Fellegi–Sunter) built for Data First; nothing adjudicated against the tool itself.

**ONS Integrated Data Service / Integrated Data Programme — None (searched directly, not inferred).** Highest adverse material is Tier 3:
- PAC "Government use of data" (27 Mar 2026) — value-for-money / adoption criticism only, zero data-protection findings. https://committees.parliament.uk/publications/52403/documents/290832/default
- OSR follow-up "Data sharing and linkage for the public good" (17 Jul 2024) — recommendatory; no sanction. https://osr.statisticsauthority.gov.uk/publication/data-sharing-and-linkage-for-the-public-good-follow-up-report/pages/3/
- NSDEC minutes (3 Apr 2023) — named IDS *positively* as a strategic project to prioritise for ethics review.
OSR and NSDEC have no enforcement power → structurally cannot reach T1/T2.

**ADR UK — None.** Governance rests on the Digital Economy Act 2017, the Five Safes and NSDEC ethics review. The ICO has *endorsed* the Five Safes model.
*Source:* https://www.adruk.org/about-us/ensuring-adr-uk-data-is-used-ethically-and-responsibly/

## Adjacent Tier-1 — immigration exemption ruled unlawful three times (high confidence)

Decisive nuance: these concern an exemption from individuals' **own** data-subject rights (access / erasure / objection), NOT inter-departmental linkage or sharing. The defect was procedural (safeguards must be in law, not policy). Adjacent to — legally distinct from — the linkage playbook (per David Erdos, UKCLA, 17 Apr 2023).

- **[2021] EWCA Civ 800** — Court of Appeal, 26 May 2021 (Warby LJ, with Singh and Underhill LJJ). Original DPA 2018 immigration exemption unlawful: "an unauthorised derogation from the fundamental rights conferred by the GDPR." Failed UK GDPR Art 23(2). Declaration suspended ([2021] EWCA Civ 1573) to 31 Jan 2022 → remedied by SI 2022/76.
- **[2023] EWHC 713 (Admin)** — High Court, 29 Mar 2023 (Saini J). Revised exemption STILL unlawful; Grounds 1 & 2 succeeded. Ratio: safeguards "must appear on the face of the legislation or in a binding code (approved by Parliament) and with statutory force." Declaratory orders suspended by agreement. https://www.bailii.org/ew/cases/EWHC/Admin/2023/713.html · https://caselaw.nationalarchives.gov.uk/ewhc/admin/2023/713
- **[2023] EWCA Civ 1474** — Court of Appeal, 11 Dec 2023. Confirmed para 4 still breached Art 23(2). The ruling the 2024 fix answered (declaration suspended to 11 Mar 2024).

*Background:* https://lordslibrary.parliament.uk/data-protection-regulations-and-the-immigration-exemption/ · https://www.openrightsgroup.org/campaign/immigration-exemption-campaign-page/

## Current statutory status (2026, confirmed verbatim vs legislation.gov.uk)

- **SI 2024/342** — The Data Protection Act 2018 (Amendment of Schedule 2 Exemptions) Regulations 2024. Made 7 Mar 2024, in force 8 Mar 2024 (reg 1(2)). Omits para 4 sub-paras (1A)/(1B); substitutes new paras 4A/4B requiring case-by-case, per-provision, afresh-each-time decisions, a substantial-risk balancing / necessity-proportionality test, and vulnerability / Convention / Refugee / Trafficking safeguards, with recording and notification duties — all on the face of the statute. https://www.legislation.gov.uk/uksi/2024/342/made · EM: https://www.legislation.gov.uk/uksi/2024/342/pdfs/uksiem_20240342_en_001.pdf
- **Data (Use and Access) Act 2025 (c.18)** — Royal Assent 19 Jun 2025; successor to the failed DPDI Bill. Left the immigration exemption UNTOUCHED (only amends the separate crime exemption, Sch 11 para 29). https://www.legislation.gov.uk/ukpga/2025/18 · gov.uk summary: https://www.gov.uk/guidance/data-use-and-access-act-2025-data-protection-and-privacy-changes
- No fourth round of litigation found post-March 2024 (negative finding; medium confidence — search-tooling limited).
- ICO guidance on the current exemption: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/exemptions/immigration-exemption-a-guide/

## Closest-to-linkage hit (Tier 2)

**ICO consultation response on the National Fraud Initiative, 26 Mar 2021.** Warned the Cabinet Office "has not yet undertaken a DPIA" and should before any processing; necessity / proportionality not demonstrated; on-demand matching (AppCheck) "could potentially allow participants to conduct disproportionate searches for information about particular individuals across a wide range of sources without lawful cause." Most on-point item for the linkage thesis, but a consultation response — NOT enforcement. No T1 on inter-departmental matching found.
*Source:* https://ico.org.uk/about-the-ico/consultations/cabinet-office-s-consultation-on-the-expansion-of-the-national-fraud-initiative-data-matching-purposes-2021/

## Handle-with-care (recurring misframings)

- **Royal Free–DeepMind, ICO 3 Jul 2017** — a FINDING of DPA 1998 non-compliance (~1.6M patient records), remedied via a voluntary UNDERTAKING. NO fine, NO notice. Cite as "finding via undertaking," never a penalty. Borderline T1/T2. https://ico.org.uk/action-weve-taken/enforcement/royal-free-london-nhs-foundation-trust/
- **Home Office visa-streaming algorithm, 2020** — withdrawn 7 Aug 2020 before any hearing (JCWI/Foxglove JR); no ruling, no admission. Firmly T2. https://www.foxglove.org.uk/2020/08/04/home-office-says-it-will-abandon-its-racist-visa-algorithm-after-we-sued-them/
- **DWP Universal Credit [2020] EWCA Civ 778** — real ruling vs DWP, but Wednesbury irrationality over salary-payment timing; ZERO data-protection holding. Irrelevant to linkage. https://www.bailii.org/ew/cases/EWCA/Civ/2020/778.html
- **Home Office GPS tagging of migrants, ICO 1 Mar 2024** — genuine T1 enforcement notice + warning, but DPIA/surveillance failure, NOT data-matching. https://ico.org.uk/action-weve-taken/enforcement/2024/03/home-office/

## Open items

1. Did the Cabinet Office complete the 2021 DPIA the ICO demanded; any ICO follow-up once expanded NFI matching went live?
2. Any T1 on DWP fraud matching / HMRC bulk sharing / Digital Economy Act 2017 public-service-delivery sharing powers beyond the NFI consultation? Not searched to exhaustion.
3. ICO enforcement register renders via JavaScript — the ONS "none found" rests on converging searches, not one authoritative dynamic query.
