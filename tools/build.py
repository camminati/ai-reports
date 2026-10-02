#!/usr/bin/env python3
"""Build the static site into dist/ (Python 3.9+, standard library only).

    python tools/build.py [--out dist]

Layout it expects:
    reports/<slug>/report.json   metadata shown on the landing page
    reports/<slug>/deck.json     slide order, sections, fonts
    reports/<slug>/slides/*.html one <section id="..."> per slide (1920x1080 canvas)
    reports/<slug>/SOURCES.md    optional, copied next to the viewer

Output:
    dist/index.html              landing page listing every report
    dist/reports.json            machine-readable index
    dist/<slug>/index.html       slide viewer (keyboard, swipe, notes, print to PDF)
    dist/<slug>/SOURCES.md       if present
    dist/.nojekyll
"""
import html
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / 'reports'

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
FALLBACK_FACES = [
    'https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;600;700&display=swap',
    'https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&display=swap',
]

esc = html.escape

# Fonts are self-hosted (assets/fonts, SIL Open Font License) so the pages make no requests to
# Google and the slides render with the same metrics everywhere.
FONT_DIR = ROOT / 'assets' / 'fonts'
FONT_FILES = [
    ('IBM Plex Sans', 400, 'normal', 'ibm-plex-sans-latin-400-normal.woff2'),
    ('IBM Plex Sans', 500, 'normal', 'ibm-plex-sans-latin-500-normal.woff2'),
    ('IBM Plex Sans', 600, 'normal', 'ibm-plex-sans-latin-600-normal.woff2'),
    ('IBM Plex Sans', 400, 'italic', 'ibm-plex-sans-latin-400-italic.woff2'),
    ('Source Serif 4', 400, 'normal', 'source-serif-4-latin-400-normal.woff2'),
    ('Source Serif 4', 600, 'normal', 'source-serif-4-latin-600-normal.woff2'),
    ('Source Serif 4', 700, 'normal', 'source-serif-4-latin-700-normal.woff2'),
    ('Source Serif 4', 400, 'italic', 'source-serif-4-latin-400-italic.woff2'),
]
BUNDLED = {f[0] for f in FONT_FILES}


def font_css(prefix):
    return ''.join(
        f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};font-display:swap;"
        f"src:url({prefix}{fn}) format('woff2')}}\n" for fam, w, st, fn in FONT_FILES)


# Defaults the slide format promises for text without inline values (h1 96/600/1.1, h2 64/600/1.15,
# h3 44/600/1.2, p 32/400/1.4). font-size does not inherit into h1-h3 but does into p and li.
SLIDE_BASE_CSS = (
    "section{font-size:32px;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;text-rendering:optimizeLegibility}"
    "section h1,section h2,section h3,section p,section ul,section ol{margin:0}"
    "section h1{font-size:96px;font-weight:600;line-height:1.1;text-wrap:balance}"
    "section h2{font-size:64px;font-weight:600;line-height:1.15;text-wrap:balance}"
    "section h3{font-size:44px;font-weight:600;line-height:1.2;text-wrap:balance}"
    "section p,section li{line-height:1.4}"
    "section a{color:inherit;text-decoration:underline}"
)


def load_reports():
    reports = []
    for meta_path in sorted(REPORTS.glob('*/report.json')):
        d = meta_path.parent
        meta = json.loads(meta_path.read_text(encoding='utf-8'))
        deck = json.loads((d / 'deck.json').read_text(encoding='utf-8'))
        reports.append({'slug': d.name, 'dir': d, 'meta': meta, 'deck': deck})
    reports.sort(key=lambda r: r['meta'].get('date', ''), reverse=True)
    return reports


# ---------------------------------------------------------------- viewer

