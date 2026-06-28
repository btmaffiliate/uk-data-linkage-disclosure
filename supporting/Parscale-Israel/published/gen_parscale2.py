#!/usr/bin/env python3
"""Parscale/Israel full-report graphics pack: stat band, apparatus map, network-infra forensics, AI architecture. Responsive HTML."""
import pathlib
B="/private/tmp/claude-501/-Users-btmaffiliate/02450b35-2455-41ae-8079-f578e21574b5/scratchpad/bm/"

CSS="""<style>
.gpk{font-family:var(--sans,-apple-system,Helvetica,Arial,sans-serif);color:#c2cbd5}
.gpk .gcard{border:1px solid var(--border,#2a323c);border-radius:14px;padding:18px;background:rgba(255,255,255,.02);margin:0}
.gpk h4{margin:0 0 3px;color:#fff;font-family:var(--display,Georgia,serif);font-size:1.15rem}
.gpk .sub{color:#9aa7b4;font-size:.82rem;margin:0 0 14px}
.gpk .tier{font-family:var(--mono,monospace);font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;padding:1px 6px;border-radius:5px;border:1px solid;margin-left:6px;vertical-align:middle}
.gpk .tc{color:#3fd07f;border-color:#3fd07f55}.gpk .tr{color:#f4b740;border-color:#f4b74055}.gpk .ta{color:#ff7a7a;border-color:#ff7a7a55}
/* stat band */
.statband{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;border:1px solid var(--border,#2a323c);border-radius:14px;padding:16px;background:rgba(255,255,255,.02)}
.statc{border-left:3px solid var(--c);padding:6px 12px}
.snum{font-family:var(--display,Georgia,serif);font-size:1.8rem;font-weight:800;color:var(--c);line-height:1.05}
.slab{font-size:.79rem;color:#c2cbd5;margin-top:3px;line-height:1.3}.slab small{font-size:.7rem;color:#8a93a0}
/* apparatus */
.app .top{border:1px solid #ff5d5d66;background:#1a0e10;border-radius:11px;padding:11px 14px;text-align:center;max-width:520px;margin:0 auto}
.app .hub{border:1px solid #f4b74066;background:#1a160c;border-radius:11px;padding:10px 14px;text-align:center;max-width:420px;margin:0 auto}
.app .ar{text-align:center;color:#5b6b7a;font-size:1.1rem;margin:5px 0}
.app .nt{color:#fff;font-weight:700}.app .ns{color:#9aa7b4;font-size:.8rem;margin-top:1px}
.app .grid{display:flex;flex-wrap:wrap;gap:8px;margin-top:4px}
.app .nd{flex:1 1 240px;border:1px solid #5aa9ff44;background:#0c1622;border-radius:9px;padding:9px 12px}
.app .nd.cur{border-color:#3fd07f;background:#0e1a12}
.app .nd.old{border-color:#39475a;background:#0d1014;opacity:.7}
.app .nd b{color:#fff;font-size:.88rem;display:block}.app .nd span{color:#9aa7b4;font-size:.77rem}
.app .nd i{font-style:normal;color:#7fb0e6;font-family:var(--mono,monospace);font-size:.7rem}
/* infra */
.tw{overflow-x:auto;border:1px solid var(--border,#2a323c);border-radius:10px}
.gpk table{border-collapse:collapse;width:100%;font-size:.78rem;min-width:560px}
.gpk th,.gpk td{border-bottom:1px solid #1f2730;padding:7px 10px;text-align:left;white-space:nowrap}
.gpk th{color:#fff;background:rgba(255,255,255,.03);font-weight:650}
.gpk td.ok{color:#3fd07f}.gpk td.b{color:#5aa9ff}
.cluster{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px}
.cl{flex:1 1 260px;border-radius:10px;padding:11px 13px;border:1px solid}
.cl.a{border-color:#5aa9ff55;background:rgba(90,169,255,.05)}.cl.b{border-color:#a78bfa55;background:rgba(167,139,250,.05)}
.cl b{color:#fff;display:block;margin-bottom:4px}.cl span{font-size:.8rem;color:#9aa7b4}
.cl code{font-family:var(--mono,monospace);font-size:.76rem;color:#cfe3ff}
/* layers */
.lay{display:flex;flex-direction:column;gap:8px}
.lr{border-left:3px solid var(--c);border-radius:0 9px 9px 0;background:#0c0f14;padding:10px 13px}
.lr b{color:#fff;font-size:.92rem}.lr .ln{font-family:var(--mono,monospace);font-size:.66rem;color:var(--c);letter-spacing:.05em;text-transform:uppercase}
.lr p{margin:3px 0 0;font-size:.83rem;color:#9aa7b4}
.real{border:1px solid #3fd07f44;background:rgba(63,208,127,.05);border-radius:10px;padding:11px 14px;margin-top:12px}
.real b{color:#7fe0a6}.real p{margin:4px 0 0;font-size:.84rem;color:#bfe8cf}
@media(max-width:560px){.app .nd,.cl{flex:1 1 100%}}
</style>"""

