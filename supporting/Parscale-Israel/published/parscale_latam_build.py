#!/usr/bin/env python3
import pathlib, re, markdown
b="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"
G=pathlib.Path(b+"latam_embed.txt").read_text()
assert "'''" not in G and not G.rstrip().endswith("'")
SENT="@@G@@"

MD="/Users/btmaffiliate/uk-data-linkage-disclosure/supporting/Parscale-Israel/LATAM-DOSSIER.md"
raw=pathlib.Path(MD).read_text()
i=raw.find("## The thesis")
body_md=raw[i:] if i>0 else raw
html=markdown.Markdown(extensions=["extra","tables","sane_lists","toc"]).convert(body_md)
TAGCOL={"confirmed":"#3fd07f","reported":"#f4b740","alleged":"#ff7a7a",
 "disinformation":"#ff5d5d","manipulative-legal":"#f4b740","aggressive-legitimate":"#3fd07f"}
def _tag(m):
    k=m.group(1).strip().lower(); col=TAGCOL.get(k)
    if not col: return m.group(0)
    return ('<span style="font-family:var(--mono,monospace);font-size:.66rem;font-weight:700;letter-spacing:.03em;'
            'text-transform:uppercase;color:%s;border:1px solid %s55;border-radius:5px;padding:0 5px;white-space:nowrap">%s</span>'%(col,col,m.group(1)))
html=re.sub(r"\[([A-Za-z][A-Za-z \-/]{2,40})\]", _tag, html)
html=html.replace('<a href="','<a target="_blank" rel="noopener" href="')
html=html.replace("<table>",'<div class="tablewrap"><table>').replace("</table>","</table></div>")
STYLE=("<style>.palrep{font-family:var(--sans,-apple-system,Helvetica,Arial,sans-serif);color:var(--text2,#c2cbd5);line-height:1.62;font-size:.96rem}"
 ".palrep h2{font-family:var(--display,Georgia,serif);color:#fff;font-size:1.4rem;margin:30px 0 6px;padding-top:18px;border-top:1px solid var(--border,#2a323c)}"
 ".palrep h3{font-family:var(--display,Georgia,serif);color:#eaf0f6;font-size:1.08rem;margin:20px 0 4px}"
 ".palrep p{margin:9px 0}.palrep strong{color:#fff}.palrep em{color:var(--text2)}"
 ".palrep a{color:var(--accent,#5aa9ff);text-decoration:none;border-bottom:1px solid #5aa9ff33;word-break:break-word}"
 ".palrep ul,.palrep ol{margin:8px 0 8px 1.15rem;padding:0}.palrep li{margin:5px 0}"
 ".palrep hr{border:none;border-top:1px solid var(--border,#2a323c);margin:22px 0}"
 ".palrep code{font-family:var(--mono,monospace);font-size:.85em;background:#11161c;border:1px solid #232b34;border-radius:5px;padding:1px 5px;color:#cfe3ff}</style>")
REPORT=STYLE+'<div class="palrep">'+html+'</div>'

GH="https://github.com/btmaffiliate/uk-data-linkage-disclosure/blob/main/supporting/Parscale-Israel/LATAM-DOSSIER.md"
content=[
 "<em style='color:var(--text2)'>The companion to the <a href=\"/writing/parscale-information-operations\" style=\"color:var(--accent)\">complete record</a>, expanded. There is a machine that has helped win a string of right-wing elections across Latin America &mdash; and Brad Parscale built its infrastructure. But the machine&rsquo;s driver, and the source of its documented disinformation, is the Argentine operative <strong>Fernando Cerimedo</strong>. That role-split is the whole story, and getting it exactly right is what makes it undismissable: <strong>Parscale built the machine; a documented disinformation operator drives it</strong> &mdash; not &ldquo;Parscale ran Latin American disinformation.&rdquo;</em>",
 SENT,
 "<a href=\""+GH+"\" style=\"color:var(--accent)\">&#8599; The full dossier with every per-claim source (GitHub)</a> &nbsp;&middot;&nbsp; first reported by the NYT (Dec 2025), El Pa&iacute;s Bolivia, and the CLIP consortium &mdash; credited throughout.",
 "---",
 REPORT,
]
FAQ=[
 ("Did Brad Parscale run disinformation in Latin American elections?","Not on the documented record. His role is the data/targeting infrastructure (via the consultancy Numen). The documented disinformation - Brazil's 2022 'stolen election' hoax, fake-account networks, the fraud-narrative playbook - is the record of his partner Fernando Cerimedo. In no country is the disinformation forensically tied to Parscale or Numen."),
 ("What is Numen?","A Buenos Aires political consultancy. It is Cerimedo's pre-existing firm, in which Parscale is described as a partner from around 2023; it advised Milei (Argentina 2023), Paz (Bolivia 2025) and Asfura (Honduras 2025) using Parscale's Campaign Nucleus and EyesOver platforms."),
 ("Did Trump interfere in the Honduras election?","Trump endorsed Asfura and pardoned ex-president Hernandez within days of the November 2025 vote - both benefiting the same party. That is documented co-occurrence. Coordination with Parscale's paid campaign work is neither proven nor disproven; Parscale denies any contact with the administration about it."),
]
essay={
 "title":"The Machine Goes South: Parscale, Numen, and the Latin American Election Operation",
 "label":"Investigation · Foreign Elections · Expanded",
 "date":"June 2026",
 "series_slug":"parscale-latin-america",
 "seo_title":"Brad Parscale in Latin America: Numen, Cerimedo & the Election Machine",
 "seo_description":"How Brad Parscale's data-targeting machine (via the Numen consultancy) traveled into Milei's Argentina, Paz's Bolivia and Asfura's Honduras - in partnership with documented disinformation operator Fernando Cerimedo. Tiered, sourced, role-split.",
 "seo_keywords":"Brad Parscale Latin America, Numen, Fernando Cerimedo, La Derecha Diario, Milei, Rodrigo Paz, Nasry Asfura, Honduras election, Bolivia election, disinformation, Campaign Nucleus, EyesOver",
 "seo_about":[{"@type":"Person","name":"Brad Parscale","sameAs":"https://en.wikipedia.org/wiki/Brad_Parscale"}],
 "faq":FAQ,
 "og_image":"/static/og/parscale-israel-card.png",
 "content":content,
}
bodyrepr=repr(essay).replace(repr(SENT),"_LATAM_G")
block=("\n\n\n# -*- coding: utf-8 -*-\n# Appended 2026-06-28: Parscale LATIN AMERICA / Numen expansion.\n"
 "_LATAM_G = r'''"+G+"'''\n"
 'ESSAYS["parscale-latin-america"] = '+bodyrepr+"\n")
p=b+"host_live_essays.py"
src=pathlib.Path(p).read_text()
mark="# Appended 2026-06-28: Parscale LATIN AMERICA / Numen expansion."
ix=src.find(mark)
if ix!=-1:
    cut=src.rfind("\n\n\n",0,ix); src=src[:cut if cut!=-1 else ix]
src=src.rstrip()+"\n"+block
pathlib.Path(p).write_text(src)
import py_compile; py_compile.compile(p,doraise=True)
ns={}; exec(compile(src,p,"exec"),ns)
e=ns["ESSAYS"]["parscale-latin-america"]; full="".join(e["content"])
print("OK. blocks:",len(e["content"]),"| graphic:","lam" in full,"| report:","palrep" in full,"| frame:","drives it" in full,"| assigns:",src.count('ESSAYS["parscale-latin-america"]'))
