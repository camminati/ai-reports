from playwright.sync_api import sync_playwright
D='/path/to/scratchpad/artifact-files/<artifact-id>/project/slides/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1920,'height':1080})
    for sid in ['lead1','past','open','open2']:
        pg.set_content('<html><body style="margin:0"><style>*{margin:0;padding:0;box-sizing:border-box}section{position:relative;width:1920px;height:1080px}aside{display:none}</style>'+open(D+sid+'.html').read()+'</body></html>')
        r=pg.evaluate('''()=>{const s=document.querySelector('section');const L=s.querySelector('[style*="top:128px"]');const lr=L.getBoundingClientRect();
        const eb=s.querySelector('p').getBoundingClientRect();const rg=document.createRange();rg.selectNodeContents(s.querySelector('p'));const ebt=rg.getBoundingClientRect();
        const h2=s.querySelector('h2').getBoundingClientRect();
        const rows=[...s.querySelectorAll('div[style*="align-items:stretch"]')].map(e=>Math.round(e.getBoundingClientRect().height));
        return {legend:[Math.round(lr.left),Math.round(lr.top),Math.round(lr.right),Math.round(lr.bottom)],ebtext_right:Math.round(ebt.right),h2:[Math.round(h2.top),Math.round(h2.bottom)],rows}}''')
        print(sid,r)
    b.close()
