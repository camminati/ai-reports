D='/path/to/scratchpad/artifact-files/<artifact-id>/project/slides/'
def edit(name,pairs):
    t=open(D+name+'.html').read()
    for a,b in pairs:
        assert t.count(a)==1,(name,a[:80],t.count(a))
        t=t.replace(a,b)
    open(D+name+'.html','w').write(t)

# summary
edit('summary',[
 ('About 88% of surveyed firms use AI somewhere, 39% report any profit impact','About 89% of surveyed firms use AI somewhere, 37% report any profit impact'),
 ('nearly nine in ten surveyed organizations use AI in at least one function (McKinsey 2026, also reported in the Stanford AI Index 2026); 44% say AI is scaling across the enterprise; 39% report enterprise-level EBIT impact;',
  '89% of surveyed organizations use AI in at least one function (McKinsey 2026, Exhibit 1; 88% a year earlier, the figure the Stanford AI Index 2026 reports); 44% of AI-using organizations say AI is scaling across the enterprise; 37% of respondents report at least some enterprise-level EBIT impact;'),
 ('workflow redesign is among the strongest of 31 variables McKinsey tested.','in McKinsey 2026, nearly three-quarters of high performers have fundamentally redesigned workflows against one-quarter of other respondents.'),
])
# adopt-def
edit('adopt-def',[
 ('Adoption ranges from 18% to 88%, depending on who is counted','Adoption ranges from 18% to 89%, depending on who is counted'),
 ('<div style="width:458px; height:36px;','<div style="width:463px; height:36px;'),
 ('color:#a85a08">≈88%</p>','color:#a85a08">89%</p>'),
 ('McKinsey 2026: nearly nine in ten respondents report regular use in at least one function; Stanford AI Index 2026 reports 88%.','McKinsey 2026 (PDF, Exhibit 1): 89% of respondents report regular use in at least one function (88% in 2025, the figure the Stanford AI Index 2026 reports); 1,719 respondents in 97 countries, weighted by each country\'s share of global GDP.'),
])
# funnel
edit('funnel',[
 ('<span style="color:#4A5560">· nearly nine in ten</span>','<span style="color:#4A5560">· 89%, nearly nine in ten</span>'),
 ('<div style="width:757px;height:40px;background:#0B6E6B;border-radius:8px"></div></div><p style="font-size:40px;line-height:1.1;font-weight:600;color:#0B6E6B">≈88%</p>','<div style="width:765px;height:40px;background:#0B6E6B;border-radius:8px"></div></div><p style="font-size:40px;line-height:1.1;font-weight:600;color:#0B6E6B">89%</p>'),
 ('<span style="color:#4A5560">· up from 38%</span>','<span style="color:#4A5560">· of AI users, up from 38%</span>'),
 ('<div style="width:335px;height:40px;background:#0B6E6B;border-radius:8px"></div></div><p style="font-size:40px;line-height:1.1;font-weight:600;color:#0B6E6B">39%</p>','<div style="width:318px;height:40px;background:#0B6E6B;border-radius:8px"></div></div><p style="font-size:40px;line-height:1.1;font-weight:600;color:#0B6E6B">37%</p>'),
 ('McKinsey State of AI 2026 (published 25 Aug 2026, 1,719 respondents, fielded 4 May to 8 Jun 2026). Nearly nine in ten report regular use in at least one function; 44% say AI is scaling across the enterprise (38% a year earlier); 39% report EBIT impact at the enterprise level (some secondary summaries cite 37%; we use the wording on McKinsey\'s own page); about 6% are high performers, defined as attributing 5% or more of EBIT to AI and reporting significant value. All figures are self-reported.',
  'McKinsey, The state of AI in 2026 (PDF, Aug 2026; 1,719 respondents in 97 countries, fielded 4 May to 8 Jun 2026, weighted by each country\'s share of global GDP; 36% of respondents work for organizations above $1bn revenue). 89% report regular use in at least one function (88% in 2025; Exhibit 1). 44% of AI-using organizations are at least scaling AI across the enterprise (38% a year earlier); the exhibit is titled "among organizations using AI", so of all respondents it would be about 39% (our arithmetic, 0.44 x 0.89). 37% of respondents attribute at least some EBIT impact to AI, essentially unchanged from 2025. About 6% are high performers: 5% or more of EBIT from AI and "significant" value (92 of 1,521 AI-using respondents). The bars therefore have different bases and are not one strict funnel. All figures are self-reported.'),
])
# patterns
edit('patterns',[
 ('44% scaling, 39% any EBIT impact, ≈6% significant (McKinsey 2026)','44% scaling, 37% any EBIT impact, ≈6% significant (McKinsey 2026)'),
 ('reports 44% scaling, 39% any enterprise EBIT impact and about 6% high performers','reports 44% scaling (of AI users), 37% any enterprise EBIT impact and about 6% high performers'),
])
# metrics
edit('metrics',[
 ('Public range: 18% to 88%, by definition.','Public range: 18% to 89%, by definition.'),
 ('McKinsey: 44% of firms say AI is scaling.','McKinsey: 44% of AI users say AI is scaling.'),
 ('McKinsey: 39% any EBIT impact, about 6% significant.','McKinsey: 37% any EBIT impact, about 6% significant.'),
 ('Census BTOS 18% to McKinsey about 88%','Census BTOS 18% to McKinsey 89%'),
 ('McKinsey 2026 scaling 44%, any EBIT impact 39%','McKinsey 2026 scaling 44% (of AI users), any EBIT impact 37%'),
])
# factors
edit('factors',[
 ('One of the strongest of 31 variables tested (McKinsey relative-weights analysis).','Nearly three-quarters of high performers, one-quarter of others (McKinsey 2026).'),
 ('High performers are more than 3× as likely to aim to transform the business.','High performers are 3.3× as likely to intend to transform the business within three years.'),
 ('Workflow redesign is the strongest repeated success factor','Workflow redesign shows the widest gap between high performers and the rest'),
 ('McKinsey ran a relative-weights analysis on 31 variables; intentional workflow redesign has one of the strongest contributions to meaningful business impact.','The 2026 report PDF contains no relative-weights ranking; an earlier reading of McKinsey\'s web article cited 31 variables, which we could not confirm in the PDF. What the PDF does show: nearly three-quarters of high performers (up from 55% last year) have fundamentally redesigned workflows because of AI, against one-quarter of other respondents (n = 92 vs 1,429), and in Exhibit 11 this is the widest gap of the eleven practices shown (our reading of the chart). High performers are also 3.3 times as likely to intend to transform their business within three years, twice as likely to say senior leaders demonstrate commitment and that impact-measurement processes exist, and more than three times as likely to be scaling agents in most functions.'),
])
# actions
edit('actions',[
 ('The strongest repeated factor in McKinsey’s high-performer analysis.','The widest gap between high performers and others in McKinsey’s 2026 survey.'),
 ('(2) McKinsey 2026 relative-weights analysis on workflow redesign;','(2) McKinsey 2026 high-performer comparison on workflow redesign;'),
])
# caveats notes
edit('caveats',[
 ('Consultancy and analyst sources: Gartner, McKinsey and BCG are commercial research houses.','Consultancy and analyst sources: Gartner, McKinsey and BCG are commercial research houses. McKinsey 2026 is an online survey of 1,719 people in 97 countries, weighted by country GDP, with 36% from organizations above $1bn revenue; its shares use different bases (all respondents, AI users, or high performers, n = 92), so they are not one strict funnel.'),
])
# src1
edit('src1',[
 ('<b>McKinsey (25 Aug 2026), The State of AI: Global Survey 2026</b>','<b>McKinsey (Aug 2026), The state of AI in 2026: On the road to ROI (PDF read in full)</b>'),
])
# lead1 row 2
edit('lead1',[
 ('US unemployment 4.1% (Aug 2026). Stanford: exposed jobs for 22–25-year-olds 19% below peers, via fewer hires; authors see no economy-wide displacement.','US unemployment 4.1% (Aug 2026). Stanford: exposed 22–25-year-olds 19% below peers via fewer hires; no economy-wide displacement. McKinsey: 14% of AI users report AI-linked headcount cuts.'),
 ('NY Fed (1 Sep 2026, regional survey','McKinsey, The state of AI in 2026 (PDF, p. 25, Exhibit 16; 1,521 AI-using respondents): 14% report that AI contributed to an overall decline in workforce size in the past year, 8% an increase, 66% little or no change; a year earlier 32% had expected declines. 39% now expect decreases next year, 43% little or no change. Self-reported. NY Fed (1 Sep 2026, regional survey'),
])
print('ok')