def fig(inner,cap):
    return f'<figure class="diagram"><div class="gpk">{inner}</div><figcaption>{cap}</figcaption></figure>'

# STAT BAND
STATS=[("5","FARA registrant nodes<br><small>one Israel&rarr;Havas apparatus</small>","#5aa9ff"),
 ("$9m","Clock Tower X contract<br><small>FARA-confirmed; ~$15m reported paid</small>","#f4b740"),
 ("12","coordinated sites, one operator<br><small>confirmed by our infra check</small>","#3fd07f"),
 ("Sept&ndash;Oct 2025","registered in ~10-min bursts<br><small>the fingerprint</small>","#a78bfa"),
 ("4","AI models named as targets<br><small>ChatGPT, Gemini, Claude, Grok</small>","#ff5d5d"),
 ("0","ties to Palantir<br><small>&mdash; and 0 models found citing it</small>","#8a93a0")]
sb="".join(f'<div class="statc" style="--c:{c}"><div class="snum">{n}</div><div class="slab">{l}</div></div>' for n,l,c in STATS)
f_stat=fig(f'<div class="statband">{sb}</div>',
 'The operation in six numbers. The contract value and registrant count are from FARA filings; the 12-site network and its registration bursts are confirmed by our own infrastructure check; the &ldquo;0 models citing it&rdquo; is the effectiveness reality-check reporters found.')

# APPARATUS MAP
NODES=[("Clock Tower X &mdash; Brad Parscale","#7649","$6m&rarr;$9m","AI/SEO, 12-site network, Gen-Z social, Salem integration","cur"),
 ("Show Faith by Works","#7653","up to $4.1m","evangelical outreach (W. US); proposed church geofencing","nd"),
 ("Bridges Partners","#7652","~$900k","the &lsquo;Esther Project&rsquo; &mdash; paid pro-Israel influencers","nd"),
 ("Davis Media NY","#7662","not pinned","influencer/media; dual-funded (Havas + Tel Aviv firm)","nd"),
 ("SKDKnickerbocker","#7552","$600k","earlier (Jan 2024), terminated Aug 2024 &mdash; the precursor","old")]
nd="".join(f'<div class="nd {cl if cl in("cur","old") else ""}"><b>{n}</b><i>FARA {f}</i> <span>&middot; {amt}</span><span style="display:block">{desc}</span></div>' for n,f,amt,desc,cl in NODES)
f_app=fig(
 '<div class="app"><div class="top"><div class="nt">State of Israel &mdash; Ministry of Foreign Affairs <span class="tier tr">reported</span></div><div class="ns">2025&ndash;26 public-diplomacy push (global budget ~$150m, US tranche a subset)</div></div>'
 '<div class="ar">&darr;</div>'
 '<div class="hub"><div class="nt">Havas Media (Germany) <span class="tier tc">confirmed</span></div><div class="ns">contracting hub &mdash; signs US agents &ldquo;on behalf of&rdquo; Israel (Bollor&eacute; Group)</div></div>'
 '<div class="ar">&darr; registered FARA agents</div>'
 f'<div class="grid">{nd}</div></div>',
 'Clock Tower X is the largest US node, not a standalone. Each box is a separate FARA registrant under the same Israel&rarr;Havas structure. Keep them distinct: the church-geofencing is a <em>different</em> registrant (Show Faith by Works), and its execution is unconfirmed.')

