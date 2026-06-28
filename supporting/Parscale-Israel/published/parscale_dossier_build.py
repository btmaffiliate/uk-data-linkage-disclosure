#!/usr/bin/env python3
import pathlib, re, markdown
b="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"
TL=pathlib.Path(b+"pscale_timeline_embed.txt").read_text()
assert "'''" not in TL and not TL.rstrip().endswith("'")
TL_SENT="@@TL@@"

# ---- convert the career dossier MD -> inline HTML ----
MD="/Users/btmaffiliate/uk-data-linkage-disclosure/supporting/Parscale-Israel/CAREER-DOSSIER.md"
raw=pathlib.Path(MD).read_text()
i=raw.find("**Method & integrity.**")
body_md=raw[i:] if i>0 else raw
html=markdown.Markdown(extensions=["extra","tables","sane_lists","toc"]).convert(body_md)

TAGCOL={"confirmed":"#3fd07f","reported":"#f4b740","alleged":"#ff7a7a",
 "disinformation":"#ff5d5d","manipulative-but-legal":"#f4b740","manipulative-legal":"#f4b740",
 "aggressive-legitimate":"#3fd07f","mythology":"#8a93a0","mythology-corrected":"#8a93a0"}
def _tag(m):
    k=m.group(1).strip().lower()
    col=TAGCOL.get(k)
    if not col: return m.group(0)
    return ('<span style="font-family:var(--mono,monospace);font-size:.66rem;font-weight:700;letter-spacing:.03em;'
            'text-transform:uppercase;color:%s;border:1px solid %s55;border-radius:5px;padding:0 5px;white-space:nowrap">%s</span>'
            % (col,col,m.group(1)))
html=re.sub(r"\[([A-Za-z][A-Za-z \-]{2,40})\]", _tag, html)
html=html.replace('<a href="','<a target="_blank" rel="noopener" href="')
html=html.replace("<table>",'<div class="tablewrap"><table>').replace("</table>","</table></div>")

STYLE=("<style>"
 ".palrep{font-family:var(--sans,-apple-system,Helvetica,Arial,sans-serif);color:var(--text2,#c2cbd5);line-height:1.62;font-size:.96rem}"
 ".palrep h2{font-family:var(--display,Georgia,serif);color:#fff;font-size:1.45rem;margin:32px 0 6px;padding-top:18px;border-top:1px solid var(--border,#2a323c)}"
 ".palrep h3{font-family:var(--display,Georgia,serif);color:#eaf0f6;font-size:1.1rem;margin:22px 0 4px}"
 ".palrep p{margin:9px 0}.palrep strong{color:#fff}"
 ".palrep a{color:var(--accent,#5aa9ff);text-decoration:none;border-bottom:1px solid #5aa9ff33;word-break:break-word}"
 ".palrep ul,.palrep ol{margin:8px 0 8px 1.15rem;padding:0}.palrep li{margin:5px 0}"
 ".palrep hr{border:none;border-top:1px solid var(--border,#2a323c);margin:22px 0}"
 ".palrep code{font-family:var(--mono,monospace);font-size:.85em;background:#11161c;border:1px solid #232b34;border-radius:5px;padding:1px 5px;color:#cfe3ff}"
 ".palrep .tablewrap{overflow-x:auto;margin:14px 0;border:1px solid var(--border,#2a323c);border-radius:10px}"
 ".palrep table{border-collapse:collapse;width:100%;font-size:.8rem;min-width:600px}"
 ".palrep th,.palrep td{border-bottom:1px solid #1f2730;padding:7px 10px;text-align:left;vertical-align:top}"
 ".palrep th{color:#fff;background:rgba(255,255,255,.03);font-weight:650}"
 "</style>")
# jump nav from h2 ids
h2s=re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html)
def _clean(t): return re.sub(r"<[^>]+>","",t).strip()
NAVS=("<style>.palnav{border:1px solid var(--border,#2a323c);border-radius:12px;padding:14px 16px;background:rgba(90,169,255,.05);margin:0 0 6px}"
 ".palnav .nh{font-family:var(--mono,monospace);font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent,#5aa9ff);margin-bottom:9px}"
 ".palnav .nl{display:flex;flex-wrap:wrap;gap:6px 9px}.palnav a{color:#c2cbd5;text-decoration:none;font-size:.82rem;border:1px solid var(--border,#2a323c);border-radius:7px;padding:4px 9px;background:#0b0d10}"
 ".palnav a:hover{border-color:var(--accent,#5aa9ff);color:#fff}</style>")
toc="".join(f'<a href="#{i}">{_clean(t)}</a>' for i,t in h2s)
TOC='<figure class="diagram">'+NAVS+f'<div class="palnav"><div class="nh">Jump to a section</div><div class="nl">{toc}</div></div></figure>'
REPORT=STYLE+TOC+'<div class="palrep">'+html+'</div>'

