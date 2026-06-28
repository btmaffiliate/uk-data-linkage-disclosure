#!/usr/bin/env python3
import pathlib, re, markdown
b="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"
G=pathlib.Path(b+"capstone_embed.txt").read_text()
assert "'''" not in G and not G.rstrip().endswith("'")
SENT="@@G@@"
MD="/Users/btmaffiliate/uk-data-linkage-disclosure/supporting/CAPSTONE.md"
raw=pathlib.Path(MD).read_text()
i=raw.find("## The one thing to take away")
body_md=raw[i:] if i>0 else raw
html=markdown.Markdown(extensions=["extra","tables","sane_lists","toc"]).convert(body_md)
html=html.replace('<a href="/writing/','<a href="/writing/')  # keep internal links plain
html=re.sub(r'<a href="(https?://[^"]+)"', r'<a target="_blank" rel="noopener" href="\1"', html)
STYLE=("<style>.palrep{font-family:var(--sans,-apple-system,Helvetica,Arial,sans-serif);color:var(--text2,#c2cbd5);line-height:1.64;font-size:.98rem}"
 ".palrep h2{font-family:var(--display,Georgia,serif);color:#fff;font-size:1.45rem;margin:30px 0 6px;padding-top:18px;border-top:1px solid var(--border,#2a323c)}"
 ".palrep p{margin:10px 0}.palrep strong{color:#fff}.palrep em{color:var(--text2)}"
 ".palrep blockquote{border-left:3px solid var(--accent,#5aa9ff);margin:14px 0;padding:6px 16px;background:rgba(90,169,255,.05);color:#dbe7f5;font-size:1.02rem}"
 ".palrep a{color:var(--accent,#5aa9ff);text-decoration:none;border-bottom:1px solid #5aa9ff33}"
 ".palrep ul,.palrep ol{margin:8px 0 8px 1.15rem;padding:0}.palrep li{margin:6px 0}"
 ".palrep hr{border:none;border-top:1px solid var(--border,#2a323c);margin:22px 0}</style>")
REPORT=STYLE+'<div class="palrep">'+html+'</div>'
PDF="/static/the-whole-picture.pdf"
GH="https://github.com/btmaffiliate/uk-data-linkage-disclosure/blob/main/supporting/CAPSTONE.md"
content=[
 "<em style='color:var(--text2)'>The capstone &mdash; one place, everything we found and how it actually connects. Two machines were documented across this work: one that <strong>surveils and sorts</strong> populations, one that <strong>persuades</strong> them. They are <strong>not a single conspiracy</strong> &mdash; and I won&rsquo;t claim they are. What binds them is a pattern, and the pattern is why it&rsquo;s not good: the systems that surveil, sort and persuade whole populations increasingly run <strong>with the oversight switched off</strong>. Built from public records, tiered, and as careful about what is <em>not</em> connected as about what is.</em>",
 SENT,
 "<a href=\""+PDF+"\" style=\"color:var(--accent);font-weight:600\">&#8595; Download the full capstone as a PDF</a> &nbsp;&middot;&nbsp; <a href=\""+GH+"\" style=\"color:var(--accent)\">&#8599; source on GitHub</a> &nbsp;&middot;&nbsp; <a href=\"/writing/investigations\" style=\"color:var(--accent)\">the full index</a>",
 "---",
 REPORT,
]
FAQ=[
 ("Is this all one conspiracy?","No - and the work explicitly refuses that claim. Two distinct machines are documented (surveillance/record-linkage, and influence operations). They share a structural pattern - oversight switched off, foreign ownership/funding at the operational and persuasion ends, AI as the new frontier - not a single hidden network. Tested links that came up empty (e.g. Parscale-Palantir, a Thiel-network web) are stated as plainly as the findings."),
 ("What is the core finding?","An accountability vacuum that recurs in system after system: the most consequential population-scale systems - surveillance, data-linkage, and now AI-mediated persuasion - operate via sole-source or secret contracts, without published impact assessments, often foreign-owned or foreign-funded, and with the public never asked the prior question."),
 ("Is anyone accused of a crime?","No. Everything is built from public records; it documents an accountability gap, labels allegations as allegations, and corrects the myths. The argument is about oversight, not criminality."),
]
essay={
 "title":"The Whole Picture: What It All Adds Up To",
 "label":"Public-Interest Investigation · The Capstone",
 "date":"June 2026",
 "series_slug":"the-whole-picture",
 "seo_title":"The Whole Picture: The Data State & The Influence Machine",
 "seo_description":"The capstone of a 2026 investigation: how the data state (Splink, Palantir, ICE, the City of London) and the influence machine (Parscale, the Israel FARA apparatus, the First Wave of AI-influence) share one pattern - oversight switched off - and what is, and isn't, connected.",
 "seo_keywords":"surveillance, data linkage, Palantir, Splink, Brad Parscale, FARA, AI influence, accountability, investigation, Brandon Myers",
 "seo_about":[{"@type":"Person","name":"Brandon Myers","url":"https://brandonmyers.net/"}],
 "faq":FAQ,
 "og_image":"/static/og/splink.png",
 "content":content,
}
bodyrepr=repr(essay).replace(repr(SENT),"_CAP_G")

