# Linked Without Consent: Probabilistic Matching, Policing, and Accountability in UK Public-Sector Data
## A Public-Interest Disclosure for Journalists

**Compiled:** 2026-06-10 · **Version:** 2.0 · Fully source-checked (0 dead links).

> **What this is, and is not.** A transparency record built only from **public, primary sources**, each
> verified live. **It alleges no illegality.** The processing described is, as far as the record shows,
> **lawful** — that is precisely the point: the UK lawfully links citizens' records **without their
> consent**, and in places feeds those links to **police**, with **no published accuracy figures and no
> stated remedy** for a wrong match. The argument here is democratic, not criminal: *is "lawful" enough?*
> Claims are status-graded; gaps are marked UNKNOWN and become FOI requests, never guesswork.
> **Verify the primary sources and take a media-law review before publishing.**

### Confidence labels
**CONFIRMED** (primary/official, read) · **LIKELY** (good secondary, or live page not fully readable
here) · **UNKNOWN** (no sourced answer → FOI) · **SPECULATION** (labelled hypothesis; never as fact).

---

## 1. The finding, in one paragraph
UK public bodies link individuals' administrative records **at scale and without consent** — lawfully,
under "public task" and law-enforcement powers, not consent. The Ministry of Justice's open-source
**Splink** tool performs this matching **probabilistically** (it returns *likely* matches, not certain
ones). The MoJ's own transparency record shows Splink used not only for research but **operationally**,
including a pilot that **sends police a daily list of probation clients' Police National Computer (PNC)
numbers** to flag arrests. The accompanying **Data Protection Impact Assessments exist but are not
published**; there is **no confirmed human check before each police share**; there is **no published
false-match rate**; and there is **no stated remedy** for a person wrongly matched. None of this is
unlawful. All of it is, at present, **un-scrutinised.**

## 2. Why "without consent" is lawful — and why that is the wrong place to stop
Consent is one of six lawful bases in UK GDPR, and for public authorities usually the **wrong** one —
the ICO tells them to rely on **public task (Art. 6(1)(e))**, not consent. The system is non-consensual
**by design**:
- **Justice:** public task + **DPA 2018 Part 3** (law-enforcement processing) — consent is never the basis.
- **Research/statistics:** the DPA 2018 Sch. 1 "research" condition (safeguards now at UK GDPR **Art. 84B**).
- **NHS:** **s. 251 NHS Act 2006** exists *specifically* to permit confidential patient data use **without
  consent**; the National Data Opt-Out is the mechanism that proves the baseline is non-consensual.
- **ONS Census → PDS:** statutory (SRSA 2007); census-statistics use is *excluded even from the opt-out*.

So "they linked it without consent" is not a scandal — it is the lawful design. **The real question is
what accompanies non-consensual linkage: an opt-out, clear notice, published safeguards, and — when it
touches police — accuracy and redress.** On the justice programmes, several of those are missing.

## 3. The police data flow — the highest-stakes part (CONFIRMED unless noted)
From the MoJ **"Splink Master Record" Algorithmic Transparency Record (published 6 Oct 2025)** *(A-S51)*:
- **Core Person Record** — real-time linkage building one identifier per person across prison, probation
  and courts (DELIUS, NOMIS, Common Platform, LIBRA, FamilyMan, CaseMan).
- **Probation in Court** — pulling an individual's probation record when they appear in court.
- **Police pilot (North Essex Probation)** — Splink identifies PNC numbers for supervised individuals and
  **sends them to police every day**.
- **Stated safeguard:** Splink **"does not directly make decisions about individuals"**; a **human makes
  the final decision** on candidate matches; **DPIAs were conducted for each use case.**
- **The gap (UNKNOWN):** the DPIAs are **not published**; it is **not stated** whether a human reviews
  **each daily police batch** before it is sent; there is **no published false-match rate**; there is **no
  described remedy** for a wrongful match; the controller and exact basis are not stated (likely **DPA
  Part 3** — *LIKELY, A-S52/53*).

> **Why this matters:** Splink is **probabilistic**. A wrong match in a research file is a bad statistic;
> a wrong match **feeding police daily** is a real person wrongly flagged. When probabilistic matching
> meets policing, the *absence* of published accuracy and redress stops being a paperwork point and
> becomes the core public-safety question. This is lawful — and, on the public record, unaccountable.

## 4. The wider linkage estate (context, CONFIRMED unless noted)
- **Data First** links seven cross-justice datasets incl. **OASys** (1,100+ vars, DV/sexual-offending),
  plus a **MoJ–DfE** education link. Its own transparency record says it is **research-only** — true *for
  Data First*; §3 shows Splink used operationally elsewhere. *(A-S06, A-S18, A-S19)*
- **BOLD** links justice data to **health & social care, HMRC Child Benefit and drug-treatment (NDTMS)**;
  basis Art. 6(1)(e)+9(2)(h); **no stated opt-out**. *(A-S22)*
