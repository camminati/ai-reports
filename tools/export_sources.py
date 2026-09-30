#!/usr/bin/env python3
"""Write SOURCES.md for a report from its numbered source slides (ids starting with 'src').

Usage: python tools/export_sources.py reports/<slug>
"""
import html, json, re, sys
from pathlib import Path

root = Path(sys.argv[1])
order = json.loads((root / 'deck.json').read_text())['order']
title = json.loads((root / 'report.json').read_text())['title']
rows = []
for sid in order:
    if not sid.startswith('src'):
        continue
    text = (root / 'slides' / f'{sid}.html').read_text()
    text = re.sub(r'<aside>.*?</aside>', '', text, flags=re.S)
    for p in re.findall(r'<p style="font-size:24px;line-height:1\.3[^>]*>(.*?)</p>', text, re.S):
        head = re.search(r'<b[^>]*>\[(\d+)\] · (.*?) · slide (\d+)</b>', p)
        if not head:
            continue
        name = re.findall(r'<b>(.*?)</b>', p, re.S)
        a = re.search(r'<a href="(.*?)">', p)
        rows.append((int(head.group(1)), html.unescape(head.group(2)), int(head.group(3)),
                     html.unescape(name[0]), html.unescape(a.group(1))))
rows.sort()
out = [f'# Sources: {title}', '',
       'Numbered in order of first appearance in the slides. Slide numbers refer to the deck.', '',
       '| # | Publisher | Title | First slide | Link |', '|---|---|---|---|---|']
for n, pub, slide, name, url in rows:
    out.append(f'| {n} | {pub} | {name.replace("|", "/")} | {slide} | <{url}> |')
(root / 'SOURCES.md').write_text('\n'.join(out) + '\n')
print(f'{len(rows)} sources -> {root / "SOURCES.md"}')
