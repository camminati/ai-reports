from lib import *
def tie(a,b,c):
    return row([fixed([p(a,24,INK,'font-weight:600;')],400,pad=12),
      f'<div style="width:190px;flex:none;display:flex;flex-direction:column;justify-content:center">{p(b,24,MUTED)}</div>',
      f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center">{p(c,24)}</div>'])
ties=card([h3('Documented ties to AI firms'),
  tie('Axel Springer (Bild, Welt)','Dec 2023','With OpenAI; “tens of millions” of euros a year (press).'),
  tie('News Corp (WSJ, The Times)','May 2024','With OpenAI; over $250m (WSJ).'),
  tie('FT; The Guardian','2024; 2025','With OpenAI; terms not disclosed.'),
  tie('New York Times','2025','With Amazon, $20–25m a year. Suing OpenAI since Dec 2023.')],gap=10,pad=26)
st=card([h3('Stances we could source'),
  p('<b>Handelsblatt</b>, Aug 2026: do not believe every word of Altman, Musk or Amodei; they have financial incentives.',24),
  p('<b>TIME</b>, Dec 2025: “The Architects of AI”, Person of the Year, for “wowing and worrying humanity”.',24),
  p('<b>Fortune</b>, 2026: leaders “walking back” jobs claims; CEO manifestos a “closed loop of founders, investors and reporters”.',24),
  ],gap=10,pad=26)
callout=card([p('<b>Not found:</b> any study of how Bild, Zeit, Spiegel, the BBC, The Times or The Economist portray AI or its leaders, or linking deals to tone. Ties are context, not proof of bias.',26)],bg=AMBER_L,border=AMBER_L,pad=24,gap=4,flex='none')
slide('media2','Media','Publishers have ties to AI firms; outlets are thinly studied',
 stack([row([ties.replace('flex:1;','flex:1.35;',1),st]),callout],gap=20),
 'Sources: OpenAI announcements; Nieman Lab; GeekWire (30 Jul 2025); NPR; Handelsblatt; TIME; Fortune; EBU/BBC (21 Oct 2025).','D',
 'Publisher licensing and litigation, with verification status. Axel Springer and OpenAI (13 Dec 2023): terms confirmed by OpenAI (summaries including otherwise paid content, attribution, links, training use); "tens of millions of euros per year" is press-reported only (Bloomberg, FT via The Decoder). Financial Times and OpenAI, 29 Apr 2024, terms not disclosed. News Corp and OpenAI, 22 May 2024: over 250 million dollars, per WSJ reporting via Nieman Lab; the multi-year length was not verified. Guardian Media Group and OpenAI, 14 Feb 2025, terms not disclosed. New York Times and Amazon: announced May 2025, at least 20 million dollars a year (up to about 25 million), nearly 1% of NYT 2024 revenue (WSJ via GeekWire, 30 Jul 2025). NYT sued OpenAI and Microsoft on 27 Dec 2023 claiming billions in damages (NPR); Axios reported on 8 Sep 2026 that summary-judgment motions were argued and a ruling was pending (exact date low confidence). Stances: Handelsblatt interview with Altman (14 Aug 2026) and commentary by Thomas Jahn (18 Aug 2026), "Wir sollten Sam Altman und Elon Musk nicht jedes Wort glauben"; TIME named "The Architects of AI" Person of the Year on 11 Dec 2025 (Zuckerberg, Su, Musk, Huang, Altman, Hassabis, Amodei, Li) citing job displacement, harm to users and bubble risks alongside the praise; interpretation: celebratory with caution. Fortune 26 May 2026 and 13 Aug 2026 (see previous slide). Books: Keach Hagey, The Optimist, and Karen Hao, Empire of AI (2025), are sceptical portraits of Altman (via a Transformer review). BBC and EBU News Integrity in AI Assistants (21 Oct 2025): 22 public-service media organisations, 18 countries, more than 3,000 responses, almost half had at least one significant issue, a third serious sourcing problems, a fifth major accuracy issues; this is media auditing AI, not covering it. Bild: Springer memo of June 2023, about 200 of 1,000 Bild staff affected, Doepfner: AI could make independent journalism "better than it ever was, or simply replace it"; the deal came six months later, timeline only. Blocked to us: economist.com, theguardian.com, and some academic publishers, so The Economist and Guardian stances are not assessed.',
 bg=PAPER2)

# patterns rewrite
def prow(iff,then,ev,evbg,evtxt):
    return row([fixed([p(iff,28,INK,'font-weight:600;')],520,pad=12,justify='center'),
      f'<div style="flex:1;background:{CARD};border:1px solid {LINE};border-radius:16px;padding:12px 24px;display:flex;flex-direction:column;justify-content:center">{p(then,24)}</div>',
      f'<div style="width:400px;flex:none;background:{evbg};border-radius:16px;padding:12px 24px;display:flex;flex-direction:column;justify-content:center;gap:2px"><p style="font-size:28px;line-height:1.3;color:{INK};font-weight:600">{e(ev)}</p><p style="font-size:24px;line-height:1.3;color:{INK}">{e(evtxt)}</p></div>'])
hdr=row([f'<p style="width:520px;flex:none;font-size:24px;font-weight:600;color:{MUTED};letter-spacing:1px;text-transform:uppercase">If</p>',
         f'<p style="flex:1;font-size:24px;font-weight:600;color:{MUTED};letter-spacing:1px;text-transform:uppercase">Then, in the sources</p>',
         f'<p style="width:400px;flex:none;font-size:24px;font-weight:600;color:{MUTED};letter-spacing:1px;text-transform:uppercase">Evidence strength</p>'])
rows=[hdr,
 prow('AI is added to old tasks; the workflow stays','Broad use, rare profit: 44% scaling, 39% any EBIT impact, ≈6% significant (McKinsey 2026)',
      'Strong',TEAL_L,'Large surveys agree; self-reported'),
 prow('People are cut before quality is proven','Reversed or paid for: Klarna, Commonwealth Bank, McDonald’s',
      'Medium',AMBER_L,'Public cases; no rate exists'),
 prow('A bot speaks for the company','The company answers for it: Air Canada held liable (2024)',
      'Medium',AMBER_L,'One ruling; clear principle'),
 prow('One vendor holds the data, models and licences','Price and exit risk come later: 59% cite lock-in; VMware +800–1,500%',
      'Medium',AMBER_L,'Survey plus an interested party'),
 prow('A narrow, measured task with a clean process','Documented gains: claims in 10 minutes; change work ≈50% of effort',
      'Weak',PAPER2,'Company-reported, selected cases'),
]
slide('patterns','Patterns','Five patterns link choices to outcomes',stack(rows,gap=12),
 'Sources: McKinsey (2026); BCG (2025); company statements and press; BC CRT (2024); Bitkom (2026); CISPE via Network World.','17',
 'This slide replaces an earlier version that leaned on Gartner forecasts. Evidence strength is our own assessment of how well each link is supported by the public sources reviewed, not a published rating. Strong: McKinsey State of AI 2026 (n = 1,719) reports 44% scaling, 39% any enterprise EBIT impact and about 6% high performers; BCG (n = 1,250) shows a similar shape. Medium: Klarna (CEO to Bloomberg, May 2025: lower quality), Commonwealth Bank (21 Aug 2025 reversal) and McDonald\'s (Jun 2024) are public reversals but there is no count of how often this happens; Moffatt v Air Canada (19 Feb 2024) is one tribunal ruling with a general principle; lock-in: Bitkom Cloud Report 2026 (59% cite lock-in) and the CISPE-affiliated observatory on VMware (800-1,500% price increases reported by European customers), an interested party. Weak: the insurer results are company-reported in a Bitkom white paper and cases were selected for showing success. Gartner-based patterns (cost multiplication, data readiness) remain on the trend-indicator slides. All patterns are associations, none is a controlled test.',
 bg=PAPER)
print('b7 ok')
