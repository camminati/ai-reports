import re,sys
sys.path.insert(0,'.')
exec(open('fix1.py').read().split("foot('exit'")[0])
def app(sid,item):
    f=D+sid+'.html'; s=open(f).read()
    k=s.rfind('</p></div></div>'); assert k>0,sid
    s=s[:k+4]+item+s[k+4:]; open(f,'w').write(s)
# sources
sub('src7','sam-altman-s-open-ai-paradox','sam-altmans-open-ai-paradox',count=2)
def it(l,u):
    short=re.sub(r"^https?://(www\.)?","",u)[:55]
    return f'<p style="font-size:24px;line-height:1.3;color:#12202F"><b>{l}</b><br><a href="{u}">{short}</a></p>'
app('src5',it('TIME: Albania’s AI-powered minister Diella','https://time.com/7324934/albania-ai-minister-diella/'))
app('src5',it('European Law Blog: Court of Rome and the one-stop-shop','https://www.europeanlawblog.eu/pub/92oig1ws'))
app('src5',it('AI Act Article 99: penalties','https://artificialintelligenceact.eu/article/99/'))
app('src8',it('The Decoder (19 Dec 2023): Axel Springer–OpenAI deal, tens of millions of euros a year','https://the-decoder.com/axel-springer-and-openai-license-agreement-is-worth-tens-of-millions-of-euros-per-year/'))
print('fix2 ok')
