#!/usr/bin/env python3
"""Parscale information-operations timeline, classified by the 4 categories. Responsive HTML."""
import pathlib
B="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"

# category -> (color, label)
CAT={"D":("#ff5d5d","Disinformation"),"M":("#f4b740","Manipulative-but-legal"),
     "A":("#3fd07f","Aggressive-legitimate"),"X":("#8a93a0","Mythology / NOT him")}

EV=[
 ("2011","A","Giles-Parscale founded","San Antonio web/marketing firm; builds Trump's 2016 digital."),
 ("2016","M","Project Alamo","Industrial microtargeting + &lsquo;dark posts&rsquo;; a &lsquo;Deterrence&rsquo; program tags ~3.5M Black voters &mdash; manipulative targeting of true-but-weaponized content, not fabricated."),
 ("2016","X","Cambridge Analytica","A $5.9m vendor &mdash; but the &ldquo;psychographics won it&rdquo; legend is debunked (even by CA); the 87m-profile harvest was CA&rsquo;s, not proven used in Trump targeting."),
 ("2019","X","WinRed created","He helped stand up the platform &amp; pushed adoption &mdash; but the deceptive pre-checked-donation boxes (~$122m refunds) were built by Coby/Lansing, NOT him."),
 ("2018&ndash;20","D","Campaign manager","His operation ran demonstrably doctored attack ads &mdash; the altered Biden &lsquo;earpiece&rsquo; photo, a deceptively edited video (Twitter&rsquo;s first &lsquo;manipulated media&rsquo; label), census-impersonation ads Facebook removed."),
 ("Jul 2020","X","Demoted &mdash; and OUT","Replaced by Stepien; withdrew Sept 2020. NOT Stop the Steal / Jan 6 &mdash; he privately blamed Trump and told rioters to stop. The mastermind legend ends here."),
 ("2020","A","Campaign Nucleus","Real campaign SaaS; the &lsquo;AI&rsquo; claims are self-reported and unproven (Trump 2024 disavowed AI tools; Axios couldn&rsquo;t reproduce them)."),
 ("2023&ndash;25","M","Numen &mdash; foreign elections","Sells data/targeting into Milei (AR), Paz (BO), Asfura (HN) with Fernando Cerimedo &mdash; a documented disinformation operator (Brazil 2022). Parscale built the machine; the false content is Cerimedo&rsquo;s."),
 ("Jan 2025","A","Salem Media CSO","Joins the conservative-media network as Chief Strategy Officer &mdash; later a recipient of his own foreign-money routing."),
 ("Sep 2025","M","Clock Tower X &mdash; FARA Israel","Registered foreign agent for the State of Israel (via Havas); a disclosed AI-influence apparatus built to bend ChatGPT/Gemini/Claude/Grok. Self-dealing; effect unproven."),
 ("2026","M","The network &amp; the texts","One fingerprinted 11-site operator; SparkFire bots text Americans under fake &lsquo;peace&rsquo;-group names with no disclosure on the texts."),
]

CSS="""<style>
.ptl{font-family:var(--sans,-apple-system,Helvetica,Arial,sans-serif);color:#c2cbd5;border:1px solid var(--border,#2a323c);border-radius:14px;padding:18px;background:rgba(255,255,255,.02)}
.ptl h4{margin:0 0 3px;color:#fff;font-family:var(--display,Georgia,serif);font-size:1.15rem}
.ptl .sub{color:#9aa7b4;font-size:.82rem;margin:0 0 14px}
.ptl .leg{display:flex;flex-wrap:wrap;gap:6px 14px;margin:0 0 14px}
.ptl .leg span{font-size:.78rem;display:flex;align-items:center;gap:6px}
.ptl .dot{width:11px;height:11px;border-radius:3px;display:inline-block}
.ptl .tl{position:relative;padding-left:22px}
.ptl .tl:before{content:"";position:absolute;left:6px;top:4px;bottom:4px;width:2px;background:#2a323c}
.ptl .ev{position:relative;margin:0 0 14px;padding-left:8px}
.ptl .ev:before{content:"";position:absolute;left:-21px;top:3px;width:12px;height:12px;border-radius:50%;background:var(--c);box-shadow:0 0 0 3px #0b0d10,0 0 9px var(--c)}
.ptl .yr{font-family:var(--mono,monospace);font-size:.72rem;color:#8a93a0;letter-spacing:.03em}
.ptl .ev b{color:#fff;font-size:.95rem}
.ptl .pill{font-family:var(--mono,monospace);font-size:.58rem;font-weight:700;text-transform:uppercase;letter-spacing:.04em;padding:1px 6px;border-radius:5px;border:1px solid var(--c);color:var(--c);margin-left:7px;vertical-align:middle}
.ptl .ev p{margin:3px 0 0;font-size:.84rem;color:#9aa7b4;line-height:1.5}
</style>"""

leg="".join(f'<span><i class="dot" style="background:{c}"></i>{l}</span>' for k,(c,l) in CAT.items())
evs="".join(
 f'<div class="ev" style="--c:{CAT[cat][0]}"><span class="yr">{yr}</span> <b>{t}</b>'
 f'<span class="pill">{CAT[cat][1]}</span><p>{d}</p></div>' for yr,cat,t,d in EV)

FIG=CSS+('<figure class="diagram"><div class="ptl"><h4>The machine over time</h4>'
 '<p class="sub">Twenty years of Brad Parscale&rsquo;s political-influence work, each milestone classified. The point of the colour-coding: most of it is manipulation-by-design, not fabricated disinformation &mdash; and the grey items are where the legend outruns the record.</p>'
 f'<div class="leg">{leg}</div><div class="tl">{evs}</div></div>'
 '<figcaption>Classified timeline. Red = demonstrably false content; amber = deceptive-but-legal design/targeting; green = aggressive-but-truthful tech; grey = widely claimed but NOT supported (incl. Stop the Steal, the CA-psychographics myth, and the WinRed boxes others built).</figcaption></figure>')

pathlib.Path(B+"pscale_timeline_embed.txt").write_text(FIG)
pathlib.Path(B+"pscale_timeline.html").write_text(f"<!doctype html><meta charset=utf-8><body style='margin:0;background:#0b0d10;color:#e7edf3;padding:24px;width:820px'>{FIG}</body>")
print("timeline built; events:",len(EV),"| bytes:",len(FIG),"| safe:", "'''" not in FIG)
