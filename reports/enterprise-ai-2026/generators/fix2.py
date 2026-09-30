import re,sys
sys.path.insert(0,'.')
exec(open('fix1.py').read().split("foot('exit'")[0])
def app(sid,item):
    f=D+sid+'.html'; s=open(f).read()
    k=s.rfind('</p></div></div>'); assert k>0,sid
    s=s[:k+4]+item+s[k+4:]; open(f,'w').write(s)
# cases-ok
sub('cases-ok','DOMCURA: claims up to €3,500, fully automatic.','DOMCURA: claims up to €3,500 fully automatic; 10 min if documents are complete.')
sub('cases-ok','MRH Trowe: mail intake, €0.14 per letter.','MRH Trowe: mail intake, $0.14 per letter (Bitkom’s figure is in dollars).')
sub('cases-ok','at 0.14 euros per letter (target 0.25)','at 0.14 US dollars per letter (target 0.25 dollars; the Bitkom paper states dollars)')
# lead1
sub('lead1','Half of entry-level white-collar jobs gone in 1–5 years.','AI could wipe out half of entry-level white-collar jobs in 1–5 years and lift unemployment to 10–20%.')
sub('lead1','via fewer hires; no widespread displacement.','via fewer hires; authors see no economy-wide displacement.')
sub('lead1','>Not shown<','>No evidence found<')
sub('lead1','AI leaders’ forecasts against the evidence','Predictions by AI leaders, checked against evidence')
sub('lead1','the authors call these early descriptive indicators and state they find no evidence of widespread economy-wide displacement;','the authors call these early descriptive indicators and write that they do not see widespread, economy-wide job displacement associated with AI;')
sub('lead1','NY Fed (1 Sep 2026): 4% of service firms laid off workers because of AI.','NY Fed (1 Sep 2026, regional survey of service firms in New York and Northern New Jersey): 4% laid off workers in response to AI over six months.')
# lead2
sub('lead2','AGI claims can serve as marketing tied to investment.','AGI claims can be a business strategy for AI firms.')
sub('lead2','while expecting to be 24% faster','while expecting to be about a quarter faster')
sub('lead2','research-intern goal set the day OpenAI','research-intern goal announced on the day OpenAI')
sub('lead2','But every forecaster here sells','But every forecaster on the previous slide sells')
# media
sub('media','who are 16% of the sample (US: 71.9%).','who are 16% of the 300 most-cited scholars (US: 71.9%).')
sub('media','OBS 2025: 2,217 articles, 9 outlets','Otto Brenner Stiftung 2025: 2,000+ articles, 9 outlets')
sub('media','2,217 articles from nine German outlets','more than 2,000 articles from nine German outlets')
sub('media','industry-affiliated scholars are 16% of the sample but','industry-affiliated scholars are 16% of the 300 most-cited scholars (150 per country) but')
# media2
sub('media2','do not believe every word of Altman, Musk or Amodei; they have financial incentives.','we should not believe every word of Sam Altman and Elon Musk; industry leaders have financial incentives.')
# gov
sub('gov','OECD Digital Government Outlook 2026, 36 member countries','OECD Digital Government Outlook 2026, 36 responding countries (not Germany or the US)')
sub('gov','(36 member countries, 2025 data)','(36 responding countries; Germany and the United States did not participate; 2025 data)')
# dep
sub('dep','Most German firms use US clouds, prefer not to, and see no substitute','Most German firms use US clouds, few would choose them, 43% see no alternative')
sub('dep','still 5.6% projected for 2031 (Bruegel policy brief, dataset Europe2031.ai).','5.6% projected for 2031 (Bruegel, citing Europe2031.ai; excludes AI capacity inside US clouds’ EU data centres).')
# extremes
sub('extremes','annulled the fine on 18 Mar 2026; its legal ground was not verified here.','annulled the fine on 18 Mar 2026, reportedly because the Garante lacked competence, not on the merits.')
sub('extremes','the Court of Rome annulled the decision on 18 Mar 2026 (Wilson Sonsini);','the Court of Rome annulled the decision on 18 Mar 2026 (Wilson Sonsini gives no reasoning; the European Law Blog reports a jurisdictional ground: the Garante lacked competence under the GDPR one-stop-shop rules, after the Irish regulator recognised OpenAI Ireland as its single establishment);')
sub('extremes','these predate Diella and did not include her development; no one has been indicted.','OCCRP says her development was not among the tenders involved; how the probe timing relates to Diella is unclear; no one has been indicted.')
# reg
sub('reg','stay as written; only the dates shift.','stay as written; only the dates shift. Fines for banned practices: up to €35m or 7% of worldwide turnover.')
sub('reg','Fine amounts are not stated on this slide because we did not verify them in this research.','Maximum fine for prohibited practices: 35 million euros or 7% of total worldwide annual turnover, whichever is higher (AI Act Article 99(3), per artificialintelligenceact.eu; not re-checked against the Omnibus).')
# industry
sub('industry','Workers using GenAI at work (RPS, Nov 2025)','Workers using GenAI at work (Real-Time Population Survey, Nov 2025)')
# summary
sub('summary','No model forecasts both sides','No model forecasts adoption and failure together')
# funnel, adopt-def
sub('funnel','Use AI in 1+ function','Use AI in at least one function')
sub('adopt-def','Organizations worldwide, 1+ function','Organizations worldwide, at least one function')
# causes
sub('causes','Organizations that master these fundamentals turn pilots into production at twice the rate (Gartner, Jan 2026).','As many pilots reach production at firms that master these five fundamentals (Gartner, Jan 2026).')
sub('causes','Gartner expects inference cost per agentic workflow to rise more than fivefold through 2028 (Aug 2026).','Expected rise in the run cost of one agentic workflow through 2028: more than five times today’s (Gartner, Aug 2026).')
# metrics
sub('metrics','S&amp;P: 46% scrapped before adoption.','S&amp;P: on average 46% of projects scrapped before wide use.')
# sources
sub('src6','sam-altman-s-open-ai-paradox','sam-altmans-open-ai-paradox',count=2)
def it(l,u):
    short=re.sub(r"^https?://(www\.)?","",u)[:55]
    return f'<p style="font-size:24px;line-height:1.3;color:#12202F"><b>{l}</b><br><a href="{u}">{short}</a></p>'
app('src5',it('TIME: Albania’s AI-powered minister Diella','https://time.com/7324934/albania-ai-minister-diella/'))
app('src5',it('European Law Blog: Court of Rome and the one-stop-shop','https://www.europeanlawblog.eu/pub/92oig1ws'))
app('src5',it('AI Act Article 99: penalties','https://artificialintelligenceact.eu/article/99/'))
app('src8',it('The Decoder (19 Dec 2023): Axel Springer–OpenAI deal, tens of millions of euros a year','https://the-decoder.com/axel-springer-and-openai-license-agreement-is-worth-tens-of-millions-of-euros-per-year/'))
print('fix2 ok')
