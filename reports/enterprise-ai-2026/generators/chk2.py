import json,os,sys
from playwright.sync_api import sync_playwright
D='/tmp/claude-0/-home-claude/d83e9c40-3403-54e5-b4cb-d33f00f5ffd5/scratchpad/artifact-files/30f3ab63-14e0-49e5-9d25-52d5f6df0be8/project/'
order=json.load(open(D+'deck.json'))['order']
SC=float(sys.argv[1]) if len(sys.argv)>1 else 1.08
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={'width':1920,'height':1080})
    for i,sid in enumerate(order,1):
        h=open(D+'slides/'+sid+'.html').read()
        pg.set_content('<html><body style="margin:0"><style>*{margin:0;padding:0;box-sizing:border-box}section{position:relative;width:1920px;height:1080px;overflow:visible}aside{display:none}</style>'+h+'</body></html>')
        r=pg.evaluate('''(SC)=>{const s=document.querySelector('section');let content=0;
          const abs=[];
          for(const e of s.querySelectorAll('*')){const st=getComputedStyle(e);
            if(st.position==='absolute'){abs.push(e);continue}
            if(e.closest('[style*="position:absolute"]')&&e.closest('[style*="position:absolute"]')!==s) continue;
            const r=e.getBoundingClientRect(); if(r.width>0&&r.height>0) content=Math.max(content,r.bottom)}
          let foot=null,num=null;
          for(const a of abs){const t=a.textContent.trim(); const r=a.getBoundingClientRect(); const st=getComputedStyle(a);
            if(st.whiteSpace==='nowrap'){const rg=document.createRange();rg.selectNodeContents(a);const tw=rg.getBoundingClientRect().width;foot={left:r.left,top:r.top,bottom:r.bottom,tw:tw*SC,boxw:r.width,text:t}}
            else num={left:r.left,top:r.top,text:t}}
          return {content:Math.round(content),foot,num}}''',SC)
        f=r['foot'];n=r['num']
        issues=[]
        if f:
            if f['left']+f['tw']>n['left']-16 if n else False: issues.append(f"footer text runs into page number (right edge ~{round(f['left']+f['tw'])} vs {round(n['left'])})")
            if f['left']+f['tw']>1920-64: issues.append('footer beyond slide edge')
            if r['content']>f['top']-12: issues.append(f"content bottom {r['content']} reaches footer top {round(f['top'])}")
            if abs(f['left']-128)>1 or abs(f['bottom']-(1080-64))>2: issues.append(f"footer position off-standard left={round(f['left'])} bottom={round(f['bottom'])}")
        else: issues.append('no footer' if sid!='cover' else '')
        if n and n['text']!=str(i) and sid!='cover': issues.append(f"page number {n['text']} != {i}")
        print(i,sid,r['content'],'; '.join(x for x in issues if x) or 'ok')
    b.close()
