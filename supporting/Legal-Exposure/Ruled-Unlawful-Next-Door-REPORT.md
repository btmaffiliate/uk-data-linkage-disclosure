# Ruled Unlawful Next Door: What Has Actually Been Adjudicated

**Public-interest investigation · Legal exposure · June 2026**
Part 3 of the UK data-linkage series. Companion to *The Quiet Joining-Up* and *Statistics or Operations?*
Published: https://brandonmyers.net/writing/ruled-unlawful-next-door
Slides: [HTML](slides/uk-data-linkage-tier1-exposure.html) · [PPTX](slides/uk-data-linkage-tier1-exposure.pptx) · [PDF](slides/uk-data-linkage-tier1-exposure.pdf)

---

This piece asks the coldest question of the series: **has any of the UK's government data-linkage machinery actually been ruled unlawful — and if so, where, exactly?**

I set a deliberately high bar and graded every finding against it:

- **Tier 1** — an ICO enforcement notice, monetary penalty or formal reprimand against the named system, *or* a court ruling that the processing was unlawful. Named, dated, citable.
- **Tier 2** — a regulator concern short of enforcement, or a judicial review that settled or was withdrawn rather than ruled.
- **Tier 3** — criticism, however serious, without an adjudication behind it.

Three independent research passes, ~300 adversarial verification agents, 99 sources, 4 claims thrown out for overreach (including one of my own).

## The verdict in one paragraph

**No Tier-1 adjudication exists against any of the four named systems** — MoJ Data First, Splink, the ONS Integrated Data Service, or ADR UK. No fine, no enforcement notice, no reprimand, no court ruling. The genuine rulings of unlawfulness are all **adjacent** — they hit Home Office data processing next door, using the same legal posture. So I will not tell you Data First has been found unlawful. It has not. What I will tell you, and can prove, is that **the same shortcut — putting citizens' data-protection safeguards in policy instead of law — has been struck down by the courts three times running.**

## Per-target verdict

| System | Highest tier | Adjudication | Basis |
|---|---|---|---|
| MoJ Data First | **None** | No legal challenge, ICO action, or court ruling | DPIA + Five Safes + identifier removal + panel oversight only |
| Splink | **None** | None | Open-source record-linkage tool built *for* Data First |
| ONS IDS / IDP | **None** (searched) | None | Highest adverse material is Tier 3 (PAC value-for-money; OSR/NSDEC recommendatory) |
| ADR UK | **None** | None | DEA 2017 + Five Safes + NSDEC. ICO has *endorsed* Five Safes |

## What WAS ruled unlawful — three times

The real adjudications are next door, in the Home Office's immigration data regime. They are not about linkage; they are about an *exemption* that strips migrants of the right to see and challenge their own data. But they matter, because they condemn precisely the move the linkage machinery relies on: keeping the safeguards out of the statute.

- **Round 1 — Court of Appeal, 26 May 2021.** *R (Open Rights Group & the3million) v SSHD* **[2021] EWCA Civ 800** — the DPA 2018 immigration exemption was unlawful, an "unauthorised derogation from the fundamental rights conferred by the GDPR," because the Article 23(2) safeguards were nowhere in the legislation. Relief suspended; government re-legislated (SI 2022/76).
- **Round 2 — High Court, 29 March 2023.** **[2023] EWHC 713 (Admin)** (Saini J) — the *revised* exemption was *still* unlawful: safeguards "must appear on the face of the legislation or in a binding code (approved by Parliament) and with statutory force."
- **Round 3 — Court of Appeal, 11 December 2023.** **[2023] EWCA Civ 1474** — confirmed the exemption still breached Article 23(2). This is the ruling the government's second fix answered.

**Where it stands now (2026):** the exemption is back in force in amended form. **SI 2024/342** — The Data Protection Act 2018 (Amendment of Schedule 2 Exemptions) Regulations 2024 — was made 7 March 2024 and came into force 8 March 2024, finally putting case-by-case decision-making, a necessity-and-proportionality test, and vulnerability and Convention-rights safeguards *on the face of the statute*. The successor statute, the **Data (Use and Access) Act 2025** (Royal Assent 19 June 2025), left the immigration exemption untouched. No fourth round of litigation found as of mid-2026.

## The line I will not cross

The immigration rulings are Tier-1 and unshakeable — but they are about an exemption from people's *own* data-subject rights, not about linking or sharing datasets. The defect struck down was procedural: safeguards belong in law, not policy. None of the three judgments discusses inter-departmental sharing, record linkage, or bulk matching.

So the fair claim is: **the same department, using the same trick of keeping safeguards out of the statute, was ruled unlawful three times.** The unfair claim — which I will not make — is that the courts have condemned government data-*linkage*. They have not. Accuracy is the weapon; an opponent who catches one overstatement discredits everything true beside it.

## The closest thing to a linkage adjudication (Tier 2)

On **26 March 2021** the Information Commissioner formally responded to the Cabinet Office's plan to expand the **National Fraud Initiative**'s data-matching purposes. The regulator warned, in writing, that the Cabinet Office "has not yet undertaken a DPIA" and should before any processing, that necessity and proportionality were not demonstrated, and that on-demand matching "could potentially allow participants to conduct disproportionate searches for information about particular individuals across a wide range of sources without lawful cause."

That is a regulator, on the record, warning that a government data-*matching* programme risks unlawful, disproportionate processing without a completed impact assessment — the single most on-point item in the whole investigation. But it is a consultation response, not enforcement. **No Tier-1 enforcement notice or court ruling on inter-departmental government data-matching was found.**

## Four items that look stronger than they are

- **Royal Free–DeepMind (ICO, 3 July 2017).** The ICO *found* the trust breached the DPA 1998 in sharing ~1.6 million patient records — but the remedy was a voluntary **undertaking**, not a fine or enforcement notice. Cite as "a finding via undertaking," never as a penalty.
- **Home Office visa-streaming algorithm (2020).** Withdrawn before any hearing after a JR by JCWI and Foxglove. **Tier 2** — a climbdown with no admission and no ruling. "Successful judicial review" is press shorthand.
- **DWP Universal Credit, [2020] EWCA Civ 778.** A real ruling against DWP — but on irrationality over salary-payment timing. Zero data-protection holding. Irrelevant to linkage.
- **Home Office GPS tagging of migrants (ICO, 1 March 2024).** A genuine Tier-1 enforcement notice and warning — but about surveillance and DPIA failure, not data-matching.

## What I could not close

1. Whether the Cabinet Office ever completed the DPIA the ICO demanded in 2021, and whether the ICO followed up once expanded matching went live.
2. Whether any Tier-1 action exists against the other big sharing regimes — DWP fraud matching, HMRC bulk sharing, Digital Economy Act 2017 powers — beyond the NFI consultation. Not searched to exhaustion.
3. The ICO enforcement register renders dynamically; the ONS "none found" rests on converging searches rather than a single authoritative query. An unreported or very recent filing cannot be fully excluded.

---

*Methodology: three independent research passes, ~300 adversarial verification agents, 99 sources, 75 claims verified, 4 killed for overreach. Every legislative fact confirmed verbatim against legislation.gov.uk; every court holding against the primary judgment or the National Archives caselaw record. Public sources only; no non-public system was accessed. Full source list and archival captures in [`sources/`](sources/) and [`screenshots/`](screenshots/).*
