# THE CONSENT GAP
## How governments link their citizens' records into single profiles — lawfully, globally, and without ever asking

*The complete brief. Public-interest research built entirely from the institutions' own published
documents. Two adversarially-verified deep-research passes + direct review of Splink's official
documentation + per-country sweeps (incl. Polish & Hebrew). Compiled 4 June 2026. Confidence flagged
throughout; corrections noted openly; nothing asserted without a source.*

---

# PART I — THE BRIEF (one page)

**One tool, one window into a global default.** *Splink* — a free record-linkage program built by the
UK Ministry of Justice — joins a person's separate records across government where there is no shared ID.

**1. They linked 56 million people — silently.** The UK ONS linked the **2021 Census to DWP benefits and
HMRC tax records** — **96.7%, ~56 million people.** No consent. No notification. No opt-out. *(ONS)*

**2. It's no longer just statistics — it identifies named individuals.** The Ministry of Justice uses it
**in real time in court**, and "to find **Police National Computer numbers** associated with individuals,
in order to request relevant arrest information from the police." *(GOV.UK Algorithmic Transparency Record)*

**3. It reaches the most vulnerable people alive.** Documented users include **UNHCR (refugee data)**, the
**Shared Child Health Record in Laos**, and the **2024 Gambian census.** *(Splink official Use Cases)*

**4. It's not one country.** Confirmed government use across **~8 countries + the EU and the UN** — and
that's only who *published* it. *(Splink official Use Cases)*

**5. This is the new normal.** **~54% of UNECE countries already build their census on linked
administrative data; ~half go fully register-based by 2030.** *(UNECE)*

**6. The legal basis is the scandal.** None of it is illegal. It runs on **statute, not consent.** The
gap is **structural** — the default setting of the modern state.

> **The line that doesn't move:** *Your records — health, tax, justice, benefits — are being joined into a
> single profile of you, lawfully, across most of the developed world. You were never asked. You cannot
> say no. And almost no one was told.*

---

# PART II — THE FULL REPORT

## What Splink is
Free, open-source probabilistic record-linkage library built by the **UK Ministry of Justice**
(Fellegi-Sunter model, ADR UK-funded, ~6M downloads). It joins separate records about the same person —
with no shared ID — at population scale (~100M records). Open source, so its *user list is unknowable*
(no registry); what follows is only **documented** use.

> **Corrections made openly (v1→v2):** (1) **Germany (Destatis) IS a user** — earlier discarded after
> checking the wrong sources. (2) **Canada IS an adopter** — earlier wrongly called a non-adopter.

## Confirmed government / public-sector adopters
*(Source: Splink official Use Cases + cited primary sources.)*

**🇬🇧 United Kingdom — pervasive, national + local.** ONS (Census, Business & Demographic Index), NHS
England (Person_ID linkage), MoJ (courts/prisons/probation cross-justice ID + BOLD probation dashboards),
MoD (Veterans Card), UK Health Security Agency (HIV↔health records), Dept for Education, Competition &
Markets Authority, Office for Health Improvement & Disparities (health↔justice), Homes England (Land
Registry↔Ordnance Survey, 30M records), Dept for Business & Trade, Welsh Revenue Authority (operational
tax), **+ many local councils** — Lewisham (auto-enrolled 500+ families for Free School Meals),
Leicestershire, Gateshead, Richmond, Wandsworth, Westmorland & Furness ("single view of the child"),
London Office of Technology & Innovation (rough sleeping). *Operational, deep.*

**🇦🇺 Australia** — ABS: Person Linkage Spine (Medicare+Centrelink+Tax); National Disability Data Asset. *Operational.*
**🇩🇪 Germany** — Federal Statistical Office (Destatis): register-based census linkage. *Operational.*
**🇺🇸 United States** — Defense Health Agency/DoD (dedup 200M+ hospital records); Florida Cancer Registry (feasibility); Catalyst Cooperative (utility data). *Mixed.*
**🇨🇦 Canada** — Ontario Ministry of Children, Community & Social Services (**main** integration tool); Environment & Climate Change Canada. *Operational.*
**🇨🇱 Chile** — Ministry of Health (with UCL): migrant immunisation-access linkage. *Research.*
**🇬🇲 Gambia** — 2024 national census + post-enumeration survey. *Operational.*
**🇱🇦 Laos** — Shared Child Health Record: pediatric de-duplication. *Operational (health).*

**International organisations:** 🇪🇺 **European Medicines Agency** (duplicate adverse-event reports);
🌐 **UNHCR** (deduplicating datasets — **refugee data**).

**Academia (broader still):** Cambridge (CAMPOP, full-count census linkage 1851–1921); Harvard /
Vanderbilt / Mass General (8.1M death records↔EHR); Princeton / Minnesota; Stanford; **Bern (Switzerland)**;
UPenn / Princeton / UC Berkeley (108M individuals: property↔voter files↔donations); Lao PDR child health.

