# Splink: The Full Report (v2 — expanded & corrected)
### Who uses the Ministry of Justice's citizen record-linkage tool, who doesn't, and what it means

*Public-interest research from publicly available documents. Compiled 4 June 2026. Two deep-research
passes plus direct review of Splink's official "Use Cases" documentation (the maintainer-curated,
authoritative adopter list). Confidence flagged; corrections from the first version noted openly.*

> **Corrections to v1 (made openly):** (1) **Germany (Destatis) IS a confirmed user** — register-based
> census linkage; v1 wrongly discarded it after checking the wrong sources. (2) **Canada IS an
> adopter** — v1 wrongly called it a "non-adopter"; in fact the Ontario Ministry of Children,
> Community & Social Services uses Splink as its *main* data-integration tool, and Environment &
> Climate Change Canada uses it too.

---

## 1. Executive summary

**Splink** (UK Ministry of Justice; Fellegi-Sunter; ADR UK-funded; ~6M downloads) joins separate
records about the same person — with no shared ID — into linked records at population scale.

Documented adoption is **broader than the first pass showed**, and concentrated in the public sector:
**~8 countries plus two international organisations** have publicly documented government use, on top
of pervasive UK use and academic uptake. The driver is the **English-language data-science + open-source
+ academic network**, not a political alliance (it spans the EU, the UN, Africa and SE Asia).

The civil-liberties core is unchanged: where governments deploy it, they fuse sensitive citizen records
with **no individual consent, notification, or opt-out** — and it now reaches **refugee data (UNHCR)**.

---

## 2. CONFIRMED government / public-sector adopters
*(Source: Splink official Use Cases documentation + the cited primary sources.)*

### 🇬🇧 United Kingdom — pervasive, national + local
ONS (Census, Business & Demographic Index), NHS England (Person_ID linkage service), Ministry of
Justice (courts/prisons/probation cross-justice ID + BOLD probation dashboards), Ministry of Defence
(Veterans Card), UK Health Security Agency (HIV↔health records), Department for Education (learner
matching), Competition & Markets Authority, Office for Health Improvement & Disparities (health↔justice),
Homes England (Land Registry↔Ordnance Survey, 30M records), Department for Business & Trade, Welsh
Revenue Authority (operational tax), **and numerous local councils** — Lewisham (auto-enrolled 500+
families for Free School Meals), Leicestershire, Gateshead, Richmond, Wandsworth, Westmorland & Furness
("single view of the child"), London Office of Technology & Innovation (rough-sleeping). *Operational, deep.*

### 🇦🇺 Australia — ABS: Person Linkage Spine (Medicare+Centrelink+Tax); National Disability Data Asset. *Operational.*
### 🇩🇪 Germany — Federal Statistical Office (Destatis): linking register-based census data. *Operational.*
### 🇺🇸 United States — Defense Health Agency/DoD (dedup 200M+ hospital records); Florida Cancer Registry (feasibility); Catalyst Cooperative (utility data). *Mixed: operational + research.*
### 🇨🇦 Canada — Ontario Ministry of Children, Community & Social Services (**main** data-integration tool); Environment & Climate Change Canada. *Operational.*
### 🇨🇱 Chile — Ministry of Health (with UCL): migrant immunisation-access linkage. *Research.*
### 🇬🇲 Gambia — 2024 national census + post-enumeration survey linkage. *Operational (census).*
### 🇱🇦 Laos (Lao PDR) — Shared Child Health Record: pediatric record de-duplication (non-Latin script). *Operational (health).*

### International organisations
- 🇪🇺 **European Medicines Agency** — detecting duplicate adverse-event reports (veterinary medicines).
- 🌐 **UNHCR (UN Refugee Agency)** — identifying/addressing duplicates in datasets. **(Refugee data.)**

### Academia (broader still)
University of Cambridge (CAMPOP — full-count census linking 1851–1921); Harvard / Vanderbilt / Mass
General Brigham (8.1M death records↔EHR); Princeton / Minnesota; Stanford; **Bern, Switzerland**;
UPenn / Princeton / UC Berkeley (108M individuals: property↔voter files↔donations); Lao PDR child health.

---

## 3. Negatives & null results (still useful)
- 🇵🇱 **Poland** — no Splink; GUS does its own register-based census linkage.
- 🇮🇱 **Israel** — no Splink; Ofek national HIE + HMO-linked EHRs (its own infrastructure).
- 🏴 **Scotland / Wales** — Public Health Scotland, NRS, and Wales' SAIL Databank do extensive linkage via their *own* TTP/MRL systems; no Splink found.
- 🇳🇿 **New Zealand** — IDI links via Fellegi-Sunter (the method), no documented Splink.
- 🇮🇪 **Ireland (CSO)** — Protected Identifier Key (PIK) system; no Splink found.
- **No evidence:** Netherlands, Norway, Sweden, Finland, Denmark, France, Spain, Italy, Eurostat, Brazil, South Africa, India.
- **Statistics Canada (the NSI)** — not shown using it, *even though other Canadian government bodies do.*

---

## 4. The pattern — corrected
Not Commonwealth (Canada uses it *provincially* but NZ doesn't; Australia does), not Five-Eyes (spans
the **EU, UN, Gambia, Laos, Switzerland, Chile**). The real driver: a **free, open-source UK-government
tool** spreading through the **English-language statistics community, academic collaborations
(UCL→Chile), open-source distribution, and international development/health projects** (Gambia census,
Laos child health, UNHCR). Language + open source + research/aid networks — not geopolitics.

---

