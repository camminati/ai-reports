import sys
from playwright.sync_api import sync_playwright
D='/tmp/claude-0/-home-claude/d83e9c40-3403-54e5-b4cb-d33f00f5ffd5/scratchpad/artifact-files/30f3ab63-14e0-49e5-9d25-52d5f6df0be8/project/slides/'
import json
order=json.load(open(D+'../deck.json'))['order']
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1920,'height':1080})
    for i,sid in enumerate(order,1):
        pg.set_content('<html><body style="margin:0"><style>*{margin:0;padding:0;box-sizing:border-box}section{position:relative;width:1920px;height:1080px}aside{display:none}</style>'+open(D+sid+'.html').read()+'</body></html>')
        r=pg.evaluate('''()=>{let m=0,who='';for(const e of document.querySelectorAll('section *')){const r=e.getBoundingClientRect();if(r.width>0&&r.right>m){m=r.right;who=e.tagName+':'+(e.textContent||'').slice(0,30)}}return [Math.round(m),who]}''')
        if r[0]>1795: print('OVERFLOW',i,sid,r)
    b.close()
