#!/usr/bin/env python3
"""The machine goes south: Numen/Parscale/Cerimedo LatAm operation. Role-split + tiered. Responsive HTML."""
import pathlib
B="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"

CSS="""<style>
.lam{font-family:var(--sans,-apple-system,Helvetica,Arial,sans-serif);color:#c2cbd5;border:1px solid var(--border,#2a323c);border-radius:14px;padding:18px;background:rgba(255,255,255,.02)}
.lam h4{margin:0 0 3px;color:#fff;font-family:var(--display,Georgia,serif);font-size:1.15rem}
.lam .sub{color:#9aa7b4;font-size:.82rem;margin:0 0 14px}
.lam .firm{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:6px}
.lam .who{flex:1 1 260px;border-radius:10px;padding:11px 13px;border:1px solid}
.lam .pa{border-color:#5aa9ff55;background:#0c1622}.lam .ce{border-color:#ff5d5d55;background:#1a0e10}
.lam .who .nm{color:#fff;font-weight:700;font-size:.95rem}
.lam .who .rl{font-family:var(--mono,monospace);font-size:.62rem;text-transform:uppercase;letter-spacing:.05em;margin:2px 0 5px}
.lam .pa .rl{color:#5aa9ff}.lam .ce .rl{color:#ff8a8a}
.lam .who p{margin:0;font-size:.82rem;color:#9aa7b4;line-height:1.5}
.lam .ar{text-align:center;color:#5b6b7a;font-size:.74rem;font-family:var(--mono,monospace);margin:9px 0 7px}
.lam .camps{display:flex;flex-wrap:wrap;gap:8px}
.lam .camp{flex:1 1 240px;border:1px solid var(--border,#2a323c);border-radius:10px;padding:11px 13px;background:#0b0d10}
.lam .camp .c-h{color:#fff;font-weight:700;font-size:.9rem;margin-bottom:5px}
.lam .camp .row{font-size:.8rem;margin:3px 0;color:#9aa7b4;line-height:1.45}
.lam .camp .row b{color:#cfe3ff;font-weight:600}
.lam .pill{font-family:var(--mono,monospace);font-size:.56rem;font-weight:700;text-transform:uppercase;letter-spacing:.03em;padding:0 5px;border-radius:4px;border:1px solid;white-space:nowrap}
.lam .tc{color:#3fd07f;border-color:#3fd07f55}.lam .tr{color:#f4b740;border-color:#f4b74055}.lam .ta{color:#8a93a0;border-color:#8a93a055}
.lam .origin{border:1px dashed #ff5d5d55;background:rgba(255,93,93,.05);border-radius:10px;padding:10px 13px;margin:12px 0}
.lam .origin b{color:#ff8a8a}
.lam .disc{border-left:3px solid #3fd07f;background:rgba(63,208,127,.05);border-radius:0 10px 10px 0;padding:11px 14px;margin-top:14px}
.lam .disc b{color:#7fe0a6}.lam .disc p{margin:4px 0 0;font-size:.84rem;color:#bfe8cf;line-height:1.55}
@media(max-width:560px){.lam .who,.lam .camp{flex:1 1 100%}}
</style>"""

FIG=CSS+'''<figure class="diagram"><div class="lam">
<h4>The machine goes south</h4>
<p class="sub">One Buenos Aires consultancy &mdash; Numen &mdash; behind a string of right-wing wins across Latin America. The role-split is the whole story: who builds the machine, and who drives it.</p>
<div class="firm">
<div class="who pa"><div class="nm">Brad Parscale <span class="pill tr">partner</span></div><div class="rl">The infrastructure</div><p>Supplies the data/targeting stack &mdash; Campaign Nucleus + EyesOver. Cerimedo: &ldquo;Brad set up all the infrastructure I work with.&rdquo; No documented authorship of any false content.</p></div>
<div class="who ce"><div class="nm">Fernando Cerimedo <span class="pill tc">owner/operator</span></div><div class="rl">The driver &mdash; and the disinformation</div><p>Runs the ground game and the content. Documented disinfo record: ~50,000 self-admitted fake accounts, La Derecha Diario, the fraud-narrative playbook. The lies are his.</p></div>
</div>
<div class="origin"><b>The template&rsquo;s origin &mdash; Brazil 2022 <span class="pill tc">confirmed</span></b><br><span style="font-size:.83rem;color:#e7cccc">Cerimedo&rsquo;s #BrasilFoiRoubado &ldquo;stolen election&rdquo; livestream &mdash; court-ordered down by Brazil&rsquo;s TSE, named in the federal-police probe. This is the playbook later seen elsewhere. <em>Predates the Parscale partnership; it is Cerimedo&rsquo;s act.</em></span></div>
<div class="ar">&darr; the same machine, three elections (2023&ndash;2025)</div>
<div class="camps">
<div class="camp"><div class="c-h">🇦🇷 Argentina &mdash; Milei (2023)</div>
<div class="row"><b>Parscale:</b> firm/tool level only <span class="pill ta">not personal</span></div>
<div class="row"><b>Cerimedo:</b> digital chief; 50k fake accounts; top in-kind donor</div>
<div class="row"><b>Disinfo:</b> &ldquo;fraude colosal&rdquo; claims &mdash; but from the Mileis, court-ruled <span class="pill tr">unfounded</span>; not tied to Numen</div></div>
<div class="camp"><div class="c-h">🇧🇴 Bolivia &mdash; Paz (2025)</div>
<div class="row"><b>Parscale:</b> reportedly traveled <span class="pill ta">single-source</span></div>
<div class="row"><b>Cerimedo:</b> now Paz&rsquo;s &ldquo;asesor personal&rdquo;</div>
<div class="row"><b>Disinfo:</b> documented in volume, but the ProBox study found <b>no link</b> to Numen/Paz <span class="pill tc">checked</span></div></div>
<div class="camp"><div class="c-h">🇭🇳 Honduras &mdash; Asfura (2025)</div>
<div class="row"><b>Parscale:</b> advised remotely <span class="pill tc">did NOT travel</span></div>
<div class="row"><b>Cerimedo:</b> on-the-ground; ran a parallel count</div>
<div class="row"><b>Context:</b> Trump endorsed Asfura + pardoned ex-pres Hern&aacute;ndez days before the vote; razor-thin disputed count</div></div>
</div>
<div class="disc"><b>The discipline &mdash; read this before you share it</b><p>In not one of these countries is the documented disinformation forensically tied to Parscale or Numen. The lies trace to Cerimedo&rsquo;s record and to the candidates&rsquo; own camps. Parscale&rsquo;s documented role is the <b>machine</b>; the <b>content</b> is others&rsquo;. The honest, undismissable line: <b>Parscale built the infrastructure a documented disinformation operator drives</b> &mdash; not &ldquo;Parscale ran Latin American disinformation.&rdquo;</p></div>
</div><figcaption>The Numen operation, 2022&ndash;2025. Blue = Parscale (infrastructure); red = Cerimedo (operator + the documented disinformation). Tiers mark what is confirmed vs. single-source vs. checked-and-unlinked. First reported by the NYT (Dec 2025), El Pa&iacute;s Bolivia, and the CLIP consortium &mdash; this adds the role-split and the tiering.</figcaption></figure>'''

pathlib.Path(B+"latam_embed.txt").write_text(FIG)
pathlib.Path(B+"latam.html").write_text(f"<!doctype html><meta charset=utf-8><body style='margin:0;background:#0b0d10;color:#e7edf3;padding:24px;width:860px'>{FIG}</body>")
print("latam graphic built; bytes:",len(FIG),"| safe:", "'''" not in FIG)