- **NHS England Data Linkage Hub** (Splink on PDS) and **ONS Census 2021 → PDS** (assigns NHS numbers).
  *(A-S13, A-S14)*
- Access is de-identified, via the ONS Secure Research Service and SAIL Databank. *(A-S06, A-S30/31/33)*

## 5. The legal backdrop just shifted (CONFIRMED on primary text)
The **Data (Use and Access) Act 2025** (in force **5 Feb 2026**) replaced UK GDPR Art. 22 with Arts.
22A–22D: for ordinary data the bar on solely-automated significant decisions **relaxed** (special-category
data keeps a near-ban); it **loosened the Art. 14 duty to inform** people whose data was obtained
indirectly; and it lets the **Secretary of State define, by regulation,** what counts as "meaningful human
involvement." *(A-S42–A-S50)* — i.e. the rules on *automated decisions* and on *being told* were weakened
in the same period this linkage expanded. (Recorded as context; no targeting of these programmes is alleged.)

## 6. The City of London Corporation (parallel case)
- The **City of London Police** (national lead force for fraud) runs the **National Fraud Intelligence
  Bureau**, which **automatically links** the nation's fraud reports into police intelligence packages.
  **Action Fraud → Report Fraud (4 Dec 2025).** Its analytics **platform/vendor is undisclosed** (a
  "Palantir" claim circulated but is **unverified** — recorded UNKNOWN). *(B-S01; B-S03 live/unread)*
- Governance: a **business-vote franchise** unique in the UK; **City's Cash (~£2.3bn) sits outside FOI**;
  the **Remembrancer** lobbies Parliament from the Commons under-gallery. *(B-S02; B-S05/06 live/unread)*

## 7. The questions to put (UNKNOWN → FOI; allege nothing)
1. **Publish the DPIAs** for the Core Person Record and the probation→police PNC pilot.
2. For the PNC pilot: **is each daily share human-checked before it reaches police?** What is the
   **false-match rate**, and the **remedy** for a wrongly matched individual?
3. State the **lawful basis** (DPA Part 3?) and whether **any opt-out or objection** exists for Data First/BOLD.
4. How are linked individuals **informed** (Art. 14), and what changed under DUAA 2025?
5. **Name the analytics platform** behind the National Fraud Intelligence Bureau.
6. State **why City's Cash is outside FOI** and publish its accounts.

## 8. What this does NOT say
- It does **not** allege any unlawful processing, surveillance abuse, or corruption.
- It does **not** claim Palantir runs the fraud database — explicitly **UNKNOWN**.
- It does **not** connect Splink or DuckDB to the City of London — searched; **no evidence found**.
- It does **not** say non-consensual linkage is illegal — it is **lawful**; the issue is accountability.

## 9. Method & limits
All sources fetched and re-checked (0 dead). Statute verified against current legislation.gov.uk text.
**Limits:** several official PDFs (Data First privacy statement, MoJ–DfE notice, HMPPS/NPS notices) and
pages (`reportfraud.police.uk`, `cityoflondon.gov.uk`) resolve but **could not be read in full here** —
claims on them are **LIKELY**, not CONFIRMED. Compiled with AI assistance; **a human and a
media/data-protection lawyer should review before publication or transmission to officials.**

## 10. Source register (verified live 2026-06-10)
**Part A — linkage / police**
A-S01 Splink repo · A-S03 Splink IJPDS (ijpds.org/article/view/1794) · A-S06 Data First (ADR UK 2023-24) ·
A-S13 NHS Data Linkage Hub · A-S14 ONS Census→PDS · A-S18 gov.uk Data First · A-S19 Data First (Splink)
ATR · A-S22 BOLD privacy notice · **A-S51 Splink Master Record ATR (gov.uk, 6 Oct 2025)** ·
A-S52/53 HMPPS/NPS notices (live, unread) · A-S37 DPA 2018 Sch.1 · A-S42 DUAA 2025 (ukpga/2025/18) ·
A-S43–46 UK GDPR Arts. 22A–22D · A-S47 Art. 6(1)(ea) · A-S49 Annex 1 · A-S50 Art. 14 ·
A-S30/31 ONS SRS · A-S33 SAIL.
**Part B — City of London**
B-S01 NFIB (Wikipedia) · B-S02 City of London Corporation (Wikipedia) · B-S03 Report Fraud privacy
(reportfraud.police.uk) · B-S05 FOI (cityoflondon.gov.uk) · B-S06 Remembrancer's Office · B-S07 Business
vote · B-S09 "Streets paved with gold" (Bureau of Investigative Journalism, 2012).

_Full machine-readable registers, claims matrices, link-checker and ready-to-send FOI drafts are in the
working repositories `uk-linkage-investigation/` and `city-of-london-investigation/`._
