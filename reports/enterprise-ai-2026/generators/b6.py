from lib import *
# lead2
ctx=card([h3('Documented context'),
  p('<b>3 Mar 2025:</b> Anthropic raises $3.5bn at $61.5bn. <b>10 Mar:</b> Amodei’s “90% of code” talk.',26),
  p('<b>22 May 2025:</b> Claude 4 launches. <b>28 May:</b> Amodei’s jobs warning; motive stated: “a duty and obligation to be honest”.',26),
  p('<b>Aug 2025:</b> Altman says investors are “overexcited” while OpenAI raises at $300bn.',26),
  p('<b>28 Oct 2025:</b> research-intern goal set the day OpenAI completed its for-profit recapitalisation.',26)],gap=12,pad=28)
crit=card([h3('Critics and walk-backs'),
  p('White House AI adviser Sacks, Oct 2025: Anthropic runs “a sophisticated regulatory capture strategy based on fear-mongering”. Amodei replied publicly.',26),
  p('Kristian Kersting (TU Darmstadt), Mar 2025: AGI claims can serve as marketing tied to investment.',26),
  p('Fortune, May 2026: Altman “delighted to be wrong” on jobs; Amodei: if 90% of a job is automated, people do the other 10%.',26),
  p('Karpathy, Oct 2025: “a decade of agents”, not a year.',26)],gap=12,pad=28)
meas=card([p('<b>Measured, not predicted:</b> METR’s Jul 2025 trial found experienced developers 19% slower with AI tools, while expecting to be 24% faster (16 developers, 246 tasks; a snapshot of early-2025 tools). METR’s Feb 2026 follow-up called its new data an “unreliable signal”.',26)],bg=PAPER2,border=LINE,pad=24,gap=4,flex='none')
inter=card([p('<b>Our reading (interpretation):</b> timing beside a fundraising round or launch does not prove motive, and no source states these forecasts were made to raise money. But every forecaster here sells or invests in the technology, so treat their timelines as claims to test.',26)],bg=AMBER_L,border=AMBER_L,pad=24,gap=4,flex='none')
slide('lead2','AI leaders’ forecasts','Why leaders say what they say: context, critics, and a measurement',
 stack([row([ctx,crit]),row([meas,inter])],gap=20),
 'Sources: Anthropic (Mar, May 2025); Axios; TechCrunch (21 Oct 2025); Fortune (19 Aug 2025; 26 May 2026); METR (Jul 2025, Feb 2026).','B',
 'Context evidence. Anthropic announced a 3.5 billion dollar Series E at 61.5 billion dollars post-money on 3 Mar 2025, a week before Amodei spoke at the Council on Foreign Relations (10 Mar 2025). Claude 4 launched on 22 May 2025; Axios published Amodei\'s jobs warning on 28 May 2025, quoting him: "We, as the producers of this technology, have a duty and an obligation to be honest about what is coming", speaking in hopes of jarring government and companies into preparing. Whether the timing was deliberate is not documented. David Sacks, Oct 2025: "Anthropic is running a sophisticated regulatory capture strategy based on fear-mongering"; Amodei replied on 21 Oct 2025 (TechCrunch). Fortune, 19 Aug 2025: OpenAI had raised 8.3 billion dollars at 300 billion; Altman said "Are we in a phase where investors as a whole are overexcited about AI? My opinion is yes." Altman\'s research-intern goal was posted on 29 Oct 2025 after the 28 Oct livestream, the day OpenAI completed its for-profit recapitalisation (TechCrunch); any link is interpretation. Fortune 26 May 2026 reports Altman ("I\'m delighted to be wrong about this") and Amodei ("If you automate 90% of the job, then everyone does the 10% of the job") softening job predictions. Kersting: Fortune 28 Mar 2025 on an AAAI survey in which more than three quarters of respondents said scaling current approaches is unlikely to yield AGI. METR RCT (10 Jul 2025): 16 experienced open-source developers, 246 tasks, 19% longer with AI, expected 24% speed-up and believed afterwards 20%; METR warns it is a snapshot; METR update 24 Feb 2026: -18% and -4% estimates called an unreliable signal because developers refused to work without AI. METR also reports the length of tasks models can do doubling about every 7 months (2019-2025).',
 bg=PAPER2)

