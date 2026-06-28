# Investigations-desk pitch — "The First Wave"

*A one-page pitch. Lead with the original contribution; credit prior reporting; offer to collaborate. Tailor the greeting per outlet (Bellingcat / OCCRP / ICIJ / ProPublica / The Intercept follow-up).*

---

**Subject: Original infrastructure forensics on the Israel→Havas AI-influence network — and the bigger pattern behind it**

Hello [name],

I'm an independent researcher (brandonmyers.net). You've likely seen the reporting — The Intercept, Sludge, Responsible Statecraft — on Israel paying Brad Parscale's Clock Tower X, via Havas, to run a pro-Israel influence campaign built to shape AI outputs. I'm not pitching that story; you and others broke it. I'm bringing **two things that aren't in the published record**, and offering them to a desk that can take them further.

**1. Original infrastructure forensics (reproducible).** I ran a passive technical analysis (whois / DNS / fetch) of the campaign's eleven "independent" advocacy sites. They are demonstrably **one coordinated operation**: nine sit on a single Cloudflare account (identical anycast IPs, name servers, and WordPress/Elementor/Yoast build), registered in **two ~10-minute bursts** (18 Sep & 10 Oct 2025), with `factsignal.org` as the interlinking hub; two more cluster on shared Squarespace. Every site carries the FARA disclosure footer — so the story is **coordination, scale and self-dealing, not a hidden network.** Full method and per-domain table attached; anyone can reproduce it in an afternoon.

**2. The bigger frame nobody has assembled.** The Israel/Parscale case is, on a full FARA sweep, the **first disclosed instance of a government buying AI-output shaping through FARA.** It doesn't stand alone: Russia's "Pravda" network (Viginum; NewsGuard; DFRLab) is the only state peer in actually manipulating model outputs; a commercial "generative engine optimization" industry has industrialized the technique; the poisoning science is settled (Anthropic/UK AISI: ~250 documents can backdoor a model); and the AI platforms have stayed publicly silent about being targeted. **No one has connected those into a single thesis** — *the first wave of states buying AI-output shaping.* (Honest caveat I'd insist on in any draft: effectiveness is contested — Harvard's Misinformation Review found a much smaller effect than NewsGuard — and that dispute belongs in the piece.)

**What I have, ready to share:** the reproducible forensics; the four primary FARA filings (#7649) downloaded and preserved, with OCR of the registration + amendments (incl. the verbatim "deficiency" correction); a tiered, fully-sourced dossier of the whole Havas apparatus (five registrants, ~$8–15M, the sub-recipients); and the Latin-American companion (Numen/Cerimedo) for context. All public-records; allegations labelled; the myths corrected.

**What I'm asking:** I'd like to hand this to a desk that can do the primary shoe-leather I can't — the named influencers, the SparkFire principals, a DOJ/FARA-Unit response, the platforms on the record. Happy to share everything, walk through the forensics, and be credited or not, as you prefer.

Evidence repo: github.com/btmaffiliate/uk-data-linkage-disclosure (supporting/Parscale-Israel).

Best,
Brandon Myers · brandonmyers.net

---

### Targeting notes (pick the desk)
- **Bellingcat** — the infrastructure forensics is exactly their open-source method; strongest fit for #1.
- **OCCRP** — the cross-border money + the Latin-American (Numen) angle.
- **ICIJ** — if you want the global apparatus treated as one coordinated cross-border project.
- **The Intercept (Daniel Boguslaw)** — already on it; offer the forensics + the "first wave" frame as a follow-up.
- **ProPublica** — the US-accountability + self-dealing (Salem) angle.

### Discipline reminders before you hit send
- Lead with the **forensics** (original); never claim you broke the underlying story.
- Keep your name on the **work**, your reasons out of it.
- Offer; don't demand credit. Desks respond to "here's verified original material," not "publish my piece."