## 4.5 The bigger picture — Splink is one window into a global norm
Splink is a visible *thread*; the fabric is far larger. **Linking citizens' records without individual
consent is now the dominant — and fast-growing — model of official statistics**, internationally endorsed:

- **UNECE 2020 census round (48 countries):** 14 (29%) **fully register-based**, 12 (25%) **combined** —
  i.e. **~54% built their census on linked administrative/register data**; only 46% still traditional.
  *(UNECE, "Overview of the 2020 round of censuses.")*
- **2030 round:** about **half** of UNECE countries expect to go **fully register-based**, and "most
  others expect to use administrative data partly." The door-to-door census is being retired.
- **Nordic countries** (Denmark, Sweden, Finland, Norway) have run **fully register-based** population
  systems for **decades** — the model the UK, NZ and Australia are now adopting.
- **OECD & UN** guidance **explicitly permits** statistical/health data linkage "subject to safeguards,"
  and notes the legal bases that allow it **without individual consent** "vary by country."

**The mechanism is the whole point:** register-based statistics *inherently* link a person's records
across government **without asking them** — the legal basis is **statute, not consent**. So the consent
gap is **not** a UK quirk or a Splink quirk. It is **structural to how modern states now count and know
their populations** — a near-universal default, expanding toward total coverage by 2030. Splink is
simply one of the most *visible and open-source* instances of a practice almost every developed state
already runs, and the rest are adopting.

## 5. Why it matters (+ fair counter-case)
**Concern:** sensitive citizen records fused into person-level profiles, no consent/notification/opt-out,
drifting from statistics to operational identification (UK real-time court use; PNC lookups) — now
reaching **refugee data (UNHCR)** and **child health records (Laos)**.
**Counter-case (for credibility):** lawful; accurate method; real safeguards (Five Safes, accredited
researchers, secure environments, de-identification); genuine public goods; open-source = more
transparent than proprietary tools.
**Synthesis:** the quiet, lawful normalisation of cross-domain citizen linkage without meaningful
consent — pioneered deepest in the UK, now documented across ~8 countries + the EU and UN, and mirrored
everywhere by each state's own systems.

---

## 5.5 Legal standing & the GDPR paradox
*(Informed analysis, not a legal opinion — a data-protection specialist should pressure-test any
specific claim before publication.)*

The instinct is "surely this breaks GDPR." **It almost certainly does not** — and the accurate finding
is far stronger than an alleged violation would be.

**GDPR does not require consent.** Consent is just one of six lawful bases (Art 6). State data-linkage
runs on:
- **Art 6(1)(e)** — a task in the **public interest / official authority** (the workhorse for census,
  official statistics, public health).
- **Art 6(1)(c)** — legal obligation.

**GDPR is deliberately engineered to *permit* statistical linkage:**
- **Art 89** — a carve-out for "processing for statistical purposes," subject to safeguards
  (pseudonymisation, data minimisation).
- **Art 5(1)(b)** — further processing for statistical purposes is **expressly *not* "incompatible"**
  with the original collection purpose; this defuses the purpose-limitation objection.
- **Art 14(5)(b)** — a controller may **skip informing individuals** where notification is impossible or
  "disproportionate effort." *This is the legal home of the entire consent gap — the article that makes
  the silence lawful.*
- **Recital 162** and **Regulation (EU) 223/2009 (European Statistics)** explicitly accommodate official
  statistics.

**Precision on the EU body:** the **European Medicines Agency** is an EU institution, so its processing
falls under **Regulation (EU) 2018/1725 (the EUDPR)** — GDPR's sibling for EU bodies — **not GDPR
itself.** Same principles, different instrument. (A lawyer will catch this; cite it correctly.)

### The paradox — the real story
> **The world's strongest privacy law legally authorises the very thing people assume it protects them
> from.** GDPR does not prohibit mass, non-consensual, cross-domain linkage of citizens' records — it
> supplies the lawful basis (public task), the statistics exemption, *and* the carve-out that means the
> individual is never told. The consent gap is **not an illegality. It is legal by design.**

This reframes the issue from *criminal* to *democratic*: nobody has to break GDPR, because GDPR blesses
it. The defence "but it's fully GDPR-compliant" becomes the indictment.

**Genuine legal pressure points (where it *is* arguable):** data minimisation (Art 5(1)(c)) vs. linking
everything to everything; transparency (Arts 13–14) vs. the disproportionate-effort silence; the right to
object (Art 21) being curtailed for statistical processing; and whether the **Data Protection Impact
Assessments** (Art 35) required for this high-risk processing are adequate — or even published.

## 6. The honest count
- **Confirmed government/public-sector adopters: ~8 countries** (UK, Australia, Germany, US, Canada, Chile, Gambia, Laos) **+ 2 international bodies** (EU/EMA, UNHCR).
- **UK is by far the deepest** (national agencies + many local councils).
- **Academic use: at least 4 countries** (US, UK, Switzerland, Laos).
- **Confirmed/likely non-users:** Poland, Israel, Scotland & Wales (own systems), NZ, Ireland, + ~10 others with no evidence.
- **Credit scoring/credit bureaus: UNVERIFIED. Excluded.**
- **True footprint is larger still** — open-source, ~6M downloads, no user registry; undocumented use exists but isn't nameable.

## 7. Method & sourcing
2 deep-research passes (adversarial 2-of-3 verification) + direct review of Splink's official Use Cases
page + per-country sweeps (incl. Polish & Hebrew). Primary source for the international list:
moj-analytical-services.github.io/splink (Use Cases). Negatives and corrections reported openly.
