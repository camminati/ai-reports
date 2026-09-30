import re
D='/tmp/claude-0/-home-claude/d83e9c40-3403-54e5-b4cb-d33f00f5ffd5/scratchpad/artifact-files/30f3ab63-14e0-49e5-9d25-52d5f6df0be8/project/slides/'
def sub(sid,old,new,count=1):
    f=D+sid+'.html'; s=open(f).read()
    n=s.count(old)
    assert n>=1,(sid,old[:60],'not found')
    if count==1: assert n==1,(sid,old[:60],n)
    s=s.replace(old,new); open(f,'w').write(s)
def foot(sid,new):
    f=D+sid+'.html'; s=open(f).read()
    s2,n=re.subn(r'(white-space:nowrap">)([^<]*)(</p>)',lambda m:m.group(1)+new+m.group(3),s)
    assert n==1,(sid,n); open(f,'w').write(s2)
foot('exit','Sources: It’s FOSS (2025); Open Source For You (Nov 2025); Kemp IT Law; BMDS (21 May 2026).')
foot('lead1','Sources: CFR; Axios; Fortune (Jan 2026); Google (Apr 2026); BLS; Stanford DEL; OpenAI (Sep 2026).')
foot('lead2','Sources: Anthropic; Axios; TechCrunch (Oct 2025); Fortune (2025, 2026); METR (2025, 2026).')
foot('media','Sources: Reuters Institute; Otto Brenner Stiftung; CAIS; Zai et al.; Roe and Perkins; Ittefaq et al.')
foot('media2','Sources: OpenAI; Nieman Lab; GeekWire; NPR; Handelsblatt; TIME; Fortune; EBU/BBC (Oct 2025).')
print('footers ok')
