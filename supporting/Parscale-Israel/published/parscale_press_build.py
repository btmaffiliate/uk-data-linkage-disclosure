#!/usr/bin/env python3
import pathlib
b="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"

REG="https://efile.fara.gov/docs/7649-Registration-Statement-20250918-1.pdf"
FARA="https://efile.fara.gov/"
HILL="https://thehill.com/policy/international/5528458-brad-parscale-israel-foreign-agent/"
INT="https://theintercept.com/2026/05/28/israeli-government-money-brad-parsc/"
RS="https://responsiblestatecraft.org/brad-parscale-israel/"
SLUDGE="https://readsludge.com/2025/10/06/israels-new-u-s-influence-campaigns-target-tiktok-churches-and-chatgpt/"
WEX="https://www.washingtonexaminer.com/news/investigations/4501168/israel-funds-front-websites-push-chatgpt-promote-pro-war-messaging/"
SNOPES="https://www.snopes.com/news/2025/12/22/israel-contract-chatgpt/"
REPO="https://github.com/btmaffiliate/uk-data-linkage-disclosure/tree/main/supporting/Parscale-Israel"

def H(t,s="1.3rem"): return "<strong style='font-family:var(--display);font-size:"+s+";color:var(--white);display:block;margin-top:8px'>"+t+"</strong>"
def B(t): return "<span style='display:block;padding-left:4px'>&bull; "+t+"</span>"

