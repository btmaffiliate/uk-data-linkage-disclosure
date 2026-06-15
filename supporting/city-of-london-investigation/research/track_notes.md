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
