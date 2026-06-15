# In Plain English
## How the UK joins up your records, tries to predict what you'll do, and who's building it

*Written for anyone — no jargon. It's a faithful, plainer retelling of the source-checked disclosure files.
It alleges **no crime**. Everything described appears to be **lawful**. The point isn't "they broke the
law" — it's "should they be allowed to do this with so little told to you, and so little checked?"
Each claim is marked: **CONFIRMED** (nailed down from official sources), **REPORTED** (widely reported,
not yet pinned to the primary document), or **UNKNOWN** (no answer found — needs a formal records request).*

---

## The short version
The UK government takes the separate records it holds about you — justice, benefits, health, tax, census —
and **joins them into one linked picture of you.** It does this **without asking you**, which is **legal**
(the law lets public bodies do it for "public task" reasons; consent was never the basis). Most of it is
mundane and used for statistics and research, behind safeguards.

But three things deserve hard questions:
1. Some of this matching is being used **operationally on real people** — including a pilot that **sends
   police a daily list** of supervised individuals — and the matching is **probabilistic** (it guesses
   *likely* matches, not certain ones).
2. The government is also building tools that **predict behaviour** — and one benefits algorithm has
   **already been admitted to be biased**.
3. A single **US data company, Palantir**, has quietly ended up inside many of the UK's most sensitive
   data systems.

None of that is illegal. Almost none of it has been properly explained to the public. That's the story.

---

## 1. They join your records — without asking *(CONFIRMED)*
Your records used to sit in different places. Now software matches them into one linked identity. The
government doesn't ask permission because the law says it doesn't have to — for official bodies, "we're
doing a public task" is the legal basis, not your consent. There are real safeguards (researchers usually
see the data stripped of names, in secure rooms). **So "no consent" isn't the scandal — it's the design.
The question is what comes *with* that: are you told? Can you object? Is it accurate? On some programmes,
the honest answer is: not clearly.**

## 2. The risky part: guesswork that reaches the police *(CONFIRMED, with key gaps UNKNOWN)*
The Ministry of Justice's own public record shows its matching tool (an open-source program called
**Splink**) being used not just for research but **operationally**:
- building **one identifier per person** across prisons, probation and courts;
- pulling someone's probation record when they appear **in court**;
- a **pilot that identifies supervised people's police reference numbers and sends them to police every
  day**.

The tool **guesses likely matches** — it's probabilistic. In a research file, a wrong guess is a bad
statistic. **Feeding police daily, a wrong guess is a real person wrongly flagged.** And here are the gaps
the public record does **not** answer (**UNKNOWN → these become formal questions**): the impact assessments
exist but **aren't published**; it's **not stated** whether a human checks each daily police list before
it's sent; there's **no published error rate**; and there's **no stated way to put it right** if you're
wrongly matched. Lawful — but, on the public record, unchecked.

## 3. The part that sounds like science fiction — but is real *(CONFIRMED)*
- **The DWP's benefits fraud AI was admitted to be biased.** The department's *own* internal fairness check
  found its fraud-detection algorithm flagged people **unevenly — by things like age, disability and
  nationality.** That's not a critics' claim; it's the government's own finding.
- **The Ministry of Justice built a "Homicide Prediction Project."** A real project (later renamed) to build
  a tool that tries to **predict who might commit a serious violent crime**, using justice and police data.
  It was uncovered by a civil-liberties group.
- Offender risk tools (like **OASys**) already score people on **1,100+ data points**, including domestic-
  violence and sexual-offending history.

This is the heart of it: the linked data isn't just counted — it's increasingly used to **predict and sort
people.** And at least one of those systems was **already found to be unfair**.

## 4. The law just got weaker, at the same time *(CONFIRMED on the text)*
A new law — the **Data (Use and Access) Act 2025** (in force February 2026) — **loosened** two protections
right as this linkage expanded: it **relaxed the ban on purely automated decisions** that significantly
affect you (for ordinary data), and it **weakened the duty to tell you** when your data was gathered
indirectly. It also lets a minister **redefine, by regulation, what counts as "meaningful human
involvement."** (Stated as context — no claim that it was done *for* these programmes.)

## 5. The City of London angle *(mixed: CONFIRMED governance; platform UNKNOWN)*
The **City of London Police** is the national lead for fraud and runs the **National Fraud Intelligence
Bureau**, which **automatically links** the country's fraud reports into intelligence packages. **Which
company's software powers it is not disclosed** — a "Palantir" claim has circulated but is **not confirmed
(single trade source; UNKNOWN — needs a records request).** Separately, the City of London Corporation has
a genuinely unusual setup: **businesses get votes**, a **~£2.3bn private fund ("City's Cash") sits outside
freedom-of-information law**, and an official called the **Remembrancer** lobbies Parliament from inside the
chamber. All public record; all fair to ask about.

## 6. Palantir — the US company in the plumbing *(REPORTED; keep it precise)*
A single US data-analytics firm, **Palantir** (deep US intelligence/defence roots), has won or partnered on
contracts across many of the UK's most sensitive systems — **reportedly**:
- the **NHS Federated Data Platform** (~£330m/7yr; reported access to identifiable data on ~65m patients —
  now under government review);
- **Ministry of Defence** analytics (~£240m); the **Financial Conduct Authority** data lake; **firearms
  licensing** across all 43 forces; a **Met Police** deal that was **blocked** in 2026;
- by one count, **34+ contracts across 10+ departments (~£670m)**.

**Two honesty rules that keep this credible:**
- **Palantir is NOT the MoJ's Splink.** The justice-linkage tool is the government's own open-source
  software — *not* Palantir. Don't merge them.
- **The NHS Palantir platform is a *different* system** from the NHS Splink linkage. Keep them separate.
- This is about **scale and opacity of lawful contracts**, *not* personal wrongdoing and *not* "get Thiel."

The honest headline: *a US intelligence-linked firm has quietly embedded across UK state data — health,
defence, finance, policing — much of it under-scrutinised, some now under review.* That's true, big, and
defensible.

## 7. Why it matters even though it's all legal
You end up with: a **complete, linked, consent-free picture of every citizen**, increasingly used to
**predict and sort** people, with at least one system **already found biased**, key safeguards **unpublished
or weakened**, and a **foreign intelligence-linked contractor** woven through it. Even if every piece is
lawful, **nobody put that whole picture to the public, and you can't easily see it, question it, or opt
out.** That's a democratic problem, not a criminal one — and democratic problems get fixed by **daylight
and questions**, which is the point of all this.

## 8. The questions someone needs to answer (turn the UNKNOWNs into formal requests)
1. **Publish the impact assessments** for the cross-justice "Core Person Record" and the probation→police
   pilot.
2. For that police pilot: **is each daily list human-checked before it reaches police?** What's the
   **error rate**? What's the **remedy** if you're wrongly matched?
3. State the **legal basis** and whether **any opt-out or objection** exists for the big linkage programmes.
4. How are linked people **told** (if at all), and what changed under the 2025 Act?
5. **Name the software** behind the national fraud database.
6. **Why is "City's Cash" outside freedom-of-information law** — publish the accounts.

## 9. What this does NOT say (the guardrails)
- It does **not** allege any crime, surveillance abuse, or corruption.
- It does **not** claim Palantir runs the fraud database (that's **unknown**).
- It does **not** connect the MoJ's Splink tool to the City of London or to Palantir.
- It does **not** say linking-without-consent is illegal — **it's lawful.** The issue is accountability.

*Faithful plain-English summary of the source-checked dossier. Verify the primary sources and take a
media-/data-protection-law review before publishing or sending to officials.*
