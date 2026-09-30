from lib import *
import re
dj=json.load(open(f'{D}/project/deck.json'))
old=[x for x in dj['order'] if x not in ('open','open2')]
order=['cover','summary','terms','adopt-def','funnel','eu','de','industry','agents',
 'cases','cases-ok','dep','lockin','exit','gov','extremes','reg',
 'past','open','open2','models','markov','lead1','lead2','media','media2',
 'factors','causes','barriers','patterns','metrics','actions','caveats','src1','src2','src3']+json.load(open('srcids.json'))
assert set(order)>=set(dj['order']), set(dj['order'])-set(order)
dj['order']=order
dj['sections']={
 'intro':{'description':'Headline findings and plain-language terms.','start':'cover'},
 'adoption':{'description':'How much AI is used, where and by whom.','start':'adopt-def'},
 'landscape':{'description':'Real cases, dependency and lock-in costs, government extremes and regulation.','start':'cases'},
 'forecasts':{'description':'Which predictions held and which models exist.','start':'past'},
 'voices':{'description':'AI leaders’ forecasts against evidence, and how media cover AI.','start':'lead1'},
 'factors':{'description':'What separates value from abandonment.','start':'factors'},
 'action':{'description':'What to track, what to do, and how far to trust the numbers.','start':'metrics'},
 'refs':{'description':'Sources.','start':'src1'}}
json.dump(dj,open(f'{D}/project/deck.json','w'),indent=1,ensure_ascii=False)
for i,sid in enumerate(order):
    if sid=='cover': continue
    f=f'{D}/project/slides/{sid}.html'
    s=open(f).read()
    ms=list(re.finditer(r'(text-align:\s*right[^"]*">)([^<]*)(</p>)',s))
    assert ms,sid
    m=ms[-1]
    s=s[:m.start(2)]+str(i+1)+s[m.end(2):]
    open(f,'w').write(s)
    assert 'id="'+sid+'"' in s, sid
print(len(order))
