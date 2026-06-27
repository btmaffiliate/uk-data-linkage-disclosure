# Palantir: The Global Footprint — Everything They Operate On

*A verified, source-tagged catalog of Palantir Technologies' deployments, contracts, controversies, and the formal challenges against them. Every item is tagged **confirmed / reported / alleged** with a status (`operational`, `build-in-progress`, `pilot`, `evaluation`, `proposed`, `blocked`, `ended`, `alleged`) and a source. Contract values are "reported" unless tied to a primary procurement notice. Compiled from sixteen independently verified sector catalogs; verifier corrections applied throughout.*

---

## 1. Executive Summary

**The scale.** Palantir operates across at least **16 sectors and jurisdictions** spanning every US military service and multiple combatant commands, the US intelligence community, US immigration enforcement, US federal civilian and health agencies, a deep US/global commercial book, and government engagements in the UK, Germany, Israel, Ukraine, the Asia-Pacific, and the Gulf. Its products are a small, coherent stack — **Gotham** (intelligence/targeting/link-analysis), **Foundry** (data integration), **AIP** (the LLM/agentic layer atop Foundry), the **Maven Smart System (MSS)** (AI command-and-control/targeting), **TITAN** (a sensor ground-station hardware+software system), and **Apollo** (deployment) — rebranded locally wherever it lands (hessenDATA, VeRA, DAR, Skywise, Tiberius, ImmigrationOS, Aither, PRISMA, ShipOS).

**The concentration: government over commercial.** The largest, most consequential deals are public-sector and national-security: the US Army's **up to $10bn** 10-year enterprise agreement consolidating ~75 contracts; the MSS ceiling raised to **~$1.3bn**; NGA's **$646M** "Glacier Bay"; the CDC's **$443M** health "Common Operating Picture." Commercial deployments (Morgan Stanley, BP, Airbus, Stellantis, AIG, SOMPO, HD Hyundai) are real and expanding but **rarely disclose contract values** — their headline figures are business metrics, not procurement sums.

