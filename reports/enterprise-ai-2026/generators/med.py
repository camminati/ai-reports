import json,re,html
D='/tmp/claude-0/-home-claude/d83e9c40-3403-54e5-b4cb-d33f00f5ffd5/scratchpad/artifact-files/30f3ab63-14e0-49e5-9d25-52d5f6df0be8/project/'
INK='#12202F';PAPER='#F6F3EC';PAPER2='#ECE6D8';CARD='#FFFDF8';LINE='#D9D2C0';MUTED='#4A5560';TEAL='#0B6E6B'
SERIF="'Source Serif 4', Georgia, serif";SANS="'IBM Plex Sans', Arial, sans-serif"
e=lambda t: html.escape(t,quote=False)
def head(eb,t):
    return (f'<div style="display:flex;flex-direction:column;gap:8px"><p style="font-size:24px;line-height:1.2;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{TEAL}">{e(eb)}</p>'
            f'<h2 style="font-family:{SERIF};font-size:64px;font-weight:600;line-height:1.1;color:{INK}">{e(t)}</h2></div>')
def foot(txt,num):
    return (f'<p style="position:absolute;left:128px;bottom:64px;width:1440px;font-size:24px;line-height:1.2;color:{MUTED};white-space:nowrap">{e(txt)}</p>'
            f'<p style="position:absolute;right:128px;bottom:64px;width:120px;font-size:24px;line-height:1.2;color:{MUTED};text-align:right">{num}</p>\n')
def rw(name,sample,finding):
    return (f'<div style="display:flex;gap:24px;align-items:stretch">'
     f'<div style="width:520px;flex:none;background:{CARD};border:1px solid {LINE};border-radius:16px;padding:12px 28px;display:flex;flex-direction:column;justify-content:center;gap:2px">'
     f'<p style="font-size:24px;line-height:1.3;color:{INK};font-weight:600">{e(name)}</p><p style="font-size:24px;line-height:1.3;color:{MUTED}">{e(sample)}</p></div>'
     f'<div style="flex:1;background:{CARD};border:1px solid {LINE};border-radius:16px;padding:12px 24px;display:flex;flex-direction:column;justify-content:center">'
     f'<p style="font-size:24px;line-height:1.35;color:{INK}">{e(finding)}</p></div></div>')
