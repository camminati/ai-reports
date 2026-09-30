#!/usr/bin/env python3
"""Layout check for a report's slides (needs: pip install playwright && playwright install chromium).

Usage: python tools/check_layout.py reports/<slug> [--stress 1.15]

Renders every slide at 1920x1080 and reports
  * content that reaches the footer,
  * footer text that runs into the page number or off the slide,
  * horizontal overflow (anything right of x = 1795),
  * page numbers that are not sequential.
--stress widens footer text by a factor to allow for font differences
(the checker uses fallback fonts unless the web fonts are reachable).
"""
import json, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

JS = """(SC) => {
  const s = document.querySelector('section'); let content = 0, right = 0; const abs = [];
  for (const e of s.querySelectorAll('*')) {
    const st = getComputedStyle(e);
    if (st.position === 'absolute') { abs.push(e); continue; }
    const host = e.closest('[style*="position:absolute"]');
    if (host && host !== s) continue;
    const r = e.getBoundingClientRect();
    if (r.width > 0 && r.height > 0) { content = Math.max(content, r.bottom); right = Math.max(right, r.right); }
  }
  let foot = null, num = null;
  for (const a of abs) {
    const r = a.getBoundingClientRect(), st = getComputedStyle(a), t = a.textContent.trim();
    if (st.whiteSpace === 'nowrap') {
      const rg = document.createRange(); rg.selectNodeContents(a);
      foot = { left: r.left, top: r.top, tw: rg.getBoundingClientRect().width * SC };
    } else num = { left: r.left, text: t };
  }
  return { content: Math.round(content), right: Math.round(right), foot, num };
}"""

def main():
    args = sys.argv[1:]
    stress = 1.15
    if '--stress' in args:
        i = args.index('--stress'); stress = float(args[i + 1]); del args[i:i + 2]
    root = Path(args[0])
    order = json.loads((root / 'deck.json').read_text())['order']
    bad = 0
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': 1920, 'height': 1080})
        for i, sid in enumerate(order, 1):
            html = (root / 'slides' / f'{sid}.html').read_text()
            pg.set_content('<html><body style="margin:0"><style>*{margin:0;padding:0;box-sizing:border-box}'
                           'section{position:relative;width:1920px;height:1080px;overflow:visible}aside{display:none}</style>'
                           + html + '</body></html>')
            r = pg.evaluate(JS, stress)
            issues = []
            f, n = r['foot'], r['num']
            if r['right'] > 1795: issues.append(f"horizontal overflow (right edge {r['right']})")
            if f:
                if n and f['left'] + f['tw'] > n['left'] - 16: issues.append('footer runs into page number')
                if f['left'] + f['tw'] > 1920 - 64: issues.append('footer beyond slide edge')
                if r['content'] > f['top'] - 12: issues.append(f"content bottom {r['content']} reaches footer")
            if n and sid != 'cover' and n['text'] != str(i): issues.append(f"page number {n['text']} != {i}")
            if issues:
                bad += 1; print(f'{i:>3} {sid}: ' + '; '.join(issues))
        b.close()
    print(f'{len(order)} slides checked, {bad} with issues')
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
