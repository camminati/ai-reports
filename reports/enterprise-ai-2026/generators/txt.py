import json,re,sys,html
D='/tmp/claude-0/-home-claude/d83e9c40-3403-54e5-b4cb-d33f00f5ffd5/scratchpad/artifact-files/30f3ab63-14e0-49e5-9d25-52d5f6df0be8/project/'
def vis(sid):
    h=open(D+'slides/'+sid+'.html').read()
    h=re.sub(r'<aside>.*?</aside>','',h,flags=re.S)
    h=re.sub(r'</(p|h1|h2|h3|li|tr|div)>','\n',h)
    h=re.sub(r'</t[dh]>',' | ',h)
    h=re.sub(r'<[^>]+>','',h)
    h=html.unescape(h)
    return '\n'.join(l.strip() for l in h.split('\n') if l.strip())
for sid in sys.argv[1:]:
    print('=====',sid); print(vis(sid))
