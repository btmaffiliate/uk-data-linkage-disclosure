#!/usr/bin/env python3
import pathlib
b="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"
REPO="https://github.com/btmaffiliate/uk-data-linkage-disclosure"

def H(t,s="1.5rem"): return "<strong style='font-family:var(--display);font-size:"+s+";color:var(--white);display:block;margin-top:8px'>"+t+"</strong>"
def L(slug,title,desc): return "<span style='display:block;padding-left:4px'>&bull; <a href=\"/writing/"+slug+"\" style=\"color:var(--accent);font-weight:600\">"+title+"</a> &mdash; "+desc+"</span>"

content=[
 "<em style='color:var(--text2)'>A standing body of <strong>public-interest, source-verified investigations</strong> into how power joins up, surveils, and influences &mdash; the data state and the influence machine. Everything here is built from public records, tiered <strong>confirmed / reported / alleged</strong>, adversarially fact-checked, and disciplined to credit who broke what and to correct the myths as plainly as the findings. The full evidence &mdash; every contract, citation, primary filing and archived source &mdash; is in the <a href=\""+REPO+"\" style=\"color:var(--accent)\">public repository</a>.</em>",
 "---",
 H("I. The data state &mdash; surveillance &amp; record-linkage"),
 "How governments quietly join up the separate records they hold on you, and who runs the operational layer.",
 L("splink","The Splink Investigation","the nine-part series on the UK government&rsquo;s record-linkage tool &mdash; lawful, undisclosed, and sliding from statistics into live operations. Start at the hub."),
 L("palantir-footprint","Palantir: The Global Footprint","the 16-sector, source-verified catalog of every Palantir deployment worldwide &mdash; and every court, regulator and investor pushing back."),
 L("the-us-database","The US Database","how ICE joins up government, biometric and commercial records to locate people for removal &mdash; the American counterpart, from the government&rsquo;s own files."),
 L("the-city-of-london","The City of London","unaccountable by design: the Square Mile&rsquo;s governance, its private fortune beyond Freedom of Information, and the national fraud database it runs."),
 "---",
 H("II. The Parscale investigation &mdash; the influence machine"),
 "Trump&rsquo;s former campaign manager, now a foreign-government influence contractor. The honest through-line: <strong>he builds a deceptive persuasion machine, for hire, foreign and domestic &mdash; not the disinformation mastermind of legend.</strong>",
 L("parscale","The Parscale Investigation","the full dossier &mdash; start here. Four interlinked parts + the evidence archive."),
 L("parscale-information-operations","&mdash; The Machine, Not the Mastermind","the complete information-operations record, 2011&ndash;2026, myths corrected."),
 L("brad-parscale-israel","&mdash; Registered Foreign Agent for Israel","the FARA Clock Tower X AI-influence apparatus, built to bend ChatGPT and Claude."),
 L("parscale-latin-america","&mdash; The Machine Goes South","the Numen operation across Argentina, Bolivia and Honduras."),
 L("parscale-press","&mdash; Press &amp; media kit","the citable facts and original forensics, free to republish."),
 "---",
 H("III. Emerging &mdash; the AI-influence beat"),
 "The bigger frame the Parscale work opened: <strong>the first wave of states buying AI-output shaping.</strong> Israel/Parscale is the first FARA-disclosed case; Russia&rsquo;s &lsquo;Pravda&rsquo; network is the only state peer; a commercial &ldquo;generative engine optimization&rdquo; industry has industrialized the technique; and the AI platforms have stayed publicly silent. The working dossier (and the preserved primary FARA filings) is in the <a href=\""+REPO+"/tree/main/supporting/Parscale-Israel\" style=\"color:var(--accent)\">evidence repository</a>.",
 "---",
 H("The thread that connects them","1.3rem"),
 "One throughline runs through all of it: <strong>the most consequential systems &mdash; the ones that surveil, sort, and persuade whole populations &mdash; increasingly operate with the oversight switched off.</strong> Under-threshold or sole-source contracts, no published impact assessments, foreign ownership at the operational end, disclosed influence that almost no one is told about. The work doesn&rsquo;t allege crimes; it documents the accountability gap &mdash; and asks the prior question nobody was asked.",
 "---",
 H("Method &amp; evidence","1.3rem"),
 "Every claim is tiered and sourced to primary documents where they exist (FARA filings, FEC records, court rulings, procurement notices). Allegations are labelled and never asserted as fact; the strongest claims others made first are credited to them; and what is <em>not</em> established &mdash; the overstatements and myths &mdash; is corrected as plainly as the findings. Full repository, primary filings, graphics and archived sources: <a href=\""+REPO+"\" style=\"color:var(--accent)\">github.com/btmaffiliate/uk-data-linkage-disclosure</a>. Built from public sources only; not legal advice.",
]
FAQ=[
 ("What are these investigations about?","How power joins up, surveils and influences populations - the 'data state' (government record-linkage, Palantir, ICE) and the 'influence machine' (Brad Parscale's foreign-government AI-influence work). All built from public records, tiered confirmed/reported/alleged."),
 ("Who is behind them?","Brandon Myers, an independent public-interest researcher (brandonmyers.net). The work synthesizes and independently verifies public records; where others broke a story first, they are credited."),
 ("Are these allegations of crimes?","No. The work documents accountability gaps from public documents; it labels allegations as allegations and does not assert wrongdoing. The point is the prior question - should this happen with the oversight switched off?"),
]
essay={
 "title":"The Investigations",
 "label":"Public-Interest Investigations · Index",
 "date":"2026",
 "series_slug":"investigations",
 "seo_title":"Investigations — Brandon Myers | Surveillance, Data & Influence",
 "seo_description":"A standing body of public-interest, source-verified investigations: the data state (Splink, Palantir, ICE, the City of London) and the influence machine (the Brad Parscale / foreign-government AI-influence investigation).",
 "seo_keywords":"Brandon Myers investigations, Splink, Palantir, Brad Parscale, FARA, ICE, surveillance, data linkage, influence operations, OSINT",
 "seo_about":[{"@type":"Person","name":"Brandon Myers","url":"https://brandonmyers.net/"}],
 "faq":FAQ,
 "og_image":"/static/og/splink.png",
 "content":content,
}
bodyrepr=repr(essay)
block=("\n\n\n# -*- coding: utf-8 -*-\n# Appended 2026-06-28: MASTER INVESTIGATIONS HUB.\n"
 'ESSAYS["investigations"] = '+bodyrepr+"\n")
p=b+"host_live_essays.py"
src=pathlib.Path(p).read_text()
mark="# Appended 2026-06-28: MASTER INVESTIGATIONS HUB."
ix=src.find(mark)
if ix!=-1:
    cut=src.rfind("\n\n\n",0,ix); src=src[:cut if cut!=-1 else ix]
src=src.rstrip()+"\n"+block
pathlib.Path(p).write_text(src)
import py_compile; py_compile.compile(p,doraise=True)
ns={}; exec(compile(src,p,"exec"),ns)
e=ns["ESSAYS"]["investigations"]; full="".join(e["content"])
print("OK hub. blocks:",len(e["content"]),"| splink:","/writing/splink" in full,"| parscale:","/writing/parscale\"" in full,"| palantir:","palantir-footprint" in full,"| assigns:",src.count('ESSAYS["investigations"]'))
