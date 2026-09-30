import re,html,sys
import srcmap
from srcmap import *
K[3]=r'AI-ready data'; K[85]=r'New York Times|NYT'; K[5]=r'inference cost'; K[19]=r'secondary report'
def pos(k):
    rx=re.compile(K[k])
    for i in sorted(vis):
        m=rx.search(vis[i])
        if m: return (i,0,m.start())
    for i in sorted(note):
        m=rx.search(note[i])
        if m: return (i,1,m.start())
    raise SystemExit('none '+str(k))
E=[]
for k,e in enumerate(ents):
    e['pos']=pos(k); E.append(e)
E.sort(key=lambda e:(e['pos'],e['idx']))
sizes=[11,11,10,10,10,10,10,10,10]; assert sum(sizes)==92
esc=lambda s:html.escape(s,quote=False)
def entry(e):
    return ('<p style="font-size:24px;line-height:1.3;color:#12202F"><b style="color:#0B6E6B">%d</b>  <b>%s</b><br><a href="%s">%s</a></p>'
            %(e['pos'][0],esc(e['label']),html.escape(e['url'],quote=True),esc(e['shown'])))
D=srcmap.D
i=0
for n,sz in enumerate(sizes,1):
    chunk=E[i:i+sz]; i+=sz
    h=(sz+1)//2
    cols=[chunk[:h],chunk[h:]]
    old=open(D+'slides/src%d.html'%n).read()
    pg=re.search(r'right:\s*128px[^>]*>(\d+)</p>',old).group(1)
    body=''.join('<div style="flex:1;display:flex;flex-direction:column;gap:16px">%s</div>'%''.join(entry(e) for e in c) for c in cols)
    a,b=chunk[0]['pos'][0],chunk[-1]['pos'][0]
    html_=('<section id="src%d" data-transition="fade" style="background:#ECE6D8;color:#12202F;font-family:\'IBM Plex Sans\', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;gap:32px">\n'
    '<div style="display:flex;flex-direction:column;gap:8px"><p style="font-size:24px;line-height:1.2;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:#0B6E6B">Sources · teal number = slide where first cited</p><h2 style="font-family:\'Source Serif 4\', Georgia, serif;font-size:64px;font-weight:600;line-height:1.1;color:#12202F">Sources (%d of 9), slides %d to %d</h2></div>\n'
    '<div style="display:flex;gap:40px;align-items:flex-start">%s</div>\n'
    '<p style="position:absolute;left:128px;bottom:64px;width:1440px;font-size:24px;line-height:1.2;color:#4A5560;white-space:nowrap">Accessed September 2026. Some pages were read through summaries; check quotes against the source before reuse.</p><p style="position:absolute;right:128px;bottom:64px;width:120px;font-size:24px;line-height:1.2;color:#4A5560;text-align:right">%s</p>\n'
    '<aside>Full list of sources, ordered by the first slide that cites them (visible text first, then speaker notes). Primary documents were opened and checked where marked in the notes; secondary reports are labelled on the slides that use them. Vendor-affiliated or interested-party sources are flagged on the slides where used. Blocked to our tools: heise, EJIL Talk, Balkan Insight, CNBC, The Register, economist.com, theguardian.com; two journal pages (Taylor &amp; Francis, Springer) were read via university abstracts.</aside>\n</section>\n')%(n,n,a,b,body,pg)
    open(D+'slides/src%d.html'%n,'w').write(html_)
    print(n,a,b,len(chunk))
