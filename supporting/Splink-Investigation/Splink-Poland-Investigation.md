# Splink in Poland — An Investigation
### Does Poland use the Ministry of Justice's record-linkage tool? What the public record shows.

*Public-interest research from publicly available sources, English and Polish. Compiled 4 June 2026.
This is a focused, single-country deep dive, reported honestly — including the null result.*

---

## Headline finding

**No evidence was found that Poland uses Splink.** Across English- and Polish-language searches —
Statistics Poland (GUS), the National Health Fund (NFZ), Polish universities, `.gov.pl`/`.edu.pl`
domains, academic and medical literature — **no Polish institution is documented as using the Splink
tool.** This is consistent with the broader global pass, which placed Statistics Poland in the
"no evidence" column.

This is a **negative result**, stated plainly: absence of a public record is not proof of non-use,
but Poland is **not** a confirmed Splink adopter, and should not be presented as one.

---

## What Poland DOES do with citizen data (the real, sourced context)

Poland does not need Splink to link citizen data — it has its own register-based statistical
infrastructure, which is the more relevant story:

- **GUS (Główny Urząd Statystyczny / Central Statistical Office)** runs data integration and record
  linkage as standard practice. A documented 2012 project linked statistical data with geospatial
  information using the 2011 National Census. *(geo.stat.gov.pl/laczenie)*
- **The 2021 National Census of Population and Housing (NSP 2021)** was heavily **register-based** —
  integrating administrative registers rather than relying solely on door-to-door collection. Census
  data is described as depersonalised/pseudonymised so a specific person cannot be tied to address and
  other collected data. *(spis.gov.pl)*
- **Medical data** is collected and processed centrally via GUS statistical reporting forms.
  *(form.stat.gov.pl — "dane medyczne")*
- **Polish academic interest in probabilistic record linkage as a method** exists independently of
  Splink — e.g. a Kraków University of Economics (UEK) paper, *"Probabilistyczne łączenie rekordów
  jako metoda…"* *(bazekon.uek.krakow.pl)*

So: the **capability, the practice, and the academic interest are all present in Poland** — Poland
links and integrates citizen and administrative data at population scale. What is **not** documented
is the use of *this particular tool* (Splink).

---

## Why the distinction matters

The honest framing is not "Poland is secretly running Splink on its citizens" — that's unsupported.
It's: *"Poland, like most modern states, integrates citizen records at scale through register-based
statistics and GUS data-linkage projects — it simply does so with its own/other methods, not the
UK's Splink tool, as far as any public document shows."*

If the concern is **citizen-data linkage and consent** (the core of the wider report), Poland belongs
in that conversation on the strength of its **register-based census and GUS integration** — not on a
Splink connection, which isn't there.

---

## Searches run (exhaustiveness)
1. `Splink … Poland GUS "Główny Urząd Statystyczny"` — no Polish adoption found.
2. `Splink "łączenie rekordów" / "probabilistyczne łączenie danych" Polska GUS NFZ spis` (Polish) — record-linkage practice found at GUS; no Splink.
3. `"splink" … site:gov.pl OR site:edu.pl OR Poland university author` — no Polish-domain or Polish-authored Splink hits.
4. `"splink" Polska uniwersytet / badania / "dane medyczne" 2023–2024` (Polish) — medical-data and university results; no Splink.

## Verdict
**Poland: CONFIRMED — no documented Splink use.** Genuine, independent citizen-data linkage exists
(GUS register-based statistics, censuses, medical reporting); the Splink tool does not appear in the
Polish public record.

## Sources
- geo.stat.gov.pl/laczenie (GUS data linking)
- spis.gov.pl (NSP 2021 census, register-based; data protection)
- form.stat.gov.pl — dane medyczne (GUS medical-data reporting)
- bazekon.uek.krakow.pl — Polish academic paper on probabilistic record linkage
- github.com/moj-analytical-services/splink; ijpds.org/article/view/1794 (Splink reference, for what was NOT found in Poland)
