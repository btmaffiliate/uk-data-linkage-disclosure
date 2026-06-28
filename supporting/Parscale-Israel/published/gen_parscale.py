#!/usr/bin/env python3
"""Parscale/Israel money-and-influence flow. Responsive HTML. Spine = confirmed (primary FARA); onward = reported; tactics = reported."""
import pathlib
B="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"

CSS="""<style>
.pflow{border:1px solid var(--border,#2a323c);border-radius:14px;padding:18px;background:rgba(255,255,255,.02);font-family:var(--sans,-apple-system,Helvetica,Arial,sans-serif);color:#c2cbd5}
.pflow .node{border-radius:11px;padding:12px 15px;margin:0 auto;max-width:560px;text-align:center;border:1px solid}
.pflow .n-conf{border-color:#3fd07f66;background:#0e1a12}
.pflow .n-spine{border-color:#5aa9ff66;background:#0c1622}
.pflow .nt{color:#fff;font-weight:700;font-size:1rem}
.pflow .ns{color:#9aa7b4;font-size:.8rem;margin-top:2px}
.pflow .arr{text-align:center;color:#5b6b7a;font-size:.74rem;font-family:var(--mono,monospace);margin:7px 0;letter-spacing:.03em}
.pflow .arr b{color:#c2cbd5}
.pflow .arr:before{content:"\\2193";display:block;color:#39475a;font-size:1.1rem;margin-bottom:2px}
.pflow .fan{display:flex;flex-wrap:wrap;gap:8px;margin-top:4px}
.pflow .leaf{flex:1 1 230px;border:1px dashed #f4b74055;background:rgba(244,183,64,.05);border-radius:9px;padding:8px 11px}
.pflow .leaf b{color:#fff;font-size:.86rem;display:block}
.pflow .leaf span{color:#cdb888;font-size:.76rem}
.pflow .tact{border:1px solid #ff5d5d44;background:rgba(255,93,93,.05);border-radius:10px;padding:11px 14px;margin-top:14px}
.pflow .tact .th{color:#ff8a8a;font-weight:650;font-size:.86rem;margin-bottom:6px}
.pflow .tact ul{margin:0;padding-left:18px}.pflow .tact li{font-size:.84rem;margin:3px 0;color:#e7cccc}
.pflow .tier{font-family:var(--mono,monospace);font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;padding:1px 6px;border-radius:5px;border:1px solid;margin-left:6px;vertical-align:middle}
.pflow .tc{color:#3fd07f;border-color:#3fd07f55}.pflow .tr{color:#f4b740;border-color:#f4b74055}
@media(max-width:560px){.pflow .leaf{flex:1 1 100%}}
</style>"""

FIG=CSS+'''<figure class="diagram"><div class="pflow">
<div class="node n-conf"><div class="nt">State of Israel <span class="tier tc">confirmed</span></div><div class="ns">named in the FARA filing as the supervising foreign principal</div></div>
<div class="arr">supervises / &ldquo;on behalf of&rdquo; &mdash; <b>per FARA #7649</b></div>
<div class="node n-conf"><div class="nt">Havas Media Germany GmbH <span class="tier tc">confirmed</span></div><div class="ns">foreign principal of record (the contracting conduit)</div></div>
<div class="arr">contract <b>reported $6m &rarr; ~$9m</b>; <b>~$15m reportedly paid</b></div>
<div class="node n-spine"><div class="nt">Clock Tower X LLC &mdash; Brad Parscale <span class="tier tc">confirmed</span></div><div class="ns">registered foreign agent &middot; FARA #7649 &middot; sworn 18 Sep 2025</div></div>
<div class="arr">onward sub-contracts <span class="tier tr">reported</span> &mdash; per FARA supplements, via The Intercept</div>
<div class="fan">
<div class="leaf"><b>SparkFire Technologies</b><span>~$6m &middot; AI chatbots / mass texting</span></div>
<div class="leaf"><b>Portman Road Strategies</b><span>~$5m &middot; Mike Shields (GOP operative)</span></div>
<div class="leaf"><b>Salem Media Representatives</b><span>&gt;$500k &middot; Parscale is Salem CSO</span></div>
<div class="leaf"><b>Three Tech</b><span>~$500k</span></div>
</div>
<div class="tact"><div class="th">What the campaign is built to do <span class="tier tr">reported &mdash; from the filing&rsquo;s scope of work, as quoted by press</span></div>
<ul>
<li>Shape generative-AI answers &mdash; <b>ChatGPT, Gemini, Grok</b> &mdash; via SEO and purpose-built content sites</li>
<li><b>~80% of content targeted at Gen-Z</b>; pro-Israel / &ldquo;combat antisemitism&rdquo; messaging</li>
<li>Faith / church audience integration through Salem Media</li>
</ul></div>
</div><figcaption>The documented spine (Israel &rarr; Havas &rarr; Clock Tower X / Parscale) is confirmed from the sworn FARA filing; the onward payments and tactics are reported from the filing&rsquo;s supplements and scope of work. He is not in the surveillance stack &mdash; he is in the influence layer beside it.</figcaption></figure>'''

pathlib.Path(B+"parscale_embed.txt").write_text(FIG)
pathlib.Path(B+"parscale.html").write_text(f"<!doctype html><meta charset=utf-8><body style='margin:0;background:#0b0d10;color:#e7edf3;padding:26px;width:760px'>{FIG}</body>")
print("parscale flow graphic built; bytes:",len(FIG),"| has ''':", "'''" in FIG)
