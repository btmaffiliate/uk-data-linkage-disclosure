# PARLIAMENTARY BRIEFING NOTE
## The Ministry of Justice "Probation-to-Police" Data-Sharing Pilot, and the Splink Record-Linkage Programme

**Prepared for:** the Office of Iqbal Mohamed MP (Dewsbury and Batley)
**By:** Brandon Myers, independent public-interest researcher — brandonmyers.net
**Date:** June 2026
**Status:** Built entirely from public documents (chiefly the Government's own Algorithmic Transparency Records). No non-public system was accessed. Claims are graded by confidence; what is a pilot, or implied rather than stated, is flagged.

---

### 1. One-paragraph summary

The Ministry of Justice has built and operates **Splink**, a free, open-source probabilistic record-linkage tool, to join records about the same person across the justice system — prisons, probation, and the courts — even where those records share no common identifier. Most of this is statistical/research use and is presented as such. But the MoJ's **own** published Algorithmic Transparency Record now also documents **operational, person-identifying** uses: a real-time "Core Person Record," the retrieval of an individual's probation history at court while a case is being prepared for sentence, and — the focus of this note — a **North Essex pilot in which the police numbers of people under probation supervision are sent to the police every day to check whether they have been arrested**. None of the transparency records describes any individual consent, notification, or opt-out, and none states an explicit statutory legal basis beyond a general "public task." This is lawful linkage migrating quietly from *counting populations* to *acting on named individuals* — without the people affected being told.

---

### 2. What Splink is (neutral, accurate)

- **Splink** is an open-source Python library for *probabilistic record linkage* (entity resolution), built and maintained by the **Ministry of Justice's** data-linking team and published openly. It implements the mainstream **Fellegi–Sunter** statistical model.
- Its purpose is to decide, with a probability score, whether two records refer to the **same person** — across datasets that have no shared ID number (e.g. matching on name, date of birth, address fragments).
- **The mathematics is not in question.** The method is standard and the published accuracy is high. The issue this briefing raises is **governance** — consent, transparency, purpose, and the slide from statistics into operations — not a technical flaw.

---

### 3. The two faces of the same tool (the central point)

The MoJ runs Splink under **two distinct, publicly documented postures**, and the distinction matters:

**(a) "Data First" — research, presented as ring-fenced.**
The gov.uk Algorithmic Transparency Record *MoJ: Data First (Splink)* (17 December 2024) describes de-identified linkage for accredited researchers via the ONS Secure Research Service and SAIL Databank. It states the data is **"not for operational decision-making"** and **"not integrated into a decision-making process."** Taken at face value, this is the legitimate, low-risk end.

**(b) "Splink Master Record" — operational, person-identifying.**
The separate gov.uk Algorithmic Transparency Record *MoJ: Splink Master Record* (6 October 2025) documents the **same tool** in live operational use across four applications:

| # | Application | What it does | Posture |
|---|---|---|---|
| 1 | **JustLink** | Weekly batch linkage producing an anonymised lookup table linking prisons (NOMIS), probation (DELIUS) and courts (Common Platform, LIBRA, FamilyMan, CaseMan). | Statistical/analytical |
| 2 | **Probation in Court** | Retrieves an individual's probation records when they come to court, "as part of the process of preparing a case for sentence." | **Operational — feeds sentencing** |
| 3 | **Core Person Record** | A **real-time** system assigning a single unique identifier to a person across prisons, probation and the criminal courts as records are created/updated. | **Operational — live identification** |
| 4 | **Police data-sharing pilot (North Essex)** | Identifies the **Police National Computer (PNC) numbers** of probation-supervised individuals; these are **sent to the police each day to identify if any arrests have occurred.** | **Operational — daily police feed** |

> **The single sentence that matters most** (MoJ's own transparency record): Splink *"is used in courts to find probation records associated with individuals coming to court… It is being piloted as part of Core Person Record, a product that aims to create a unique identifier for persons across prisons, probation and the criminal courts… It is used to find Police National Computer (PNC) numbers associated with individuals, in order to request relevant arrest information from the police."*

**This is the move from statistics to operations, in the Government's own words.** "Data First" says the linkage is *not* for operational decisions; the "Splink Master Record" documents the same tool doing exactly that on named people.

---

### 4. Why it warrants parliamentary scrutiny

1. **No consent, no notification, no opt-out.** Neither transparency record describes any mechanism by which an individual is told their records are being probabilistically linked, or can object. The Master Record states there are "no complaint procedures specific to Splink." For a daily probation→police feed about named individuals, that is a significant accountability gap.
2. **No explicit statutory basis on the face of the record.** The transparency records rest on an *implicit* "public task" basis ("data… routinely collected… for the purposes of managing court cases and offenders"). They do **not** cite a specific statutory gateway for the operational/cross-body linkage. Parliament is entitled to ask what the lawful basis is, and what DPIA was completed for the operational uses specifically (as distinct from the research use).
3. **Probabilistic ≠ certain.** A probabilistic match is, by definition, sometimes wrong. When a *statistical* false-positive becomes an *operational* one — the wrong person's records pulled at sentencing, or the wrong PNC number flagged to police — the consequence falls on an individual. The error rates, thresholds, and what happens on a mis-match are not in the public record.
4. **The legal guard-rail just moved.** The **Data (Use and Access) Act 2025** amended the UK GDPR's automated-decision-making provisions (the former Article 22), shifting solely-automated significant decisions from "prohibited unless" toward "permitted unless," with key boundaries set by **ministerial regulation** rather than statute. The operational use of probabilistic linkage in justice settings sits squarely in the territory that change affects.
5. **Function creep is the pattern, not a one-off.** A research tool, ring-fenced in one transparency record, appears operationally in another. The structural risk is that the *same* engine serves both, one configuration apart.

---

### 5. What this briefing does NOT claim (so the questions can't be deflected)

- It does **not** claim Splink is inaccurate or unlawful *per se*. The maths is sound; most use is lawful.
- It does **not** claim Splink and **Palantir** are the same system or are technically linked. **They are not, and there is no documented connection.** Splink is the MoJ's own open-source tool; Palantir is a separate US-owned commercial platform used elsewhere in government. Questions about Splink go to the **MoJ**; questions about Palantir go to the **Home Office / DHSC**.
- It does **not** claim the North Essex feed has been rolled out nationally. The transparency record describes it as a **pilot**. The legitimate questions are about its scope, evaluation, legal basis, and intended rollout.

---

### 6. Recommended parliamentary approach

- **Written Parliamentary Questions to the MoJ** on the operational uses specifically — see the separate *Draft WPQs* document. They are written to be answerable, so that an evasive or "we do not hold that information" answer is itself revealing.
- Keep the **MoJ (Splink)** and **Home Office (Palantir)** tracks separate, as you have already begun, so neither department can answer one by pointing at the other.
- WPQ answers on this topic are often thin; the **follow-up** (and the contrast between the two transparency records) is where the accountability lies.

*Full investigation, all nine parts and the complete evidence repository: see the Evidence Annex.*