content=[
 "<em style='color:var(--text2)'>A free press &amp; media kit for the investigation into <strong>Brad Parscale&rsquo;s Clock Tower X</strong> and the FARA-registered <strong>Israeli AI-influence apparatus</strong>. Everything here is built from public records and the primary FARA filings, tiered <strong>confirmed / reported</strong>, and adversarially verified. <strong>You are welcome to quote, republish or build on any of it</strong> &mdash; attribution to brandonmyers.net appreciated, not required.</em>",
 "---",
 H("The story in five sentences","1.5rem"),
 "A foreign government &mdash; the State of Israel, through the ad agency <strong>Havas Media</strong> &mdash; is paying a network of US operatives, the largest being Trump&rsquo;s former campaign manager <strong>Brad Parscale</strong> (via his company Clock Tower X LLC), to run a <strong>FARA-registered</strong> US influence campaign. By its own filing, the operation is <strong>built to shape what generative-AI systems &mdash; ChatGPT, Gemini, Claude and Grok &mdash; tell Americans about Israel.</strong> Crucially, it is <strong>disclosed and labeled</strong>: this is lawful, registered foreign <em>influence</em>, not covert interference &mdash; which is exactly why it can and should be examined in the open. An independent infrastructure check shows the campaign&rsquo;s &ldquo;independent&rdquo; advocacy sites are in fact <strong>one coordinated network</strong>, and the money loops back on itself (Parscale also runs strategy for Salem Media, a paid recipient). <strong>What is new here is not that a foreign agent exists &mdash; it is the machinery: automated, AI-targeted, self-dealing, and fingerprintable.</strong>",
 "---",
 H("The hard, citable facts"),
 B("<strong>[confirmed]</strong> <strong>Clock Tower X LLC</strong> (sole owner Brad Parscale, signed under penalty of perjury) registered as <strong>FARA #7649</strong> on 18 Sep 2025; foreign principal the <strong>State of Israel via Havas Media Germany</strong>. <span style='color:var(--text3)'>(<a href=\""+REG+"\" style=\"color:var(--accent)\">filing</a>; <a href=\""+HILL+"\" style=\"color:var(--accent)\">The Hill</a>)</span>"),
 B("<strong>[confirmed]</strong> Contract <strong>$6m, expanded to ~$9m</strong> (Dec 2025 amendment). <strong>[reported]</strong> ~<strong>$15m paid</strong> by mid-2026."),
 B("<strong>[confirmed]</strong> One of <strong>at least five FARA registrants</strong> in the same Israel&rarr;Havas push: Clock Tower X (#7649), Show Faith by Works (#7653, evangelical), Bridges Partners (#7652, the &lsquo;Esther Project&rsquo;), Davis Media NY (#7662), and the earlier SKDK (#7552, terminated)."),
 B("<strong>[reported]</strong> Onward money: ~$6m to <strong>SparkFire Technologies</strong> (AI chatbots/texting), ~$5m to Mike Shields&rsquo; <strong>Portman Road Strategies</strong>, &gt;$500k to <strong>Salem Media Representatives</strong> &mdash; the self-dealing loop, since Parscale is <strong>Salem Media&rsquo;s Chief Strategy Officer</strong>. <span style='color:var(--text3)'>(<a href=\""+INT+"\" style=\"color:var(--accent)\">The Intercept</a>)</span>"),
 B("<strong>[confirmed by our own check]</strong> The <strong>12-site advocacy network is one operator</strong> &mdash; nine sites on a single Cloudflare account (identical IPs/stack), registered in two ~10-minute bursts (18 Sep &amp; 10 Oct 2025), with <code>factsignal.org</code> as the hub. <strong>Every site carries the FARA disclosure footer</strong> (labeled, not hidden)."),
 B("<strong>[reported, from the filing&rsquo;s scope of work]</strong> Built to influence AI outputs via the <strong>MarketBrew</strong> SEO tool, the content network, Salem authority-laundering and SparkFire&rsquo;s chatbot funnel; ~80% Gen-Z targeted. <span style='color:var(--text3)'>(<a href=\""+SLUDGE+"\" style=\"color:var(--accent)\">Sludge</a>; <a href=\""+WEX+"\" style=\"color:var(--accent)\">Washington Examiner</a>)</span>"),
 B("<strong>[effect not established]</strong> Reporters could not get ChatGPT, Gemini, Claude or Grok to cite the network; there is <strong>no OpenAI or Anthropic deal</strong>. State it as intent, not proven effect. <span style='color:var(--text3)'>(<a href=\""+SNOPES+"\" style=\"color:var(--accent)\">Snopes</a>)</span>"),
 B("<strong>[confirmed negative]</strong> <strong>No documented tie to Palantir.</strong>"),
 "---",
 H("What is original here &mdash; and what is not (please credit)"),
 "Honesty is the point of this kit. <strong>The core story was first reported by others</strong> &mdash; <a href=\""+RS+"\" style=\"color:var(--accent)\">Responsible Statecraft</a> (Quincy Institute) and <a href=\""+INT+"\" style=\"color:var(--accent)\">The Intercept</a>, with Sludge, Jack Poulson, the Washington Examiner, Axios, Haaretz, Times of Israel and Snopes. <strong>Please credit them.</strong>",
 "What is original to this report: <strong>(1)</strong> the independent <strong>infrastructure forensics</strong> proving the single-operator network; <strong>(2)</strong> the consolidated, tiered, graphic <strong>synthesis + apparatus map</strong>; <strong>(3)</strong> the disciplined <strong>corrections</strong> &mdash; labeled-not-hidden, intent-not-effect, and not-Palantir.",
 "---",
 H("Story angles worth pursuing"),
 B("<strong>The self-dealing loop.</strong> Foreign-state money routed to the agent&rsquo;s own employer (Salem). The cleanest, most under-covered, least-speculative thread."),
 B("<strong>The AI-manipulation machinery</strong> as a template for what disclosed foreign influence now looks like &mdash; and whether platforms can or should detect it."),
 B("<strong>The apparatus, not the man.</strong> Five registrants under one Israel&rarr;Havas structure &mdash; the scale story beyond Parscale."),
 B("<strong>The infrastructure fingerprint.</strong> Reproducible in an afternoon (whois/DNS) &mdash; we invite other researchers to verify and extend it."),
 "---",
 H("The discipline (so you can trust it)"),
 B("Every claim tiered; the spine anchored to <strong>primary FARA filings</strong>, not just press."),
 B("<strong>Labeled, not hidden</strong> &mdash; we do not claim an undisclosed or unlawful network."),
 B("<strong>Intent, not proven effect</strong> &mdash; &ldquo;built to bend AI,&rdquo; not &ldquo;bent AI.&rdquo;"),
 B("Israel&rsquo;s <strong>~$150m budget is global</strong>; the documented US tranche is a subset."),
 B("Apparatus nodes kept <strong>distinct</strong> (the church-geofencing is a separate registrant); and this FARA-registered foreign operation is <strong>distinct from domestic advocacy</strong> like AIPAC."),
 "---",
 H("Evidence &amp; reuse"),
 B("<strong>Full report:</strong> <a href=\"/writing/brad-parscale-israel\" style=\"color:var(--accent)\">brandonmyers.net/writing/brad-parscale-israel</a> &mdash; stat band, apparatus map, infrastructure table, AI-architecture, money flow, sources."),
 B("<strong>Evidence dossier &amp; graphics</strong> (free to use): <a href=\""+REPO+"\" style=\"color:var(--accent)\">GitHub</a>."),
 B("<strong>Primary filings:</strong> DOJ FARA eFile, registrant <a href=\""+FARA+"\" style=\"color:var(--accent)\">#7649</a>."),
 B("<strong>Contact:</strong> <a href=\"/contact\" style=\"color:var(--accent)\">brandonmyers.net/contact</a> &mdash; happy to walk a reporter through the sourcing or the infrastructure check."),
 "<em style='color:var(--text3);font-size:.9rem;display:block;margin-top:8px'>Public sources only; no non-public system was accessed. Allegations are labelled and not asserted as fact. This is not legal advice.</em>",
]

