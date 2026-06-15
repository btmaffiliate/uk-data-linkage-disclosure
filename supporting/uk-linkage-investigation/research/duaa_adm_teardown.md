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
