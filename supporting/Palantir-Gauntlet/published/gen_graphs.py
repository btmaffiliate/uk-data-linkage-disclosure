#!/usr/bin/env python3
"""Palantir catalog graphics pack: status, geography, money (ceilings vs primary), pushback timeline, procurement pattern. Responsive HTML/SVG."""
import pathlib
B="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"

CSS = """<style>
.gpk{--g:#3fd07f;--a:#f4b740;--r:#ff5d5d;--b:#5aa9ff;--mut:#8a93a0;font-family:var(--sans,-apple-system,Helvetica,Arial,sans-serif);color:#c2cbd5}
.gpk .gcard{border:1px solid var(--border,#2a323c);border-radius:14px;padding:18px 18px 16px;background:rgba(255,255,255,.02);margin:0}
.gpk h4{margin:0 0 3px;color:#fff;font-family:var(--display,Georgia,serif);font-size:1.15rem}
.gpk .sub{color:#9aa7b4;font-size:.82rem;margin:0 0 14px}
/* horizontal bars */
.gpk .bar{display:flex;align-items:center;gap:10px;margin:7px 0}
.gpk .blab{flex:0 0 38%;font-size:.82rem;color:#e7edf3;text-align:right;line-height:1.2}
.gpk .blab small{color:#8a93a0;display:block;font-size:.72rem}
.gpk .btrack{flex:1;background:#11161c;border-radius:5px;overflow:hidden;height:22px;position:relative}
.gpk .bfill{height:100%;border-radius:5px;min-width:2px;transform-origin:left;animation:gw 1.1s cubic-bezier(.2,.7,.2,1) both}
@keyframes gw{from{transform:scaleX(0)}to{transform:scaleX(1)}}
.gpk .bval{position:absolute;right:8px;top:50%;transform:translateY(-50%);font-family:var(--mono,monospace);font-size:.74rem;color:#fff;font-weight:700;text-shadow:0 1px 2px #000}
/* segmented stat bar */
.gpk .seg{display:flex;height:34px;border-radius:8px;overflow:hidden;margin:4px 0 12px}
.gpk .seg div{display:flex;align-items:center;justify-content:center;color:#06120a;font-weight:800;font-size:.8rem;min-width:24px;animation:gw 1s both}
.gpk .legend{display:flex;flex-wrap:wrap;gap:6px 16px}
.gpk .legend span{font-size:.8rem;color:#c2cbd5;display:flex;align-items:center;gap:6px}
.gpk .dot{width:11px;height:11px;border-radius:3px;display:inline-block}
/* timeline */
.gpk .tl{position:relative;padding-left:20px;margin-top:4px}
.gpk .tl:before{content:"";position:absolute;left:5px;top:4px;bottom:4px;width:2px;background:linear-gradient(#3fd07f,#f4b740,#ff5d5d)}
.gpk .tev{position:relative;margin:0 0 13px;padding-left:6px}
.gpk .tev:before{content:"";position:absolute;left:-19px;top:4px;width:11px;height:11px;border-radius:50%;background:var(--c,#ff5d5d);box-shadow:0 0 0 3px #0b0d10,0 0 10px var(--c,#ff5d5d)}
.gpk .tyr{font-family:var(--mono,monospace);font-size:.72rem;color:#8a93a0;letter-spacing:.04em}
.gpk .tev b{color:#fff;font-size:.92rem}
.gpk .tev span{display:block;color:#9aa7b4;font-size:.82rem;margin-top:1px}
.gpk .pill{font-family:var(--mono,monospace);font-size:.62rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;padding:1px 7px;border-radius:5px;border:1px solid;margin-left:6px;vertical-align:middle}
/* procurement grid */
.gpk .pgrid{display:flex;flex-wrap:wrap;gap:8px}
.gpk .pc{flex:1 1 250px;border:1px solid #ff5d5d44;background:rgba(255,93,93,.05);border-radius:9px;padding:9px 12px}
.gpk .pc b{color:#fff;font-size:.86rem;display:block}
.gpk .pc small{color:#cf9b9b;font-size:.76rem}
.gpk .pc i{font-style:normal;color:#ffb3b3;font-family:var(--mono,monospace);font-size:.66rem;text-transform:uppercase;letter-spacing:.04em}
@media(max-width:560px){.gpk .blab{flex:0 0 46%}.gpk .pc{flex:1 1 100%}}
</style>"""

def fig(title, sub, inner):
    return ('<figure class="diagram"><div class="gpk"><div class="gcard">'
            f'<h4>{title}</h4><p class="sub">{sub}</p>{inner}</div></div></figure>')

