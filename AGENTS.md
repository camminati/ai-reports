# AGENTS.md

Guidance for AI coding agents working in this repository.

## Commits and pull requests

* Do not add any AI attribution to commit messages, pull request titles or descriptions.
  No `Co-Authored-By` trailers naming an assistant, no "Generated with ..." lines, no session
  links, no "assisted by" remarks. Commit messages describe the change and nothing else.
* Write commit messages in the imperative, short subject line first, optional body after a blank line.
* Do not push to `main` directly; work on a branch and open a pull request.

## Repository layout

* `reports/<slug>/` holds one presentation: `report.json` (landing page metadata), `deck.json`
  (slide order, sections, fonts), `slides/*.html` (one `<section>` per slide, 1920x1080, inline
  styles), `SOURCES.md` (generated).
* `tools/build.py` builds the site (landing page plus one viewer per report) into `dist/`.
* `.github/workflows/ci.yml` checks branches and pull requests; `.github/workflows/pages.yml` deploys to GitHub Pages and `.gitlab-ci.yml` to GitLab Pages,
  both from the default branch.
* `reports/enterprise-ai-2026/generators/` is an archive. Do not re-run it: the slide files are the
  source of truth and the old scripts would overwrite later edits.

## Working on a report

* New report: `python tools/new_report.py <slug> "Title" "Summary"`.
* Keep the slide format: footer at `left:128px; bottom:64px; width:1440px; white-space:nowrap`,
  page number at `right:128px; bottom:64px`, and keep page numbers sequential after adding or
  removing slides.
* Every figure needs a source, a date and a definition. Mark secondary, abstract-only or
  self-reported figures on the slide. Sources are numbered `[n]` in order of first appearance;
  footers cite name plus number. After changing source slides run
  `python tools/export_sources.py reports/<slug>`.
* Before committing: `python tools/build.py` and `python tools/check_layout.py reports/<slug>`
  (needs Playwright with Chromium). The layout check uses fallback fonts unless web fonts are
  reachable, so review the slides in a browser too.
* Do not commit `dist/` or `public/`.