GHM="https://github.com/btmaffiliate/uk-data-linkage-disclosure/blob/main/supporting/Parscale-Israel/CAREER-DOSSIER.md"
content=[
 "<em style='color:var(--text2)'>This is the exhaustive version: Brad Parscale&rsquo;s complete information-operations record, 2011&ndash;2026, built from nine parallel research streams and adversarially verified against primary FARA, FEC and court records. The honest finding, stated up front so the rest can be trusted: <strong>he is the builder of a deceptive persuasion <em>machine</em> &mdash; for hire, foreign and domestic &mdash; not the disinformation mastermind of legend.</strong> Most of the strict-sense disinformation in his orbit belongs to others; what is his is documented below, and what is <em>not</em> his is corrected just as plainly. Every claim is tiered; every tactic is classified.</em>",
 TL_SENT,
 "<a href=\""+GHM+"\" style=\"color:var(--accent)\">&#8599; The full dossier with every per-claim source (GitHub)</a> &nbsp;&middot;&nbsp; companion: <a href=\"/writing/brad-parscale-israel\" style=\"color:var(--accent)\">the Israel/Clock Tower X report</a>.",
 "---",
 REPORT,
]

FAQ=[
 ("Did Brad Parscale run Stop the Steal or Jan 6?","No. He was demoted in July 2020 and withdrew before the election. Released texts show he privately blamed Trump's rhetoric and publicly told rioters to stop. He had no documented operational role in any election-fraud scheme."),
 ("Is Brad Parscale a disinformation operative?","More precisely: he builds deceptive persuasion and targeting machinery. His operation ran demonstrably doctored ads in 2020, and he now runs a foreign-funded AI-influence operation - but much of the strict-sense disinformation associated with his name (the Russian IRA, the WinRed dark patterns, the Brazil 'stolen election' hoax) was the work of others."),
 ("Did Cambridge Analytica's psychographics win 2016?","No - that is overstated and effectively debunked, including by Cambridge Analytica's own executives. The campaign relied on RNC data; the 87-million-profile Facebook harvest was CA's wrongdoing and was never shown to have been used in Trump's targeting."),
 ("Is he connected to Palantir?","No. A separate investigation specifically tested and ruled that out."),
]
essay={
 "title":"Brad Parscale: The Machine, Not the Mastermind",
 "label":"Investigation · The Complete Information-Operations Record",
 "date":"June 2026",
 "series_slug":"parscale-information-operations",
 "seo_title":"Brad Parscale: The Complete Information-Operations Record",
 "seo_description":"An exhaustive, tiered record of Brad Parscale's information operations, 2011-2026 - microtargeting, doctored 2020 ads, Campaign Nucleus, foreign elections, and the FARA Israel AI-influence apparatus - with the myths (Stop the Steal, CA psychographics) corrected.",
 "seo_keywords":"Brad Parscale, Brad Parscale disinformation, Project Alamo, Cambridge Analytica, Campaign Nucleus, WinRed, Clock Tower X, FARA, Numen, Cerimedo, microtargeting, influence operations",
 "seo_about":[{"@type":"Person","name":"Brad Parscale","sameAs":"https://en.wikipedia.org/wiki/Brad_Parscale"}],
 "faq":FAQ,
 "og_image":"/static/og/parscale-israel-card.png",
 "content":content,
}
bodyrepr=repr(essay).replace(repr(TL_SENT),"_PSCALE_TL")
block=("\n\n\n# -*- coding: utf-8 -*-\n# Appended 2026-06-28: Parscale COMPLETE information-operations record.\n"
 "_PSCALE_TL = r'''"+TL+"'''\n"
 'ESSAYS["parscale-information-operations"] = '+bodyrepr+"\n")
p=b+"host_live_essays.py"
src=pathlib.Path(p).read_text()
mark="# Appended 2026-06-28: Parscale COMPLETE information-operations record."
ix=src.find(mark)
if ix!=-1:
    cut=src.rfind("\n\n\n",0,ix); src=src[:cut if cut!=-1 else ix]
src=src.rstrip()+"\n"+block
pathlib.Path(p).write_text(src)
import py_compile; py_compile.compile(p,doraise=True)
ns={}; exec(compile(src,p,"exec"),ns)
e=ns["ESSAYS"]["parscale-information-operations"]; full="".join(e["content"])
print("OK. blocks:",len(e["content"]),"| timeline:","ptl" in full,"| report:","palrep" in full,"| TOC secs:",len(h2s),"| machine-frame:","Machine, Not the Mastermind"==e["title"][len('Brad Parscale: '):])
print("assigns:",src.count('ESSAYS["parscale-information-operations"]'))