# 1) STATUS segmented bar (82 rows)
STAT=[("operational",57,"#3fd07f"),("ended",7,"#5b6b7a"),("alleged",6,"#8a93a0"),
      ("blocked",4,"#ff5d5d"),("pilot",4,"#5aa9ff"),("proposed/eval",2,"#a78bfa"),
      ("build-in-progress",1,"#f4b740"),("equity",1,"#2dd4bf")]
tot=sum(n for _,n,_ in STAT)
seg="".join(f'<div style="flex:{n};background:{c}" title="{k}: {n}">{n if n/tot>0.05 else ""}</div>' for k,n,c in STAT)
leg="".join(f'<span><i class="dot" style="background:{c}"></i>{k} · {n}</span>' for k,n,c in STAT)
f_status=fig("What the 82 catalogued deployments actually are",
    "Counted from the master table. Most are live &mdash; but &lsquo;operational&rsquo; is not &lsquo;proven harmless&rsquo;, and the 6 alleged are held as alleged.",
    f'<div class="seg">{seg}</div><div class="legend">{leg}</div>')

# 2) GEOGRAPHY bars (deployment count)
GEO=[("United States",40,"#ff5d5d"),("United Kingdom",14,"#f4b740"),("Germany",6,"#5aa9ff"),
     ("Ukraine",6,"#5aa9ff"),("Australia",4,"#3fd07f"),("New Zealand",2,"#3fd07f"),
     ("UAE",2,"#a78bfa"),("Israel",1,"#8a93a0"),("Other (FR/IT/AO/multi)",4,"#5b6b7a")]
gmax=max(n for _,n,_ in GEO)
gbars="".join(
  f'<div class="bar"><div class="blab">{k}</div><div class="btrack">'
  f'<div class="bfill" style="width:{n/gmax*100:.1f}%;background:{c};animation-delay:{i*0.06:.2f}s"></div>'
  f'<span class="bval">{n}</span></div></div>' for i,(k,n,c) in enumerate(GEO))
f_geo=fig("The footprint is overwhelmingly American",
    "Deployments by country in the master table. The US carries ~half the catalogue and the great bulk of the dollar value and controversy.",
    gbars)

# 3) MONEY — two panels: reported ceilings (maximums) vs confirmed/primary awards. $M; GBP->USD x1.27.
CEIL=[("US Army enterprise agreement","up to $10bn / 10yr",10000),
      ("Maven Smart System (MSS)","~$1.3bn ceiling",1300),
      ("UK–Palantir Strategic Partnership","up to £750m envelope",953),
      ("US Army Vantage follow-on","$618.9m ceiling",619),
      ("US Navy 'ShipOS'","up to $448m",448)]
PRIM=[("NGA 'Glacier Bay'","$646m · primary",646),
      ("CDC Common Operating Picture","$443m · reported",443),
      ("UK MoD enterprise agreement","£240.6m · primary",306),
      ("NHS Federated Data Platform","£182.2m published · primary",231),
      ("US Army TITAN","$178.4m · primary",178),
      ("ICE case management (ICM)","~$139m · reported",139),
      ("FDA drug-review Foundry","$44.4m · reported",44),
      ("NIH N3C COVID enclave","$36m · reported",36),
      ("ICE ImmigrationOS (building)","$30m · reported",30),
      ("NGA Platform Licenses","$28.3m · primary",28),
      ("UK NFLMS firearms","~£9m · primary",11)]
def moneybars(data,col):
    mx=max(v for *_,v in data)
    return "".join(
      f'<div class="bar"><div class="blab">{k}<small>{lab}</small></div><div class="btrack">'
      f'<div class="bfill" style="width:{max(v/mx*100,1.4):.1f}%;background:{col};animation-delay:{i*0.05:.2f}s"></div>'
      f'<span class="bval">{("$%g"%v if v<1000 else "$%.1fk"%(v/1000)).replace("$%.1fk"%(v/1000),"$%.1fbn"%(v/1000))}m</span>'
      f'</div></div>' for i,(k,lab,v) in enumerate(data))
# simpler value formatter
def vfmt(v): return f"${v/1000:.1f}bn" if v>=1000 else f"${v}m"
def mbars(data,col):
    mx=max(v for *_,v in data)
    return "".join(
      f'<div class="bar"><div class="blab">{k}<small>{lab}</small></div><div class="btrack">'
      f'<div class="bfill" style="width:{max(v/mx*100,1.4):.1f}%;background:{col};animation-delay:{i*0.05:.2f}s"></div>'
      f'<span class="bval">{vfmt(v)}</span></div></div>' for i,(k,lab,v) in enumerate(data))