# NETWORK INFRA TABLE
ROWS=[("allyvia.org","2025-09-18","Cloudflare","162.159.136/137.54","A"),
 ("culturavia.org","2025-09-18","Cloudflare","162.159.136/137.54","A"),
 ("econora.org","2025-09-18","Cloudflare","162.159.136/137.54","A"),
 ("innovascope.org","2025-09-18","Cloudflare","162.159.136/137.54","A"),
 ("paxpoint.org","2025-09-18","Cloudflare","162.159.136/137.54","A"),
 ("cognitura.org","2025-10-10","Cloudflare","162.159.136/137.54","A"),
 ("compassionpulse.org","2025-10-10","Cloudflare","162.159.136/137.54","A"),
 ("factsignal.org","2025-10-10","Cloudflare","162.159.136/137.54","A &middot; hub"),
 ("justorium.org","2025-10-10","Cloudflare","162.159.136/137.54","A"),
 ("feedingyoufiction.com","2025-10-24","Squarespace","198.185.159.x","B"),
 ("alliesforpeace.com","2025-10-20","Squarespace","198.185.159.x","B")]
tr="".join(f'<tr><td class="b">{d}</td><td>{c}</td><td>{r}</td><td><code style="font-family:var(--mono,monospace);font-size:.74rem">{ip}</code></td><td>{cl}</td><td class="ok">yes</td></tr>' for d,c,r,ip,cl in ROWS)
f_infra=fig(
 '<div class="tw"><table><tr><th>domain</th><th>created</th><th>host</th><th>shared IP</th><th>cluster</th><th>FARA label?</th></tr>'+tr+'</table></div>'
 '<div class="cluster">'
 '<div class="cl a"><b>Cluster A &mdash; 9 sites, one Cloudflare account</b><span>Identical anycast IPs <code>162.159.136.54 / .137.54</code>, identical name servers, identical WordPress + Elementor + Yoast stack. Created in two ~10-minute bursts (18 Sep &amp; 10 Oct 2025). <code>factsignal.org</code> is the hub that links to the other eight.</span></div>'
 '<div class="cl b"><b>Cluster B &mdash; 2 sites, shared Squarespace</b><span>feedingyoufiction.com + alliesforpeace.com on shared Squarespace IPs, registered 4 days apart &mdash; the video/media arm.</span></div>'
 '</div>',
 'Our own check (whois / dig / fetch, 28 Jun 2026): a single coordinated operator, not eleven independent sites. <strong>And every property carries the FARA disclosure footer</strong> &mdash; so this network is labeled, not hidden. The story is coordination + scale + self-dealing, not a missing-label violation.')

# AI ARCHITECTURE
LAYERS=[("Seed","#5aa9ff","The 12-site content ring","~100 root assets + up to 5,000 variants/month pushed onto freshly-built sites, written to &ldquo;deliver GPT framing results&rdquo; for the open web that models scrape."),
 ("Optimize","#f4b740","MarketBrew (named in the filing)","A predictive search-algorithm <em>simulation</em> tool &mdash; models how Google/Bing rank, then tunes content to win visibility and AI-retrieval. This is generative-engine optimization, not random spam."),
 ("Distribute","#a78bfa","Salem Media authority + SparkFire chatbots","Same narratives laundered through Salem&rsquo;s high-authority properties (RedState, PJ Media, 200+ radio) &mdash; the leg models weight most &mdash; while SparkFire&rsquo;s AI texts people 1:1 and funnels them to the ring&rsquo;s URLs, manufacturing the engagement signals.")]
lr="".join(f'<div class="lr" style="--c:{c}"><span class="ln">{i+1}. {ln}</span><br><b>{t}</b><p>{p}</p></div>' for i,(ln,c,t,p) in enumerate(LAYERS))
f_ai=fig(
 f'<div class="lay">{lr}</div>'
 '<div class="real"><b>Does it work? The reality check.</b><p>Built to bend AI &mdash; but reporters could not get ChatGPT, Gemini, Claude or Grok to actually cite the network, and Snopes debunked the viral claim that &ldquo;Israel signed a deal with ChatGPT&rdquo; (there is no OpenAI or Anthropic deal). State it as <strong>method and intent, documented in the filing &mdash; not proven effect.</strong></p></div>',
 'Three layers wired into one funnel: seed the open web, optimize for AI retrieval, distribute through authority + a chatbot that manufactures the signals. The architecture is real and named in the filing; the demonstrated impact on AI outputs, so far, is not.')

DASH=CSS+f_stat+f_app+f_infra+f_ai
pathlib.Path(B+"parscale2_embed.txt").write_text(DASH)
pathlib.Path(B+"parscale2.html").write_text(f"<!doctype html><meta charset=utf-8><body style='margin:0;background:#0b0d10;color:#e7edf3;padding:24px;width:900px'>{DASH}</body>")
print("parscale2 pack built; figs:4 | bytes:",len(DASH),"| safe:", "'''" not in DASH)
