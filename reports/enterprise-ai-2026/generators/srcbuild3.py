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
for _n,_e in enumerate(E,1): _e['num']=_n
import sys
N=int(sys.argv[1]); base,extra=divmod(94,N); sizes=[base+(1 if j<extra else 0) for j in range(N)]; assert sum(sizes)==94
esc=lambda s:html.escape(s,quote=False)
from srcpub import split
FIX={9:('S&P Global','Market Intelligence, Voice of the Enterprise: AI and ML (2025)'),
}
def pubtitle(e):
    l=e['label']; p,t=split(l)
    if p is None: return '?',l
    rep={'Federal Reserve FEDS Note':('Federal Reserve','FEDS Note: '),'Bitkom press release':('Bitkom','Press release: '),'Bitkom Research':('Bitkom','Research: '),
         'Deloitte Insights':('Deloitte',''),'Reuters factbox via Yahoo':('Reuters (via Yahoo)','Factbox: '),'AI Act Article 99':('EU AI Act','Article 99: '),
         'Lammar':('Lammar, Horst and Mueller',''),'S&P Global Market Intelligence':('S&P Global','')}
    pre=''
    if p in rep: p,pre=rep[p]
    if p=='Lammar, Horst and Mueller': t=t.replace('Horst and Mueller, ','')
    t=pre+t
    return p,t[0].upper()+t[1:]
def entry(e):
    p,t=pubtitle(e)
    return ('<p style="font-size:24px;line-height:1.3;color:#12202F"><b style="color:#0B6E6B;letter-spacing:1px">[%d] · %s · slide %d</b><br><b>%s</b><br><a href="%s">%s</a></p>'
            %(e['num'],esc(p.upper()),e['pos'][0],esc(t),html.escape(e['url'],quote=True),esc(e['shown'])))
i=0
for n,sz in enumerate(sizes,1):
    chunk=E[i:i+sz]; i+=sz
    h=(sz+1)//2
    cols=[chunk[:h],chunk[h:]]
    pg=str(36+n)
    body=''.join('<div style="flex:1;display:flex;flex-direction:column;gap:16px">%s</div>'%''.join(entry(e) for e in c) for c in cols)
    a,b=chunk[0]['pos'][0],chunk[-1]['pos'][0]
    html_=('<section id="src%d" data-transition="fade" style="background:#ECE6D8;color:#12202F;font-family:\'IBM Plex Sans\', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;gap:32px">\n'
    '<div style="display:flex;flex-direction:column;gap:8px"><p style="font-size:24px;line-height:1.2;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:#0B6E6B">Sources · [number], publisher, first slide citing it</p><h2 style="font-family:\'Source Serif 4\', Georgia, serif;font-size:64px;font-weight:600;line-height:1.1;color:#12202F">Sources (%d of %d), slides %d to %d</h2></div>\n'
    '<div style="display:flex;gap:40px;align-items:flex-start">%s</div>\n'
    '<p style="position:absolute;left:128px;bottom:64px;width:1440px;font-size:24px;line-height:1.2;color:#4A5560;white-space:nowrap">Accessed September 2026. Some pages were read through summaries; check quotes against the source before reuse.</p><p style="position:absolute;right:128px;bottom:64px;width:120px;font-size:24px;line-height:1.2;color:#4A5560;text-align:right">%s</p>\n'
    '<aside>Full list of sources, ordered by the first slide that cites them (visible text first, then speaker notes). Primary documents were opened and checked where marked in the notes; secondary reports are labelled on the slides that use them. Vendor-affiliated or interested-party sources are flagged on the slides where used. Blocked to our tools: heise, EJIL Talk, Balkan Insight, CNBC, The Register, economist.com, theguardian.com; two journal pages (Taylor &amp; Francis, Springer) were read via university abstracts.</aside>\n</section>\n')%(n,n,N,a,b,body,pg)
    open(D+'slides/src%d.html'%n,'w').write(html_)
    print(n,a,b,len(chunk))
