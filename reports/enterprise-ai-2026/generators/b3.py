from lib import *
def exitc(t,sub,lines,pt,pb):
    return card([h3(t),p(sub,24,MUTED)]+[p(l,24) for l in lines]+[pill(pt,pb)],pad=24,gap=8)
body=grid([
 exitc('Schleswig-Holstein','Office software to open source',[
  'About <b>80%</b> of workplaces on LibreOffice; 20% stay on Microsoft for specialist apps.',
  '<b>€15m</b> a year saved from 2026; <b>€9m</b> one-off in 2026.'],'Savings state-reported',TEAL_L),
 exitc('International Criminal Court','Microsoft 365 to openDesk',[
  'Trigger: chief prosecutor reportedly locked out of his Microsoft account (May 2025, US sanctions).',
  'About <b>1,800</b> workstations; no cost published.'],'Cost unknown',AMBER_L),
 exitc('EU Data Act · law','Switching charges end 12 Jan 2027',[
  'Switching charges, including egress fees, become prohibited.',
  'Still allowed: subscription and early-termination fees; ongoing multi-cloud transfer.'],'Cuts the toll, not the effort',TEAL_L),
 exitc('German federal government','Sovereign AI cloud',[
  '<b>≈€250m</b> awarded 21 May 2026: T-Systems-led consortium first, SVA-led second.',
  'Open standards and open-source parts.'],'Announced, not yet proven',AMBER_L),
])
slide('exit','Dependency · Exit','Exits exist; the price is money, effort and leftovers',body,
 'Sources: Schleswig-Holstein via It’s FOSS (2025); Open Source For You (7 Nov 2025); Kemp IT Law; BMDS press release (21 May 2026).','9e',
 'Exit routes. Schleswig-Holstein: the state digital minister Dirk Schrödter reported that almost 80% of state government workplaces (excluding tax administration) had moved to LibreOffice, with 15 million euros a year in licence savings from 2026 and a one-off 9 million euros allocated for 2026; 20% remain on Microsoft because of technical dependencies in specialised applications. Source: secondary report (It\'s FOSS); the heise report on the same figures was not accessible to us. ICC: reported in October and November 2025 as moving about 1,800 workstations to openDesk (Collabora, Open-Xchange, Nextcloud) delivered by ZenDiS, a German state-owned organisation; the reported trigger is the temporary lock-out of Chief Prosecutor Karim Khan from his Microsoft account in May 2025 after US sanctions on ICC officials; The Register piece was not accessible, so this rests on Open Source For You and other secondary coverage; No cost or completion date was published. EU Data Act: from 12 January 2027 all switching charges, including egress fees, are prohibited; permitted are subscription fees, proportionate early-termination fees, pre-agreed support and charges for services outside switching; multi-cloud continuous data egress is not covered by the ban (Kemp IT Law summary). German federal government: the Federal Ministry for Digital and State Modernisation announced on 21 May 2026 a contract worth about 250 million euros for a sovereign AI cloud platform for federal, state and local administration; first place T-Systems-led consortium, second SVA-led. Announced does not mean delivered.',
 bg=PAPER)

# gov
def kv(big,txt,color=TEAL,w=250):
    return row([fixed([f'<p style="font-family:{SERIF};font-size:42px;line-height:1.1;font-weight:600;color:{color}">{e(big)}</p>'],w,justify='center'),
      f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center">{p(txt,26)}</div>'])
L=card([h3('Use is nearly universal'),p('OECD Digital Government Outlook 2026, 36 member countries',24,MUTED),
  kv('35 of 36','use AI in at least one government function.'),
  kv('64%','use generative AI, mostly for staff productivity (56%) and automated reporting (42%).'),
  kv('27 of 36','use it in public services; 13 in policymaking.')],gap=14,pad=28)
R=card([h3('Guardrails and proof lag behind'),p('Same OECD report',24,MUTED),
  kv('14 of 36','require a risk assessment before deployment.',AMBER),
  kv('11 of 36','audit after deployment; only 6 keep an open algorithm register.',AMBER),
  kv('10 of 36','measure the financial or other impact of AI at all.',AMBER)],gap=14,pad=28)
slide('gov','Government','Governments adopt widely but rarely measure what it delivers',row([L,R]),
 'Source: OECD, Digital Government Outlook 2026, chapter on adopting and governing AI in government.','9f',
 'OECD Digital Government Outlook 2026 (36 member countries, 2025 data): 35 of 36 use AI in at least one government function; by function: internal processes 31, public services 27, policymaking 13, oversight 12; 64% use generative AI for at least one purpose, most often staff productivity (56%) and automated reporting (42%); all but three members have AI-in-government strategies. Guardrails: 14 of 36 require pre-deployment risk assessments, 12 have internal review committees, 11 do post-deployment audits, 11 have formal transparency standards, 6 maintain open algorithm registers; only 10 of 36 measure financial or non-financial impact, although half base adoption decisions on efficiency projections. Only 13 of 36 deploy their own accelerators (GPUs). A second index, the Public Sector AI Adoption Index 2026 from the Center for Data Innovation (survey of 3,335 public servants in ten countries including Germany, sponsored by Google), was consulted but not used for numbers because it is sponsor-funded.',
 bg=PAPER2)
print('b3 ok')
