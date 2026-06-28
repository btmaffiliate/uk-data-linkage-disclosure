#!/usr/bin/env python3
"""Two graphics: SparkFire vendor profile + the Esther Project influencer gap. Responsive HTML."""
import pathlib
B="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"

CSS="""<style>
.op{font-family:var(--sans,-apple-system,Helvetica,Arial,sans-serif);color:#c2cbd5;border:1px solid var(--border,#2a323c);border-radius:14px;padding:18px;background:rgba(255,255,255,.02)}
.op h4{margin:0 0 3px;color:#fff;font-family:var(--display,Georgia,serif);font-size:1.15rem}
.op .sub{color:#9aa7b4;font-size:.82rem;margin:0 0 14px}
.op .node{border-radius:10px;padding:11px 13px;border:1px solid;margin:0 0 8px}
.op .nh{color:#fff;font-weight:700;font-size:.95rem}
.op .ns{color:#9aa7b4;font-size:.8rem;margin-top:2px;line-height:1.45}
.op .ar{text-align:center;color:#5b6b7a;font-size:.74rem;font-family:var(--mono,monospace);margin:7px 0}
.op .row{display:flex;flex-wrap:wrap;gap:7px;margin:6px 0}
.op .chip{flex:1 1 200px;border:1px solid var(--border,#2a323c);border-radius:8px;padding:7px 10px;background:#0b0d10;font-size:.82rem}
.op .chip b{color:#fff;display:block;font-size:.84rem}
.op .chip span{color:#9aa7b4;font-size:.76rem}
.op .pill{font-family:var(--mono,monospace);font-size:.58rem;font-weight:700;text-transform:uppercase;letter-spacing:.03em;padding:0 5px;border-radius:4px;border:1px solid var(--c);color:var(--c)}
.op .tc{--c:#3fd07f}.op .tr{--c:#f4b740}.op .tg{--c:#8a93a0}
.op .gapbox{border:1px dashed #f4b74077;background:rgba(244,183,64,.06);border-radius:10px;padding:11px 14px}
.op .gapbox b{color:#f4d58a}
.op .x{border:1px solid #ff5d5d44;background:rgba(255,93,93,.05);border-radius:9px;padding:8px 11px;font-size:.8rem;color:#e7c3c3}
@media(max-width:560px){.op .chip{flex:1 1 100%}}
</style>"""

# Graphic A: SparkFire
PACS=[("Never Back Down","$120k · pro-DeSantis PAC"),("Sentinel Action Fund","~$123k · Heritage-linked"),
 ("Hardworking Americans","$150k · GOTV texts"),("First Principles PAC","$200k · Leo &lsquo;Lexington&rsquo; network"),
 ("And Justice for All","$134k · voter-contact"),("State Action Fund","~$38k")]
pac="".join(f'<div class="chip"><b>{a}</b><span>{b}</span></div>' for a,b in PACS)
A=CSS+('<figure class="diagram"><div class="op"><h4>SparkFire Technologies &mdash; persuasion-for-hire</h4>'
 '<p class="sub">The AI-texting vendor at the operational core &mdash; barely covered anywhere. Profiled from its own site, FARA-sourced reporting, and FEC records.</p>'
 '<div class="node tc" style="border-color:#3fd07f55;background:#0e1a12"><div class="nh">SparkFire Technologies, LLC <span class="pill tc">confirmed</span></div>'
 '<div class="ns">Atlanta; founded <strong>March 2023</strong> by <strong>Jeremy Haile</strong> (CEO) &amp; <strong>Tree McGlown</strong> (Pres.) &mdash; both ex-Sideqik (influencer-marketing). Unfunded. Product: the &ldquo;flywheel,&rdquo; AI persuasion texting marketed explicitly to <strong>Political / Government / Advocacy</strong>.</div></div>'
 '<div class="ar">&uarr; paid >$6m by &nbsp;|&nbsp; &darr; runs</div>'
 '<div class="row"><div class="chip" style="border-color:#ff5d5d55"><b>&larr; Clock Tower X (Israel/Havas)</b><span>&gt;$6m for &ldquo;Direct Engagement&rdquo; <span class="pill tc">confirmed (filing-sourced)</span></span></div>'
 '<div class="chip" style="border-color:#f4b74055"><b>&rarr; the fake-persona texts</b><span>&ldquo;Friends for Peace&rdquo;/&ldquo;Partners in Peace&rdquo; &mdash; no disclosure on the texts; self-claimed 45% conversion <span class="pill tr">reported</span></span></div></div>'
 '<div style="font-family:var(--mono);font-size:.66rem;text-transform:uppercase;letter-spacing:.06em;color:#9aa7b4;margin:12px 0 6px">Its independent client book &mdash; a GOP texting vendor first (FEC, ~$641k) <span class="pill tc">confirmed</span></div>'
 f'<div class="row">{pac}</div>'
 '<div class="x" style="margin-top:10px">Discipline: the First-Principles&ndash;to&ndash;Leonard-Leo link is a <strong>vendor</strong> relationship (SparkFire texts for many committees) &mdash; an ecosystem data-point, <strong>not</strong> a Parscale&ndash;Leo tie. Do not inflate it.</div>'
 '</div><figcaption>SparkFire: not a shell spun up for the job, but a persuasion-martech firm whose influence use-case is core &mdash; contracted into the Israel operation while already texting for conservative PACs. Founders, money-in, money-out, and client book, sourced.</figcaption></figure>')