# media
def stat(big,txt,color=TEAL):
    return row([fixed([f'<p style="font-family:{SERIF};font-size:40px;line-height:1.1;font-weight:600;color:{color}">{e(big)}</p>'],190,justify='center',pad=14),
      f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center">{p(txt,24)}</div>'])
c1=card([h3('Who is quoted'),
  stat('33%','of unique sources in UK AI news came from industry: about 2× academia, 6× government (760 articles, 6 outlets, 2018).'),
  stat('56.6%','of UK news mentions of top AI scholars went to industry-affiliated ones, who are 16% of the sample (US: 71.9%).')],gap=12,pad=26)
c2=card([h3('How it is framed'),
  stat('≈60%','of UK articles were tied to industry products or announcements (2018).'),
  stat('Economic','framing dominates German press (OBS 2025: 2,217 articles, 9 outlets; CAIS 2018–21: 4,968 articles).'),
  stat('79.4%','of positions inside the “progress” frame were pro-AI; ethics was the least-used frame (Zai 2025).')],gap=12,pad=26)
c3=card([h3('Tone is mixed, not one-sided'),
  stat('37%','of UK headlines on ChatGPT and AI (Jan–May 2023) were “impending danger”; 11% highlighted positives.',AMBER),
  stat('21% / 13%','of headlines in 12 countries’ newspapers, 2010–23, were negative / positive; 66% neutral.',AMBER)],gap=12,pad=26)
slide('media','Media','Studies find coverage that is business-framed and industry-sourced',
 grid([c1,c2,c3],cols=3),
 'Sources: Brennen et al., Reuters Institute (2018, 2019); Otto Brenner Stiftung (2025); CAIS (2022); Zai et al. (2025); Roe and Perkins (2023); Ittefaq et al. (2025).','C',
 'Systematic content analyses of news about AI. Brennen, Howard and Nielsen (Reuters Institute, 13 Dec 2018): 760 articles from six UK outlets (Telegraph, MailOnline, Guardian, HuffPost, BBC, Wired UK), Jan-Aug 2018; nearly 60% of articles indexed to industry products, initiatives or announcements; 33% of unique sources affiliated with industry, almost twice academia and six times government. Brennen, Schulz, Howard and Nielsen (17 Dec 2019): industry-affiliated scholars are 16% of the sample but 56.6% of UK and 71.9% of US news mentions, while their share of citations is only 15% and 19.3%. Otto Brenner Stiftung working paper 78 (Grittmann et al., 30 Apr 2025): 2,217 articles from nine German outlets (SZ, Spiegel, Zeit, FAZ, Welt, Focus, FR, taz, tagesschau.de), Dec 2022 to Nov 2023, coverage strongly shaped by economic perspectives; about a quarter address social consequences; the presence of AI companies and their mostly male representatives is striking. CAIS Factsheet 7 (Oct 2022): 4,968 German articles 2018-21, clear dominance of economic framing. Zai, Rohrbach and Haenggli Fricker (Frontiers in Communication, 30 Jun 2025): 1,588 articles from WSJ, NY Post, Guardian, The Sun, Sueddeutsche, BILD, Tages-Anzeiger and Blick, Nov 2020 to Nov 2022; progress frame 35.5% of frames, 79.4% of positions within it pro-AI; the authors state they did not aim to compare outlets. Counterweights: Roe and Perkins (Nature HSSC, Oct 2023), 671 UK headlines Jan-May 2023, impending danger 37%, positive capabilities 11%; Ittefaq et al. (Telematics and Informatics, Jan 2025), 38,787 articles from 12 newspapers 2010-2023, top frame business/economy/jobs (37.4%), headlines 21.04% negative, 13.33% positive, 65.63% neutral. Periods and countries differ; generative-AI-era coverage (2024-26) has little rigorous study so far. Most numbers were read from abstracts or summaries.',
 bg=PAPER)
print('b6 ok')