VIEWER_CSS = """
:root{--ink:#12202f;--paper:#f6f3ec;--bar:#12202fe6;--bar-ink:#f6f3ec;--accent:#0b6e6b}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:#0c1620;color:var(--bar-ink);font-family:'IBM Plex Sans',Arial,sans-serif;overflow:hidden}
#stage{position:fixed;inset:0 0 44px 0;display:flex;align-items:center;justify-content:center;overflow:hidden}
#frame{width:1920px;height:1080px;position:relative;flex:none;transform-origin:center center;background:#fff;box-shadow:0 8px 40px #0008}
.slide{display:none;width:1920px;height:1080px;position:absolute;inset:0;overflow:hidden}
.slide.on{display:block}
.slide>section{position:relative;width:1920px;height:1080px;overflow:hidden;box-sizing:border-box}
.slide aside{display:none}
#bar{position:fixed;left:0;right:0;bottom:0;height:44px;background:var(--bar);display:flex;align-items:center;gap:8px;padding:0 12px;font-size:14px;z-index:5}
#bar a,#bar button,#bar select{color:var(--bar-ink);background:transparent;border:1px solid #f6f3ec44;border-radius:6px;padding:5px 10px;font:inherit;text-decoration:none;cursor:pointer}
#bar select option{color:#12202f}
#bar a:hover,#bar button:hover,#bar select:hover{background:#f6f3ec22}
#bar a:focus-visible,#bar button:focus-visible,#bar select:focus-visible{outline:2px solid #6fcbc5;outline-offset:2px}
#count{min-width:74px;text-align:center;font-variant-numeric:tabular-nums}
#sp{flex:1}
#notes{position:fixed;left:0;right:0;bottom:44px;max-height:34vh;overflow:auto;background:#f6f3ec;color:#12202f;padding:14px 20px;font-size:15px;line-height:1.5;border-top:3px solid var(--accent);display:none;z-index:4}
#notes.on{display:block}
#notes b{color:var(--accent)}
@media (max-width:640px){#bar .opt{display:none}}
@media print{
  html,body{height:auto;overflow:visible;background:#fff}
  #bar,#notes{display:none!important}
  #stage{position:static;display:block;overflow:visible}
  #frame{transform:none!important;box-shadow:none;height:auto;width:1920px}
  .slide{display:block!important;position:relative;break-after:page;page-break-after:always}
  @page{size:1920px 1080px;margin:0}
}
"""

VIEWER_JS = """
(function(){
  var slides=[].slice.call(document.querySelectorAll('.slide')), n=slides.length, cur=0;
  var stage=document.getElementById('stage'), frame=document.getElementById('frame'), count=document.getElementById('count'),
      sel=document.getElementById('sections'), notes=document.getElementById('notes'),
      starts=JSON.parse(document.getElementById('starts').textContent);
  document.querySelectorAll('.slide a[href^="http"]').forEach(function(a){a.target='_blank';a.rel='noopener'});
  function fit(){
    var h=document.body.classList.contains('notes')?notes.offsetHeight:0;
    stage.style.bottom=(44+h)+'px';
    var w=innerWidth, hh=innerHeight-44-h, s=Math.min(w/1920,hh/1080);
    frame.style.transform='scale('+s+')';
  }
  function show(i,push){
    cur=Math.max(0,Math.min(n-1,i));
    slides.forEach(function(s,k){s.classList.toggle('on',k===cur)});
    count.textContent=(cur+1)+' / '+n;
    var aside=slides[cur].querySelector('aside');
    notes.innerHTML=aside?'<b>Notes:</b> '+aside.innerHTML:'<b>Notes:</b> none for this slide.';
    var si=0; starts.forEach(function(st,k){if(st<=cur)si=k}); sel.selectedIndex=si;
    if(push!==false)history.replaceState(null,'','#'+(cur+1));
    if(document.body.classList.contains('notes'))fit();
  }
  function go(d){show(cur+d)}
  addEventListener('keydown',function(e){
    if(e.target.tagName==='SELECT'||e.metaKey||e.ctrlKey||e.altKey)return;
    var k=e.key;
    if(k==='ArrowRight'||k==='PageDown'||k===' '||k==='Enter'){go(1);e.preventDefault()}
    else if(k==='ArrowLeft'||k==='PageUp'||k==='Backspace'){go(-1);e.preventDefault()}
    else if(k==='Home')show(0); else if(k==='End')show(n-1);
    else if(k==='n'||k==='N')toggleNotes(); else if(k==='f'||k==='F')fs();
  });
  var x0=null;
  addEventListener('touchstart',function(e){x0=e.touches[0].clientX},{passive:true});
  addEventListener('touchend',function(e){if(x0===null)return;var dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>50)go(dx<0?1:-1);x0=null});
  document.getElementById('prev').onclick=function(){go(-1)};
  document.getElementById('next').onclick=function(){go(1)};
  sel.onchange=function(){show(starts[sel.selectedIndex])};
  function toggleNotes(){document.body.classList.toggle('notes');notes.classList.toggle('on');fit()}
  function fs(){if(document.fullscreenElement)document.exitFullscreen();else document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen()}
  document.getElementById('nbtn').onclick=toggleNotes;
  document.getElementById('fbtn').onclick=fs;
  document.getElementById('pbtn').onclick=function(){print()};
  addEventListener('resize',fit); addEventListener('hashchange',function(){show((parseInt(location.hash.slice(1))||1)-1,false)});
  fit(); show((parseInt(location.hash.slice(1))||1)-1,false);
})();
"""


