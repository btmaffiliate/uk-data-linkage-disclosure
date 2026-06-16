# Documented connections between Splink and Palantir — evidence log

_Compiled 2026-06-16. Each item: claim · source URL · verbatim/close quote · status. Conclusion at end.
Honest scope: this is an evaluation of whether a **direct** Splink↔Palantir connection is documented.
It is not advocacy; it records what the public/primary record actually shows._

## A. What Splink is (primary source)
- **MoJ Analytical Services; MIT licence; "Fast, accurate and scalable probabilistic data linkage with
  support for multiple SQL backends."** Backends: **DuckDB, Spark, Postgres** (README), plus Athena/SQLite
  (docs). **Palantir Foundry is NOT a backend; "Palantir"/"Foundry" appear nowhere in the repo.**
  - `https://github.com/moj-analytical-services/splink` (accessed 2026-06-16, read).

## B. What Palantir Foundry is (separate platform)
- Commercial data-integration platform with its **own** entity-resolution/linking; documented data
  connectors/backends are Foundry's own — **no Splink integration documented.**
  - `https://www.palantir.com/platforms/foundry/data-integration/` (accessed 2026-06-16).

## C. Direct connection searches — all negative
- **Splink ↔ Foundry integration:** none documented. `https://www.palantir.com/docs/foundry/...` returns
  Foundry's own connectors; no Splink. (accessed 2026-06-16)
- **Palantir contributors / Foundry issues on the Splink repo:** none surfaced.
  `https://github.com/moj-analytical-services/splink/graphs/contributors` ·
  `.../splink/issues` (accessed 2026-06-16)
- **Foundry-vs-Splink comparison/integration:** none found; they are independent entity-resolution tools.

## D. The only real connective tissue — INDIRECT, via PwC (label clearly)
- **PwC ↔ Palantir is a formal UK alliance** (preferred partners; PwC uses Foundry/AIP). Multiple primary
  corporate sources:
  - `https://www.pwc.co.uk/services/alliances/insights/pwc-palantir.html`
  - `https://www.businesswire.com/news/home/20251118441737/en/...` ("Multi-Year… Preferred Partners in the UK", 2025-11-18)
  - `https://www.pwc.co.uk/press-room/press-releases/PwC-and-Palantir-technologies-collaborate-...` (2023)
- **PwC ↔ NFIB:** PwC won the crime & intelligence-management tech for the Action Fraud replacement
  (FCCRAS / Report Fraud); Capita won the contact-centre contract.
  - `https://www.consultancy.uk/news/34612/...` (names PwC + Capita; names **Palantir as PwC's "technology
    alliance partner"** on it — **single trade source**)
- **BUT:** no source ties **Splink** to PwC's NFIB build. The NFIB↔Palantir link is single-sourced; the
  procurement record (gov.uk Home Office FCCRAS; CoLP) names **Capita + PwC**, not Palantir, not Splink.

## E. The recurring ghost (flagged, NOT evidence)
- The claim "Report Fraud / NFIB analytics **includes Palantir Foundry + Microsoft**" appears in search-
  engine summaries but is **NOT in the cited primary sources** (Wikipedia NFIB names no vendor — checked
  twice; FCCRAS procurement names Capita + PwC). Treat as **unverified**.

## Conclusion (high confidence)
**There is no documented direct technical or corporate connection between Splink and Palantir.** They are
separate: Splink is MoJ open-source (MIT), running on DuckDB/Spark/etc.; Palantir Foundry is a separate
commercial platform with its own linkage. The only real link is **indirect**: PwC is Palantir's UK
alliance partner *and* the NFIB tech provider — but Splink is not documented anywhere in that chain.

**Implication for the disclosure:** the two stories must stay **separate**. Asserting "Splink is Palantir"
or "Palantir runs the MoJ linkage" is unsupported and would be the fastest way to discredit the work. The
"Palantir blindspot" framing actually *depends* on them being distinct — the point is precisely that the
state built its **own** open-source engine (Splink) **instead of** buying Palantir, which is why it escapes
the vendor-procurement scrutiny aimed at Palantir.
