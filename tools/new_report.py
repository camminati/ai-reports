#!/usr/bin/env python3
"""Scaffold a new report: python tools/new_report.py <slug> "Title" ["One-sentence summary"]"""
import json, re, sys
from datetime import date
from pathlib import Path

slug, title = sys.argv[1], sys.argv[2]
summary = sys.argv[3] if len(sys.argv) > 3 else ''
if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', slug):
    sys.exit('slug: lowercase letters, digits and hyphens only')
d = Path(__file__).resolve().parent.parent / 'reports' / slug
if d.exists():
    sys.exit(f'{d} already exists')
(d / 'slides').mkdir(parents=True)
(d / 'report.json').write_text(json.dumps({
    'title': title, 'summary': summary, 'date': date.today().isoformat(),
    'language': 'en', 'audience': '', 'tags': []}, indent=2, ensure_ascii=False) + '\n')
(d / 'deck.json').write_text(json.dumps({
    'title': title, 'order': ['cover', 'first'],
    'sections': {'intro': {'description': 'Start', 'start': 'cover'}},
    'faces': {'source-serif-4': {'family': 'Source Serif 4', 'href': 'https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;600;700&display=swap'},
              'ibm-plex-sans': {'family': 'IBM Plex Sans', 'href': 'https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&display=swap'}}},
    indent=2) + '\n')
(d / 'slides' / 'cover.html').write_text(f'''<section id="cover" style="display:flex;flex-direction:column;gap:40px;justify-content:end;padding:128px;background:#12202f">
<div style="width:160px;height:8px;background:#f2b65c;border-radius:4px"></div>
<h1 style="font-family:'Source Serif 4',Georgia,serif;font-size:96px;font-weight:600;line-height:1.1;color:#f6f3ec">{title}</h1>
<p style="font-family:'IBM Plex Sans',Arial,sans-serif;font-size:32px;line-height:1.3;color:#d9d2c0">{summary}</p>
</section>
''')
(d / 'slides' / 'first.html').write_text('''<section id="first" style="background:#f6f3ec;color:#12202f;font-family:'IBM Plex Sans',Arial,sans-serif;padding:128px 128px 160px">
<h2 style="font-family:'Source Serif 4',Georgia,serif;font-size:64px;font-weight:600;line-height:1.1">First slide</h2>
<p style="position:absolute;left:128px;bottom:64px;width:1440px;font-size:24px;line-height:1.2;color:#4a5560;white-space:nowrap">Sources: [1].</p><p style="position:absolute;right:128px;bottom:64px;width:120px;font-size:24px;line-height:1.2;color:#4a5560;text-align:right">2</p>
<aside>Speaker notes go here.</aside>
</section>
''')
print(f'created {d}; edit the slides, then: python tools/build.py')
