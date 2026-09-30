from lib import *
import re
S=[
('Entrepreneur (May 2025): Klarna CEO on hiring humans again','https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396'),
('ABC News (21 Aug 2025): Commonwealth Bank reverses AI job cuts','https://www.abc.net.au/news/2025-08-21/cba-backtracks-on-ai-job-cuts-as-chatbot-lifts-call-volumes/105679492'),
('Al Jazeera (19 Jun 2024): McDonald’s ends AI drive-through pilot','https://www.aljazeera.com/economy/2024/6/19/mcdonalds-scrap-ai-pilot-at-drive-through-outlets-after-order-mix-ups'),
('McCarthy Tétrault: Moffatt v Air Canada (2024 BCCRT 149)','https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot'),
('Bitkom (Mar 2026): white paper “Beyond the Pilot”, insurance','https://www.bitkom.org/sites/main/files/2026-03/bitkom-whitepaper-beyond-the-pilot-kuenstliche-intelligenz-in-der-versicherungswirtschaft.pdf'),
('UK Parliament (2 Jun 2025): Copilot cross-government experiment','https://questions-statements.parliament.uk/written-statements/detail/2025-06-02/hcws669'),
('Bitkom (17 Jun 2026): Cloud Report 2026','https://www.bitkom.org/sites/main/files/2026-06/17062026-bitkom-studienbericht-cloud-report-2026.pdf'),
('Synergy Research: European cloud providers’ share holds at 15%','https://www.srgresearch.com/articles/european-cloud-providers-local-market-share-now-holds-steady-at-15'),
('Bruegel: Europe’s AI compute infrastructure shortfall','https://www.bruegel.org/policy-brief/how-can-europe-address-its-pressing-ai-compute-infrastructure-shortfall'),
('Network World: VMware price rises in Europe (CISPE report)','https://www.networkworld.com/article/3994107/vmware-customers-in-europe-face-up-to-1500-price-increases-under-broadcom-ownership.html'),
('It’s FOSS: Schleswig-Holstein leaves Microsoft (secondary)','https://itsfoss.com/news/german-state-ditch-microsoft/'),
('Open Source For You (7 Nov 2025): ICC moves to openDesk','https://www.opensourceforu.com/2025/11/international-criminal-court-drops-microsoft-365-for-open-source-opendesk-platform/'),
('Kemp IT Law: end of cloud switching charges (Data Act)','https://kempitlaw.com/insights/the-end-of-switching-charges-commercial-impact-and-compliance-priorities/'),
('BMDS (21 May 2026): award for the sovereign AI cloud','https://bmds.bund.de/aktuelles/pressemitteilungen/detail/bmds-erteilt-zuschlag-fuer-souveraene-ki-cloud'),
('OECD: Digital Government Outlook 2026, AI in government','https://www.oecd.org/en/publications/digital-government-outlook_0496b2bc-en/full-report/adopting-and-governing-ai-in-government_7ef312a9.html'),
('Wikipedia: Diella (AI system)','https://en.wikipedia.org/wiki/Diella_(AI_system)'),
('OCCRP: Albania’s AI minister and the agency under investigation','https://www.occrp.org/en/feature/albanias-cheerful-ai-minister-is-the-product-of-a-government-agency-under-investigation-for-massive-corruption'),
('RFE/RL: Romania’s AI adviser Ion (2023)','https://www.rferl.org/a/romania-ai-political-adviser-ion-/32304377.html'),
('Reuters factbox via Yahoo: scrutiny of DeepSeek','https://finance.yahoo.com/news/factbox-governments-regulators-increase-scrutiny-095326244.html'),
('Lewis Silkin (14 Jan 2025): Italian fine on OpenAI','https://www.lewissilkin.com/en/insights/2025/01/14/openai-faces-15-million-fine-as-the-italian-garante-strikes-again-102jtqc'),
('Wilson Sonsini: Court of Rome annuls the fine','https://www.wsgr.com/en/insights/openai-prevails-in-landmark-italian-ai-and-gdpr-enforcement-case.html'),
('Lewis Silkin (27 Jul 2026): AI Omnibus in force','https://www.lewissilkin.com/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today-102nedo'),
('Gibson Dunn: AI Act omnibus agreement','https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/'),
('IW Köln: IW-Report 2025, KI als Wettbewerbsfaktor','https://www.iwkoeln.de/fileadmin/user_upload/Studien/Report/PDF/2025/IW-Report_2025-KI-als-Wettbewerbsfaktor.pdf'),
('CFR (10 Mar 2025): Amodei in conversation','https://www.cfr.org/event/ceo-speaker-series-dario-amodei-anthropic'),
('Axios (28 May 2025): Amodei on white-collar jobs','https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic'),
('Fortune (29 Jan 2026): AI-written code at Anthropic and OpenAI','https://www.fortune.com/2026/01/29/100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-cherny-roon'),
('Google (22 Apr 2026): 75% of new code AI-generated','https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/'),
('Stanford Digital Economy Lab (12 Aug 2026): Canaries update','https://digitaleconomy.stanford.edu/news/canariesaug26/'),
('BLS (4 Sep 2026): Employment situation','https://www.bls.gov/news.release/empsit.nr0.htm'),
('NY Fed (1 Sep 2026): businesses using AI to transform work','https://libertystreeteconomics.newyorkfed.org/2026/09/businesses-are-using-ai-to-transform-work-not-cut-jobs/'),
('Altman (Jan 2025): “Reflections”','https://blog.samaltman.com/reflections'),
('Reworked: 2025 was to be the year of the agent (Deloitte)','https://www.reworked.co/digital-workplace/2025-was-supposed-to-be-the-year-of-the-agent-it-never-arrived/'),
('Simon Willison (26 Feb 2026): Karpathy on coding agents','https://simonwillison.net/2026/Feb/26/andrej-karpathy/'),
('Fortune (24 Jan 2025): Zuckerberg on AI engineer and capex','https://fortune.com/2025/01/24/mark-zuckerberg-ai-engineer-capex-spend'),
('TechCrunch (2 Jul 2026): Zuckerberg on agent progress','https://techcrunch.com/2026/07/02/mark-zuckerberg-tells-staff-that-ai-agents-havent-progressed-as-quickly-as-hed-hoped/'),
('OpenAI (Sep 2026): research acceleration inside OpenAI','https://openai.com/index/research-acceleration-view-inside-openai/'),
('TechCrunch (21 Oct 2025): Amodei answers Sacks','https://techcrunch.com/2025/10/21/anthropic-ceo-claps-back-after-trump-officials-accuse-firm-of-ai-fear-mongering/'),
('Fortune (19 Aug 2025): Altman’s bubble warning and OpenAI’s raise','https://fortune.com/2025/08/19/sam-altman-s-open-ai-paradox-warning-of-ai-bubble-while-raising-trillions'),
('Fortune (26 May 2026): leaders walking back jobs claims','https://fortune.com/2026/05/26/sam-altman-dario-amodei-walking-back-ai-jobs-apocalypse-prophecies-ipo/'),
('METR (10 Jul 2025): developer productivity trial','https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/'),
('Anthropic (3 Mar 2025): Series E','https://www.anthropic.com/news/anthropic-raises-series-e-at-usd61-5b-post-money-valuation'),
('Reuters Institute (2018): UK media coverage of AI','https://reutersinstitute.politics.ox.ac.uk/sites/default/files/2018-12/Brennen_UK_Media_Coverage_of_AI_FINAL.pdf'),
('Reuters Institute (2019): industry experts in AI news','https://reutersinstitute.politics.ox.ac.uk/industry-experts-or-industry-experts-academic-sourcing-news-coverage-ai'),
('Otto Brenner Stiftung (2025): KI im medialen Diskurs','https://www.otto-brenner-stiftung.de/was-wir-tun/publikationen/kuenstliche-intelligenz-im-medialen-diskurs/'),
('CAIS (2022): Factsheet 7, Medienberichterstattung','https://www.cais-research.de/wp-content/uploads/Factsheet-7-Medienberichterstattung.pdf'),
('Zai et al., Frontiers in Communication (2025)','https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2025.1599854/full'),
('Roe and Perkins (2023), Humanities and Social Sciences Comms','https://www.nature.com/articles/s41599-023-02282-w'),
('Ittefaq et al. (2025), Telematics and Informatics','https://www.sciencedirect.com/science/article/abs/pii/S0736585324001278'),
('Handelsblatt (18 Aug 2026): commentary on believing AI leaders','https://www.handelsblatt.com/meinung/kommentare/kommentar-wir-sollten-sam-altman-elon-musk-oder-dario-amodei-nicht-jedes-wort-glauben-02/100247265.html'),
('TIME (11 Dec 2025): Person of the Year, Architects of AI','https://time.com/7339685/person-of-the-year-2025-ai-architects/'),
('EBU and BBC (21 Oct 2025): News integrity in AI assistants','https://www.ebu.ch/research/open/report/news-integrity-in-ai-assistants'),
('OpenAI (13 Dec 2023): Axel Springer partnership','https://openai.com/index/axel-springer-partnership/'),
('Nieman Lab: News Corp and OpenAI deal','https://www.niemanlab.org/reading/openai-and-news-corp-strike-a-content-deal-valued-at-over-250-million/'),
('GeekWire (30 Jul 2025): Amazon and the NYT','https://www.geekwire.com/2025/report-amazon-to-pay-at-least-20m-a-year-in-ai-content-deal-with-new-york-times/'),
('Fortune (21 Jun 2023): Springer, Bild and AI','https://fortune.com/europe/2023/06/21/german-media-mogul-mathias-dopfner-elon-musk-layoff-tabloid-bild-a-i'),
]
def item(l,u):
    short=re.sub(r'^https?://(www\.)?','',u)
    if len(short)>58: short=short[:55]+'…'
    return (f'<p style="font-size:24px;line-height:1.3;color:{INK}"><b>{e(l)}</b><br><a href="{u}">{e(short)}</a></p>')
n=12; chunks=[S[i:i+n] for i in range(0,len(S),n)]
ids=[]
for k,ch in enumerate(chunks,1):
    sid=f'src{3+k}'; ids.append(sid)
    half=(len(ch)+1)//2
    col=lambda xs: '<div style="flex:1;display:flex;flex-direction:column;gap:16px">'+''.join(item(*x) for x in xs)+'</div>'
    body='<div style="display:flex;gap:40px;align-items:flex-start">'+col(ch[:half])+col(ch[half:])+'</div>'
    slide(sid,'Sources',f'Sources (addendum): landscape slides, part {k} of {len(chunks)}',body,
      'Accessed September 2026. Some pages were read through summaries; check quotes against the source before reuse.','S',
      'Sources for the slides added on case studies, dependency, government, regulation, AI-leader forecasts and media coverage. Vendor-affiliated or interested-party sources are flagged on the slides where used. Blocked to our tools: heise, EJIL Talk, Balkan Insight, CNBC, The Register, economist.com, theguardian.com.',bg=PAPER2)
print(ids)
json.dump(ids,open('srcids.json','w'))
