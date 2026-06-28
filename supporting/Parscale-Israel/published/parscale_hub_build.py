#!/usr/bin/env python3
import pathlib
b="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"
TL=pathlib.Path(b+"pscale_timeline_embed.txt").read_text()
assert "'''" not in TL and not TL.rstrip().endswith("'")
SENT="@@TL@@"
REPO="https://github.com/btmaffiliate/uk-data-linkage-disclosure/tree/main/supporting/Parscale-Israel"

def H(t,s="1.3rem"): return "<strong style='font-family:var(--display);font-size:"+s+";color:var(--white);display:block;margin-top:8px'>"+t+"</strong>"
def B(t): return "<span style='display:block;padding-left:4px'>&bull; "+t+"</span>"
def PART(n,slug,title,desc): return "<span style='display:block;padding-left:4px'>"+n+". <a href=\"/writing/"+slug+"\" style=\"color:var(--accent);font-weight:600\">"+title+"</a> &mdash; "+desc+"</span>"

content=[
 "<em style='color:var(--text2)'>A standing investigation into <strong>Brad Parscale</strong> &mdash; Trump&rsquo;s former campaign manager, now a foreign-government influence contractor. The honest through-line, stated so the rest can be trusted: <strong>he is the builder of a deceptive persuasion <em>machine</em> &mdash; for hire, foreign and domestic &mdash; not the disinformation mastermind of legend.</strong> Every claim is tiered (confirmed / reported / alleged) and every tactic classified; the core stories were broken by others (credited throughout), and what is original here &mdash; the infrastructure forensics and the consolidated record &mdash; is marked as such.</em>",
 SENT,
 "---",
 H("The investigation","1.5rem"),
 PART("1","parscale-information-operations","The Machine, Not the Mastermind","the complete information-operations record, 2011&ndash;2026, with the myths (Stop the Steal, the Cambridge Analytica legend) corrected."),
 PART("2","brad-parscale-israel","Registered Foreign Agent for Israel","the FARA-registered Clock Tower X AI-influence apparatus &mdash; built, in its own filing, to bend ChatGPT, Gemini and Claude."),
 PART("3","parscale-latin-america","The Machine Goes South","the Numen operation across Argentina, Bolivia and Honduras &mdash; Parscale built the machine; a documented disinformation operator drives it."),
 PART("4","parscale-press","Press &amp; media kit","the citable facts, the original infrastructure forensics, and the story angles &mdash; free to republish."),
 "---",
 H("The headline findings"),
 B("<strong>Foreign agent, documented.</strong> Clock Tower X LLC (Parscale, sole owner) is a registered foreign agent for the <strong>State of Israel via Havas Media</strong> (FARA #7649) &mdash; a disclosed AI-influence operation; <strong>$6m&rarr;~$9m</strong>, ~$15m reported paid."),
 B("<strong>Original to this work:</strong> our own infrastructure forensics proved the operation&rsquo;s 12 &lsquo;independent&rsquo; advocacy sites are <strong>one operator</strong> (shared Cloudflare account, ~10-minute registration bursts, a single hub) &mdash; reproducible by anyone with whois/DNS."),
 B("<strong>The foreign-elections machine.</strong> Through the consultancy <strong>Numen</strong>, Parscale&rsquo;s data/targeting stack helped win elections in Argentina, Bolivia and Honduras &mdash; alongside Fernando Cerimedo, who carries a documented disinformation record (Brazil 2022)."),
 B("<strong>His own documented deception</strong> sits in the 2020 campaign he ran: doctored Biden ads, census-impersonation ads Facebook removed."),
 "---",
 H("The discipline (and the credits)"),
 "The core stories were <strong>first reported by others</strong> &mdash; The Intercept and Responsible Statecraft (the Israel contract), The New York Times and El Pa&iacute;s Bolivia (the Latin American work), ProPublica, Channel 4, DFRLab and the CLIP consortium. They are credited throughout. This investigation&rsquo;s contribution is the <strong>independent verification, the consolidated and tiered record, and the corrections</strong> &mdash; including, just as plainly, what Parscale did <em>not</em> do: he did not run Stop the Steal; the Cambridge Analytica &ldquo;psychographics&rdquo; legend is overstated; the WinRed donation scam and the Brazil hoax were other people. A record that corrects the myths against its own subject is the kind that holds.",
 "---",
 H("The evidence"),
 B("<strong>Full evidence archive</strong> (dossiers, the career record, the LatAm dossier, the network print-screens, graphics &amp; generators): <a href=\""+REPO+"\" style=\"color:var(--accent)\">GitHub</a>."),
 B("<strong>Primary filings:</strong> DOJ FARA eFile, registrant <a href=\"https://efile.fara.gov/\" style=\"color:var(--accent)\">#7649</a>; FEC, Brazilian TSE, US court records &mdash; all cited per-claim in the dossiers."),
 "<em style='color:var(--text3);font-size:.9rem;display:block;margin-top:8px'>Built from public records only; allegations are labelled and not asserted as fact; not legal advice.</em>",
]
FAQ=[
 ("Who is Brad Parscale?","Trump's 2016 digital director and 2020 campaign manager, founder of Campaign Nucleus, and - since 2025 - a registered foreign agent for the State of Israel via his firm Clock Tower X. He builds political data-and-targeting and influence infrastructure for clients foreign and domestic."),
 ("Is Brad Parscale a foreign agent?","Yes - documented in his own sworn FARA filing (#7649, 18 September 2025), as an agent of the State of Israel via Havas Media Germany."),
 ("Did Parscale run Stop the Steal or Jan 6?","No. He was demoted in July 2020 and withdrew before the election; released texts show he privately blamed Trump and told rioters to stop."),
 ("Is Parscale connected to Palantir?","No. This investigation specifically tested and ruled that out."),
]
essay={
 "title":"The Parscale Investigation",
 "label":"Investigation · Index",
 "date":"June 2026",
 "series_slug":"parscale",
 "seo_title":"The Brad Parscale Investigation: The Complete Record",
 "seo_description":"A standing, source-verified investigation into Brad Parscale: the FARA-registered Israeli AI-influence operation, the Latin American election machine, the complete 2011-2026 information-operations record, and a free media kit.",
 "seo_keywords":"Brad Parscale, Brad Parscale investigation, Clock Tower X, FARA, Numen, Cerimedo, Campaign Nucleus, foreign agent, disinformation, influence operations",
 "seo_about":[{"@type":"Person","name":"Brad Parscale","sameAs":"https://en.wikipedia.org/wiki/Brad_Parscale"}],
 "faq":FAQ,
 "og_image":"/static/og/parscale-israel-card.png",
 "content":content,
}
bodyrepr=repr(essay).replace(repr(SENT),"_HUB_TL")
block=("\n\n\n# -*- coding: utf-8 -*-\n# Appended 2026-06-28: Parscale INVESTIGATION HUB.\n"
 "_HUB_TL = r'''"+TL+"'''\n"
 'ESSAYS["parscale"] = '+bodyrepr+"\n")
p=b+"host_live_essays.py"
src=pathlib.Path(p).read_text()
mark="# Appended 2026-06-28: Parscale INVESTIGATION HUB."
ix=src.find(mark)
if ix!=-1:
    cut=src.rfind("\n\n\n",0,ix); src=src[:cut if cut!=-1 else ix]
src=src.rstrip()+"\n"+block
pathlib.Path(p).write_text(src)
import py_compile; py_compile.compile(p,doraise=True)
ns={}; exec(compile(src,p,"exec"),ns)
e=ns["ESSAYS"]["parscale"]; full="".join(e["content"])
print("OK hub. blocks:",len(e["content"]),"| timeline:","ptl" in full,"| 4 parts:",full.count("/writing/parscale")>=3 and "/writing/brad-parscale-israel" in full,"| assigns:",src.count('ESSAYS["parscale"]'))
