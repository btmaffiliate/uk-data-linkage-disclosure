# The Splink Ecosystem: Every App Tied to the Tool

## 1. How big, how concentrated

The Splink ecosystem is **broad in reach but narrow in genuine code-level dependency, and overwhelmingly concentrated in one place: the UK government, and specifically the Ministry of Justice (MoJ) that created it.** Splink (`moj-analytical-services/splink`) is downloaded ~867k–892k times a month (~19M total per pepy.tech), and GitHub's "Used by" graph reports ~110 dependent repositories and ~16 dependent packages — but that count is an **upper bound that conflates lockfile pins, manifest mentions, and competitor benchmarks**, not productised integrations (the single most-starred "dependent," `goldenmatch`, has *no* Splink dependency at all and benchmarks *against* it). The truly load-bearing core is tiny: Splink itself plus a handful of official MoJ companion repos and a short list of hard runtime libraries (DuckDB, sqlglot, Altair, igraph, Jinja2). The most consequential surface is not software-on-software but **government-on-Splink**: at least eight UK public-sector systems consume Splink output — MoJ's JustLink, Splink Master Record, Core Person Record, the North Essex Probation/police arrest-detection dashboard, and the ADR UK/MoJ Data First research datasets; plus ONS (Business Index, and the 2021 Census-to-PDS linkage) and an in-development NHS England probabilistic linkage service. Genuinely maintained third-party productised wrappers number **exactly two** (Databricks ARC — now deprecated — and Antigranular's `op_splink`). Everything else loudly attached to Splink in the market (Quantexa, Palantir Foundry, Senzing, dedupe, Zingg, BigMatch, G-Link, DALI, etc.) is a **rival used *instead of* Splink, not built on it.**

---

## 2. Master table

| Name | What it is | Relationship | Primary source |
|---|---|---|---|
| **Splink (v3 / v4)** | The core MoJ open-source Python probabilistic record-linkage / dedup library (Fellegi-Sunter, pluggable SQL backends) | Core | github.com/moj-analytical-services/splink |
| **Splink charts / `Linker.visualisations`** | Built-in charting API (match weights, waterfall, m/u, cluster studio, comparison viewer) | Core | moj-analytical-services.github.io/splink/api_docs/visualisations.html |
| **Fellegi-Sunter probabilistic model (m/u, λ, match weights, TF adjustments)** | Splink's core scoring engine | Core | moj-analytical-services.github.io/splink/topic_guides/theory/fellegi_sunter.html |
| **Expectation-Maximisation (EM) training engine** | Unsupervised parameter estimation (`Linker.training.estimate_parameters_using_expectation_maximisation()`) | Core | moj-analytical-services.github.io/splink/api_docs/training.html |
| **splink_datasets** | In-built example datasets (FEBRL, fake person data, historical) surfaced via `splink.datasets` | Official companion (repo thin/likely stale; resolution logic lives in core Splink) | github.com/moj-analytical-services/splink_datasets |
| **splink_graph** | PySpark graph-metrics library for cluster-quality QA / false-positive detection; consumes Splink *output* | Official companion (not a runtime importer of `splink`) | pypi.org/project/splink-graph/ |
| **splink_udfs** | C++ DuckDB extension: phonetic/distance/n-gram UDFs for fuzzy matching | Official companion | github.com/moj-analytical-services/splink_udfs |
| **splink_demos** | Jupyter notebook tutorials for Splink | Official companion | github.com/moj-analytical-services/splink_demos |
| **splink_cluster_studio** | Interactive HTML cluster-QA dashboard; now also built into Splink charts | Official companion (standalone repo still exists; dashboard folded into core) | github.com/moj-analytical-services/splink_cluster_studio |
| **splink_comparison_viewer** | Pairwise comparison-viewer dashboard; now built into Splink charts | Official companion (standalone repo exists; dashboard now in core) | github.com/moj-analytical-services/splink_comparison_viewer |
| **uk_address_matcher** | UK address matcher built on a pre-trained Splink model (two-pass) | Official companion (hard Splink-dependent app) | github.com/moj-analytical-services/uk_address_matcher |
| **splink_synthetic_data / splink-data-generation** | Labelled synthetic person datasets for testing/benchmarking linkage | Official companion (produces inputs; not a runtime importer) | pypi.org/project/splink-data-generation/ |
| **live_splink (DuckDB-WASM in-browser demo)** | Client-side Splink linkage in the browser, no install | Official companion (author-official, *medium* — personal site, not MoJ org) | robinlinacre.com/live_splink/ |
| **DuckDB** | In-process OLAP engine; default/recommended backend | Backend dependency | moj-analytical-services.github.io/splink/topic_guides/splink_fundamentals/backends/backends.html |
| **Apache Spark (PySpark)** | Distributed SQL engine for 100M+ record linkages | Backend dependency | (backends topic guide, as above) |
| **AWS Athena** | Serverless Presto/Trino SQL backend (`splink[athena]`); incomplete fuzzy coverage, minimal dev support | Backend dependency (Splink-5-drop rumour *unverified* — see §5) | (backends topic guide) |
| **SQLite** | Embedded SQL backend; fuzzy via `splink[sqlite]`→rapidfuzz | Backend dependency | (backends topic guide) |
| **PostgreSQL** | Relational SQL backend (`splink[postgres]`); fuzzy gaps, minimal dev | Backend dependency | (backends topic guide) |
| **sqlglot** | SQL transpiler enabling backend-agnostic SQL generation (`sqlglot>=17.6.0`) | Runtime dependency (hard core dep) | github.com/moj-analytical-services/splink/blob/master/pyproject.toml |
| **Altair (Vega-Lite)** | Charting library behind diagnostic visualisations (`altair>=5.0.1`) | Runtime dependency (hard core dep) | (pyproject.toml, as above) |
| **python-igraph** | Connected-components clustering of pairwise links (`igraph>=0.11.2`) | Runtime dependency (hard core dep) | (pyproject.toml) |
| **Jinja2** | SQL/HTML template rendering (`Jinja2>=3.0.3`) | Runtime dependency (hard core dep) | (pyproject.toml) |
| **pandas** | Dataframe I/O to/from Splink | Runtime dependency (*medium* — dependency-group, not unconditional core) | (pyproject.toml) |
| **PyArrow** | Columnar/Arrow-Parquet interchange (`splink[pyarrow]`) | Runtime dependency (*medium* — optional extra) | (pyproject.toml) |
| **rapidfuzz** | C++ fuzzy-string UDFs for SQLite backend (`splink[sqlite]`) | Runtime dependency | (pyproject.toml) |
| **SQLAlchemy + psycopg2-binary** | Connection layer for Postgres backend (`splink[postgres]`) | Runtime dependency | (pyproject.toml) |
| **splinkclickhouse (ADBond)** | ClickHouse / chDB backend adapter; hard-depends on Splink; self-described *unofficial* | Third-party integration / Dependent | github.com/ADBond/splinkclickhouse |
| **Databricks ARC (databricks-arc)** | Databricks accelerator wrapping Splink + Hyperopt auto-tuning; **deprecated, unmaintained** | Third-party integration / Dependent | github.com/databricks-industry-solutions/auto-data-linkage |
| **Antigranular op_splink** | Differentially-private Splink variant inside Antigranular's hosted platform (`%%agimport op_splink`) | Third-party integration | docs.antigranular.com/private-python/packages/splink/ |
| **healmatcher** | Healthcare record-matcher (NYULH HEAL Lab) wrapping Splink's linkage | Dependent or fork (*high-medium* — pin not surfaced on PyPI) | pypi.org/project/healmatcher/ |
| **entify** | Early "workspace" web app for Splink-powered ER workflows | Dependent or fork (*medium* — ~0 stars, PyPI unconfirmed) | github.com/rasinmuhammed/entify |
| **Tuva EMPI** | Open-source healthcare master patient index built on Splink (legacy/OSS engine) | Dependent or fork (*medium* — manifest line unverified; EMPI Lite is *not* Splink) | github.com/tuva-health/tuva_empi |
| **ihmeuw/person_linkage_case_study** | IHME case study emulating US Census linkage with Splink | Dependent or fork (*medium* — tutorial repo, not a package) | github.com/ihmeuw/person_linkage_case_study |
| **enginux/splink-official (+ splink, DataCleaner)** | Fork/mirror of the Splink repo + a CSV-prep helper | Dependent or fork (mirror, no added value detected) | github.com/enginux/splink-official |
| **th368/splink_testing** | Apparent personal test fork of Splink | Dependent or fork (*low* — unverified personal fork) | github.com/th368/splink_testing |
| **GitHub dependents long tail (~110 repos / ~16 pkgs)** | Aggregate "Used by" graph; mostly 0-star personal repos | Dependent or fork (*low* — upper bound, conflates pins/mentions/benchmarks) | github.com/moj-analytical-services/splink/network/dependents |
| **MoJ JustLink (batch pipeline)** | Weekly anonymised cross-justice links lookup table (no PII) | Gov consumer | gov.uk/algorithmic-transparency-records/moj-splink-master-record |
| **Splink Master Record (MoJ)** | Clustered per-person master record; named ATRS subject | Gov consumer | gov.uk/algorithmic-transparency-records/moj-splink-master-record |
| **Core Person Record (MoJ)** | Real-time cross-justice unique-person-ID pilot | Gov consumer (pilot, not production) | gov.uk/algorithmic-transparency-records/moj-splink-master-record |
| **North Essex Probation/PNC dashboard (BOLD)** | Splink derives PNC numbers sent to police daily for arrest detection | Gov consumer | gov.uk/algorithmic-transparency-records/moj-splink-master-record |
| **ADR UK / MoJ Data First datasets** | De-identified linked admin datasets (7 justice domains) via ONS SRS + SAIL | Gov consumer | gov.uk/algorithmic-transparency-records/moj-data-first-splink |
| **ONS Business Index (ex-IDBR)** | UK business register modernised under RDMF; Splink at 100M+ scale | Gov consumer (*high* — corroboration is the ONS-engineer interview, not the implementation plan) | government-transformation.com (ONS engineer interview) |
| **ONS 2021 Census → PDS linkage** | Census records linked to PDS; report names "Splink 2" by version | Gov consumer (**upgraded to high**) | ons.gov.uk … census2021topersonaldemographicsservicelinkagereport |
| **ONS Demographic Index / DIMS** | DI spine + indexing pipeline returning a Demographic Entry ID | Gov consumer (*medium/unconfirmed* — no source names Splink as the DI/DIMS engine) | gov.uk … joined-up-data implementation plan |
| **NHS England Splink probabilistic linkage service (Data Linkage Hub)** | New Splink-cored PDS-linkage service feeding Person_ID/MPS work; up to 19% quality gain | Gov consumer (in development, not the live engine) | ijpds.org/article/view/3271 |
| **Fellegi-Sunter model (1969)** | Canonical probabilistic-linkage theory Splink implements | Lineage | moj-analytical-services.github.io/splink/topic_guides/theory/fellegi_sunter.html |
| **fastLink (R, kosukeimai/fastLink)** | R EM-on-FS package MoJ explicitly built on | Lineage (algorithmic predecessor, not a runtime dep) | github.com/kosukeimai/fastLink |
| **sparklink** | The original repo name for Splink ("Spark"+"link"), now redirects | Lineage | github.com/moj-analytical-services/sparklink |
| **splink_analysis_match / splink_scalaudfs** | Early MoJ Spark-era FS-in-Spark repos | Lineage (*medium* — same-org artefacts of uncertain developmental link) | github.com/moj-analytical-services/splink_analysis_match |
| **US Census BigMatch** | US federal large-file record-linkage program | Alternative — not tied | census.gov/library/working-papers/2007/adrm/rrc2007-01.html |
| **StatCan G-Link** | SAS/GUI FS linkage tool (Generalized Systems) | Alternative — not tied | www150.statcan.gc.ca/n1/en/catalogue/10H0036 |
| **AIHW DALI** | Australian SAS-based linkage tool (AIHW reportedly considering replacing it *with* Splink) | Alternative — not tied | aihw.gov.au/our-services/data-linkage |
| **ChoiceMaker (CHeReL / "NSW ChoiceMaker")** | Commercial FS linkage software used by NSW/ACT health linkage | Alternative — not tied | ncbi.nlm.nih.gov/pmc/articles/PMC8142947/ |
| **WA DLS3** | Bespoke WA Health in-house linkage engine | Alternative — not tied | ijpds.org/article/view/1138 |
| **FEBRL** | OSS Python biomedical linkage system (demo data reused by Splink) | Alternative — not tied (shared sample data ≠ integration) | users.cecs.anu.edu.au/~Peter.Christen/Febrl/… |
| **Datavant** | Commercial PPRL/tokenization platform | Alternative — not tied | datavant.com/blog/privacy-preserving-record-linkage |
| **Match*Pro (NCI/SEER)** | Cancer-registry FS linkage app (raw-PII + PPRL) | Alternative — not tied | seer.cancer.gov/tools/matchpro/ |
| **dedupe / dedupe.io** | OSS active-learning ER library + hosted service | Alternative — not tied | github.com/dedupeio/dedupe |
| **Zingg** | OSS Spark-based ML entity-resolution tool | Alternative — not tied | github.com/zinggAI/zingg |
| **Python Record Linkage Toolkit (recordlinkage)** | OSS Python linkage library (also uses FEBRL demo data) | Alternative — not tied | github.com/J535D165/recordlinkage |
| **Quantexa** | UK decision-intelligence/ER platform (£175m HMRC contract) | Alternative — not tied | thenextweb.com/news/quantexa-hmrc-ai-tax-fraud-sovereignty |
| **Palantir Foundry / FDP (Foundry Entity Resolution)** | NHS FDP holder; proprietary native ER | Alternative — not tied | palantir.com/foundry-entity-resolution/ |
| **Senzing / Tilores / AWS Entity Resolution / Tamr / Reltio / Informatica / Data Ladder** | Commercial ER/MDM products in "top tools" roundups | Alternative — not tied | github.com/J535D165/data-matching-software |
| **Mphasis Datalytyx (consultancy blog)** | Single Medium post advocating ARC+Splink | Not productised — blog mention only | medium.com/mphasis-datalytyx/… |
| **NICD (National Innovation Centre for Data)** | Educational Splink how-to guide + collaboration offer | Not productised — tutorial/mention only | nicd.org.uk/knowledge-hub/… |
| **Apache Spark MLlib** | Generic Spark ML library | Not a like-for-like alternative — category note only (see §4) | spark.apache.org/mllib/ |
| **Splink (splink.io, Dublin payments) / Splunk** | Unrelated fintech app and unrelated observability product | Name collision — not Splink | (n/a) |

---

## 3. By relationship tier

### Core Splink
This *is* Splink. The library (`pip install splink`, repo `moj-analytical-services/splink`, current major version **v4**, with v3 legacy), its built-in charting API (`Linker.visualisations`), and the two pillars of its statistical engine: the **Fellegi-Sunter probabilistic model** (per-comparison m/u probabilities, a λ match prior, additive log-Bayes-factor match weights, term-frequency adjustments) and the **Expectation-Maximisation training engine** (`Linker.training.estimate_parameters_using_expectation_maximisation()`) that estimates those parameters unsupervised, per blocking rule. The README states verbatim that "Splink's linkage algorithm is based on Fellegi-Sunter's model of record linkage, with various customisations to improve accuracy."

### Official companion tooling (moj-analytical-services org)
The genuinely official artefacts beyond the core: **splink_datasets** (in-built example data — note the repo itself is thin/likely stale; the actual download logic lives in core `splink.datasets`), **splink_graph** (PySpark cluster-QA metrics — it *consumes Splink's output clusters* but does **not** import the `splink` package, so it is a complement, not a runtime dependent), **splink_udfs** (a C++ DuckDB extension of fuzzy/phonetic UDFs), **splink_demos** (teaching notebooks), **uk_address_matcher** (a hard Splink-dependent UK address matcher shipping a pre-trained Splink model; its output literally shows "splink: probabilistic match"), and **splink_synthetic_data / splink-data-generation** (labelled synthetic test inputs by Splink's lead author — again, *produces inputs*, does not import the package).

Two visualisation repos — **splink_cluster_studio** and **splink_comparison_viewer** — began as standalone MoJ repos and *still exist*, but their dashboards are now exposed directly inside Splink via `Linker.visualisations`. Treat them as official companion tooling that has largely merged into core, not as independently maintained packages. The in-browser **live_splink** (DuckDB-WASM, no install) is *author-official* — built by Splink's creator Robin Linacre on his personal site, **not** under the MoJ org — hence **medium** confidence on its "official" status.

### Backend dependencies (SQL execution engines)
Splink expresses its linkage in SQL and dispatches it to a **pluggable** backend; nothing is hardcoded to one engine. The natively supported backends per the official backends guide are **DuckDB** (default/recommended, fastest single-machine, complete fuzzy coverage — also a hard core dep `duckdb>=0.9.2`), **Apache Spark/PySpark** (distributed, complete coverage, `splink[spark]`), **AWS Athena** (`splink[athena]`, incomplete fuzzy coverage, minimal dev support), **SQLite** (ships via stdlib `sqlite3`; fuzzy needs `splink[sqlite]`→rapidfuzz; incomplete coverage), and **PostgreSQL** (`splink[postgres]`; fuzzy gaps, minimal dev).

### Runtime dependencies (core libraries — *not* backends)
Distinct from the SQL backends, the hard core Python runtime libraries (`pyproject.toml`, master) are **sqlglot** (`>=17.6.0`, the SQL transpiler central to backend-agnostic SQL generation), **Altair/Vega-Lite** (`>=5.0.1`, the diagnostic charts), **python-igraph** (`>=0.11.2`, connected-components clustering), and **Jinja2** (`>=3.0.3`, SQL/HTML templating). **pandas** (dependency-group `>=1.3.5`) and **PyArrow** (`splink[pyarrow]`) are optional/extra, not unconditional core — **medium** confidence as "required to run." **rapidfuzz** (`splink[sqlite]`) supplies the SQLite fuzzy UDFs; **SQLAlchemy + psycopg2-binary** (`splink[postgres]`) are the Postgres connection layer. *(These are real, verified hard deps — but they are libraries, not SQL execution backends, and are tagged accordingly to match Splink's own taxonomy.)*

### Dependent / fork packages (genuinely import or fork Splink)
Real importers are few. **splinkclickhouse** (ADBond) registers ClickHouse/chDB as a Splink backend and self-describes as "unofficial… not directly supported by the Splink team." **Databricks ARC** wraps Splink as its linking engine ("ARC's linking engine is the UK MoJ's open-sourced entity resolution package, Splink") with Hyperopt auto-tuning — but is **deprecated/unmaintained**, its README advising "you instead use Splink directly." **healmatcher** (NYULH HEAL Lab) wraps Splink's core linkage (high-*medium* — the splink pin isn't surfaced on PyPI). **entify** (~0 stars), **Tuva EMPI** (legacy OSS engine "built on Splink" per vendor docs; manifest line unverified; the newer **EMPI Lite** is a non-Splink dbt reimplementation), and **ihmeuw/person_linkage_case_study** (a tutorial repo, not a package) are all **medium**. **enginux/splink-official** is a no-value mirror fork; **th368/splink_testing** is a **low**-confidence personal test fork. The **~110-repo / ~16-package** GitHub dependents long tail is a **low**-confidence upper bound — mostly 0-star personal repos, and the graph demonstrably conflates lockfile pins, manifest mentions, and competitor benchmarks.

### Government consumers (systems that run on Splink output)
**MoJ** (all high-confidence, gov.uk ATRS records + the "Running Splink in Production" blog):
- **JustLink** — weekly batch pipeline linking/deduping person records across NOMIS (prisons), DELIUS (probation), Common Platform/LIBRA (courts), FamilyMan and CaseMan, producing a fully anonymised links lookup table (no PII). *Source note:* the ATRS record names Splink + those systems + the weekly batch framing; the containerised **Splink+DuckDB-on-EC2/Airflow/S3/Athena** mechanics come from the separate production blog, **not** the ATRS URL.
- **Splink Master Record** — the clustered per-person output (records above the FS threshold grouped into one-person clusters); the named ATRS subject.
- **Core Person Record** — a real-time cross-justice unique-person-ID **pilot** (Splink in real-time mode), explicitly not full production.
- **North Essex Probation Delivery Unit dashboard** (BOLD programme, 2025 Civil Service Award) — ATRS verbatim: "Splink is used to identify Police National Computer (PNC) numbers associated with individuals supervised by North Essex Probation Delivery Unit," and "Those numbers are sent to the police each day to identify if any arrests have occurred." The cleanest, most operationally pointed tie in the entire ecosystem.
- **ADR UK / MoJ Data First** — Splink dedup + cross-domain linkage producing de-identified linked datasets across seven justice domains (~43 tables), served to accredited researchers via the ONS Secure Research Service and SAIL Databank. Splink was originally built *within* this programme.

**ONS** (100M+ record scale):
- **Business Index (ex-IDBR)** under RDMF — high confidence, but the load-bearing "Splink + Business Index + 100M, near-real-time" claim comes from an **ONS engineer interview** (government-transformation.com), **not** the joined-up-data implementation plan (which only says RDMF "has been testing the Splink tool with the view to use it").
- **2021 Census → PDS linkage** — **upgraded to high confidence**: the ONS Census-2021-to-PDS linkage report states explicitly that "Splink 2 was used, which is a probabilistic linkage library implementing the Fellegi Sunter method."
- **Demographic Index / DIMS** — remains **medium/unconfirmed**: ONS top-line materials list the DI as a Splink application, but no source names Splink as the *DI/DIMS* engine specifically. (The Census→PDS tie above is a distinct linkage and must not be conflated with the DI pipeline itself.)

**NHS England** — a new Splink-cored probabilistic linkage service to the Personal Demographics Service (PDS), feeding Person_ID / Master Person Service work, reporting up to **19% linkage-quality improvement** and exposing linkage probability to users. Status: **in development**, not the live production Person_ID engine. *Source note:* the 19%/PDS claims are in **IJPDS article 3271**, not the NHS Data Linkage Hub page (which only says they are "currently working on implementing a probabilistic linkage model using Splink").

### Third-party / commercial integrations (productised)
Only **two** genuinely productised commercial integrations exist: **Databricks ARC** (covered above — deprecated) and **Antigranular op_splink**, a **differentially-private variant** of Splink offered inside Antigranular's hosted private-Python platform (`%%agimport op_splink`). Antigranular's docs state they "created a differentially private version of the SPlink library, op_splink." *(Per the verifier, this is best framed as a "DP variant" rather than a definitive internal "wrapper," since the docs don't state it wraps upstream Splink internally.)*

### Lineage (what Splink derives from)
**Fellegi-Sunter (1969)** is the canonical probabilistic-linkage theory Splink implements — conceptual ancestry, not a dependency. **fastLink** (R; Enamorado, Fifield & Imai) is the direct algorithmic predecessor: MoJ's own gov.uk write-up states Splink "builds on fastLink's implementation in R of an Expectation-Maximisation algorithm to estimate a Fellegi-Sunter linkage model" — but fastLink is R, not a runtime dependency of the Python/SQL Splink. **sparklink** is literally the original repo for the same project ("THIS REPO HAS MOVED to …/splink"). The early MoJ repos **splink_analysis_match** and **splink_scalaudfs** are best described as **same-org Spark-era FS-in-Spark artefacts of uncertain developmental relationship** to the released package (**medium** — the source proves existence/purpose, not causal contribution).

---

## 4. What is NOT tied to Splink (so the map can't be misread)

**Rival tools governments and orgs use *instead of* Splink.** None embeds, wraps, depends on, or integrates with Splink. They are listed *only* to disambiguate — many appear in the same "top entity-resolution tools" roundups or were explicit leads to check:

- **Government/statistical-agency rivals:** **US Census BigMatch**, **StatCan G-Link**, **AIHW DALI** (notably, AIHW has reportedly *considered replacing DALI with Splink* — which confirms DALI is a *competitor*, not an integration), **ChoiceMaker** (used by NSW/ACT's CHeReL — the "NSW ChoiceMaker" lead), and **WA DLS3** (bespoke WA Health engine).
- **PPRL / registry tools:** **Datavant** (tokenization), **Match*Pro** (NCI/SEER cancer registries).
- **OSS / SaaS peers:** **FEBRL**, **dedupe / dedupe.io**, **Zingg**, **Python Record Linkage Toolkit (recordlinkage)**. *Important:* Splink (and recordlinkage) reuse **FEBRL's bundled demo datasets** — that is shared *sample data*, not a code dependency or integration. It does not make FEBRL or recordlinkage "tied to" Splink.
- **Commercial ER/MDM platforms:** **Quantexa** (£175m HMRC tax-fraud work), **Palantir Foundry / FDP** (NHS Federated Data Platform; proprietary "Foundry Entity Resolution"), and the cluster **Senzing / Tilores / AWS Entity Resolution / Tamr / Reltio / Informatica / Data Ladder**. No evidence any of them embeds Splink. *(The Palantir "not tied" finding rests on absence of evidence — the cited page returned no substantive content — which is the correct standard for an alternative, but it does not *actively* corroborate anything.)*

**Apache Spark MLlib** is listed only as a **category note, not a true alternative.** MLlib is a generic ML library, not a record-linkage product, and Splink uses Spark *SQL* (not MLlib) as a backend. It is neither a Splink dependency nor a like-for-like competitor; do not read it as either.

**Name collisions (entirely unrelated):**
- **Splink (splink.io)** — a Dublin-based **payments / sales platform** fintech app. Unrelated to MoJ Splink.
- **Splunk** — the observability/log-analytics product. Unrelated (and not even the same name).

**Mis-tagged "dependents" that are actually alternatives or non-integrations:**
- **goldenmatch** (`benseverndev-oss/goldenmatch`) — the **#1 most-starred entry** (117 stars) in Splink's GitHub "Used by" dependents graph, yet its `pyproject.toml` lists **no splink dependency**; Splink appears only as a *benchmark* it markets itself as outperforming. It is a **competing alternative, not a dependent** — and the single clearest proof the dependents graph overstates real usage.
- **Mphasis Datalytyx** — evidence is a **single Medium blog post** advocating ARC+Splink, not a product or documented client deliverable. **Downgraded: blog mention, not an integration.**
- **NICD** — evidence is an **educational how-to guide + a generic "collaborate with us" offer.** No productised Splink-based service. **Downgraded: tutorial/mention, not a commercial integration.**

---

## 5. Still-uncorroborated / low-confidence items

- **AWS Athena dropped in Splink 5** — **NOT corroborated by any primary source.** The backends guide does not say this; GitHub releases/CHANGELOG/PyPI do not confirm it. Treat the "dropped in Splink 5" clause as an **unverified rumour** (the Athena backend itself is genuine and confirmed).
- **ONS Demographic Index / DIMS engine** — no source names Splink as the DI/DIMS engine specifically; **medium/unconfirmed** (distinct from the high-confidence Census→PDS tie).
- **NHS England Splink service** — explicitly **in development**, not the live Person_ID/MPS engine.
- **Tuva EMPI** — "built on Splink" per vendor docs, but the backend `pyproject.toml`/manifest line was **not directly verified** (repo restructured); **medium**.
- **healmatcher** — Splink dependence rests on the package's own prose, not a surfaced pin; **high-medium**.
- **entify** — ~0 stars / ~15 commits, PyPI availability unconfirmed; **medium**, do not count as a maintained productised dependent.
- **th368/splink_testing** — unverified low-engagement personal fork; **low**.
- **GitHub dependents graph (~110 repos / ~16 packages)** — **low**: an upper bound, individually unverified, conflating lockfile pins, manifest mentions, and competitor benchmarks.
- **splink_analysis_match / splink_scalaudfs** — same-org Spark-era artefacts; **causal contribution to the released package is undocumented** (medium).
- **live_splink** — author-official by authorship (Robin Linacre's personal site), not MoJ-org owned; **medium** as "official."
- **pandas / PyArrow as core deps** — read from a single `pyproject.toml` parse; pandas is a dependency-group rather than unconditional core, so "required to run" is nuanced (**medium**).
- **op_splink** — confirmed as a DP variant via Antigranular's own docs, but the internal-"wrapper" claim is an inference, and current maintenance/availability was not separately verified.
- **Databricks ARC date inconsistency** — README says "not under development since early 2022," yet PyPI shows `databricks-arc` v0.1.18 dated 3 Nov 2023; do not present both as settled (likely a late patch on an otherwise abandoned project).
- **Versions** reflect Splink **4.0.16** (master `pyproject.toml` / PyPI, March 2026) and may differ in a future Splink 5.

---

## 6. Sources

**Core / official MoJ:**
- github.com/moj-analytical-services/splink — core library
- github.com/moj-analytical-services/splink/blob/master/pyproject.toml — runtime deps
- moj-analytical-services.github.io/splink/api_docs/visualisations.html — charting API
- moj-analytical-services.github.io/splink/api_docs/training.html — EM training
- moj-analytical-services.github.io/splink/topic_guides/theory/fellegi_sunter.html — FS theory
- moj-analytical-services.github.io/splink/topic_guides/splink_fundamentals/backends/backends.html — backends
- github.com/moj-analytical-services/splink_datasets, splink_graph (also pypi.org/project/splink-graph/), splink_udfs, splink_demos, splink_cluster_studio, splink_comparison_viewer, uk_address_matcher, sparklink, splink_analysis_match
- pypi.org/project/splink-data-generation/ — synthetic data (live PyPI link; the github.com/.../splink_synthetic_data URL is 404/moved)
- robinlinacre.com/live_splink/ — in-browser WASM demo

**Government (gov consumers):**
- gov.uk/algorithmic-transparency-records/moj-splink-master-record — JustLink, Master Record, Core Person Record, North Essex
- gov.uk/algorithmic-transparency-records/moj-data-first-splink — Data First
- gov.uk … joined-up-data … implementation-plan — RDMF/ONS context (note: only says RDMF was "testing" Splink)
- government-transformation.com (ONS engineer interview) — Business Index / 100M scale (the real primary source for that claim)
- ons.gov.uk … census2021topersonaldemographicsservicelinkagereport — "Splink 2 was used"
- ijpds.org/article/view/3271 — NHS England PDS linkage, 19% improvement
- nhsengland.github.io/datascience/our_work/data-linkage-hub/ — NHS "currently working on implementing… Splink"

**Dependents / third-party:**
- github.com/ADBond/splinkclickhouse
- github.com/databricks-industry-solutions/auto-data-linkage (PyPI: databricks-arc)
- docs.antigranular.com/private-python/packages/splink/ — op_splink
- pypi.org/project/healmatcher/; github.com/rasinmuhammed/entify; github.com/tuva-health/tuva_empi; github.com/ihmeuw/person_linkage_case_study; github.com/enginux/splink-official; github.com/th368/splink_testing
- github.com/moj-analytical-services/splink/network/dependents — dependents graph (upper bound)
- github.com/benseverndev-oss/goldenmatch — mis-tagged "dependent" (actually an alternative)
- pepy.tech / pypistats — download figures

**Lineage:**
- github.com/kosukeimai/fastLink — fastLink (R)

**Alternatives (NOT tied):**
- census.gov/library/working-papers/2007/adrm/rrc2007-01.html — BigMatch
- www150.statcan.gc.ca/n1/en/catalogue/10H0036 — G-Link
- aihw.gov.au/our-services/data-linkage — DALI (+ realworlddatascience.net: AIHW considering Splink)
- ncbi.nlm.nih.gov/pmc/articles/PMC8142947/ — ChoiceMaker/CHeReL
- ijpds.org/article/view/1138 — WA DLS3
- users.cecs.anu.edu.au/~Peter.Christen/Febrl/ — FEBRL
- datavant.com/blog/privacy-preserving-record-linkage — Datavant
- seer.cancer.gov/tools/matchpro/ — Match*Pro
- github.com/dedupeio/dedupe; github.com/zinggAI/zingg; github.com/J535D165/recordlinkage; github.com/J535D165/data-matching-software
- thenextweb.com/news/quantexa-hmrc-ai-tax-fraud-sovereignty — Quantexa
- palantir.com/foundry-entity-resolution/ — Palantir (negative-by-absence)
- spark.apache.org/mllib/ — Spark MLlib (category note only)

**Boundary / non-productised mentions:**
- medium.com/mphasis-datalytyx/… — Mphasis blog (mention only)
- nicd.org.uk/knowledge-hub/… — NICD guide (tutorial only)

*Verifier verdict across all six segments: SOLID. Corrections applied in this map: (1) Athena "dropped in Splink 5" stripped to unverified rumour; (2) sqlglot/Altair/igraph/Jinja2 retagged Runtime dependency vs SQL backend; (3) source URLs corrected for JustLink mechanics (production blog), NHS (IJPDS 3271), and ONS Business Index (ONS-engineer interview); (4) ONS item split — Census→PDS upgraded to high, DI/DIMS kept medium/unconfirmed; (5) goldenmatch carved out as Alternative-not-tied; (6) Mphasis + NICD downgraded out of the integration list to mentions; (7) Spark MLlib downgraded to a category note; (8) op_splink softened from "wrapper" to "DP variant"; (9) name collisions splink.io and Splunk explicitly fenced off.*
