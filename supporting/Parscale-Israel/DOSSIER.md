# Brad Parscale & Israel — Investigation Dossier

*Public-records OSINT. Compiled June 2026. Tags: **[confirmed]** = primary document / multiple reputable sources; **[reported]** = single credible outlet; **[alleged]** = unproven claim, attributed. Published in full at https://brandonmyers.net/writing/brad-parscale-israel*

## Verdict

The hypothesis tested was "connect Parscale to the Palantir/surveillance stack." **That is a clean negative** — no documented business, contract, data, personnel, or money tie between Parscale (or his firms) and Palantir Technologies, and no Thiel→Parscale business relationship. The closest link is two hops and personal (a Palantir employee advised Cambridge Analytica 2013–14; CA staff embedded with Parscale 2016), and Palantir disavowed CA.

**The real, documented finding is elsewhere:** Parscale is a **registered foreign agent for the State of Israel** (via Havas Media), running an AI-influence operation built — per its own scope of work — to shape generative-AI outputs. This is sourced to his own sworn FARA filing, adversarially verified against the primary DOJ FARA record.

## The documented spine — [confirmed], primary source

- **Clock Tower X LLC** (Delaware, organized 11 Jun 2025; sole owner **Bradley Parscale**, signed under penalty of perjury) registered under FARA as **#7649** on **18 September 2025**.
  - Primary: https://efile.fara.gov/docs/7649-Registration-Statement-20250918-1.pdf
- Foreign principal of record: **Havas Media Germany GmbH**, which the filing states is **"supervised … State of Israel"** / engaged "by or on behalf of the State of Israel" for a US "combat antisemitism" campaign.
  - Primary: https://efile.fara.gov/docs/7649-Exhibit-AB-20250918-1.pdf
- **Precision (do not overstate):** the principal is Israel **via Havas** — an earlier version naming Israel directly was filed as a deficiency and **corrected** (amendment 20 Oct 2025). Do NOT say "direct contract with the Israeli government."
  - Primary: https://efile.fara.gov/docs/7649-Amendment-20251020-2.pdf

## The money — [reported] (range; attribute)

- Contract reported **$6m** initially via Havas → expanded to **~$9m** (Dec 2025 amendment) → **~$15m reportedly paid** by mid-2026.
- Onward sub-contracts per FARA supplements (reported via The Intercept): SparkFire Technologies ~$6m (AI chatbots/texting); Portman Road Strategies (Mike Shields) ~$5m; Salem Media Representatives >$500k; Three Tech ~$500k.
- Sources: https://thehill.com/policy/international/5528458-brad-parscale-israel-foreign-agent/ ; https://theintercept.com/2026/05/28/israeli-government-money-brad-parsc/ ; https://readsludge.com/2025/10/06/israels-new-u-s-influence-campaigns-target-tiktok-churches-and-chatgpt/

## The tactics — [reported] (from the filing's SOW, as quoted by press)

- Designed to **shape generative-AI answers — ChatGPT, Gemini, Grok** — via SEO + purpose-built content sites; **~80% of content targeted at Gen-Z**; faith/church integration through Salem Media (Parscale is Salem CSO since Jan 2025).
- Note: the "church geofencing" element partly derives from a *separate* registrant ("Show Faith by Works LLC") — do not conflate with Clock Tower X's own SOW.

## Do not overstate

- **Not Palantir.** No connection. This piece is the opposite of that arrow.
- **Not a direct Israel contract** — it is via Havas (the direct framing was the filed error).
- **Cambridge Analytica "psychographics won 2016" is overstated** — by Parscale's own account CA was hired largely for staff; campaign switched to RNC data for the general. (ProPublica: https://www.propublica.org/article/the-myths-of-the-genius-behind-trumps-reelection-campaign)
- **The "$617m shell company" (AMMC) was Kushner/campaign-controlled, not Parscale's firm.** The FEC complaint (MUR 7784) that swept in Parscale Strategy **deadlocked, was dismissed, and the dismissal was affirmed on appeal (Jan 2024)** — no finding against him. (https://www.fec.gov/data/legal/matter-under-review/7784/)
- **No reliable net-worth figure exists** — online numbers are unsourced aggregators.

## Method

Three independent research passes (Palantir/surveillance; the Trump data operation; the money trail), then an adversarial verification pass that read the **primary FARA filings directly** (not just press). Spine = confirmed from the sworn registration; onward payments and tactics tagged reported and attributed. Built from public records only; no non-public source accessed; not legal advice.

---

## UPDATE (2026-06-28) — full report + original infrastructure forensics

**It is an apparatus, not one man.** Clock Tower X (#7649) is the largest US node of an Israel-MFA → Havas Media operation with ≥5 FARA registrants: Show Faith by Works (#7653, ~$4.1m, evangelical/church geofencing — separate registrant, execution possibly scrapped), Bridges Partners (#7652, ~$900k, the "Esther Project" paid influencers), Davis Media NY (#7662), and the earlier terminated SKDK (#7552, $600k, Jan 2024). Israel's global public-diplomacy budget (~$150m 2025) is GLOBAL — the US FARA tranche is a subset (low tens of millions). Keep distinct from domestic advocacy (AIPAC).

**Original evidence — the 12-site network (our own passive check, 28 Jun 2026):**
- Cluster A: 9 .org sites on ONE Cloudflare account — identical anycast IPs (162.159.136.54 / .137.54), identical name servers, identical WordPress+Elementor+Yoast stack — registered in two ~10-minute bursts (18 Sep & 10 Oct 2025); `factsignal.org` is the hub linking the other eight.
- Cluster B: feedingyoufiction.com + alliesforpeace.com on shared Squarespace.
- **CRITICAL: every site carries the FARA disclosure footer** ("distributed by Clock Tower X LLC on behalf of the State of Israel"). The network is LABELED, not hidden. Do NOT frame as an undisclosed/illegal network — the story is coordination + scale + self-dealing + AI intent.

**Money (recipients):** Clock Tower X → SparkFire Technologies ~$6m (AI chatbot/texting; founders Jeremy Haile / Tree McGlown, Atlanta), Portman Road Strategies ~$5m (Mike Shields, GOP operative; 14 of 18 Clock Tower staff are his Convergence Media employees), Salem Media Representatives >$500k (SELF-DEALING — Parscale is Salem CSO), Three Tech ~$500k (Medina OH; "80 Serbian engineers"). Contract: $9m FARA-confirmed, ~$15m reported paid.

**AI-manipulation: method documented, effect unproven.** Built to bend ChatGPT/Gemini/Claude/Grok via MarketBrew (predictive-SEO tool), the content ring, Salem authority-laundering, and SparkFire's chatbot funnel. BUT reporters could not get any model to cite the network, and Snopes debunked the "Israel signed a deal with ChatGPT" claim (no OpenAI/Anthropic deal). State as intent, not effect.

Full report live at https://brandonmyers.net/writing/brad-parscale-israel (now ~48KB: stat band, apparatus map, infra forensics table, AI-architecture, money flow, do-not-overstate, FAQ).