INVBLOCK='''# ── Unified cross-investigation nav (interlink everything) ──
_INV_NAV = [
 ("Start here", [("investigations","The Investigations (index)"),("the-whole-picture","The Whole Picture (capstone)")]),
 ("The data state", [("splink","The Splink Investigation"),("palantir-footprint","Palantir: The Global Footprint"),("the-us-database","The US Database"),("the-city-of-london","The City of London")]),
 ("The influence machine", [("parscale","The Parscale Investigation"),("the-first-wave","The First Wave"),("parscale-information-operations","The Complete Record"),("brad-parscale-israel","Foreign Agent for Israel"),("parscale-latin-america","The Machine Goes South"),("parscale-press","Media kit")]),
]
_INV_ALL = ["investigations","the-whole-picture","splink","press","how-splink-works","the-quiet-joining-up","statistics-or-operations","who-uses-splink","ruled-unlawful-next-door","the-operational-twin","palantir-global","the-joined-up-state","splink-ecosystem","palantir-footprint","the-us-database","the-city-of-london","parscale","parscale-information-operations","brad-parscale-israel","parscale-latin-america","parscale-press","the-first-wave"]
for _s in _INV_ALL:
    if _s in ESSAYS:
        ESSAYS[_s]["inv_nav"] = _INV_NAV
        ESSAYS[_s].setdefault("series_slug", _s)
'''

p=b+"host_live_essays.py"
src=pathlib.Path(p).read_text()
# strip prior inv_nav block AND prior capstone block
for mk in ["# ── Unified cross-investigation nav (interlink everything) ──",
           "# Appended 2026-06-28: CAPSTONE"]:
    ix=src.find(mk)
    if ix!=-1:
        cut=src.rfind("\n\n\n",0,ix); src=src[:cut if cut!=-1 else ix].rstrip()+"\n"
capstone_block=("\n\n\n# -*- coding: utf-8 -*-\n# Appended 2026-06-28: CAPSTONE (the whole picture).\n"
 "_CAP_G = r'''"+G+"'''\n"
 'ESSAYS["the-whole-picture"] = '+bodyrepr+"\n")
src=src.rstrip()+"\n"+capstone_block+"\n\n\n"+INVBLOCK
pathlib.Path(p).write_text(src)
import py_compile; py_compile.compile(p,doraise=True)
ns={}; exec(compile(src,p,"exec"),ns)
e=ns["ESSAYS"]["the-whole-picture"]; full="".join(e["content"])
print("OK capstone. blocks:",len(e["content"]),"| graphic:","cap" in full and "two machines" in full,"| report:","palrep" in full,"| pdf link:",PDF in full,"| inv_nav on capstone:","inv_nav" in e,"| whole-picture in nav:", "the-whole-picture" in str(ns["_INV_NAV"]))
