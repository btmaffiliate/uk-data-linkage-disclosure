# Master source table

Flags re-verified by `scripts/source_checker.py`. LIVE = HTTP 200. Sources marked
"(live, unread)" returned 200 to the checker but block the fetch client, so their full text
was not personally read; claims on them are graded LIKELY.

| # | Title | Publisher | Pub date | URL | Accessed | Track | Flag |
|---|-------|-----------|----------|-----|----------|-------|------|
| S01 | National Fraud Intelligence Bureau | Wikipedia | — | https://en.wikipedia.org/wiki/National_Fraud_Intelligence_Bureau | 2026-06-10 | T1 | LIVE (read) |
| S02 | City of London Corporation | Wikipedia | — | https://en.wikipedia.org/wiki/City_of_London_Corporation | 2026-06-10 | T2 | LIVE (read) |
| S03 | Report Fraud — Privacy information | City of London Police | — | https://www.reportfraud.police.uk/privacy-information/ | 2026-06-10 | T1 | LIVE (unread) |
| S05 | Freedom of Information Act 2000 (City of London) | City of London Corporation | — | https://www.cityoflondon.gov.uk/about-us/access-to-information/freedom-of-information | 2026-06-10 | T2 | LIVE (unread) |
| S06 | Remembrancer's Office — Working with Parliament | City of London Corporation | — | https://www.cityoflondon.gov.uk/about-us/about-the-city-of-london-corporation/remembrancers-office | 2026-06-10 | T2 | LIVE (unread) |
| S07 | Business/worker vote registration | City of London Corporation | — | https://www.cityoflondon.gov.uk/about-us/voting-elections/business-vote-registration | 2026-06-10 | T2 | LIVE (unread) |
| S09 | Streets paved with gold: the council that works for banks | The Bureau of Investigative Journalism | 2012-07-09 | https://www.thebureauinvestigates.com/stories/2012-07-09/streets-paved-with-gold-the-council-that-works-for-banks | 2026-06-10 | T2 | LIVE (secondary, dated) |

**Dropped as unverifiable (403 to every client here; see `raw_links.json` `_meta`):**
cityoflondon.police.uk National Lead Force; committees.parliament.uk CoLP written evidence;
whatdotheyknow.com City of London FOI archive. Their points are carried by S01 / S05; re-add after a browser read.

> To-source precisely (currently from search/secondary, see open_questions): City of London (Ward
> Elections) Act 2002 on legislation.gov.uk; the Times (2019) and Which? (2018) Action Fraud originals;
> latest City's Cash accounts.