def build_viewer(rep, out_dir):
    d, deck, meta = rep['dir'], rep['deck'], rep['meta']
    order = deck['order']
    slide_html = []
    for sid in order:
        text = (d / 'slides' / f'{sid}.html').read_text(encoding='utf-8')
        slide_html.append(f'<div class="slide" data-id="{esc(sid)}">{text}</div>')
    sections = deck.get('sections', {})
    starts, labels = [], []
    for key, sec in sections.items():
        if sec['start'] in order:
            starts.append(order.index(sec['start']))
            labels.append(meta.get('section_labels', {}).get(key, key.replace('-', ' ').capitalize()))
    pairs = sorted(zip(starts, labels))
    if not pairs or pairs[0][0] != 0:
        pairs.insert(0, (0, 'Start'))
    starts = [p[0] for p in pairs]
    options = ''.join(f'<option>{esc(l)}</option>' for _, l in pairs)
    extra = [f['href'] for f in deck.get('faces', {}).values()
             if f.get('family') not in BUNDLED and f.get('href')]
    font_links = (FONTS + ''.join(f'<link rel="stylesheet" href="{esc(h)}">' for h in extra)) if extra else ''
    title = esc(meta['title'])
    has_sources = (d / 'SOURCES.md').exists()
    src_link = '<a class="opt" href="SOURCES.md">Sources (md)</a>' if has_sources else ''
    page = f"""<!doctype html>
<html lang="{esc(meta.get('language', 'en'))}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{esc(meta.get('summary', ''))}">
{font_links}
<style>{font_css('../fonts/')}{SLIDE_BASE_CSS}{VIEWER_CSS}</style>
</head>
<body>
<div id="stage"><div id="frame">{''.join(slide_html)}</div></div>
<div id="notes" role="region" aria-label="Speaker notes"></div>
<nav id="bar" aria-label="Slide controls">
  <a href="../" title="All reports">&larr; Reports</a>
  <button id="prev" aria-label="Previous slide">&lsaquo;</button>
  <span id="count" aria-live="polite">1 / {len(order)}</span>
  <button id="next" aria-label="Next slide">&rsaquo;</button>
  <select id="sections" class="opt" aria-label="Jump to section">{options}</select>
  <span id="sp"></span>
  <button id="nbtn" class="opt" title="Toggle notes (N)">Notes</button>
  <button id="fbtn" class="opt" title="Fullscreen (F)">Fullscreen</button>
  <button id="pbtn" class="opt" title="Print or save as PDF">PDF</button>
  {src_link}
</nav>
<script id="starts" type="application/json">{json.dumps(starts)}</script>
<script>{VIEWER_JS}</script>
</body>
</html>
"""
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / 'index.html').write_text(page, encoding='utf-8')
    if has_sources:
        shutil.copy(d / 'SOURCES.md', out_dir / 'SOURCES.md')


# ---------------------------------------------------------------- landing

