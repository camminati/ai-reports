from lib import *
import re
def table(rows):
    t=''.join(f'<tr><td style="color:{TEAL}">{e(a)}</td><td>{e(b)}</td></tr>' for a,b in rows)
    return (f'<table style="font-size:28px;color:{INK};font-family:{SANS}"><tr><th style="width:28%;text-align:left">Term</th><th style="width:72%;text-align:left">Plain meaning</th></tr>{t}</table>')
def gl(sid,title,rows,notes,bg):
    body=table(rows)
    s=(f'<section id="{sid}" data-transition="fade" style="background:{bg};color:{INK};font-family:{SANS};padding:128px 128px 160px;display:flex;flex-direction:column;gap:32px">\n'
       +head('Summary',title)+'\n'+body+'\n'
       +f'<p style="position:absolute;left:128px;bottom:64px;width:1440px;font-size:24px;line-height:1.2;color:{MUTED};white-space:nowrap">Definitions are simplified for this deck; each source uses its own wording.</p>'
       +f'<p style="position:absolute;right:128px;bottom:64px;width:120px;font-size:24px;line-height:1.2;color:{MUTED};text-align:right">0</p>\n'
       +f'<aside>{e(notes)}</aside>\n</section>\n')
    open(f'{D}/project/slides/{sid}.html','w').write(s)
gl('terms2','Terms for technology, cost and dependence',[
 ('Generative AI (GenAI)','AI that writes text, code or images from instructions, such as ChatGPT or Claude'),
 ('Inference and tokens','Inference is the computing done each time a model answers; tokens are the text pieces it is billed by'),
 ('Compute','The chips and data-centre power needed to train and run AI, counted in gigawatts (GW) of capacity'),
 ('Hyperscaler','One of the very large cloud providers: Amazon, Microsoft or Google'),
 ('Vendor lock-in','Being tied to one supplier because leaving costs too much money or effort'),
 ('Egress fee','A charge for moving your own data out of a cloud provider'),
 ('Digital sovereignty','Keeping control of your own data, software and infrastructure, without depending on a foreign supplier'),
 ('Open source','Software whose code is public and free to use and change, such as LibreOffice'),
],'Second glossary page, covering words used on the case-study, dependency, cost and government slides. Definitions are our plain-language paraphrases. Egress fees and switching charges are addressed by the EU Data Act from 12 January 2027. Compute figures on the dependency slide come from a Bruegel brief citing the Europe2031.ai dataset.',PAPER)
gl('terms3','Terms for law, evidence and reading the numbers',[
 ('EU AI Act','The EU law on AI; “high-risk” uses, for example hiring or credit decisions, carry the strictest duties'),
 ('AGI','Artificial general intelligence: AI that matches people across most tasks; there is no agreed test'),
 ('Regulatory capture','When the rules end up shaped to suit the firms they are meant to control'),
 ('Self-reported','Answers given by the company or respondent in a survey, not measured or audited'),
 ('Percentage point','The gap between two percentages: 13.5% to 20.0% is +6.5 points, not +6.5%'),
 ('Weighted by employees','Each firm counts by its number of staff, so large firms weigh more'),
 ('Back-test, trial','A back-test checks a forecast against what happened; a trial compares groups in an experiment'),
 ('Survey names','BTOS: US Census business survey. SBU: Atlanta Fed executive survey. n = number of respondents'),
],'Third glossary page, covering words used on the regulation, forecast, media and adoption slides. The high-risk examples reflect the AI Act categories for employment and creditworthiness; the AI Act text itself was not re-read for this deck. Definitions are our plain-language paraphrases.',PAPER2)
# rename terms slide
f=D+'/project/slides/terms.html'; s=open(f).read()
assert 'Eight terms, in plain language' in s
s=s.replace('Eight terms, in plain language','Terms for AI adoption and value'); open(f,'w').write(s)
# deck order
dj=json.load(open(f'{D}/project/deck.json'))
o=dj['order']
for k in ('terms3','terms2'):
    if k not in o: o.insert(o.index('terms')+1,k)
json.dump(dj,open(f'{D}/project/deck.json','w'),indent=1,ensure_ascii=False)
for i,sid in enumerate(o):
    if sid=='cover': continue
    ff=f'{D}/project/slides/{sid}.html'; t=open(ff).read()
    ms=list(re.finditer(r'(text-align:\s*right[^"]*">)([^<]*)(</p>)',t)); assert ms,sid
    m=ms[-1]; t=t[:m.start(2)]+str(i+1)+t[m.end(2):]; open(ff,'w').write(t)
print(len(o))
