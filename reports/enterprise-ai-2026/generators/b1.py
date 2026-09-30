from lib import *
def case(title,sub,lines,pilltxt,pillbg):
    return card([h3(title),p(sub,24,MUTED)]+[p(l,26) for l in lines]+[pill(pilltxt,pillbg)],gap=10,pad=28)
body=grid([
 case('Klarna · fintech, Sweden','Customer service AI assistant',[
  '<b>Feb 2024:</b> said its assistant did the work of 700 agents.',
  '<b>May 2025:</b> CEO: AI was cheaper but “lower quality”; hiring humans again.']
  ,'Partly reversed',AMBER_L),
 case('Commonwealth Bank · Australia','Voice bot in the call centre',[
  '<b>Jul 2025:</b> announced 45 call-centre job cuts.',
  '<b>21 Aug 2025:</b> reversed and apologised; the union reported rising call volumes.']
  ,'Reversed within weeks',AMBER_L),
 case('McDonald’s with IBM · USA','Voice ordering at drive-throughs',[
  'About 100 restaurants, pilot since 2021.',
  '<b>Jun 2024:</b> ended after viral videos of wrong orders.']
  ,'Pilot ended',AMBER_L),
 case('Air Canada · airline, Canada','Website chatbot gave wrong refund advice',[
  '<b>19 Feb 2024:</b> a tribunal held the airline liable for what its bot said.',
  '“Responsible for all the information on its website.”']
  ,'Legal precedent',TEAL_L),
])
slide('cases','Case studies','Four public reversals: the cost was in quality and liability',body,
 'Sources: Entrepreneur/Bloomberg (May 2025); ABC News (21 Aug 2025); Al Jazeera (19 Jun 2024); BC CRT 2024 BCCRT 149.','9a',
 'Four documented cases where an AI deployment was pulled back or held the company liable. Klarna: in Feb 2024 it said its assistant did the work of 700 customer-service agents and handled 75% of chats in its first month; in May 2025 CEO Sebastian Siemiatkowski told Bloomberg that AI was cheaper but produced lower quality and that Klarna would hire humans for support again (headcount had fallen 22% to about 3,500 during a hiring freeze). Savings figures of about $40 million appear only in secondary blogs and are not used here. Commonwealth Bank of Australia: announced 45 call-centre redundancies in July 2025 after a voice bot; on 21 Aug 2025 it reversed and apologised; the Finance Sector Union said call volumes were rising and managers were on the phones; the union raised a dispute at the Fair Work Commission. McDonald\'s: voice-ordering pilot with IBM in about 100 outlets ended in June 2024; McDonald\'s gave no formal reason, the ending followed viral videos of order errors. Air Canada: Moffatt v Air Canada, British Columbia Civil Resolution Tribunal, 19 Feb 2024 (2024 BCCRT 149): the chatbot told a customer he could claim a bereavement fare retroactively, contradicting the airline\'s own page; the tribunal rejected the argument that the bot was a separate entity. The exact amount awarded was not verified here. Four cases are a sample of well-publicised reversals, not a failure rate; nobody counts the quiet successes and failures.',
 bg=PAPER2)

# cases-ok
def metric(big,txt):
    return row([fixed([f'<p style="font-family:{SERIF};font-size:44px;line-height:1.1;font-weight:600;color:{TEAL}">{e(big)}</p>'],300,justify='center'),
                f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center">{p(txt,28)}</div>'])
left=card([h3('German insurers, company-reported'),p('Bitkom white paper “Beyond the Pilot”, Mar 2026',24,MUTED),
  metric('6–8 wk → 10 min','DOMCURA: claims up to €3,500, fully automatic.'),
  metric('−7% claims cost','inca Solutions: agentic AI, 24-hour settlement.'),
  metric('3 days → 180 s','MRH Trowe: mail intake, €0.14 per letter.'),
  ],gap=14,pad=28)
right=card([h3('UK government trial, self-reported'),p('20,000 civil servants, 12 organisations, Sep–Dec 2024',24,MUTED),
  metric('26 min / day','Average time saved, as reported by users.'),
  metric('82%','say they would not go back to working without the assistant.'),
  metric('17%','reported no noticeable time saving.'),
  ],gap=14,pad=28)
slide('cases-ok','Case studies','Where it worked: narrow tasks, self-reported gains',
 row([left.replace('flex:1;','flex:1.15;',1),right]),
 'Sources: Bitkom (Mar 2026); UK Government written statement HCWS669 (2 Jun 2025). Company- and self-reported figures.','9b',
 'Documented successes. German insurers (Bitkom white paper Beyond the Pilot, March 2026) report: DOMCURA cut processing of complete claims from 6-8 weeks to 10 minutes, with claims up to 3,500 euros handled fully automatically and 12 unfilled positions not refilled; inca Solutions, using agentic AI in motor claims, reports a 7% reduction in claims costs and settlement within 24 hours; MRH Trowe cut mail intake from 3 days to 180 seconds at 0.14 euros per letter (target 0.25) with about 95% extraction accuracy and about half of documents fully automated; ERGO GPT grew from 3,000 to 9,000 users between April and December 2024, with more than 3 million prompts. All numbers are company-reported in a trade-association paper, not audited. The Allianz example in the same paper puts change management at roughly 50% of total implementation effort. UK cross-government Microsoft 365 Copilot experiment (September to December 2024, 20,000 civil servants in 12 organisations, written statement of 2 June 2025): average 26 minutes saved a day, self-reported; 82% would not want to go back; 17% noticed no time saving; the professions saving least reported lowest satisfaction. The tool is from the vendor that supplied it; time saved is not the same as money saved or output gained. The DWP later reported 19 minutes a day (The Register, 4 Feb 2026); not verified in the primary report.',
 bg=PAPER)
print('b1 ok')
