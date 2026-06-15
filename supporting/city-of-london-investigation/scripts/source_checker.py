#!/usr/bin/env python3
"""
source_checker.py — freshness / liveness checker for evidence/raw_links.json

STDLIB ONLY (urllib, concurrent.futures, json, argparse, datetime). No pip installs.

For each link it performs a GET with a browser User-Agent, follows redirects, and
classifies the result:

  DEAD     - request failed (network/timeout) OR final HTTP status >= 400
  REDIRECT - request succeeded but the final URL differs from the registered URL
  STALE    - access_date older than --max-age-days (default 90), OR the source was
             pre-flagged "STALE?" in raw_links.json
  UNCLEAR  - the source was pre-flagged "UNCLEAR"
  OK       - live, not redirected, fresh, not pre-flagged

Precedence when more than one applies: DEAD > UNCLEAR > REDIRECT > STALE > OK.
(DEAD always wins so CI fails loudly; UNCLEAR is an explicit human flag we keep
surfacing; a redirect is more actionable than mere staleness.)

Writes research/source_check_report.md and prints a summary table.
Exit code is non-zero if ANY link is DEAD (for CI).
"""

import argparse
import json
import os
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINKS_PATH = os.path.join(REPO_ROOT, "evidence", "raw_links.json")
REPORT_PATH = os.path.join(REPO_ROOT, "research", "source_check_report.md")


def parse_date(s):
    if not s:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y"):
        try:
            return datetime.strptime(s, fmt).date()
        except (ValueError, TypeError):
            continue
    return None


def fetch(url, timeout):
    """Return (ok, status, final_url, note). ok=False means DEAD."""
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            status = getattr(resp, "status", resp.getcode())
            final_url = resp.geturl()
            # Read a small chunk to confirm the body is actually reachable.
            resp.read(2048)
            ok = status < 400
            return ok, status, final_url, ""
    except urllib.error.HTTPError as e:
        return (e.code < 400), e.code, url, f"HTTPError {e.code}"
    except urllib.error.URLError as e:
        return False, None, url, f"URLError: {e.reason}"
    except Exception as e:  # noqa: BLE001 - we want any failure to read as DEAD
        return False, None, url, f"{type(e).__name__}: {e}"


def normalise(u):
    if not u:
        return u
    return u.rstrip("/")


def classify(link, max_age_days, today, timeout):
    url = link.get("url", "")
    pre_flag = (link.get("status_flag") or "").upper()
    ok, status, final_url, note = fetch(url, timeout)

    classification = "OK"
    detail = []

    if not ok:
        classification = "DEAD"
        if note:
            detail.append(note)
        elif status is not None:
            detail.append(f"HTTP {status}")
        return _result(link, classification, status, final_url, detail)

    # Live. Now apply softer flags (precedence handled by order below).
    if pre_flag == "UNCLEAR":
        classification = "UNCLEAR"
        detail.append("pre-flagged UNCLEAR")
    elif normalise(final_url) != normalise(url):
        classification = "REDIRECT"
        detail.append(f"-> {final_url}")
    else:
        # staleness checks
        stale = False
        if pre_flag in ("STALE?", "STALE"):
            stale = True
            detail.append("pre-flagged STALE?")
        acc = parse_date(link.get("access_date"))
        if acc is not None:
            age = (today - acc).days
            if age > max_age_days:
                stale = True
                detail.append(f"accessed {age}d ago (>{max_age_days})")
        else:
            stale = True
            detail.append("no access_date")
        if stale:
            classification = "STALE"

    if status is not None and "HTTP" not in " ".join(detail):
        detail.append(f"HTTP {status}")
    return _result(link, classification, status, final_url, detail)


def _result(link, classification, status, final_url, detail):
    return {
        "id": link.get("id"),
        "title": link.get("title"),
        "url": link.get("url"),
        "final_url": final_url,
        "status": status,
        "classification": classification,
        "detail": "; ".join(d for d in detail if d),
    }


def main():
    ap = argparse.ArgumentParser(description="Check freshness/liveness of evidence sources.")
    ap.add_argument("--max-age-days", type=int, default=90)
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--links", default=LINKS_PATH)
    args = ap.parse_args()

    with open(args.links, "r", encoding="utf-8") as f:
        data = json.load(f)
    links = data.get("links", [])
    today = date.today()

    results = [None] * len(links)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {
            ex.submit(classify, lk, args.max_age_days, today, args.timeout): i
            for i, lk in enumerate(links)
        }
        for fut in futs:
            i = futs[fut]
            results[i] = fut.result()

    order = {"DEAD": 0, "REDIRECT": 1, "STALE": 2, "UNCLEAR": 3, "OK": 4}
    results.sort(key=lambda r: (order.get(r["classification"], 9), r["id"] or ""))

    counts = {}
    for r in results:
        counts[r["classification"]] = counts.get(r["classification"], 0) + 1

    # ---- console summary ----
    print(f"\nSource check — {today.isoformat()} — {len(results)} links")
    print("-" * 72)
    for r in results:
        print(f"  [{r['classification']:<8}] {r['id']:<5} HTTP {str(r['status']):<4} {r['title']}")
        if r["detail"]:
            print(f"            {r['detail']}")
    print("-" * 72)
    print("  " + "  ".join(f"{k}={v}" for k, v in sorted(counts.items())))

    # ---- markdown report ----
    lines = []
    lines.append("# Source Check Report")
    lines.append("")
    lines.append(f"_Generated: {today.isoformat()} · max-age-days={args.max_age_days}_")
    lines.append("")
    lines.append("| ID | Status | HTTP | Title | Detail |")
    lines.append("|----|--------|------|-------|--------|")
    for r in results:
        det = (r["detail"] or "").replace("|", "\\|")
        title = (r["title"] or "").replace("|", "\\|")
        lines.append(
            f"| {r['id']} | {r['classification']} | {r['status']} | {title} | {det} |"
        )
    lines.append("")
    lines.append("**Counts:** " + ", ".join(f"`{k}={v}`" for k, v in sorted(counts.items())))
    lines.append("")
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"\nWrote {os.path.relpath(REPORT_PATH, REPO_ROOT)}")

    if counts.get("DEAD", 0) > 0:
        print(f"\nFAIL: {counts['DEAD']} DEAD link(s).", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
