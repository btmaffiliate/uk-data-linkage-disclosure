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