## Negatives & null results (so it's honest, not cherry-picked)
- 🇵🇱 **Poland** — no Splink; GUS does its own register-based census linkage.
- 🇮🇱 **Israel** — no Splink; Ofek national HIE + HMO-linked EHRs (its own infrastructure).
- 🏴 **Scotland / Wales** — PHS, NRS, SAIL Databank link via their *own* TTP/MRL systems; no Splink.
- 🇳🇿 **New Zealand** — IDI links via Fellegi-Sunter (the method), no documented Splink.
- 🇮🇪 **Ireland (CSO)** — Protected Identifier Key (PIK); no Splink.
- **No evidence:** Netherlands, Norway, Sweden, Finland, Denmark, France, Spain, Italy, Eurostat, Brazil, South Africa, India.
- **Statistics Canada (the NSI)** — not shown using it, *even though other Canadian government bodies do.*

## The pattern — corrected
Not Commonwealth (Canada uses it provincially, NZ doesn't). Not Five Eyes (it spans the **EU, UN, Gambia,
Laos, Switzerland, Chile**). The driver: a **free, open-source UK-government tool** spreading through the
**English-language statistics community, academic collaborations (UCL→Chile), open-source distribution,
and international development/health projects** (Gambia census, Laos child health, UNHCR). Language + open
source + research/aid networks — not geopolitics.

## The bigger picture — Splink is one window into a global norm
**Linking citizens' records without individual consent is now the dominant, fast-growing model of official
statistics.**
- **UNECE 2020 census round (48 countries):** 29% **fully register-based**, 25% **combined** → **~54% on
  linked administrative data**; only 46% traditional. *(UNECE)*
- **2030 round:** ~half expect **fully register-based**; "most others… administrative data partly."
- **Nordics** fully register-based for **decades**.
- **OECD & UN** explicitly permit statistical/health linkage "subject to safeguards"; legal bases allowing
  it *without consent* "vary by country."
**The mechanism is the point:** register-based statistics *inherently* link a person's records across
government **without asking them** — the basis is **statute, not consent**. The consent gap is
**structural**, expanding toward total coverage by 2030. Splink is just the most visible, open-source
instance.

## Legal standing & the GDPR paradox
*(Informed analysis, not a legal opinion — have a data-protection specialist pressure-test before publishing.)*
The instinct is "surely this breaks GDPR." **It almost certainly does not** — and that's the stronger story.
- **Consent isn't required.** It's one of six lawful bases (Art 6). State linkage runs on **Art 6(1)(e)
  public task** and **6(1)(c) legal obligation**.
- **GDPR is built to permit it:** **Art 89** carves out statistical processing; **Art 5(1)(b)** makes
  further statistical processing *expressly not "incompatible"*; **Art 14(5)(b)** lets controllers **skip
  informing people** on "disproportionate effort" grounds — *the legal home of the consent gap*; Recital
  162 / Reg. (EU) 223/2009 accommodate official statistics.
- **Precision:** the **EMA** is an EU body → **Reg. (EU) 2018/1725 (EUDPR)**, not GDPR itself.
> **The paradox:** the world's strongest privacy law *legally authorises* the very thing people assume it
> protects them from. The gap is **legal by design — democratic, not criminal.** "But it's GDPR-compliant"
> becomes the indictment.
**Arguable pressure points:** data minimisation (5(1)(c)); transparency (13–14) vs the disproportionate-
effort silence; right to object (21) curtailed for statistics; adequacy/publication of DPIAs (Art 35).

## Why it matters (+ the fair counter-case)
**Concern:** sensitive records fused into person-level profiles; no consent/notification/opt-out; drifting
from statistics to operational identification (real-time court use; PNC lookups); now reaching **refugee
data (UNHCR)** and **child health (Laos)**.
**Counter-case (for credibility):** lawful; accurate method; real safeguards (Five Safes, accredited
researchers, secure environments, de-identification); genuine public goods (census accuracy, health
research, fraud reduction); open source = more transparent than proprietary tools.
**Synthesis:** the quiet, lawful normalisation of cross-domain citizen linkage without meaningful consent —
deepest in the UK, documented across ~8 countries + the EU and UN, mirrored everywhere by each state's own
systems.

## The honest count
- **Confirmed government/public-sector Splink adopters: 8 countries** (UK, Australia, Germany, US, Canada,
  Chile, Gambia, Laos) **+ 2 international bodies** (EU/EMA, UNHCR); **9 if academic-only is counted**
  (add Switzerland).
- **UK by far the deepest** (national + many local councils).
- **The wider no-consent linkage norm: ~26 of 48 UNECE countries already**, heading toward universal by 2030.
- **Credit scoring/credit bureaus: UNVERIFIED. Excluded.**
- **True Splink footprint larger but unnameable** (open source, no registry).

## Method & sourcing
Two deep-research passes (fan-out search → fetch → adversarial 2-of-3 verification → synthesis; 50 claims
verified, 0 survived as false) + direct review of Splink's official Use Cases page + per-country sweeps.
Primary sources: GOV.UK Algorithmic Transparency Records, ONS, ABS, NHS England, Splink official docs,
IJPDS (peer-reviewed), UNECE, OECD. Negatives, nulls, and corrections reported openly.

## Where to take it
Lead with the one-page brief (Part I). Best homes: **medConfidential** or **Foxglove** (UK data/health
rights, litigation-capable), the **Bureau of Investigative Journalism**, the **Guardian** data team;
formal routes via the **ICO** and **Office for Statistics Regulation**. Approach openly, real name — it's
all public-source, so there's nothing to hide and nothing to leak.

---
*Full archived evidence (their words, screenshots, saved pages, downloadable bundle):
brandonmyers.net/writing/the-quiet-joining-up*
