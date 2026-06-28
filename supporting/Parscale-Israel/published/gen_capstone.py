#!/usr/bin/env python3
"""Capstone overview: two halves + shared pattern + honest negatives. Responsive HTML."""
import pathlib
B="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"

CSS="""<style>
.cap{font-family:var(--sans,-apple-system,Helvetica,Arial,sans-serif);color:#c2cbd5;border:1px solid var(--border,#2a323c);border-radius:14px;padding:18px;background:rgba(255,255,255,.02)}
.cap h4{margin:0 0 3px;color:#fff;font-family:var(--display,Georgia,serif);font-size:1.15rem}
.cap .sub{color:#9aa7b4;font-size:.82rem;margin:0 0 14px}
.cap .cols{display:flex;flex-wrap:wrap;gap:10px}
.cap .col{flex:1 1 300px;border-radius:11px;padding:13px 15px;border:1px solid}
.cap .col.a{border-color:#5aa9ff55;background:rgba(90,169,255,.05)}
.cap .col.b{border-color:#ff5d5d55;background:rgba(255,93,93,.05)}
.cap .ct{font-family:var(--mono,monospace);font-size:.64rem;letter-spacing:.08em;text-transform:uppercase;margin-bottom:3px}
.cap .col.a .ct{color:#5aa9ff}.cap .col.b .ct{color:#ff8a8a}
.cap .ch{color:#fff;font-weight:700;font-size:1rem;margin-bottom:9px}
.cap .col a{display:block;color:#cfe3ff;text-decoration:none;font-size:.86rem;margin:5px 0;border-bottom:1px solid transparent}
.cap .col.b a{color:#f0d3d3}
.cap .col a:hover{border-bottom-color:currentColor}
.cap .col a span{color:#9aa7b4;font-size:.78rem}
.cap .band{border:1px solid #a78bfa55;background:rgba(167,139,250,.07);border-radius:11px;padding:12px 15px;margin:12px 0}
.cap .band .bh{color:#c4b5fd;font-weight:650;font-size:.9rem;margin-bottom:6px}
.cap .band .row{display:flex;flex-wrap:wrap;gap:7px}
.cap .band .item{flex:1 1 200px;font-size:.82rem;color:#d8cff0;border-left:2px solid #a78bfa66;padding-left:9px}
.cap .neg{border:1px dashed #3fd07f66;background:rgba(63,208,127,.05);border-radius:11px;padding:12px 15px;margin-top:4px}
.cap .neg .nh{color:#7fe0a6;font-weight:650;font-size:.9rem;margin-bottom:5px}
.cap .neg p{margin:3px 0;font-size:.82rem;color:#bfe8cf}
@media(max-width:600px){.cap .col,.cap .band .item{flex:1 1 100%}}
</style>"""

FIG=CSS+'''<figure class="diagram"><div class="cap">
<h4>The whole picture &mdash; two machines, one pattern</h4>
<p class="sub">Everything documented, in one frame. Two different machines &mdash; not a single conspiracy. What binds them is a pattern, and the pattern is the story.</p>
<div class="cols">
<div class="col a"><div class="ct">Half one</div><div class="ch">The data state &mdash; surveil &amp; sort</div>
<a href="/writing/splink"><b>The Splink Investigation</b> <span>&mdash; UK govt record-linkage, no consent</span></a>
<a href="/writing/palantir-footprint"><b>Palantir: The Global Footprint</b> <span>&mdash; the operational layer, worldwide</span></a>
<a href="/writing/the-us-database"><b>The US Database</b> <span>&mdash; ICE joins up records to find people</span></a>
<a href="/writing/the-city-of-london"><b>The City of London</b> <span>&mdash; unaccountable by design</span></a>
</div>
<div class="col b"><div class="ct">Half two</div><div class="ch">The influence machine &mdash; persuade</div>
<a href="/writing/parscale"><b>The Parscale Investigation</b> <span>&mdash; the machine, not the mastermind</span></a>
<a href="/writing/brad-parscale-israel"><b>Foreign Agent for Israel</b> <span>&mdash; FARA AI-influence apparatus</span></a>
<a href="/writing/parscale-latin-america"><b>The Machine Goes South</b> <span>&mdash; exported into LatAm elections</span></a>
<a href="/writing/the-first-wave"><b>The First Wave</b> <span>&mdash; states buying AI-output shaping</span></a>
</div>
</div>
<div class="band"><div class="bh">What connects them &mdash; the pattern (not a network)</div>
<div class="row">
<div class="item"><b>Oversight off</b> &mdash; sole-source, secret, sub-threshold; no impact assessments</div>
<div class="item"><b>Foreign at the ends</b> &mdash; foreign-owned operational layer; foreign-funded persuasion</div>
<div class="item"><b>AI is the frontier</b> &mdash; the least-visible layer where both sorting &amp; shaping now happen</div>
<div class="item"><b>No one was asked</b> &mdash; the prior question never put to the people it's done to</div>
</div></div>
<div class="neg"><div class="nh">What is NOT connected &mdash; stated as plainly as the rest</div>
<p>&bull; <b>No Parscale&ndash;Palantir tie.</b> Tested directly &mdash; clean negative.</p>
<p>&bull; <b>No Thiel / Silicon-Valley cabal.</b> Run against ~85 names: one documented tie (Kushner), the rest empty. No hidden web.</p>
<p>&bull; <b>Allegations stay allegations</b> (Gaza, the &ldquo;mega-database,&rdquo; AI <em>effectiveness</em>); <b>myths corrected</b> (not Stop the Steal; the CA legend; WinRed/Brazil were others).</p>
</div>
</div><figcaption>The capstone in one image: two documented machines (surveil/sort and persuade), the structural pattern that binds them (oversight off, foreign at the operational and persuasion ends, AI the new frontier), and &mdash; the part that makes it hold &mdash; what was tested and found NOT connected.</figcaption></figure>'''

pathlib.Path(B+"capstone_embed.txt").write_text(FIG)
pathlib.Path(B+"capstone.html").write_text(f"<!doctype html><meta charset=utf-8><body style='margin:0;background:#0b0d10;color:#e7edf3;padding:24px;width:900px'>{FIG}</body>")
print("capstone graphic built; bytes:",len(FIG),"| safe:", "'''" not in FIG)