rows=[
 ('Otto Brenner Stiftung, 2025','2,217 articles · 9 outlets · 2022–23','Economic framing dominates; AI firms and their mostly male spokespeople are most visible; social impacts in 1 in 4 articles (taz: almost 45%).'),
 ('CAIS Factsheet 7, 2022','4,968 articles · 37 outlets · 2018–21','Economy dominates. FAZ and SZ cover the widest range of angles; regional papers focus on economy; trade media on products.'),
 ('Leidecker-Sandmann et al., 2025','589 articles, 6 outlets (image study)','Robot images fell from 16% to 7% of all images; “chances” was the most common frame; imagery varied more after ChatGPT.'),
 ('Köstler & Ossewaarde, 2021','Government papers + 4 newspapers','Media largely adopted the federal government’s AI vision; some outlets partly challenged it (abstract only).'),
 ('Lammar, Horst & Müller, 2025','4 years of German newspapers','AI in general is told as a promising future and global race; local case stories do not counter the hype (abstract only).'),
 ('Zai et al., 2025','1,588 articles · incl. SZ and Bild','Progress was the biggest frame (35.5%), ethics the smallest; no outlet comparison, so no Bild-versus-SZ result.'),
]
notes=("German studies on how media cover AI. (1) Otto Brenner Stiftung, Arbeitspapier 78 (Grittmann, Brink, Kann, 30 Apr 2025), full PDF read: 2,217 articles (p. 20) from Sueddeutsche Zeitung, Der Spiegel, Die Zeit, FAZ, Die Welt, Focus, tagesschau.de, Frankfurter Rundschau and taz, 1 Dec 2022 to 30 Nov 2023; outlets were chosen by reach, trust and relevance (Mainz long-term media trust study); Bild is not among them. Findings: coverage strongly economic (product launches, personnel, corporate decisions); AI companies and their mostly male representatives most visible, scientific, political and civil-society actors clearly rarer; on average about one in four articles also addresses social consequences, taz almost 45% (p. 2); social consequences treated superficially; AI presented as inevitable, business decisions rarely questioned. "
 "(2) CAIS Factsheet 7 (Oct 2022): topic modelling of 4,968 articles from 37 media organisations (56% of print readership, 37% of online audience), 2018-21; economic perspective dominates; supra-regional papers (FAZ, SZ) most diverse; regional press economy-focused; trade media (Heise, PC Welt, Chip) product-focused; largest sources by volume Heise 13.5%, FAZ 7.6%, Stuttgarter Zeitung 7.0%. "
 "(3) Leidecker-Sandmann, Lueders, Moser, Boger and Lehmkuhl, Journal of Science Communication 2025: 589 illustrated articles (818 images) from SZ, FAZ, Welt, taz, Spiegel and Zeit, 2019 (125 articles) and Nov 2022 to Oct 2023 (464); human figures 44-45% of images; robot images 16% to 7%; five multimodal frames in 2019, seven in 2022/23, chances frame most prevalent. "
 "(4) Koestler and Ossewaarde, AI & Society (online 2021): frames in German federal-government documents and four German newspapers, read via the University of Twente abstract; the government uses its AI vision to uphold the status quo, media largely adopt it, some outlets partly challenge it. "
 "(5) Lammar, Horst and Mueller, Digital Journalism vol. 14 no. 2 (2025): qualitative discourse analysis of four years of German newspaper coverage, read via the Aarhus University abstract because the publisher page was blocked. "
 "(6) Zai, Rohrbach and Haenggli Fricker, Frontiers in Communication (Jun 2025): 1,588 articles from eight outlets in four countries including Sueddeutsche Zeitung and Bild, Nov 2020 to Nov 2022; progress frame 35.5% (manual coding), journalists 62.6% of voices; the authors state that they did not aim to compare outlets; data end before ChatGPT. "
 "Not covered by any of these: BBC, The Times, The Economist, generative-AI-era coverage after 2023, and tone by outlet. A Heidelberg publication 'Framing KI' appeared in search but its page was blocked, so it is not used.")
body=head('Media','German media treat AI mostly as a business story')
body+='<div style="display:flex;flex-direction:column;gap:10px">'+''.join(rw(*r) for r in rows)+'</div>'
body+=f'<p style="font-size:24px;line-height:1.3;color:{MUTED}">Studies pool outlets; none compares tone by outlet. Two were read from abstracts only.</p>'
s=(f'<section id="media-de" data-transition="fade" style="background:{PAPER};color:{INK};font-family:{SANS};padding:128px 128px 160px;display:flex;flex-direction:column;gap:32px">\n{body}\n'
   +foot('Sources: OBS 2025; CAIS 2022; JCOM 2025; AI & Society; Digital Journalism; Frontiers 2025.','28')+f'<aside>{e(notes)}</aside>\n</section>\n')
open(D+'slides/media-de.html','w').write(s)

# src9
def si(label,url,shown,extra=''):
    return f'<p style="font-size:24px;line-height:1.3;color:{INK}"><b>{e(label)}</b><br><a href="{url}">{e(shown)}</a>{e(extra)}</p>'
