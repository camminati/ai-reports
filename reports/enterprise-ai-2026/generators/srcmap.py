import re,html,json
D='/path/to/scratchpad/artifact-files/<artifact-id>/project/'
order=json.load(open(D+'deck.json'))['order']
def tx(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s)))
ents=[]
BK='/path/to/scratchpad/project_bak_src/'
for n in ['src1','src2','src3','src4','src5','src6','src7','src8','src9']:
    t=open(BK+'slides/'+n+'.html').read()
    body=re.sub(r'<aside>.*?</aside>','',t,flags=re.S)
    for p in re.findall(r'<p style="font-size:24px;line-height:1\.3;color:#12202F">(.*?)</p>',body,re.S):
        lab=html.unescape(re.search(r'<b>(.*?)</b>',p,re.S).group(1)); a=re.search(r'<a href="(.*?)">(.*?)</a>',p,re.S)
        ents.append(dict(label=lab,url=html.unescape(a.group(1)),shown=html.unescape(a.group(2)),src=n))
ents.append(dict(label='NPR (27 Dec 2023): New York Times sues OpenAI and Microsoft',url='https://www.npr.org/2023/12/27/1221821750/new-york-times-sues-chatgpt-openai-microsoft-for-copyright-infringement',shown='npr.org/2023/12/27/1221821750/new-york-times-sues-chatgpt-o…',src='x'))
ents.append(dict(label='Axios (8 Sep 2026): NYT v. OpenAI, summary-judgment arguments',url='https://www.axios.com/2026/09/08/nyt-openai-microsoft-copyright-lawsuit',shown='axios.com/2026/09/08/nyt-openai-microsoft-copyright-lawsuit',src='x'))
srcset=set(o for o in order if o.startswith('src'))
vis={};note={}
for i,sid in enumerate(order,1):
    if sid in srcset or sid=='cover': continue
    t=open(D+'slides/'+sid+'.html').read()
    a=re.search(r'<aside>(.*?)</aside>',t,re.S)
    vis[i]=tx(re.sub(r'<aside>.*?</aside>','',t,flags=re.S)); note[i]=tx(a.group(1)) if a else ''
K={ # regex per entry index (0-based in ents order)
0:r'agentic AI projects (?:canceled|cancelled)|Gartner,? \(?Jun 2025',
1:r'Jul 2024',
2:r'Gartner \(?(?:26 )?Jan 2026|Gartner, Jan 2026',
3:r'Feb 2025',
4:r'Gartner,? \(?May 2026|Gartner \(May 2026',
5:r'Gartner,? \(?(?:17 )?Aug 2026|17 Aug 2026|Gartner \(2025, 2026\)',
6:r'Hype Cycle',
7:r'McKinsey',
8:r'BCG',
9:r'S&P Global',
10:r'Deloitte',
11:r'KPMG',
12:r'FEDS Note|Fed FEDS|Federal Reserve',
13:r'Eurostat',
14:r'Digital Decade',
15:r'Commission.{0,30}agentic|European Commission agentic',
16:r'Bitkom',
17:r'Bitkom.{0,15}Sep 2026',
18:r'Digitalisierung der Wirtschaft',
19:r'Baiosphere',
20:r'Hojdik',
21:r'Steinert|Leifer',
22:r'\bRAND\b',
23:r'AI Index 2026|NANDA',
24:r'Cloud Security Alliance',
25:r'Cloudera',
26:r'Dun and Bradstreet',
27:r'Stanford AI Index 2025|Stanford HAI|280-fold',
28:r'Klarna',
29:r'Commonwealth Bank',
30:r"McDonald",
31:r'Air Canada',
32:r'Beyond the Pilot|DOMCURA',
33:r'HCWS669|Copilot',
34:r'Cloud Report',
35:r'Synergy',
36:r'Bruegel',
37:r'Network World|VMware',
38:r'Schleswig',
39:r'openDesk|Criminal Court',
40:r'Data Act|switching charge',
41:r'sovereign AI cloud|BMDS',
42:r'OECD',
43:r'Diella',
44:r'OCCRP|AKSHI',
45:r'\bIon\b',
46:r'DeepSeek',
47:r'Garante|Italian|Italy',
48:r'Court of Rome',
49:r'Omnibus',
50:r'Omnibus',
51:r'IW Köln|IW-Report|\bIW\b',
52:r'Diella',
53:r'European Law Blog|one-stop',
54:r'Art\. 99|Article 99|€35m',
55:r'CFR',
56:r'Axios',
57:r'Fortune \(Jan 2026\)|70–90%',
58:r'Google \(Apr 2026\)|Google: 75%',
59:r'Stanford DEL|Stanford Digital Economy',
60:r'\bBLS\b',
61:r'NY Fed',
62:r'Reflections|Altman · OpenAI · Jan 2025',
63:r'Reworked',
64:r'Karpathy',
65:r'Zuckerberg',
66:r'TechCrunch',
67:r'OpenAI \(Sep 2026\)|research intern',
68:r'Sacks',
69:r'overexcited',
70:r'walking back|walk-backs',
71:r'METR',
72:r'Series E|\$3\.5bn',
73:r'Reuters Institute',
74:r'Reuters Institute',
75:r'Otto Brenner|\bOBS\b',
76:r'CAIS',
77:r'Zai',
78:r'Roe and Perkins',
79:r'Ittefaq',
80:r'Handelsblatt',
81:r'Person of the Year|Architects of AI',
82:r'EBU|BBC',
83:r'Axel Springer',
84:r'News Corp|Nieman',
85:r'Amazon',
86:r'Döpfner|Doepfner|Springer memo',
87:r'Decoder|tens of millions',
88:r'Otto Brenner|\bOBS\b',
89:r'Leidecker|JCOM',
90:r'Ossewaarde|AI & Society',
91:r'Lammar|Digital Journalism',
92:r'\(NPR\)',
93:r'Axios reported',
}
assert len(ents)==94,len(ents)
res=[]
for k,e in enumerate(ents):
    rx=re.compile(K[k])
    fv=next((i for i in sorted(vis) if rx.search(vis[i])),None)
    fn=next((i for i in sorted(note) if rx.search(note[i])),None)
    first=fv if fv else fn
    e['idx']=k; e['first']=first; e['where']='visible' if fv else ('notes' if fn else 'NONE')
    res.append(e)
if __name__=='__main__':
    for e in res:
        print(e['idx'],e['first'],e['where'],'|',e['label'][:70])
