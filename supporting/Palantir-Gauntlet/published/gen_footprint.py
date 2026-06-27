#!/usr/bin/env python3
"""Palantir global-footprint board: where it operates / where it's been challenged / what's only alleged. Responsive HTML + PNG."""
GROUPS=[
 ("Where it runs — confirmed operational","op","#3fd07f",[
   ("🇺🇸 US Army","Up to $10bn enterprise deal"),("🇺🇸 Maven Smart System","AI targeting · ~$1.3bn ceiling"),
   ("🇺🇸 NGA 'Glacier Bay'","$646M (primary-sourced)"),("🇺🇸 CDC / HHS","$443M disease surveillance"),
   ("🇺🇸 ICE","ImmigrationOS (build-in-progress)"),("🇬🇧 NHS England","Federated Data Platform ~£330m"),
   ("🇬🇧 MoD","Foundry · £240.6m direct award"),("🇩🇰 Denmark Police","POL-INTEL (Gotham)"),
   ("🇺🇦 Ukraine","war effort · demining · war-crimes"),("Commercial","Airbus · Ferrari · Stellantis · Morgan Stanley"),
 ]),
 ("Where it's been challenged, blocked or exited","chal","#ff5d5d",[
   ("🇩🇪 German Constitutional Court","2023 — police-analysis powers struck down; judgment NAMES Palantir"),
   ("🇬🇧 Met Police","~£50m deal BLOCKED by the Mayor (2026)"),
   ("🇫🇷 France (DGSI)","dropping Palantir for ChapsVision — sovereignty (2026)"),
   ("🇳🇴 Norway 'Omnia'","FAILED & cancelled (~NOK 100m)"),
   ("🇪🇺 EDPS → Europol","2022 erasure order; Gotham licence ended 2021"),
   ("💸 Divestments","ABP ~€825m · Storebrand ~$24m · Norway $2.3tn fund voted for HR review"),
 ]),
 ("Alleged — not proven, and denied by Palantir","alleged","#8a93a0",[
   ("Gaza targeting (Lavender/Gospel)","IDF-attributed systems — NOT proven Palantir products; UN rapporteur opinion, no court ruling"),
   ("US cross-agency 'mega-database'","NYT-reported; Palantir calls it 'blatantly untrue'; no primary contract found"),
 ]),
]
def chips(items): return "".join(f'<div class="fp-chip"><b>{a}</b><span>{b}</span></div>' for a,b in items)
groups="".join(f'<div class="fp-group" style="--gc:{col}"><div class="fp-h"><span class="fp-dot"></span>{name}</div><div class="fp-row">{chips(items)}</div></div>' for name,cls,col,items in GROUPS)
CSS='''<style>
.fp{border:1px solid var(--border,#2a323c);border-radius:14px;padding:16px;background:rgba(255,255,255,.02);font-family:var(--sans,-apple-system,Helvetica,Arial,sans-serif)}
.fp-group{border-left:3px solid var(--gc);padding:10px 0 12px 13px;margin-bottom:14px}
.fp-group:last-child{margin-bottom:0}
.fp-h{display:flex;align-items:center;gap:9px;color:#fff;font-weight:650;font-size:1rem;margin-bottom:10px}
.fp-dot{width:12px;height:12px;border-radius:50%;background:var(--gc);flex:0 0 auto;box-shadow:0 0 0 0 var(--gc);animation:fpp 2.2s ease-out infinite}
@keyframes fpp{0%{box-shadow:0 0 0 0 color-mix(in srgb,var(--gc) 55%,transparent)}70%{box-shadow:0 0 0 8px transparent}100%{box-shadow:0 0 0 0 transparent}}
.fp-row{display:flex;flex-wrap:wrap;gap:8px}
.fp-chip{flex:1 1 240px;border:1px solid var(--gc)55;border-radius:9px;padding:8px 11px;background:#0b0d10}
.fp-chip b{display:block;font-size:.9rem;color:#fff}
.fp-chip span{display:block;font-size:.78rem;color:#9aa7b4;margin-top:2px}
@media(max-width:640px){.fp-chip{flex:1 1 100%}}
</style>'''
FIG=f'''<figure class="diagram"><div class="fp">{groups}</div><figcaption>Palantir worldwide: the operational layer of the state's hardest functions — and the growing list of courts, regulators, parliaments and investors pushing back. Every item is tagged; allegations are labelled as alleged. Full source-verified catalog (16 sectors) on GitHub.</figcaption></figure>'''
import pathlib
b="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"
pathlib.Path(b+"footprint_embed.txt").write_text(CSS+FIG)
pathlib.Path(b+"footprint.html").write_text(f"<!doctype html><meta charset=utf-8><body style='margin:0;background:#0b0d10;color:#e7edf3;padding:26px;width:1000px'>{CSS}{FIG}</body>")
print("footprint graphic built; bytes:",len(CSS+FIG))