items=[
 ('Otto Brenner Stiftung (30 Apr 2025): Arbeitspapier 78, full text','https://www.otto-brenner-stiftung.de/fileadmin/user_data/stiftung/02_Wissenschaftsportal/03_Publikationen/AP78_KI_soz_Gerechtigkeit_WEB.pdf','otto-brenner-stiftung.de/fileadmin/…/AP78_KI_soz_Gerechtigkeit_WEB.pdf'),
 ('Leidecker-Sandmann et al., JCOM (2025): AI images in German print media','https://jcom.sissa.it/article/pubid/JCOM_2402_2025_A09/','jcom.sissa.it/article/pubid/JCOM_2402_2025_A09/'),
 ('Koestler and Ossewaarde, AI & Society: AI futures frames (abstract via Univ. Twente)','https://link.springer.com/article/10.1007/s00146-021-01161-9','link.springer.com/article/10.1007/s00146-021-01161-9'),
 ('Lammar, Horst and Mueller, Digital Journalism (2025) (abstract via Aarhus Univ.)','https://www.tandfonline.com/doi/full/10.1080/21670811.2025.2493759','tandfonline.com/doi/full/10.1080/21670811.2025.2493759'),
]
body=head('Sources','Sources (addendum): German media studies')+'<div style="display:flex;flex-direction:column;gap:16px">'+''.join(si(*i) for i in items)+'</div>'
s=(f'<section id="src9" data-transition="fade" style="background:{PAPER2};color:{INK};font-family:{SANS};padding:128px 128px 160px;display:flex;flex-direction:column;gap:32px">\n{body}\n'
   +foot('Accessed September 2026. Two publisher pages were blocked; those studies were read via university abstracts.','45')
   +'<aside>Sources for the German media studies slide. The Otto Brenner Stiftung PDF and the JCOM page were read in full or in summary; the Springer and Taylor and Francis pages were rate-limited or blocked, so those two studies rest on abstracts hosted by universities. OBS, CAIS, Zai et al. and Ittefaq et al. are also listed on the previous source slides.</aside>\n</section>\n')
open(D+'slides/src9.html','w').write(s)

# media (S27)
p=D+'slides/media.html'; t=open(p).read()
a='framing dominates German press (Otto Brenner Stiftung 2025: 2,000+ articles, 9 outlets; CAIS 2018–21: 4,968 articles).'
assert t.count(a)==1
t=t.replace(a,'framing dominates German press: 2,217 articles, 9 outlets (OBS 2025); 4,968 articles (CAIS 2018–21). Details next slide.')
a='more than 2,000 articles from nine German outlets'
assert t.count(a)==1; t=t.replace(a,'2,217 articles from nine German outlets')
a='about a quarter address social consequences; the presence of AI companies and their mostly male representatives is striking.'
assert t.count(a)==1; t=t.replace(a,'about a quarter address social consequences (taz almost 45%); the presence of AI companies and their mostly male representatives is striking. German studies are detailed on the next slide.')
t=t.replace('Sources: Reuters Institute; Otto Brenner Stiftung; CAIS; Zai et al.; Roe and Perkins; Ittefaq et al.','Sources: Reuters Institute; OBS; CAIS; Zai et al.; Roe and Perkins; Ittefaq et al.')
open(p,'w').write(t)

# media2 (S28)
p=D+'slides/media2.html'; t=open(p).read()
a='<b>Not found:</b> any study of how Bild, Zeit, Spiegel, the BBC, The Times or The Economist portray AI or its leaders, or linking deals to tone. Ties are context, not proof of bias.'
assert t.count(a)==1
t=t.replace(a,'<b>Not found:</b> any outlet-by-outlet study of how Bild, Zeit, Spiegel, the BBC, The Times or The Economist portray AI or its leaders, or of a link between deals and tone. German studies (previous slide) pool outlets. Ties are context, not proof of bias.')
a='Publishers have ties to AI firms; outlets are thinly studied'
assert t.count(a)==1; t=t.replace(a,'Publishers have ties to AI firms; tone by outlet is little studied')
a='(see previous slide)'; assert t.count(a)==1; t=t.replace(a,'(see slide 26)')
a='Blocked to us: economist.com'; assert t.count(a)==1
t=t.replace(a,'Studies of German coverage are on the previous slide; they pool outlets and none compares tone by outlet or portrayal of individual leaders. Blocked to us: economist.com')
open(p,'w').write(t)

# deck order + renumber
dp=D+'deck.json'; dj=json.load(open(dp)); o=dj['order']
if 'media-de' not in o: o.insert(o.index('media')+1,'media-de')
if 'src9' not in o: o.append('src9')
json.dump(dj,open(dp,'w'),indent=1,ensure_ascii=False)
pat=re.compile(r'(right:\s*128px[^>]*>)(\d+)(</p>)')
for i,sid in enumerate(o,1):
    if sid=='cover': continue
    f=D+'slides/'+sid+'.html'; t=open(f).read()
    m=pat.findall(t); assert len(m)==1,(sid,m)
    t=pat.sub(lambda mm: mm.group(1)+str(i)+mm.group(3),t)
    open(f,'w').write(t)
print(len(o),o[24:31])
