import json,re,sys,html
D='/path/to/scratchpad/artifact-files/<artifact-id>/project/'
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