FAQ=[
 ("Is this covert foreign interference?","No - it is disclosed, FARA-registered foreign influence. The operation is filed with the US Department of Justice and its websites carry the foreign-agent disclosure. The public-interest concern is the scale, the AI-targeting, and the self-dealing, not concealment."),
 ("What is original in this report vs. prior reporting?","The core story was first reported by Responsible Statecraft and The Intercept and others, who should be credited. Original here: the independent infrastructure forensics confirming a single-operator site network, the consolidated tiered synthesis with graphics, and the disciplined corrections."),
 ("Is Brad Parscale connected to Palantir?","No documented connection. The investigation specifically tested and ruled that out."),
]
essay={
 "title":"Press & Media Kit — Brad Parscale & the Israeli AI-Influence Apparatus",
 "label":"Press · Free to Republish",
 "date":"June 2026",
 "series_slug":"parscale-press",
 "seo_title":"Press Kit: Brad Parscale & Israel's AI-Influence Apparatus",
 "seo_description":"Free press/media kit for the investigation into Brad Parscale's Clock Tower X and the FARA-registered Israeli AI-influence apparatus: the citable facts, the original infrastructure forensics, story angles, and the evidence - free to republish.",
 "seo_keywords":"Brad Parscale, Clock Tower X, FARA 7649, Israel influence, Havas Media, press kit, media kit, AI influence, foreign agent, SparkFire, Salem Media",
 "seo_about":[{"@type":"Person","name":"Brad Parscale","sameAs":"https://en.wikipedia.org/wiki/Brad_Parscale"}],
 "faq":FAQ,
 "og_image":"/static/og/parscale-israel-card.png",
 "content":content,
}
body=repr(essay)
block=("\n\n\n# -*- coding: utf-8 -*-\n# Appended 2026-06-28: Parscale-Israel PRESS KIT.\n"
 'ESSAYS["parscale-press"] = '+body+"\n")
p=b+"host_live_essays.py"
src=pathlib.Path(p).read_text()
mark="# Appended 2026-06-28: Parscale-Israel PRESS KIT."
i=src.find(mark)
if i!=-1:
    cut=src.rfind("\n\n\n",0,i); src=src[:cut if cut!=-1 else i]
src=src.rstrip()+"\n"+block
pathlib.Path(p).write_text(src)
import py_compile; py_compile.compile(p,doraise=True)
ns={}; exec(compile(src,p,"exec"),ns)
e=ns["ESSAYS"]["parscale-press"]; full="".join(e["content"])
print("OK. blocks:",len(e["content"]),"| credit-others:","first reported by others" in full,"| disclosed-framing:","not covert interference" in full,"| faq:",len(e["faq"]))
print("dup-check parscale-press assigns:",src.count('ESSAYS["parscale-press"]'),"| brad post still 1:",src.count('ESSAYS["brad-parscale-israel"]'))
