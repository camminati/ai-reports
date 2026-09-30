from lib import *
def brow(lab,val,pct,color=TEAL,valc=TEAL):
    w=int(pct*4.2)
    return (f'<div style="display:flex;align-items:center;gap:20px"><p style="width:400px;flex:none;font-size:26px;line-height:1.25;color:{INK}">{e(lab)}</p>'
      f'<div style="width:420px;height:32px;background:#E4DDCB;border-radius:8px;display:flex;flex:none"><div style="width:{w}px;height:32px;background:{color};border-radius:8px"></div></div>'
      f'<p style="font-size:34px;font-weight:600;color:{valc}">{val}</p></div>')
left=card([h3('German companies, Bitkom Cloud Report 2026'),p('603 companies, 20+ employees, weeks 14–20 of 2026, ±3%',24,MUTED),
  brow('Use a US cloud provider','71%',71),
  brow('Would prefer a US provider','8%',8,BAR_AMBER,AMBER),
  brow('Say Germany is too dependent on US clouds','85%',85),
  brow('Would prefer German providers','91%',91),
  brow('Actually use German providers','53%',53,BAR_AMBER,AMBER),
  p('43% say there is no equivalent European alternative for their needs.',28)],gap=14,pad=28)
right=stack([
 card([h3('Market share, Europe'),p('<b>≈70%</b> of the European cloud market goes to Amazon, Microsoft and Google. European providers hold <b>≈15%</b>, down from 29% in 2017 (Synergy Research; market €61bn in 2024).',28)],pad=28,gap=8),
 card([h3('AI compute'),p('EU capacity in 2026: <b>5%</b> of global AI compute (2 GW), against <b>78%</b> for the US and <b>11%</b> for China; still 5.6% projected for 2031 (Bruegel policy brief, dataset Europe2031.ai).',28)],pad=28,gap=8),
],gap=24)
slide('dep','Dependency','Most German firms use US clouds, prefer not to, and see no substitute',
 row([left.replace('flex:1;','flex:1.45;',1),f'<div style="flex:1;display:flex;flex-direction:column">{right}</div>']),
 'Sources: Bitkom Cloud Report 2026 (17 Jun 2026); Synergy Research Group; Bruegel policy brief.','9c',
 'Bitkom Cloud Report 2026, published 17 June 2026: 603 companies with at least 20 employees, fieldwork weeks 14 to 20 of 2026, margin of error about 3 points. 71% use US cloud providers but only 8% would prefer them; 85% think Germany is too dependent on US providers (78% in 2025); 91% would prefer German providers (53% use them today), 68% EU providers (45% use them); 43% say there is no equivalent European alternative; 64% say current US policy forces them to reconsider their cloud strategy. Synergy Research Group: European providers held 29% of the European cloud market in 2017 and about 15% since 2022; Amazon, Microsoft and Google together about 70%; market of 61 billion euros in 2024 (Synergy figures). Bruegel policy brief on Europe\'s AI compute shortfall, citing the Europe2031.ai dataset: EU AI compute capacity 2 GW in 2026, 5% of the global total, against 35 GW (78%) for the US and 5 GW (11%) for China; the EU share would be 5.6% in 2031. The five planned EU AI gigafactories would supply about 4% of projected EU compute by 2031. These are survey opinions and market-research estimates; "prefer" is a stated preference, not a purchasing decision.',
 bg=PAPER)

def kv(big,txt,color=TEAL):
    return row([fixed([f'<p style="font-family:{SERIF};font-size:44px;line-height:1.1;font-weight:600;color:{color}">{e(big)}</p>'],280,justify='center'),
      f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center">{p(txt,28)}</div>'])
L=card([h3('Companies feel the lock-in'),p('Bitkom Cloud Report 2026',24,MUTED),
  kv('59%','name lock-in as the main barrier to switching cloud provider.',AMBER),
  kv('34%','have ever switched provider (26% once, 8% several times).'),
  kv('64%','saw cloud costs rise in 2025; 54% expect more in 2026; only 9% expect a fall.',AMBER),
  kv('42% → 69%','use cloud-based AI services today, versus expected in five years.')],gap=14,pad=28)
R=card([h3('A price shock in practice: VMware'),p('Prices after Broadcom took over VMware',24,MUTED),
  p('<b>800–1,500%</b> price increases reported by European customers (CISPE observatory report; AT&T in the US: 1,050%).',28),
  p('One cloud provider migrated away entirely: it took “several months mobilizing all 400 employees”.',28),
  p('CISPE, an association of European cloud providers, rated Broadcom “RED” and alleges competition-law breaches. This is an industry claim, not a court finding.',26,MUTED)],gap=14,pad=28)
slide('lockin','Dependency · Cost','Lock-in is felt as rising bills and a hard exit',
 row([L,R]),
 'Sources: Bitkom Cloud Report 2026; CISPE / European Cloud Competition Observatory via Network World (2025).','9d',
 'Lock-in economics. Bitkom Cloud Report 2026 (603 companies): 59% cite lock-in effects as the main barrier to switching, 49% insufficient strategic need; 34% have switched provider (26% once, 8% several times) and 20% plan to; 64% experienced rising cloud costs in 2025, 54% expect further rises in 2026 and only 9% expect declining costs; 42% use cloud-based AI services and 69% expect to in five years (plus 27 points), so the dependency deepens as AI workloads move to the same clouds. VMware: after Broadcom\'s acquisition, European customers reported price increases of 800% to 1,500% (Network World, summarising the European Cloud Competition Observatory report from CISPE; AT&T in the US reported 1,050%). The report says one unnamed CISPE member migrated away entirely at the cost of several months of effort by all 400 employees. Germany\'s VOICE user association filed a complaint with the European Commission. CISPE members compete with US hyperscalers and Broadcom, so read the allegations as an interested party\'s claims; no court ruling is cited. Alternatives named: Nutanix, OpenStack, Proxmox.',
 bg=PAPER2)
print('b2 ok')