**The concentration: US over world.** The overwhelming majority of dollar value, deployments, and controversy sits in the **United States**. The non-US footprint is concentrated and contested: the **UK** (NHS, MoD, policing), **Germany** (state police Gotham), **Israel** (MoD/IDF), **Ukraine** (the war effort), and pockets in **APAC** (Japan, South Korea, Australia) and the **Gulf** (UAE). At the **federal level in Germany**, Palantir has *lost* (BfV chose France's ChapsVision; the BKA process was slowed).

**The honest through-line.** Palantir is, repeatedly, the **operational data/AI layer** of the state's most sensitive functions — targeting, deportation, intelligence linkage, public-health surveillance, border control — frequently procured **sole-source, non-competitively, or secretly (redacted contracts)**, by a **US national-security firm** with founder-controlled voting and political ties. That pattern — not any single contract — is what draws courts, regulators, parliaments, and divestment campaigns. The single most undismissable adjudicated fact is the German Federal Constitutional Court's 16 Feb 2023 ruling striking down the legal powers underpinning Palantir-based police data-mining. The most serious *allegations* — Gaza targeting via Lavender/Gospel, a US cross-agency "mega-database" — remain **alleged, not court-confirmed**, and Palantir denies them.

---

## 2. Master Table of Deployments

| Customer | Country | Product | Status | What's done | Reported value | Source(s) |
|---|---|---|---|---|---|---|
| DoD CDAO / combatant commands | US | Maven Smart System | operational (confirmed) | AI C2/targeting; 20,000+ users, 35+ tools | ~$1.3bn IDIQ ceiling thru 2029 (reported) | DefenseScoop |
| US Marine Corps | US | MSS enterprise license | operational (confirmed) | Proliferate MSS across Fleet Marine Force | undisclosed | DefenseScoop |
| US Army (DoD-wide) | US | Enterprise Service Agreement (Foundry/Gotham/AIP/MSS) | operational (confirmed) | Consolidates ~75 contracts | up to **$10bn**/10yr ceiling (reported) | army.mil; CNBC |
| US Army | US | Vantage / Army Data Platform | operational (confirmed) | Central data OS, 100,000+ users | $458M (2019) + ~$400.7M ($618.9M ceiling) follow-on Dec 2024 (reported) | Defense News |
| US Army | US | TITAN ground station | operational (confirmed) | Deep-sensing AI targeting; first 2 delivered Mar 2025 | $178.4M OTA Mar 2024 (primary/reported) | DefenseScoop |
| US Navy | US | Foundry+AIP "ShipOS" | operational (confirmed) | Shipbuilding supply-chain | up to $448M, Dec 2025 (reported) | USNI; Business Wire |
| USSOCOM | US | Mission Command System | operational (confirmed) | SOF C2/COP; lead software integrator | $111M (2021) + $36.8M (Dec 2024) | Business Wire |
| NGA | US | "Glacier Bay" (Foundry/Gotham/AIP inferred) | operational (confirmed) | Geospatial-intel (scope undisclosed) | **$646M** FFP, Sep 2025 (primary) | NGA |
| NGA | US | Platform Licenses | operational (confirmed) | AI data/analytics | $28.3M, May 2025 (primary) | NGA |
| US Space Force | US | Foundry space data backbone | operational (confirmed) | Common operating picture of space | $10M OTA (2021); follow-on undisclosed | FedScoop |
| NORTHCOM/NORAD | US | MSS + Vantage integration | operational (confirmed) | Homeland/border-defense picture | under MSS/Army EA ceilings | ExecutiveGov |
| Israel MoD / IDF | Israel | AIP / data-analytics (alleged targeting) | **alleged** | Battle-mgmt/logistics; alleged Gaza targeting | "tens of millions" (reported) | Bloomberg; Globes; UN A/HRC/59/23 |
| ICE (HSI) | US | Gotham (ICM) | operational (confirmed) | Core investigative case management since 2014 | ~$139.3M ICM; $145M = combined ICM+ImmigrationOS (reported) | ACLU; EFF; EPIC |
| ICE | US | FALCON | operational (confirmed) | Analytic surveillance database | undisclosed | EPIC |
| ICE | US | ImmigrationOS | **build-in-progress** (confirmed contract) | Lifecycle deportation platform | $30M sole-source Apr 2025; FOC targeted Sep 2027 | Axios; Amer. Immigration Council |
| ICE | US | ELITE targeting app | **alleged** | Deportation-target mapping; alleged Medicaid data | no separate value | Fortune; 404 Media |
| IRS / DHS | US | master "mega-database" (product unnamed) | **alleged** | Aggregate/link taxpayer data | $130M+ since 2018 (reported) | The Intercept; GovExec |
| CMS ↔ ICE | US | Medicaid data-sharing (not a Palantir contract) | **blocked** (partial) | ~79M enrollees; ELITE alleged to tap | n/a | KFF; NBC |
| CIA / In-Q-Tel | US | Gotham (co-developed) | operational (confirmed) | Alpha customer ~2005–08 | ~$2M In-Q-Tel investment (reported) | BuzzFeed; Wikipedia |
| FBI | US | Gotham | operational (confirmed) | Link analysis (reluctant customer) | undisclosed | Wikipedia; BuzzFeed |
| NSA / Five Eyes (GCHQ) | US/UK | XKEYSCORE Helper / "TWO FACE" | **alleged** | Leaked-doc integration; NSA pilot-only, ended ~2015 | n/a | The Intercept; BuzzFeed |
| DIA | US | Gotham (bid protest) | **dismissed/ended** | Protest over in-house MARS; **dismissed 2026-06-03** | no award | Axios |
| US Army (DCGS-A) | US | Gotham (litigation) | operational (confirmed) | Won CoFC 2016, Fed. Cir. 2018; 2019 Army deal | ~$876M/10yr (reported) | Defense News; FindLaw |
| CDC | US | Foundry "Common Operating Picture" | operational (confirmed) | Consolidates HHS Protect/Tiberius/DCIPHER/ASPR | **$443M**/5yr, Dec 2022 (reported) | FedScoop; PRNewswire |
| HHS (HHS Protect) | US | Gotham license / platform | **ended** | COVID hospital tracking | ~$24.9M no-bid ($7.5M primary) | FedScoop; USAspending |
| HHS (Tiberius) | US | Foundry | **ended** | Vaccine allocation | ~$17M→$31M (reported) | FedScoop |
| NIH (N3C) | US | Foundry enclave | operational (confirmed) | COVID data enclave | $36M sole-source, Sep 2020 (reported) | FedScoop |
| FDA (CDER/OCE) | US | Foundry | operational (confirmed) | Drug-review analytics | $44.4M/3yr, Dec 2020 (reported) | FedScoop |
| IRS | US | Foundry+Gotham (Lead & Case Analytics) | operational (confirmed); mega-DB **alleged** | Fraud/financial-crime analytics | $130M+ since 2018 (reported) | The Intercept |
| Cross-agency "master database" | US | Foundry | **alleged** | EO data-linkage (Palantir denies) | ~$113M new awards since Jan 2025 (reported) | NYT (via New Republic); Palantir blog |
| USDA (attendance) | US | Foundry | operational (confirmed) — **USDA only** | Badge-in occupancy tracking | $3.9M initial / $13.3M potential (reported) | American Prospect |
| VA, SSA (attendance) | US | Foundry | **sought/planned** | Similar programs sought | n/a | American Prospect |
| Dept of Education | US | Foundry (subcontractor) | operational, reported | Foreign-funding portal | $9.8M obligated / up to $61.8M (reported) | FedScoop |
| CMS (provider directory) | US | Foundry prototype | **pilot** | $1 proof-of-concept (1 of 4) | $1, Sep–Nov 2025 (reported) | FedScoop |
| Morgan Stanley | US | Foundry | operational (medium conf.) | "Single Client View" wealth platform | undisclosed | Palantir; Seeking Alpha |
| AIG (Syndicate 2479; McGill) | US/UK | Foundry+AIP (w/ Anthropic) | operational (confirmed) | Agentic underwriting ontology | $300M premium; up to 25% of $1.6B GWP (reported) | Palantir IR; Insurance Journal |
| BP | UK/global | Foundry+AIP | operational (confirmed) | Digital twin, 2M+ sensors | +20,000 bbl/day (reported metric) | Rigzone; World Oil |
| Azule Energy | Angola | Foundry | operational (confirmed) | Upstream optimization | undisclosed | Rigzone; JPT/SPE |
| Stellantis | Multinational | Foundry+AIP | operational (confirmed) | Renewed to 2031 | undisclosed | BusinessWire |
| Airbus (Skywise) | France | Foundry | operational (confirmed) | Aviation data platform, 50k+ users | undisclosed | BusinessWire |
| Ferrari (Scuderia) | Italy | Foundry | operational (confirmed) | F1 race-ops data | undisclosed | BusinessWire |
| Cleveland Clinic | US | Foundry | operational (confirmed) | Virtual Command Center | undisclosed | PR Newswire |
| Tampa General | US | Foundry+AIP | operational (confirmed) | CareComm; ~600 lives (reported) | undisclosed | Healthcare IT News |
| Merck; Sanofi | US/France | Foundry | operational (medium conf.) | Drug discovery; RWE | undisclosed | pharmaphorum |
| Parexel | US | Foundry+AIP | operational (confirmed) | Clinical-trial data | undisclosed | Parexel |
| United Airlines; Wendy's QSCC; Option Care Health | US | AIP | operational (confirmed) | AIPCon/JPM24 customers | undisclosed | BusinessWire; Fierce |
| NHS England (FDP) | UK | Foundry+AIP | operational (confirmed); legal challenge | National data platform | up to £330m envelope; **£182.2m** published CAN (reported/primary) | Digital Health; Foxglove |
| NHS England (COVID Data Store) | UK | Foundry | **ended** | Pandemic data store | £1→~£23.5m (reported) | CNBC; Digital Health |
| UK MoD (follow-on EA) | UK | Foundry | operational (confirmed) | Enterprise data analytics | **£240.6m** ex-VAT (primary, Find a Tender 083874-2025) | The Register; Find a Tender |
| UK MoD (original EA) | UK | Foundry | **ended** | Superseded by 2026 EA | £75.2m (reported) | PR Newswire |
| UK MoD (Strategic Partnership) | UK | AI/targeting ("kill chain") | operational (confirmed) | London = European defence HQ | up to £750m opportunity envelope (reported) | GOV.UK |
| Cabinet Office (Border Flow) | UK | Foundry | operational (confirmed) | Post-Brexit customs data | ~£27m, no tender (reported) | Computing; openDemocracy |
| DLUHC/MHCLG (Homes for Ukraine) | UK | Foundry CMS | operational (confirmed) | Refugee case management | ~£10m total (reported) | NAO; UKAuthority |
| Home Office/NPCC (NFLMS firearms) | UK | Palantir (product unnamed) | operational (confirmed) | National firearms/explosives licensing, 43 forces | ~£9m, up to 10yr (primary, Find a Tender 051257-2026) | The Register; PublicTechnology |
| Met Police (UDP Phase 1) | UK | Palantir (Foundry-based, reported) | **pilot** | Officer anti-misconduct profiling | ~£489,999 (reported) | The Nerve |
| Met Police (UOA) | UK | Unified Operational Analytics | **blocked** | Force-wide intel automation | up to ~£50m (reported) | Local Govt Lawyer; The Register |
| Met Police (interim) | UK | Palantir | operational (medium conf.) | 12-month pilot extension | **value not disclosed** | ITV; Police Professional |
| Bedfordshire Police ("Project Nectar") | UK | Foundry | **pilot** | Unified intel view, ~80 sources | Home Office-funded; value undisclosed | Liberty Investigates |
| EMSOU / Leicestershire | UK | Foundry ("NECTAR–EMSOU") | **pilot** | 5-force serious/organised crime | £818,750 (reported) | ROCU; Contract Finder Pro |
| Hesse Police | Germany | Gotham ("hessenDATA") | operational (confirmed) | Cross-DB analysis since 2017 | undisclosed | BVerfG; heise |
| Hamburg Police | Germany | Gotham (§49 HmbPolDVG) | **blocked** (void) | Never deployed; struck down | n/a | BVerfG |
| NRW Police | Germany | Gotham ("DAR") | operational (confirmed) | Cross-DB analysis since 2022 | undisclosed | heise; LDI NRW |
| Bavaria Police | Germany | Gotham ("VeRA") | operational (confirmed); complaint pending | Cross-procedure analysis | €25m framework, 2022 (reported) | heise; GFF |
| Baden-Württemberg Police | Germany | Gotham (via VeRA framework) | **proposed** | Pending live ~2026 | ~€25m, Mar 2025 (reported) | heise |
| BfV (domestic intel) | Germany | Gotham/AIP (considered) | **ended** (rejected) | Chose ChapsVision instead | n/a | Cybernews; heise |
| Ukraine AF (targeting) | Ukraine | Gotham + MetaConstellation | operational (reported/CEO) | Battlefield targeting fusion | free (early); undisclosed | TIME; EurasiaReview |
| HUR/GUR | Ukraine | PRISMA | operational (**reported**, CNN) | Deep-strike drone planning | undisclosed | CNN (via UNITED24) |
| Prosecutor General (Ukraine) | Ukraine | Palantir platform (UK Ltd) | operational (confirmed) | War-crimes evidence, 78,000+ cases | no fee | BusinessWire; FedScoop |
| Min. of Economy (Ukraine) | Ukraine | **AIP** | operational (confirmed) | Demining prioritization | undisclosed | BusinessWire |
| Min. of Digital Transformation | Ukraine | Foundry | operational (confirmed) | Reconstruction/damage | undisclosed | BusinessWire |
| Min. of Education (Ukraine) | Ukraine | Foundry | operational (confirmed) | School-safety data (2024 release) | 12-month agreement | BusinessWire |
| SOMPO Holdings | Japan | Foundry+AIP | operational (confirmed) | Senior-care + insurance, ~8,000 users | $22.5M (2021); $50M (2023); expansions (reported) | BusinessWire; Palantir |
| HD Hyundai | South Korea | Foundry+AIP | operational (confirmed) | Smart shipyard | $45M/5yr; "hundreds of millions" 2026 projection (reported) | BusinessWire; Barchart |
| Australian Defence (IIC) | Australia | Foundry | operational (medium conf.) | Supply-chain/vendor vetting | A$7.1M, 2024 (reported; "embedded" disputed by Defence) | Crikey |
| Australian Defence (Cyber/EW) | Australia | Palantir (unnamed) | operational (medium conf.) | ICT data-integration platform | A$7.6M, ~Feb 2026, sole-source (reported) | Crikey; Defence Connect |
| AUSTRAC | Australia | Palantir (unnamed) | operational (medium conf.) | AML transaction reporting | A$5.06M; >A$28M total (reported) | Canberra Times |
| ACIC | Australia | Gotham | operational (medium conf.) | ~42M data-point linkage | ~A$5.7M (reported) | Crikey |
| NZDF | New Zealand | Gotham | operational (medium conf.) | Planning; ~100 trained | ~NZ$7.2M 2012–18 (reported) | Ombudsman; Exit From AFFCO |
| NZ Police | New Zealand | Palantir (unnamed) | **ended** | Christchurch trial; cost | trial ended Dec 2019 | Exit From AFFCO |
| Dubai Holding (Aither JV) | UAE | "AI/data platforms" (Foundry/AIP inferred) | operational (confirmed deal) | Real estate/hospitality/finance | undisclosed (split & value not disclosed) | Palantir IR; Dubai Holding; AGBI |
| AppliedAI | UAE | **equity stake only** (not a deployment) | operational (equity) | Palantir is investor (w/ G42, Mubadala) | $55M Series A (G42-led, **Feb 2025**); Pre-Series B Jan 2026 undisclosed (reported) | Zawya; Wamda |
| Qatar NCSA | Qatar | Palantir (unnamed) | **ended** | 2022 World Cup recognition; role undisclosed | n/a | Gulf Times |

---

## 3. Sections by Sector / Jurisdiction (the 16)

### 3.1 US Department of Defense / Military

Palantir is the Pentagon's dominant battlefield-AI/data vendor, spanning every service and multiple combatant commands.

- **Maven Smart System (CDAO)** — `operational`. AI C2/targeting; 20,000+ users across 35+ tools; commands include CENTCOM, EUCOM, INDOPACOM, NORTHCOM/NORAD, TRANSCOM. Original $480M IDIQ (May 2024) raised +$795M to **~$1.3bn** through 2029 (May 2025). Embedded Anthropic's Claude (AIP/AWS at IL6) until DoD ordered Anthropic phased out. *Controversy:* MSS (with Claude) reportedly helped select ~1,000 Iranian strike targets in the first 24 hours (Washington Post-sourced — **reported, not adjudicated**); broadly **alleged** to enable Israeli Gaza targeting (UN "reasonable grounds" — **not court-confirmed**); DoD designated **Anthropic a supply-chain risk (4 Mar 2026)**, forcing Claude's removal within 180 days. *Litigation wrinkle:* a federal judge initially blocked most of the FASCSA designation as punitive; the D.C. Circuit later denied Anthropic's stay, so it remained in effect for covered systems.
- **Marine Corps MSS** — `operational`. Enterprise license (Aug 2025); **value undisclosed**. Inherits MSS targeting allegations.
- **Army Enterprise Service Agreement** — `operational`. Consolidates ~75 contracts (15 prime + 60 related); **up to $10bn**/10yr ceiling (maximum, not obligation). *Controversy:* criticized as vendor lock-in / data concentration (SEC shareholder filings); not adjudicated.
- **Army Vantage / Army Data Platform** — `operational`. $458M (2019) + ~$400.7M follow-on ($618.9M ceiling, Dec 2024); 100,000+ users; integrated with NORTHCOM MSS for border/homeland defense (civil-liberties concerns, not adjudicated).
- **TITAN** — `operational`. $178.4M Phase 3 OTA (Mar 2024, beat RTX/Raytheon); first two delivered 7 Mar 2025. Notable hardware win for a software firm.
- **Navy ShipOS (Foundry+AIP)** — `operational`. Up to $448M (Dec 2025); 2 shipbuilders, 3 shipyards, 100 suppliers.
- **SOCOM Mission Command System** — `operational`. $111M (2021) + $36.8M (Dec 2024).
- **NGA "Glacier Bay"** — `operational`. **$646M** FFP (26 Sep 2025, primary NGA notice); scope undisclosed, product inferred. A separate NGA award drew a protest NGA fended off via new defense law.
- **NGA Platform Licenses** — `operational`. $28.3M (May 2025, primary).
- **Space Force Foundry** — `operational`. $10M OTA (2021); follow-on SSC modification value/date undisclosed.
- **NORTHCOM/NORAD** — `operational`. MSS + Vantage + Pathfinder fusion for homeland/border defense.

### 3.2 Israel / IDF

- **Israel MoD / IDF** — `alleged` (partnership operational; targeting alleged). Strategic partnership signed **12–13 Jan 2024** (board met in Tel Aviv during the Gaza war). Reported remit per Globes/Calcalist: **logistics/manpower + battle-management/decision-support**, "tens of millions of dollars" (reported). **Unit 8200 (SIGINT) and Shin Bet declined** Palantir's intelligence offering after evaluation — tagged `blocked`. The most serious claims — that Palantir powers **Lavender, Gospel, and "Where's Daddy?"** — appear in UN Special Rapporteur **Francesca Albanese's report A/HRC/59/23** ("reasonable grounds," ~1 July 2025). **CRITICAL DISTINCTION:** Lavender/Gospel/Where's Daddy are **IDF-attributed systems** (+972/Local Call/Guardian), **NOT proven Palantir products**. Palantir **denies** involvement with Lavender, says those capabilities pre-date and are independent of its MoD partnership. CEO Karp's "mostly terrorists" remark (~30 Apr 2025) is widely circulated; **not adjudicated**. *Divestment:* Storebrand sold ~$24m (Oct 2024); Norges Bank backed a human-rights vote. **No court or regulator has adjudicated the targeting allegations.**

### 3.3 US Intelligence Community

- **CIA / In-Q-Tel** — `operational`. In-Q-Tel invested **~$2M (~2004)** (figure supported by **Wikipedia/BuzzFeed**, not Fortune); CIA was sole/alpha customer ~2005–08; co-developed Gotham (released 2008). "Signature client"; relationship soured post-2013 Forbes piece but persisted because the software was hard to replace.
- **FBI** — `operational`. Gotham link analysis; reluctant customer (ranking declined FY17–21).
- **NSA / Five Eyes (GCHQ)** — `alleged`. Snowden/Intercept docs: "XKEYSCORE Helper" and GCHQ's "TWO FACE" (2010–11). BuzzFeed: NSA was **pilot-only, relationship ended ~2015**. Based on leaked classified material; not court-confirmed.
- **DIA (MARS)** — `dismissed/ended`. Bid protest over in-house MARS; **protest DISMISSED 2026-06-03** (solicitation 47QFCA26R0023). Not a deployment.
- **Army DCGS-A litigation** — `operational` (adjudicated). Palantir sued (30 Jun 2016); **Court of Federal Claims ruled (31 Oct 2016)** the Army violated FASA by failing to consider commercial COTS; **affirmed by the Federal Circuit (2018)**. Landmark COTS-vs-build precedent; won a major Army deal in 2019 (~$876M/10yr, reported).
- *Dropped as unsourceable:* NCTC, ODNI as named Gotham customers.

### 3.4 US Immigration & Border Enforcement

Palantir is, by reported accounts, **ICE's largest data/analytics contractor**.

- **ICE Investigative Case Management (Gotham)** — `operational`. Core investigative platform since 2014; current ICM ~$139.3M (2022, expiring Apr 2026, slated sole-source renewal). **Note:** the ACLU-cited "**over $145M**" is a **combined ICM + ImmigrationOS figure** running to Sep 2027, *not* a standalone ICM value.
- **ICE FALCON** — `operational`. Analytic surveillance DB (phone, GPS, financial, ISP, social-network). Subject of EPIC FOIA litigation, **settled 31 Jan 2020**.
- **ICE ImmigrationOS** — **`build-in-progress`** (confirmed contract). $30M sole-source ("urgent and compelling," Apr 2025); prototype due 25 Sep 2025; **full operational capability targeted Sep 2027** — *not yet operational.* Reported $29.9M Sep 2025 maintenance task order. Aggregate 2025 ICE-Palantir value reported ~$287M; 2011–2026 ~$435M (reported, not single primary notice).
- **ICE ELITE** — `alleged`. Targeting app with dossiers + "address confidence scores"; alleged to ingest HHS/Medicaid data. Neither ICE nor Palantir confirmed; Just Futures Law filed a FOIA suit (reported 4 Jun 2026).
- **IRS "mega-database"** — `alleged`. Reported to lead an IRS effort to link taxpayer data; **the cited GovExec source does NOT name "Foundry"** and frames it as a **separate** Palantir IRS master-database effort, distinct from the IRS-to-DHS data-sharing plan. Reported, not court-confirmed.
- **CMS ↔ ICE Medicaid data-sharing** — **`blocked` (partial)**. July 2025 agreement (~79M enrollees); after 22 states sued, a federal judge (Chhabria) **enjoined most of it**, allowing only six "basic" data categories. Not a Palantir procurement; the data ELITE is alleged to tap.

### 3.5 US Federal Civilian & Health

- **CDC "Common Operating Picture"** — `operational`. **$443M**/5yr (Dec 2022); consolidates HHS Protect, Tiberius, DCIPHER, ASPR Engage; expanded to mpox/RSV.
- **HHS Protect** — `ended`. ~$24.9M no-bid ($17.4M Gotham license + $7.5M platform services, primary on USAspending); "unusual and compelling urgency."
- **Tiberius** — `ended`. Foundry vaccine allocation; ~$17M→$31M.
- **NIH N3C** — `operational`. $36M sole-source Foundry enclave (Sep 2020).
- **FDA (CDER/OCE)** — `operational`. $44.4M Foundry drug-review platform (Dec 2020).
- **IRS Lead & Case Analytics** — `operational`; mega-DB `alleged`. $130M+ since 2018. **June 17 2025** congressional letter (Wyden/Ocasio-Cortez/Markey) alleging Privacy Act + IRC §6103/§7213A violations — **allegation, not court-confirmed**.
- **Cross-agency "master database"** — `alleged`. NYT (30 May 2025) reported Palantir tapped to execute the 20 Mar 2025 EO linking SSA/immigration/tax data; **Palantir denied building a "master database," calling the NYT report "blatantly untrue."**
- **USDA attendance tool** — `operational` (**USDA only**); **VA & SSA `sought/planned`**, not operational. $3.9M initial / $13.3M potential, no-bid.
- **Dept of Education** — operational (reported). Foreign-funding portal subcontractor; $9.8M / up to $61.8M; Palantir not in federal spending records (surfaced via login-page logo).
- **CMS provider directory** — `pilot`. $1 prototype (1 of 4 firms).
- **NIH NCATS LLM4DMS** — `evaluation`. $375K (single-sourced/reported).

### 3.6 US & Global Commercial Customers

*(Values are business metrics, not procurement sums. No commercial deployment here has a court/regulator adjudication. **The Lowe's/General Mills/OpenAI "AIP users" entry has been DROPPED** — the cited AIPCon source does not name any of the three.)*

- **Finance:** Morgan Stanley (Foundry "Single Client View"; *unsourced "internally challenged" framing removed*); **AIG** (Foundry+AIP with Anthropic — Lloyd's Syndicate 2479 [$300M premium, live 1 Jan 2026], McGill follow-underwriting [up to 25% of $1.6B GWP]).
- **Energy/oil:** BP (Foundry since 2014, AIP added Sep 2024; digital twin, 2M+ sensors, +20,000 bbl/day reported); Azule Energy (Angola, ~200k bbl/day).
- **Manufacturing/auto/aerospace:** Stellantis (since 2016, renewed to 2031, AIP added); Airbus Skywise (since 2015, renewed Feb 2026, 50k+ users); Scuderia Ferrari (Foundry, since 2016/22).
- **Healthcare systems:** Cleveland Clinic (Virtual Command Center); Tampa General (CareComm, Foundry+AIP, ~600 lives reported); Option Care Health (AIP).
- **Pharma/CRO:** Merck, Sanofi (Foundry); Parexel (Foundry+AIP, first CRO).
- **AIP 2024 cohort:** United Airlines, Wendy's QSCC (use cases not detailed).

### 3.7 UK Central Government

- **NHS Federated Data Platform (Foundry+AIP)** — `operational`; legal challenge. Awarded Nov 2023; **up to £330m envelope, £182.2m published CAN** (to Feb 2027); live Mar 2024; **break clause Mar 2027**, government review underway. Foxglove/Just Treatment legal challenge over lawful basis/opt-outs — **not court-confirmed**; heavily redacted contract; data-sovereignty concerns.
- **NHS COVID-19 Data Store (Foundry)** — `ended`. £1 trial → ~£23.5m (2020–22); contracts released hours before openDemocracy/Foxglove proceedings.
- **MoD follow-on EA (Foundry)** — `operational`. **£240.6m ex-VAT (PRIMARY — Find a Tender 083874-2025)**, signed 30 Dec 2025, live 1 Apr 2026, **direct-awarded under Procurement Act 2023 s.41**; ~3x the prior £75.2m deal. openDemocracy: four ex-MoD officials hired before the win ("revolving door," reported, not wrongdoing).
- **MoD original EA** — `ended`. £75.2m (Dec 2022), superseded.
- **UK–Palantir Strategic Partnership** — `operational`. Up to **£750m identified opportunity envelope** over 5 years (not a single committed procurement); up to £1.5bn Palantir investment; London = European defence HQ; AI decision-support + targeting/"kill chain." Signed 18 Sep 2025 (GOV.UK, primary).
- **Cabinet Office Border Flow (Foundry)** — `operational`. ~£27m (Aug 2020, no tender); openDemocracy: deal followed a Sawers→Manzoni introduction.
- **DLUHC/MHCLG Homes for Ukraine (Foundry CMS)** — `operational`. Free 6 months → ~£10m total; NAO/PAC scrutiny (testing skipped).
- **Home Office/NPCC NFLMS firearms** — `operational`. ~£9m (PRIMARY — Find a Tender 051257-2026), up to 10yr, begins Sep 2026; beat Accenture & NEC.
- **Cross-government aggregate** — `low` confidence. "At least £670m" across UK govt (CAAT/journalistic estimate, not a single notice).

### 3.8 UK Policing

- **Met UDP Phase 1** — `pilot`. ~£489,999 (kept just below the £500k MOPAC scrutiny threshold); officer anti-misconduct profiling (sickness, overtime, geolocation); ~98 officers assessed, ~500 prevention notices. Met Police Federation called geolocation tracking an "outrageous… invasion of privacy."
- **Met Unified Operational Analytics (UOA)** — `blocked`. Up to ~£50m (£25.3m + £24.8m optional); **blocked 20 May 2026** by Deputy Mayor Comer-Schwartz on procurement-rules grounds (single supplier, no approved strategy, VFM), City Hall also citing Palantir's Israeli-military and US-ICE work. Palantir sent a pre-action letter; CEO Mosley called it politicised.
- **Met interim extension** — `operational` (medium conf.). 12-month pilot extension (~24–25 Jun 2026 U-turn); **value not disclosed by any located source** (Met called it "commercially sensitive" — *the "~£2m" figure has been dropped as unsourced*). Sources tie the extension to the existing misconduct pilot, not a revived UOA capability.
- **Bedfordshire "Project Nectar" (Foundry)** — `pilot`. Up to ~80 data sources; 11 special-category data types; ICO noted compliance duty.
- **EMSOU/Leicestershire "NECTAR–EMSOU" (Foundry)** — `pilot`. **£818,750** (Oct 2024–Sep 2025), Home Office-funded, reported no-bid; FOI refused.
- **NFLMS firearms** — `operational` (see §3.7). Competitively procured; SITC called Palantir reliance an "unacceptable point of weakness."

### 3.9 Germany — Police Gotham

- **Hesse "hessenDATA" (Gotham)** — `operational`. Live since 2017; ~14,000–15,000 queries/yr; **§25a HSOG ruled incompatible (BVerfG 16 Feb 2023), allowed until 30 Sep 2023**. *Note:* the ruling discusses **"hessenDATA"**; the Court did **not name "Palantir"** in the dispositive.
- **Hamburg (Gotham)** — `blocked` (void). §49 HmbPolDVG **declared void (nichtig)** — never deployed.
- **NRW "DAR" (Gotham)** — `operational`. Live since spring 2022. *Early "data-mining" criticism is under-sourced and should read "reported"; the "DAR" name itself is reported-not-confirmed in the cited LDI source.*
- **Bavaria "VeRA" (Gotham)** — `operational`; complaint pending. €25m framework (2022, buy-in-without-procurement); live ~25 Dec 2024; used ~100 times Sep 2024–mid-2025 (20+ beyond serious threats — bicycle theft, ATM burglaries). **GFF + CCC filed a constitutional complaint 23 Jul 2025** (Art. 61a BayPAG); pending.
- **Baden-Württemberg (via VeRA framework)** — `proposed`. ~€25m (Mar 2025), live ~2026; reported "no exit clause"/Palantir staff at the data centre (single-source). *The "via Bavaria VeRA framework" linkage is reported-not-confirmed.*
- **BfV (domestic intel)** — `ended` (rejected). Chose France's **ChapsVision (ArgonOS)** over Palantir; federal **BKA process slowed** ("Phantom Palantir"). Palantir has **NOT won the German federal level.**

### 3.10 Ukraine

*(Much early support was reportedly free; values largely undisclosed.)*

- **Entry / Karp Kyiv visit** — `operational`. Jun 2022; office opened; framework for later MoUs.
- **Battlefield targeting (Gotham + MetaConstellation)** — `operational` (reported/CEO-attributed). Karp: Palantir "responsible for most of the targeting in Ukraine." Fuses drone/satellite/intercept + civilian "e-Enemy" app data; MetaConstellation tasks satellite swarms.
- **HUR/GUR PRISMA** — `operational` (**reported, CNN** — Nick Paton Walsh, 31 May 2026). Deep-strike drone planning into Russia; **no Palantir release confirms PRISMA.**
- **Prosecutor General (Palantir UK Ltd)** — `operational`. War-crimes evidence for 78,000+ registered cases; no fee.
- **Min. of Economy demining (AIP)** — `operational`. *Product is **AIP** per the primary release, not "Foundry-based."* Prioritizes clearance; coordinates HALO Trust (HALO direct-contract link undocumented).
- **Min. of Digital Transformation (Foundry)** — `operational`. Reconstruction/damage cataloguing (25 May 2023).
- **Min. of Education (Foundry)** — `operational`. School-safety data; **standalone release dated 2024-03-28** (12-month agreement) — *not "secondary-only/2023" as previously framed.*
- **Brave1 / 2026 expansion** — `proposed`. Zelenskyy-Fedorov-Karp joint "data centre" (~12 May 2026); binding status unclear. (CSIS/RAND/UK-MoD "joining" unconfirmed.)
- **Data-security concern** — `alleged`. Analysts cite a 2024 Swiss audit (CLOUD Act access risk → Switzerland discontinued Palantir); no Ukraine-specific breach adjudicated.

### 3.11 Asia-Pacific

- **SOMPO Holdings (Japan, Foundry+AIP)** — `operational`. ~8,000 users across ~300 senior-care facilities + insurance/AI underwriting. $22.5M (2020/21), $50M (2023), Aug 2025 expansion (reported).
- **HD Hyundai (South Korea, Foundry+AIP)** — `operational`. Smart shipyard; $45M/5yr; Jan 2026 expansion projected at "hundreds of millions" (company projection).
- **Australian Defence IIC (Foundry)** — `operational` (medium). A$7.1M (2024); Crikey "embedded staff" claim **disputed by Defence** (field-service reps).
- **Australian Defence Cyber/EW** — `operational` (medium). A$7.6M, ~Feb 2026, **sole-source**; largest single Defence Palantir contract.
- **AUSTRAC** — `operational` (medium). A$5.06M; largest tech supplier (>A$28M); "not competitive at all."
- **ACIC (Gotham)** — `operational` (medium). ~42M data-point linkage; federal Palantir **equity stake** (>A$160M reported).
- **NZDF (Gotham)** — `operational` (medium). ~100 trained; ~NZ$7.2M (2012–18, single-source). Ombudsman case 449159; NZ govt "no plans" to expand (Apr 2026).
- **NZ Police** — `ended`. Christchurch trial ended Dec 2019 (cost).
- *Undocumented/dropped:* **Singapore** (no government deployment found); **Centene** (US, out of APAC scope).

### 3.12 Middle East & Gulf

- **Dubai Holding / Aither JV** — `operational` (deal confirmed). First UAE JV (signed 31 Oct 2025, announced 4 Nov 2025); ~18 months prior Foundry/AIP across real estate/hospitality/finance (Nakheel, Meraas, Jumeirah; 53 hotels, ~60 accountant roles freed). **Ownership split and value NOT disclosed.** *Product (Foundry/AIP) is **inferred** — primary releases say only "AI and data integration platforms."* D33 AED 100bn is a government-program figure, not a contract value.
- **AppliedAI** — **equity stake only** (NOT a deployment). Palantir is an investor (w/ G42, Mubadala). **$55M = the 11 Feb 2025 G42-led Series A**; a separate Jan 2026 Pre-Series B amount is undisclosed.
- **Israel MoD/IDF** — see §3.2.
- **Qatar NCSA** — `ended`. 2022 World Cup recognition list; role undisclosed; low confidence.
- *Dropped:* Saudi Arabia (Oracle sovereign-cloud availability ≠ customer), Bahrain, Kuwait, Oman — no documented deployments.

---

## 4. Where It Has Been Challenged

### Court rulings (court-confirmed)

| Forum | Date | Outcome |
|---|---|---|
| **German Federal Constitutional Court (BVerfG)** — 1 BvR 1547/19 (Hesse), 1 BvR 2634/20 (Hamburg) | **16 Feb 2023** | **THE STANDOUT.** Struck down automated-data-analysis powers (§25a HSOG; §49 HmbPolDVG) as violating informational self-determination. Hamburg **void**; Hesse incompatible, allowed until 30 Sep 2023. |
| US Court of Federal Claims / Federal Circuit (Palantir USG v. United States, DCGS-A) | 2016 / **2018** | Palantir **won**: Army violated FASA by failing to consider commercial COTS. Landmark. |

### Pending court challenges

- **Bavaria VeRA** constitutional complaint (GFF + CCC, 23 Jul 2025) — pending at BVerfG.
- **NRW DAR** constitutional complaint (GFF) — pending (reported).
- **Foxglove/Just Treatment v. NHS England** (FDP lawful basis) — legal challenge ongoing, partial de-redaction won; no final ruling voiding the contract.
- **Just Futures Law v. ICE** (ELITE FOIA suit, reported 4 Jun 2026) — pending.

### Regulator actions

- **EDPS → Europol** (3 Jan 2022): ordered erasure of data on individuals with no established link to crime (Europol was a long-time Gotham user; replaced Gotham ~Q3 2021). The order targeted Europol retention generally, not Palantir in the dispositive.
- **Canada — Conflict of Interest & Ethics Commissioner** (Section 41 order, 16 Sep 2020): found Palantir Canada president David MacNaughton **breached conflict-of-interest rules**; nine senior officials barred from dealings for one year.
- **Canada — Commissioner of Lobbying** (report 22 Mar 2021): **CORRECTION — found NO breach.** Of 49 communications, 31 pro-bono COVID offers were **not registrable** and MacNaughton "did not contravene" the lobbying restriction. *(The adverse finding is the Ethics order only.)*
- **DoD FASCSA → Anthropic** (4 Mar 2026): supply-chain-risk designation forcing Claude's removal from military systems (affects MSS).

### Blocked / ended deals

- **Met Police UOA (~£50m)** — blocked by Mayor/MOPAC (20 May 2026); Palantir pre-action legal threat.
- **Hamburg §49 HmbPolDVG** — void; never deployed.
- **Germany BfV** — chose ChapsVision; **federal BKA slowed**.
- **Israel Unit 8200 / Shin Bet** — declined Palantir's intelligence offering.
- **DIA MARS protest** — dismissed 2026-06-03.
- **CMS↔ICE Medicaid** — partially enjoined.
- **NZ Police** — trial ended (cost).
- *Ended-by-supersession/wind-down:* UK MoD original £75.2m EA; HHS Protect; Tiberius; NHS COVID Data Store; Qatar World Cup.

### Investor / shareholder & divestment campaigns

- **NBIM (Norway GPFG, $2.3tn)** voted FOR a Human Rights Impact Assessment at Palantir's **AGM 3 June 2026** *(CORRECTION: 2026, not 2025)*; defeated by the dual-class structure (Thiel/Karp/Cohen ~49.999% voting). Non-insiders voted ~56% for.
- **ABP (Netherlands)** divested (~€825m, Apr 2026).
- **Storebrand (Norway)** divested (~$24m, Oct 2024, over Israel work).
- **NY State Comptroller DiNapoli** refused to divest (instead increased the holding); flashpoint in the comptroller race.
- **NYC Comptroller** pressed for a human-rights assessment (Feb 2025, reported-only).

### Civil-society / academic campaigns

- **EPIC v. ICE** (FOIA, settled Jan 2020) — exposed ICM/FALCON.
- **American Oversight v. Trump admin** (2025 FOIA, pending).
- **#NoTechForICE / #NoTechForTyrants** — student/recruitment boycotts (US: 1,200+ students/17 campuses; UK: Cambridge, Edinburgh, St Andrews, Oxford).
- **Former-employee open letter** (May 2025, 13 alumni).

---

## 5. The Civil-Liberties & Foreign-Ownership Through-Line

Three patterns recur across jurisdictions and bind the catalog together:

1. **Operational, not advisory.** Palantir is repeatedly the **live data/AI layer** of the state's hardest functions: targeting (MSS, TITAN, Ukraine, alleged Gaza), deportation (ICM, ImmigrationOS, ELITE), intelligence linkage (Gotham across CIA/FBI/ACIC/EMSOU/German Länder), public-health surveillance (HHS Protect, Tiberius, CDC, NHS FDP), and border control (UK Border Flow, NORTHCOM). The German BVerfG ruling is the clearest judicial recognition that this operational layer can itself violate fundamental rights.

2. **A US national-security firm running others' sovereign data.** Whether in the UK ("data remains sovereign" assurances over the £240.6m MoD deal; the revolving-door concern), Ukraine (the 2024 Swiss CLOUD Act audit), Germany (BfV/BKA digital-sovereignty pushback), or the UAE (Palantir-staffed Aither), the recurring anxiety is **US-government/intelligence access** and dependence on a founder-controlled American firm with overt political ties. The dual-class structure that defeated the 2026 human-rights vote underscores the foreign-ownership-of-the-operational-layer concern.

3. **Sole-source, secret, and threshold-gaming procurement.** ICE ImmigrationOS ("urgent and compelling," sole-source); NIH N3C ("no other sources capable"); UK MoD £240.6m (s.41 direct award); Cabinet Office Border Flow (no tender); AUSTRAC ("not competitive at all"); the Met UDP Phase 1 (~£489,999, structured below the £500k scrutiny threshold); EMSOU (FOI refused); the heavily redacted NHS FDP contract. The procurement pattern — not just the technology — is what regulators, auditors (NAO), parliaments (EDMs, Hansard, Senate Finance), and mayors keep challenging.

---

## 6. Do Not Overstate

### Alleged, not proven

- **Gaza / Lavender / Gospel / "Where's Daddy?":** IDF-attributed systems, **NOT proven Palantir products**. The UN "reasonable grounds" finding is a special-rapporteur opinion, **not a court ruling**. Palantir denies Lavender/Gospel involvement. **No court or regulator has adjudicated complicity.**
- **The US cross-agency "mega-database":** NYT-reported; **Palantir denies it ("blatantly untrue").** No primary EO-implementation contract naming the linked datasets located.
- **IRS "mega-database":** the cited GovExec source **does not name "Foundry"** and frames the Palantir master-database effort as **separate** from the IRS-to-DHS data-sharing plan.
- **ELITE's Medicaid-data use:** reported (404 Media leaked guide); **ICE and Palantir did not confirm.**
- **Iran target-selection via MSS+Claude:** Washington Post-sourced **reporting, not adjudicated.**
- **NSA XKEYSCORE integration:** based on **leaked classified documents**; BuzzFeed says NSA was pilot-only and ended ~2015.
- **Ukraine PRISMA deep-strike role:** **CNN-reported**, no Palantir release.
- **Ukrainian data-access risk:** analyst allegation citing a Swiss audit; no Ukraine-specific breach confirmed.

### Reported, not primary

- **Most contract values are reported ceilings/announcements, not obligations.** The $10bn Army EA and ~$1.3bn MSS are **maximums**. The clearest primary-sourced figures are **NGA Glacier Bay $646M / Platform Licenses $28.3M** (NGA notices), **UK MoD £240.6m** (Find a Tender 083874-2025), **UK NFLMS ~£9m** (051257-2026), **NHS FDP £182.2m CAN**, **HHS Protect $7.5M** (USAspending), and **EMSOU £818,750**. Commercial figures ($300M syndicate premium, $1.6B McGill GWP, +20,000 bbl/day, 50k Skywise users) are **business metrics, not Palantir contract values.**
- **Korea/Japan/UAE values** are company press-release figures (HD Hyundai's "hundreds of millions" is a projection; Aither value/split undisclosed).
- **AppliedAI $55M** belongs to the **Feb 2025 G42 Series A**; it is an **equity stake, not a deployment.**

### Material corrections applied (don't repeat the old versions)

- **ImmigrationOS** is `build-in-progress`, **not operational** (FOC Sep 2027).
- The ICE "**$145M**" is **ICM + ImmigrationOS combined**, not standalone ICM.
- **DIA MARS** protest was **dismissed 2026-06-03** (not "ongoing").
- The **Canada Lobbying Commissioner found NO breach** (only the Ethics Commissioner did).
- The **NBIM AGM was 3 June 2026**, not 2025.
- **Lowe's/General Mills/OpenAI dropped** (unsourced).
- Ukraine demining product is **AIP**, not Foundry.
- **USDA-only** for the attendance tool (VA/SSA sought).
- **Singapore, Saudi Arabia, Bahrain, Kuwait, Oman, NCTC, ODNI** — undocumented/dropped.

### Gaps (known unknowns)

Marine Corps MSS license value; Glacier Bay scope; Space Force follow-on; exact obligated (vs ceiling) dollars under the $10bn EA and ~$1.3bn MSS; primary SAM.gov verification for ImmigrationOS task orders; whether a compliant §25a HSOG was enacted by 30 Sep 2023; the Met interim-extension value; the Bavaria/NRW case numbers and outcomes; Aither ownership split; whether the blocked Met UOA proceeds to a filed judicial review; the precise force lists for Nectar (9) vs EMSOU (5).

---

## 7. Consolidated Source List

**Primary / official**
- NGA Contract Announcements — nga.mil/news/Contract_Announcements.html
- army.mil — Enterprise Service Agreement (2025-07-31)
- GOV.UK — UK–Palantir Strategic Partnership (2025-09-18)
- Find a Tender — 083874-2025 (UK MoD £240.6m); 051257-2026 (UK NFLMS)
- BVerfG — bvg23-018 press release; Judgment 1 BvR 1547/19 (2023-02-16)
- EDPS — Europol erasure order (2022-01)
- Conflict of Interest & Ethics Commissioner — Section 41 Order (2020-09-16); Commissioner of Lobbying — MacNaughton report (2021-03-22)
- UN — A/HRC/59/23 (Albanese, 2025-07)
- US Senate Finance — Wyden/AOC Palantir letter (2025-06-17)
- USAspending — HHS Protect ($7.5M); Palantir IR / BusinessWire releases; Palantir blog "Correcting the Record" (2025-06)
- NZ Ombudsman — case note 449159; Hansard (2026-02-10)

**Reporting**
DefenseScoop, Breaking Defense, Defense News, CNBC, USNI News, FedScoop, Axios, Fortune, 404 Media, The Intercept, Washington Post, NYT (via New Republic), ProPublica, GovExec, American Prospect, Healthcare IT News, BuzzFeed News, Bloomberg, Globes, Calcalist/CTech (2024-01-13), Times of Israel, TIME, CNN (via UNITED24), EurasiaReview, Ukrainska Pravda, Digital Health, The Register, openDemocracy, PublicTechnology, Computing, ITV, Police Professional, The Nerve, Local Government Lawyer, heise online, Cybernews, KED Global, Barchart, Crikey, Canberra Times, Defence Connect, RNZ, AGBI, The National, Gulf Times, Zawya, Wamda.

**Advocacy / NGO / civil society**
ACLU, EFF, EPIC, American Oversight, American Immigration Council, KFF, NBC News, Foxglove, Good Law Project, Just Futures Law, Liberty Investigates, CAAT, GFF (Gesellschaft für Freiheitsrechte), Chaos Computer Club, Business & Human Rights Resource Centre, UN Watch, Al Jazeera, Anadolu, IASJ, NL Times, #NoTechForICE.

**Investor / governance**
NBIM (GPFG), ABP, Storebrand, NY State Common Retirement Fund, NYC Comptroller.

---

*Compiled from 16 verified sector catalogs. Every deployment carries a confirmed/reported/alleged tag and a status; allegations are not presented as fact; reported values are not presented as primary; corrected items reflect the latest adjudications (DIA dismissal, Canada lobbying non-breach, 2026 AGM, ImmigrationOS build-in-progress). Where the record is contested, both the allegation and Palantir's denial are stated.*
