# AI reports

Sourced research briefings on AI, published as a small static site on GitHub Pages:
a landing page that lists every report, and one slide viewer per report.

* Landing page: `https://camminati.github.io/ai-reports/`
* Report 1: `https://camminati.github.io/ai-reports/enterprise-ai-2026/`

| Report | Date | What it covers |
|---|---|---|
| [`enterprise-ai-2026`](reports/enterprise-ai-2026) | 30 Sep 2026 | Enterprise AI adoption, failure and forecasts. 46 slides, 94 numbered sources. Cross-industry, with emphasis on the EU and Germany. For CTOs and CAIOs, readable by a CFO. Sources: [SOURCES.md](reports/enterprise-ai-2026/SOURCES.md) |

## How it works

```
reports/<slug>/report.json    title, summary, date, tags (shown on the landing page)
reports/<slug>/deck.json      slide order, sections, fonts
reports/<slug>/slides/*.html  one <section> per slide, 1920x1080, inline styles
reports/<slug>/SOURCES.md     generated from the source slides
reports/<slug>/generators/    (first report only) archived generator scripts
tools/build.py                builds dist/ (Python standard library only)
.github/workflows/pages.yml   builds and deploys on every push to main
```

`python tools/build.py` writes `dist/index.html` (landing page), `dist/reports.json`
and one `dist/<slug>/index.html` viewer per report. The viewer supports arrow keys,
swipe, a section menu, speaker notes (`N`), fullscreen (`F`), deep links (`#12` opens
slide 12) and a PDF button (browser print, one slide per page).

Preview locally: `python tools/build.py && python -m http.server -d dist`

## Add a report

1. `python tools/new_report.py my-report "Title" "One-sentence summary"`
2. Edit `reports/my-report/report.json` (date, audience, tags) and the slides.
3. Push to `main`. The workflow publishes it and the landing page picks it up
   automatically, newest first.

## GitLab

The repository also builds on GitLab: `.gitlab-ci.yml` runs the same build and publishes
it with GitLab Pages (`https://<namespace>.gitlab.io/<project>/`). To mirror it:

```
git remote add gitlab git@gitlab.com:<namespace>/ai-reports.git
git push gitlab --all && git push gitlab --tags
```

Every report lives in its own folder under `reports/`, so more presentations only need a
new folder. Nothing else changes.

## Enable GitHub Pages (once)

Repository **Settings → Pages → Build and deployment → Source: GitHub Actions**.
GitHub Pages on a private repository needs a paid GitHub plan; on a free account the
repository has to be public for the site to be served.

## Checks

* `python tools/check_layout.py reports/<slug>`: renders every slide with Playwright
  and flags text running into the footer, horizontal overflow and wrong page numbers
  (`pip install playwright && playwright install chromium`). It uses fallback fonts
  unless the web fonts are reachable, so also look at the slides in a browser.
* `python tools/export_sources.py reports/<slug>`: rewrites `SOURCES.md` from the
  numbered source slides.

## Conventions used in the first report

* Every figure carries source, date and definition; secondary or unverified figures are
  labelled on the slide.
* Sources are numbered `[1]` to `[94]` in order of first appearance. Slide footers cite
  name plus number, and the source slides list number, publisher, first slide and link.
* Colour scheme for forecast checks: green = came as predicted, yellow = not yet but on
  track, red = missed or false, grey = cannot be checked.

## Caveats

Some pages were read through summaries or abstracts only; those are labelled in the
source list and slide notes. Check quotes against the source before reuse.

## License

MIT for the code (see `LICENSE`). Cited third-party material stays with its owners.