LANDING_CSS = """
:root{--paper:#f6f3ec;--card:#fffdf8;--ink:#12202f;--muted:#4a5560;--line:#d9d2c0;--accent:#0b6e6b;--chip:#ece6d8}
@media (prefers-color-scheme:dark){:root{--paper:#0f1a25;--card:#16232f;--ink:#f1ede3;--muted:#b3bdc7;--line:#2a3a48;--accent:#6fcbc5;--chip:#1f2f3d}}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--paper);color:var(--ink);font-family:'IBM Plex Sans',system-ui,sans-serif;line-height:1.55}
.wrap{max-width:960px;margin:0 auto;padding:72px 24px 96px}
.eyebrow{font-size:13px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
h1{font-family:'Source Serif 4',Georgia,serif;font-size:clamp(34px,6vw,52px);line-height:1.1;margin:10px 0 16px;font-weight:600}
.lede{font-size:19px;color:var(--muted);max-width:640px}
.list{display:grid;gap:20px;margin-top:48px}
a.card{display:block;text-decoration:none;color:inherit;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:26px 28px;transition:transform .12s,border-color .12s}
a.card:hover{border-color:var(--accent);transform:translateY(-2px)}
a.card:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.meta{font-size:14px;color:var(--muted);display:flex;flex-wrap:wrap;gap:6px 16px}
.card h2{font-family:'Source Serif 4',Georgia,serif;font-size:26px;line-height:1.2;margin:6px 0 10px;font-weight:600}
.card p{color:var(--muted)}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}
.tags span{font-size:13px;background:var(--chip);border-radius:999px;padding:3px 12px}
.go{margin-top:16px;font-weight:600;color:var(--accent);font-size:15px}
.empty{margin-top:48px;color:var(--muted)}
footer{margin-top:64px;font-size:14px;color:var(--muted);border-top:1px solid var(--line);padding-top:20px}
footer a{color:var(--accent)}
"""


def fmt_date(iso):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    m = re.match(r'(\d{4})-(\d{2})(?:-(\d{2}))?$', iso or '')
    if not m:
        return iso or ''
    y, mo, dd = m.groups()
    return f"{int(dd)} {months[int(mo) - 1]} {y}" if dd else f"{months[int(mo) - 1]} {y}"


def build_landing(reports, out):
    cards = []
    for r in reports:
        m = r['meta']
        slides = len(r['deck']['order'])
        bits = [fmt_date(m.get('date')), f'{slides} slides']
        if m.get('sources'):
            bits.append(f"{m['sources']} sources")
        if m.get('audience'):
            bits.append(esc(m['audience']))
        tags = ''.join(f'<span>{esc(t)}</span>' for t in m.get('tags', []))
        cards.append(
            f'<a class="card" href="{esc(r["slug"])}/">'
            f'<div class="meta">{" · ".join(b if b.startswith(("<", "&")) else esc(b) for b in bits)}</div>'
            f'<h2>{esc(m["title"])}</h2><p>{esc(m.get("summary", ""))}</p>'
            f'<div class="tags">{tags}</div><div class="go">Open report &rarr;</div></a>')
    body = ''.join(cards) if cards else '<p class="empty">No reports yet.</p>'
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>AI reports</title>
<meta name="description" content="Sourced research briefings on AI in the enterprise.">
<style>{font_css('fonts/')}{LANDING_CSS}</style>
</head>
<body>
<main class="wrap">
  <p class="eyebrow">Research briefings</p>
  <h1>AI reports</h1>
  <p class="lede">Sourced briefings on how AI performs in practice. The full report gives every figure its source, date and definition and ends with its source list; shorter talk versions point back to it.</p>
  <div class="list">{body}</div>
  <footer>Each report is a slide deck: arrow keys to move, N for notes, F for fullscreen, and the PDF button to print. Source code and how to add a report: see the repository README.</footer>
</main>
</body>
</html>
"""
    (out / 'index.html').write_text(page, encoding='utf-8')
    index = [{'slug': r['slug'], **{k: r['meta'].get(k) for k in ('title', 'summary', 'date', 'tags')},
              'slides': len(r['deck']['order'])} for r in reports]
    (out / 'reports.json').write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding='utf-8')


def main():
    out = ROOT / 'dist'
    if '--out' in sys.argv:
        out = Path(sys.argv[sys.argv.index('--out') + 1]).resolve()
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    reports = load_reports()
    for r in reports:
        build_viewer(r, out / r['slug'])
        print(f"built {r['slug']}: {len(r['deck']['order'])} slides")
    build_landing(reports, out)
    shutil.copytree(FONT_DIR, out / 'fonts')
    (out / '.nojekyll').write_text('')
    print(f'site written to {out}')


if __name__ == '__main__':
    main()
