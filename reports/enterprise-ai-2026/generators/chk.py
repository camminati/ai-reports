import json,sys,os
from playwright.sync_api import sync_playwright
D='/path/to/scratchpad/artifact-files/<artifact-id>/project/slides/'
ids=sys.argv[1:]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium' if os.path.exists('/opt/pw-browsers/chromium') else None)
    pg=b.new_page(viewport={'width':1920,'height':1080})
    for sid in ids:
        h=open(D+sid+'.html').read()
        pg.set_content('<html><body style="margin:0"><div style="width:1920px;height:1080px;position:relative;overflow:visible">'+h.replace('<section','<section',1)+'</div><style>*{margin:0;padding:0;box-sizing:border-box}section{position:relative;width:1920px;height:1080px;box-sizing:border-box}aside{display:none}</style></body></html>')
        r=pg.evaluate('''()=>{const s=document.querySelector('section');let mb=0,mr=0;
          for(const c of s.children){ if(c.tagName==='ASIDE')continue; const st=getComputedStyle(c); if(st.position==='absolute')continue; const r=c.getBoundingClientRect(); mb=Math.max(mb,r.bottom); mr=Math.max(mr,r.right);}
          // deepest overflow
          let deep=0;for(const e of s.querySelectorAll('*')){const st=getComputedStyle(e); if(st.position==='absolute')continue; deep=Math.max(deep,e.getBoundingClientRect().bottom)}
          return [Math.round(mb),Math.round(deep),Math.round(mr)]}''')
        print(sid,r,'OVER' if r[1]>920 else 'ok')
    b.close()
