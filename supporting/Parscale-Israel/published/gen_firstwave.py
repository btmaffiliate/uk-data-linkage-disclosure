#!/usr/bin/env python3
"""Anatomy of the first wave: states buying AI-output shaping. Responsive HTML."""
import pathlib
B="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"

CSS="""<style>
.fw{font-family:var(--sans,-apple-system,Helvetica,Arial,sans-serif);color:#c2cbd5;border:1px solid var(--border,#2a323c);border-radius:14px;padding:18px;background:rgba(255,255,255,.02)}
.fw h4{margin:0 0 3px;color:#fff;font-family:var(--display,Georgia,serif);font-size:1.15rem}
.fw .sub{color:#9aa7b4;font-size:.82rem;margin:0 0 14px}
.fw .lyr{border-left:3px solid var(--c);border-radius:0 10px 10px 0;background:#0c0f14;padding:11px 14px;margin:0 0 9px}
.fw .ln{font-family:var(--mono,monospace);font-size:.64rem;letter-spacing:.06em;text-transform:uppercase;color:var(--c)}
.fw .lt{color:#fff;font-weight:700;font-size:.98rem;margin:2px 0 4px}
.fw .lp{font-size:.84rem;color:#9aa7b4;line-height:1.5;margin:0}
.fw .two{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 9px}
.fw .case{flex:1 1 280px;border:1px solid var(--c)55;border-radius:10px;padding:11px 13px;background:#0b0d10}
.fw .case b{color:#fff;display:block;font-size:.9rem}
.fw .case span{font-size:.8rem;color:#9aa7b4;display:block;margin-top:3px;line-height:1.45}
.fw .pill{font-family:var(--mono,monospace);font-size:.58rem;font-weight:700;text-transform:uppercase;letter-spacing:.03em;padding:0 5px;border-radius:4px;border:1px solid var(--c);color:var(--c)}
.fw .caveat{border:1px dashed #f4b74066;background:rgba(244,183,64,.06);border-radius:10px;padding:11px 14px;margin-top:4px}
.fw .caveat b{color:#f4d58a}
@media(max-width:560px){.fw .case{flex:1 1 100%}}
</style>"""

FIG=CSS+'''<figure class="diagram"><div class="fw">
<h4>Anatomy of the first wave</h4>
<p class="sub">The components are all in place for governments to buy the manipulation of what AI tells you. Here is what is documented &mdash; and the one thing that isn&rsquo;t settled.</p>

<div class="lyr" style="--c:#5aa9ff"><div class="ln">The technique &mdash; confirmed</div><div class="lt">Shaping what the models say</div><p class="lp">&ldquo;Generative engine optimization&rdquo;: flood the open web and the high-authority sites that LLMs scrape and retrieve, so the model&rsquo;s answer carries your framing. A real, named method &mdash; not science fiction.</p></div>

<div style="font-family:var(--mono);font-size:.64rem;letter-spacing:.06em;text-transform:uppercase;color:#9aa7b4;margin:10px 0 6px">The two documented state cases</div>
<div class="two">
<div class="case" style="--c:#3fd07f"><b>🇮🇱 Israel &rarr; Havas &rarr; Parscale <span class="pill">confirmed</span></b><span>The <strong>first FARA-disclosed</strong> case of a government buying it. Clock Tower X, ~$15m, built in its own filing to bend ChatGPT and Claude. Commercial, contracted, labeled.</span></div>
<div class="case" style="--c:#ff5d5d"><b>🇷🇺 Russia &rarr; the &lsquo;Pravda&rsquo; network <span class="pill">confirmed</span></b><span>The only state <strong>peer in output manipulation</strong>. ~3.6m articles/yr (Viginum&rsquo;s &ldquo;Portal Kombat&rdquo;); NewsGuard found chatbots repeated its claims ~33% of the time. State-run, covert.</span></div>
</div>

<div class="lyr" style="--c:#a78bfa"><div class="ln">The enablers &mdash; confirmed</div><div class="lt">A toolchain and a settled science</div><p class="lp">A legitimate, dual-use <strong>GEO industry</strong> (Profound ~$1bn valuation, Evertune, AthenaHQ) industrialized the technique for brands &mdash; the on-ramp. And the science is settled: <strong>Anthropic + the UK AI Security Institute</strong> showed ~<strong>250 documents</strong> can backdoor a model of any size.</p></div>

<div class="lyr" style="--c:#8a93a0"><div class="ln">The blind spot &mdash; confirmed</div><div class="lt">The platforms have said almost nothing</div><p class="lp">Every major AI threat report covers adversaries <em>using</em> AI &mdash; not adversaries <em>changing</em> it. OpenAI, Google and Microsoft have effectively not publicly acknowledged being targeted. Only Anthropic published the poisoning research.</p></div>

<div class="caveat"><b>The honest caveat &mdash; contested</b><br><span style="font-size:.83rem;color:#e7d9b3">Does it actually work? Unsettled. A peer-reviewed Harvard study found a small (~5%) effect and blamed &ldquo;data voids, not manipulation&rdquo;; NewsGuard found a large one. Reporters couldn&rsquo;t get the models to cite Parscale&rsquo;s network. The right claim is <strong>intent and capability, documented &mdash; not proven effect.</strong></span></div>
</div><figcaption>The first wave: one government has now bought AI-output shaping through the front door of FARA; a state precedent (Russia), a commercial toolchain, and a proven poisoning science are all in place &mdash; while the AI platforms stay publicly silent. Effectiveness remains genuinely contested. Synthesis of reporting by The Intercept, Viginum, NewsGuard, DFRLab, the American Sunlight Project, Anthropic/UK AISI, and the Harvard Misinformation Review.</figcaption></figure>'''

pathlib.Path(B+"firstwave_embed.txt").write_text(FIG)
pathlib.Path(B+"firstwave.html").write_text(f"<!doctype html><meta charset=utf-8><body style='margin:0;background:#0b0d10;color:#e7edf3;padding:24px;width:860px'>{FIG}</body>")
print("firstwave graphic built; bytes:",len(FIG),"| safe:", "'''" not in FIG)
