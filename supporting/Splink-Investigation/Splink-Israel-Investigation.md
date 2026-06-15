# Splink in Israel — An Investigation
### Does Israel use the Ministry of Justice's record-linkage tool? What the public record shows.

*Public-interest research from publicly available sources, English and Hebrew. Compiled 4 June 2026.
A focused single-country deep dive, reported honestly — including the null result.*

---

## Headline finding

**No evidence was found that Israel uses Splink.** Across English- and Hebrew-language searches —
the Central Bureau of Statistics (CBS / הלשכה המרכזית לסטטיסטיקה), the Ministry of Health, the four
national HMOs, universities, and `.gov.il`/`.ac.il`/`.org.il` domains — **no Israeli institution is
documented as using the Splink tool.** This is a **negative result**, stated plainly: Israel is **not**
a confirmed Splink adopter and should not be presented as one.

---

## What Israel DOES do with citizen data (the real, sourced context)

Here Israel is actually a *stronger* example of the underlying phenomenon than most — it simply does
it with **its own infrastructure**, not Splink:

- **Four nationwide HMOs** — **Clalit, Maccabi, Meuhedet, Leumit** — hold decades of **linked
  electronic health records** covering essentially the entire population. Clalit's linked EHR is
  internationally described as a research "gold mine." *(MobiHealthNews; PMC7183366)*
- **Ofek** — Israel's **national Health Information Exchange**, adopted by the Ministry of Health,
  knits provider records into a **"virtual national health record."** *(PubMed 16160295; IADB national
  HIE report; eHealth Governance Country Report: Israel)*
- A **multi-billion-shekel national digital-health programme** explicitly built on the value of this
  integrated population health data. *(MobiHealthNews)*

So the **practice exists at a very high level of maturity** — population-scale linkage of citizens'
health records — but through Ofek and the HMOs' own systems, **not Splink**, as far as any public
document shows.

*(Context note, not linkage-related: Israeli health data has also been a breach target — an
Iran-linked group claimed to breach Israel's largest healthcare network. Relevant to the data's
sensitivity, not to Splink.)*

---

## Why the distinction matters

The honest framing is **not** "Israel runs Splink on its citizens" — unsupported. It's:
*"Israel operates one of the world's most integrated population health-data systems (HMO-linked EHRs +
the Ofek national exchange) — it links citizen records at scale with its own infrastructure, not the
UK's Splink tool."*

If the concern is **citizen-data linkage and consent**, Israel belongs squarely in that conversation —
on the strength of Ofek and the HMO data ecosystem — **not** on a Splink connection, which isn't there.

---

## Searches run (exhaustiveness)
1. `Splink … Israel CBS / Ministry of Health` — no Israeli adoption.
2. `"splink" Israel record linkage / קישור רשומות / CBS / university` (incl. Hebrew) — no Splink.
3. `Israel health data linkage Clalit/Maccabi/Ofek "splink"` — rich native HIE found; no Splink.
4. `"splink" site:gov.il OR ac.il OR org.il / Israeli author 2023–2024` — no Israeli-domain Splink hits.

## Verdict
**Israel: CONFIRMED — no documented Splink use.** Genuine, highly mature citizen-data linkage exists
(HMO-linked EHRs, Ofek national HIE); the Splink tool does not appear in the Israeli public record.

## Sources
- mobihealthnews.com — "A 'gold mine' of data… Israel's billion-shekel bet on digital health"
- pubmed.ncbi.nlm.nih.gov/16160295 — Israeli virtual national health record (Ofek)
- publications.iadb.org — Implementation of a National Health Information Exchange in Israel
- ehtel.org — eHealth Governance Country Report: Israel
- PMC7183366 — linked EHRs from a single Israeli healthcare delivery system
- github.com/moj-analytical-services/splink; ijpds.org/article/view/1794 (Splink reference, for what was NOT found in Israel)