money_inner=('<p style="margin:0 0 6px;color:#f4b740;font-weight:650;font-size:.86rem">Reported ceilings &mdash; maximums, not money spent</p>'
    + mbars(CEIL,"#f4b740")
    + '<p style="margin:14px 0 6px;color:#3fd07f;font-weight:650;font-size:.86rem">Confirmed &amp; primary-sourced awards &mdash; the hard numbers</p>'
    + mbars(PRIM,"#3fd07f"))
f_money=fig("The headline billions are ceilings; the firm numbers are smaller",
    "GBP converted at ~1.27. The $10bn and $1.3bn figures are contract <em>maximums</em>; the primary-sourced awards (NGA, UK MoD, NHS, TITAN) are an order of magnitude lower &mdash; and that distinction is the honest story.",
    money_inner)

# 4) PUSHBACK timeline
TL=[("2020","Norway 'Omnia' cancelled","~NOK 100m spent; Gotham never went operational","#ff5d5d","blocked"),
    ("2020","Canada Ethics Commissioner","found Palantir Canada's president breached conflict-of-interest rules","#f4b740","regulator"),
    ("2022","EDPS orders Europol erasure","data on people with no link to crime; Europol's Gotham licence lapsed ~2021","#f4b740","regulator"),
    ("2023","German Constitutional Court","struck down the police data-mining powers behind the Gotham deployments","#ff5d5d","court"),
    ("2024","Storebrand divests","~$24m sold over Palantir's Israeli-military work","#a78bfa","investor"),
    ("2025","Bavaria 'VeRA' complaint filed","GFF + CCC constitutional complaint; pending at the BVerfG","#5aa9ff","pending"),
    ("2026","Met Police deal blocked","~£50m operational deal stopped by the Mayor over single-supplier procurement","#ff5d5d","blocked"),
    ("2026","France's DGSI exits Palantir","switching to French ChapsVision on sovereignty grounds","#ff5d5d","exit"),
    ("2026","ABP divests ~€825m","largest Dutch pension fund sells its entire stake","#a78bfa","investor"),
    ("2026","Norway's $2.3tn fund votes for HR review","non-insiders ~56% in favour &mdash; defeated only by the founder dual-class voting lock","#a78bfa","investor")]
tl="".join(
  f'<div class="tev" style="--c:{c}"><span class="tyr">{yr}</span>'
  f'<b>{t}</b><span>{d}</span></div>' for yr,t,d,c,_ in TL)
f_tl=fig("The wall of pushback &mdash; and it is accelerating",
    "Courts, regulators, parliaments and investors, 2020&ndash;2026. One constitutional-court ruling, multiple blocks and national exits, and ~&euro;850m+ of divestment.",
    f'<div class="tl">{tl}</div>')

# 5) PROCUREMENT pattern
PROC=[("ICE ImmigrationOS","$30m awarded 'urgent and compelling' &mdash; no competition","sole-source"),
      ("UK MoD £240.6m","direct-awarded under Procurement Act 2023 s.41","direct award"),
      ("Cabinet Office border (~£27m)","awarded Aug 2020 with no tender","no tender"),
      ("NHS Federated Data Platform","contract released heavily redacted","secret"),
      ("Met UDP Phase 1","~£489,999 &mdash; structured just under the £500k scrutiny line","threshold-gamed"),
      ("EMSOU NECTAR (£818,750)","FOI request for the contract refused","secret"),
      ("AUSTRAC (Australia)","official quote: 'not competitive at all'","sole-source"),
      ("NIH N3C ($36m)","awarded 'no other sources capable'","sole-source")]
pg="".join(f'<div class="pc"><b>{a}</b><small>{b}</small><br><i>{c}</i></div>' for a,b,c in PROC)
f_proc=fig("How the deals got done: sole-source, secret, threshold-gamed",
    "The procurement pattern &mdash; not just the technology &mdash; is what auditors, parliaments and mayors keep challenging. A sample of the documented cases.",
    f'<div class="pgrid">{pg}</div>')

DASH=CSS+f_status+f_geo+f_money+f_tl+f_proc
pathlib.Path(B+"graphs_embed.txt").write_text(DASH)
# standalone page for PNG capture
pathlib.Path(B+"graphs.html").write_text(
  f"<!doctype html><meta charset=utf-8><body style='margin:0;background:#0b0d10;color:#e7edf3;padding:24px;width:980px'>{DASH}</body>")
print("graphs pack built; figures: 5 | bytes:",len(DASH))
