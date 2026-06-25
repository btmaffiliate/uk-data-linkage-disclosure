# EVIDENCE ANNEX
## Every factual claim in this pack, with its primary source

**Principle:** the strongest claims here are sourced to the Government's *own* published records. Where a claim is a pilot, an inference, or uncorroborated, it is flagged. Nothing in this pack relies on a non-public system.

---

### Primary sources (Government's own records)

| Claim | Source |
|---|---|
| Splink is the MoJ's open-source probabilistic record-linkage tool (Fellegi–Sunter) | github.com/moj-analytical-services/splink ; gov.uk "Splink: MoJ's open-source library for probabilistic record linkage at scale" |
| Data First is de-identified, research-only, "not for operational decision-making," "not integrated into a decision-making process" | gov.uk Algorithmic Transparency Record — **MoJ: Data First (Splink)** (17 Dec 2024) |
| Operational uses: JustLink; probation records retrieved at court for preparing a case for sentence; real-time Core Person Record; North Essex pilot sending PNC numbers to police daily | gov.uk Algorithmic Transparency Record — **MoJ: Splink Master Record** (6 Oct 2025) |
| Dataset record counts (LIBRA 19.6m; FamilyMan 20.9m; CaseMan 17.7m; Common Platform 2.9m; NOMIS 2.2m; DELIUS 2.4m) | gov.uk — Splink Master Record ATR |
| "No complaint procedures specific to Splink"; no consent/notification/opt-out described | gov.uk — Splink Master Record ATR |
| Splink built by MoJ data-linking team, ADR UK / ESRC funded; underpins Data First | IJPDS article 1794 (developer-authored, peer-reviewed) |
| Data (Use and Access) Act 2025 amended UK GDPR automated-decision-making provisions (former Art 22), with boundaries set by ministerial regulation | Data (Use and Access) Act 2025 (c.18); legislation.gov.uk |

**Key verbatim quotes** (for citing in WPQs/correspondence):
- *"The Data First datasets are not integrated into a decision-making process… not for operational decision-making."* — MoJ: Data First (Splink) ATR.
- *"It is used in courts to find probation records associated with individuals coming to court… It is being piloted as part of Core Person Record, a product that aims to create a unique identifier for persons across prisons, probation and the criminal courts… It is used to find Police National Computer (PNC) numbers associated with individuals, in order to request relevant arrest information from the police."* — MoJ: Splink Master Record ATR.

---

### Direct links

- **MoJ Data First (Splink) ATR:** https://www.gov.uk/algorithmic-transparency-records/moj-data-first-splink
- **MoJ Splink Master Record ATR:** https://www.gov.uk/algorithmic-transparency-records/moj-splink-master-record
- **gov.uk Splink overview:** https://www.gov.uk/government/publications/joined-up-data-in-government-the-future-of-data-linking-methods/splink-mojs-open-source-library-for-probabilistic-record-linkage-at-scale
- **Splink source code:** https://github.com/moj-analytical-services/splink
- **IJPDS 1794 (Splink, peer-reviewed):** https://ijpds.org/article/view/1794
- **Data (Use and Access) Act 2025:** https://www.legislation.gov.uk/ukpga/2025/18

---

### The full investigation and evidence repository

- **Investigation hub (start here):** https://brandonmyers.net/writing/splink
- **The operational-use piece ("Statistics or Operations?"):** https://brandonmyers.net/writing/statistics-or-operations
- **The legal-exposure piece ("Ruled Unlawful Next Door"):** https://brandonmyers.net/writing/ruled-unlawful-next-door
- **Press kit (free to republish, citable facts):** https://brandonmyers.net/writing/press
- **Evidence repository — every contract value, citation, and ~96 archived full-page source screenshots preserved against takedown:**
  https://github.com/btmaffiliate/uk-data-linkage-disclosure
- **The three master analyses** (Splink global adopters; Palantir UK; Palantir global) live under `supporting/` in that repository.

---

### Confidence / honesty markers (read before quoting)

- **High confidence (Government's own record):** the existence and description of JustLink, Probation in Court, Core Person Record, and the North Essex PNC→police pilot; the "not for operational decision-making" statement in the Data First record; the absence of any described consent/opt-out.
- **Flagged as a pilot:** the North Essex feed and the Core Person Record are described by the MoJ as **pilots**, not national rollouts. Do not state otherwise.
- **Implied, not stated:** the **specific statutory legal basis** for the operational uses is *not* spelled out in the transparency records — it is an inference that "public task" (UK GDPR Art 6(1)(e)) is being relied upon. This is precisely why WPQ/FOI questions on the legal basis are worth asking.
- **Explicitly NOT claimed:** that Splink and **Palantir** are the same system or are technically linked — there is **no documented connection**, and the pack says so throughout. Splink = MoJ; Palantir = Home Office/DHSC, separately.
- **The error metrics** (false-positive/negative rates, thresholds) are **not in the public record** — which is why they are asked for, not asserted.
