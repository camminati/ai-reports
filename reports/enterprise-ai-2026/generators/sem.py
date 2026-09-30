import re
D='/tmp/claude-0/-home-claude/d83e9c40-3403-54e5-b4cb-d33f00f5ffd5/scratchpad/artifact-files/30f3ab63-14e0-49e5-9d25-52d5f6df0be8/project/slides/'
G='#78C28A';Y='#F2CF5B';R='#E5786A';N='#CBD0D6'
def rd(n): return open(D+n+'.html').read()
def wr(n,t): open(D+n+'.html','w').write(t)
def sub(t,a,b,count=1):
    assert t.count(a)==count,(a[:70],t.count(a))
    return t.replace(a,b)
def legend():
    def it(c,l): return f'<div style="display:flex;align-items:center;gap:8px"><div style="width:22px;height:22px;border-radius:6px;background:{c}"></div><p style="font-size:24px;line-height:1.2;color:#4A5560">{l}</p></div>'
    return ('<div style="position:absolute;top:128px;right:128px;display:flex;align-items:center;gap:28px">'
            +it(G,'As predicted')+it(Y,'Not yet, on track')+it(R,'Missed or off track')+it(N,'Unchecked')+'</div>\n')
def add_legend(t):
    i=t.index('<div style="display:flex;flex-direction:column;gap:8px">')
    return t[:i]+legend()+t[i:]
def add_note(t,txt):
    return sub(t,'</aside>',' '+txt+'</aside>')
KEY='Colour key (our reading of the evidence): green = came as predicted; yellow = not yet, but on track; red = missed or off track; grey = cannot be checked.'

# ---- lead1
t=rd('lead1')
old_new=[
 ('background:#F2B65C;border-radius:16px;padding:18px 24px;display:flex;flex-direction:column;justify-content:center"><p style="font-size:26px;line-height:1.25;font-weight:600;color:#12202F">Partly held, self-reported</p>', Y,'ON TRACK','Held at Anthropic; self-reported'),
 ('background:#6FCBC5;border-radius:16px;padding:18px 24px;display:flex;flex-direction:column;justify-content:center"><p style="font-size:26px;line-height:1.25;font-weight:600;color:#12202F">Too early; 10–20% unemployment off track</p>', R,'OFF TRACK','Window runs to 2030'),
 ('background:#F2B65C;border-radius:16px;padding:18px 24px;display:flex;flex-direction:column;justify-content:center"><p style="font-size:26px;line-height:1.25;font-weight:600;color:#12202F">Mostly not in 2025 (“may”)</p>', Y,'ON TRACK','Late: agents worked from Dec 2025'),
 ('background:#F2B65C;border-radius:16px;padding:18px 24px;display:flex;flex-direction:column;justify-content:center"><p style="font-size:26px;line-height:1.25;font-weight:600;color:#12202F">No evidence found</p>', R,'MISSED','Meta itself: slower than hoped'),
 ('background:#6FCBC5;border-radius:16px;padding:18px 24px;display:flex;flex-direction:column;justify-content:center"><p style="font-size:26px;line-height:1.25;font-weight:600;color:#12202F">Held per OpenAI, unverified</p>', N,'UNCHECKED','OpenAI says yes; no outside check'),
]
for old,c,tag,txt in old_new:
    new=(f'background:{c};border-radius:16px;padding:12px 24px;display:flex;flex-direction:column;justify-content:center;gap:2px">'
         f'<p style="font-size:24px;line-height:1.2;font-weight:600;letter-spacing:1px;color:#12202F">{tag}</p>'
         f'<p style="font-size:24px;line-height:1.3;color:#12202F">{txt}</p>')
    t=sub(t,old,new)
t=add_legend(t)
t=add_note(t,KEY+' Judgement calls: the jobs forecast is red because unemployment is 4.1% against a 10–20% claim, although the window runs to 2030; Zuckerberg is red because Meta itself said in Jul 2026 that agents progressed more slowly than hoped; the OpenAI research intern is grey because only OpenAI can check it.')
wr('lead1',t)

# ---- past
t=rd('past')
t=sub(t,'background:#F2B65C;border-radius:16px;padding:16px 28px;display:flex;flex-direction:column;justify-content:center;gap:6px"><p style="font-size:24px;line-height:1.2;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:#12202F">Reading</p><p style="font-size:28px;line-height:1.3;color:#12202F;font-weight:600;">Too low, by Gartner’s own later count</p>',
 f'background:{G};border-radius:16px;padding:16px 28px;display:flex;flex-direction:column;justify-content:center;gap:6px"><p style="font-size:24px;line-height:1.2;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:#12202F">Reading</p><p style="font-size:28px;line-height:1.3;color:#12202F;font-weight:600;">Came true, and worse than forecast</p>')
t=sub(t,'background:#F2B65C;border-radius:16px;padding:16px 28px;display:flex;flex-direction:column;justify-content:center;gap:6px"><p style="font-size:24px;line-height:1.2;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:#12202F">Reading</p><p style="font-size:28px;line-height:1.3;color:#12202F;font-weight:600;">Adoption under-forecast, and failure rose too</p>',
 f'background:{R};border-radius:16px;padding:16px 28px;display:flex;flex-direction:column;justify-content:center;gap:6px"><p style="font-size:24px;line-height:1.2;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:#12202F">Reading</p><p style="font-size:28px;line-height:1.3;color:#12202F;font-weight:600;">Missed: adoption beat the plans, and failure rose too</p>')
t=sub(t,'background:#6FCBC5;border-radius:16px;padding:16px 28px',f'background:{G};border-radius:16px;padding:16px 28px')
t=add_legend(t)
t=add_note(t,KEY+' The S&P row is red because the plans understated actual adoption; the direction was right, the size was not.')
wr('past',t)

# ---- open / open2 pills
def pill(t,oldbg,newbg,label):
    return sub(t,f'background:{oldbg};color:#12202F;padding:8px 16px;border-radius:24px">{label}',f'background:{newbg};color:#12202F;padding:8px 16px;border-radius:24px">{label}')
t=rd('open')
t=pill(t,'#F2B65C',Y,'Consistent so far, but indirect')
t=pill(t,'#F2B65C',Y,'Incidents are common; rollbacks are not measured')
t=add_legend(t); t=add_note(t,KEY); wr('open',t)
t=rd('open2')
t=pill(t,'#F2B65C',Y,'The gap is visible in every survey')
t=pill(t,'#6FCBC5',Y,'Unit price falls, workflow cost rises')
t=add_legend(t); t=add_note(t,KEY+' Both forecasts run to 2026–2028, so no result is final; yellow means the indicators point the predicted way.'); wr('open2',t)

# ---- neutral "our reading" callouts (avoid reading amber as a verdict)
for n in ('lead2','media2'):
    t=rd(n)
    t=sub(t,'background:#F2B65C;border:1px solid #F2B65C;border-radius:16px;padding:24px','background:#FFFDF8;border:3px solid #0B6E6B;border-radius:16px;padding:22px')
    wr(n,t)
print('ok')
