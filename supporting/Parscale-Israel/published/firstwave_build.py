#!/usr/bin/env python3
import pathlib, re, markdown
b="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"
G=pathlib.Path(b+"firstwave_embed.txt").read_text()
assert "'''" not in G and not G.rstrip().endswith("'")
SENT="@@G@@"
MD="/Users/btmaffiliate/uk-data-linkage-disclosure/supporting/Parscale-Israel/AI-INFLUENCE-BEAT.md"
raw=pathlib.Path(MD).read_text()
i=raw.find("## The thesis")
body_md=raw[i:] if i>0 else raw
html=markdown.Markdown(extensions=["extra","tables","sane_lists","toc"]).convert(body_md)
TAGCOL={"confirmed":"#3fd07f","reported":"#f4b740","alleged":"#ff7a7a"}
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
 ".palrep code{font-family:var(--mono,monospace);font-size:.85em;background:#11161c;border:1px solid #232b34;border-radius:5px;padding:1px 5px;color:#cfe3ff}"
 ".palrep .tablewrap{overflow-x:auto;margin:14px 0;border:1px solid var(--border,#2a323c);border-radius:10px}"
 ".palrep table{border-collapse:collapse;width:100%;font-size:.8rem;min-width:560px}"
 ".palrep th,.palrep td{border-bottom:1px solid #1f2730;padding:7px 10px;text-align:left;vertical-align:top}"
 ".palrep th{color:#fff;background:rgba(255,255,255,.03);font-weight:650}</style>")
REPORT=STYLE+'<div class="palrep">'+html+'</div>'
GH="https://github.com/btmaffiliate/uk-data-linkage-disclosure/blob/main/supporting/Parscale-Israel/AI-INFLUENCE-BEAT.md"
content=[
 "<em style='color:var(--text2)'>The bigger frame the <a href=\"/writing/parscale\" style=\"color:var(--accent)\">Parscale investigation</a> opened. Strip away the one man and a pattern is visible: <strong>governments have begun buying the manipulation of what AI tells you.</strong> Israel&rsquo;s FARA-registered contract with Brad Parscale&rsquo;s Clock Tower X is the first <em>disclosed</em> case; Russia&rsquo;s &lsquo;Pravda&rsquo; network is the only state peer in actually shaping model outputs; a commercial industry has industrialized the technique; the poisoning science is settled; and the AI platforms have said almost nothing. No one has connected those into one thesis &mdash; this is that synthesis, with the one honest caveat (does it work?) kept in full view.</em>",
 SENT,
 "<a href=\""+GH+"\" style=\"color:var(--accent)\">&#8599; The full dossier with every per-claim source (GitHub)</a> &nbsp;&middot;&nbsp; companion: <a href=\"/writing/brad-parscale-israel\" style=\"color:var(--accent)\">the Israel/Clock Tower X case</a>.",
 "---",
 REPORT,
]
FAQ=[
 ("Are governments manipulating AI chatbots?","At least two documented state-linked cases exist. Israel, via a FARA-registered contract with Brad Parscale's Clock Tower X, is the first disclosed case of a government paying to shape AI outputs. Russia's 'Pravda' network is the only state peer documented in actually manipulating model outputs. Whether it works is genuinely contested."),
 ("Does AI 'data poisoning' actually work?","It is unsettled. Anthropic and the UK AI Security Institute showed ~250 documents can backdoor a model; NewsGuard found chatbots repeating Russian-network claims ~33% of the time; but a peer-reviewed Harvard study found a much smaller effect and attributed it to 'data voids, not manipulation.' The honest framing is documented intent and capability, not proven effect."),
 ("Is this the same as using AI to make propaganda?","No - and the distinction matters. Using AI to generate propaganda is widespread (China, Iran, Russia, Saudi). Manipulating AI to change its outputs is the novel frontier, and only two operational cases are documented: Israel (commercial/contractual) and Russia (state)."),
]
essay={
 "title":"The First Wave: How States Started Buying AI-Output Shaping",
 "label":"Investigation · The AI-Influence Beat",
 "date":"June 2026",
 "series_slug":"the-first-wave",
 "seo_title":"The First Wave: States Are Buying AI-Output Shaping",
 "seo_description":"Governments have begun paying to manipulate what AI chatbots say. Israel's FARA-registered Parscale contract is the first disclosed case; Russia's Pravda network the only state peer; a GEO industry and settled poisoning science enable it - while AI platforms stay silent. Tiered, sourced, with the effectiveness dispute in full.",
 "seo_keywords":"AI influence operations, LLM grooming, generative engine optimization, ChatGPT manipulation, Pravda network, Clock Tower X, FARA, data poisoning, Parscale, NewsGuard, Viginum",
 "seo_about":[{"@type":"Thing","name":"AI influence operations"}],
 "faq":FAQ,
 "og_image":"/static/og/parscale-israel-card.png",
 "content":content,
}
bodyrepr=repr(essay).replace(repr(SENT),"_FW_G")
block=("\n\n\n# -*- coding: utf-8 -*-\n# Appended 2026-06-28: THE FIRST WAVE (AI-influence beat) flagship.\n"
 "_FW_G = r'''"+G+"'''\n"
 'ESSAYS["the-first-wave"] = '+bodyrepr+"\n")
p=b+"host_live_essays.py"
src=pathlib.Path(p).read_text()
mark="# Appended 2026-06-28: THE FIRST WAVE (AI-influence beat) flagship."
ix=src.find(mark)
if ix!=-1:
    cut=src.rfind("\n\n\n",0,ix); src=src[:cut if cut!=-1 else ix]
src=src.rstrip()+"\n"+block
pathlib.Path(p).write_text(src)
import py_compile; py_compile.compile(p,doraise=True)
ns={}; exec(compile(src,p,"exec"),ns)
e=ns["ESSAYS"]["the-first-wave"]; full="".join(e["content"])
print("OK. blocks:",len(e["content"]),"| graphic:","fw" in full and "Anatomy" in full,"| report:","palrep" in full,"| assigns:",src.count('ESSAYS["the-first-wave"]'))