# Graphic B: Esther gap
B_G=CSS+('<figure class="diagram"><div class="op"><h4>The Esther Project &mdash; the gap</h4>'
 '<p class="sub">Israel&rsquo;s paid-influencer track (a separate registrant from Parscale&rsquo;s). The central open question &mdash; <em>who are the influencers?</em> &mdash; is precisely located here.</p>'
 '<div class="node tc" style="border-color:#5aa9ff55;background:#0c1622"><div class="nh">Bridges Partners LLC <span class="pill" style="--c:#5aa9ff;color:#5aa9ff">confirmed</span></div>'
 '<div class="ns">FARA #7652 &middot; principals Uri Steinberg &amp; Yair Levi &middot; via Havas, on behalf of Israel&rsquo;s MFA &middot; up to <strong>~$900k</strong>; ~$200k advance; influencers paid <strong>~$7k/post</strong>.</div></div>'
 '<div class="ar">&darr; recipients NAMED in the filings</div>'
 '<div class="row"><div class="chip"><b>Nadav Shtrauchler &mdash; $15k</b><span>Israeli comms consultant (ex-IDF spokesperson)</span></div>'
 '<div class="chip"><b>Pnina Rezidor &mdash; $10k</b><span>Israeli digital strategist</span></div></div>'
 '<div class="ar">&darr; but the actual US influencers&hellip;</div>'
 '<div class="gapbox"><b>14&ndash;18 paid US influencers &mdash; UNNAMED</b> <span class="pill tr">the gap</span><br>'
 '<span style="font-size:.83rem;color:#e7d9b3">Redacted in the filings; <strong>not one identified</strong> in any report. The document that would crack it: <strong>the Bridges FARA <em>supplemental statement</em></strong> &mdash; which itemizes recipients &mdash; has not been disclosed. Public Citizen + Quincy demanded DOJ force it; <strong>DOJ has not acted.</strong></span></div>'
 '<div class="x" style="margin-top:9px">Do NOT name names: the influencers who circulated early (Savetsky, Fischberger) were <strong>explicitly NOT payees</strong> &mdash; JTA ran a correction and both denied payment. The roster is genuinely unknown.</div>'
 '</div><figcaption>The Esther Project influencer gap, precisely mapped: the named Israeli back-office recipients vs. the unnamed US influencer cohort, and the exact missing document (the FARA supplemental) that would close it. A clean, actionable open lead.</figcaption></figure>')

pathlib.Path(B+"sparkfire_embed.txt").write_text(A)
pathlib.Path(B+"esther_embed.txt").write_text(B_G)
pathlib.Path(B+"operatives.html").write_text(f"<!doctype html><meta charset=utf-8><body style='margin:0;background:#0b0d10;color:#e7edf3;padding:24px;width:860px'>{A}<div style='height:20px'></div>{B_G}</body>")
print("built sparkfire+esther; bytes:",len(A),len(B_G),"| safe:", "'''" not in A and "'''" not in B_G)
