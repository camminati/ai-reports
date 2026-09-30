import html, json
D='/tmp/claude-0/-home-claude/d83e9c40-3403-54e5-b4cb-d33f00f5ffd5/scratchpad/artifact-files/30f3ab63-14e0-49e5-9d25-52d5f6df0be8'
INK='#12202F';PAPER='#F6F3EC';PAPER2='#ECE6D8';CARD='#FFFDF8';LINE='#D9D2C0';MUTED='#4A5560';TEAL='#0B6E6B';AMBER='#A85A08';BAR_AMBER='#C9791B';AMBER_L='#F2B65C';TEAL_L='#6FCBC5';MUTED_D='#B9C4CE'
SERIF="'Source Serif 4', Georgia, serif";SANS="'IBM Plex Sans', Arial, sans-serif"
def e(t): return html.escape(t,quote=False)
def rich(t):
    t=e(t)
    return t.replace('&lt;b&gt;','<b>').replace('&lt;/b&gt;','</b>')
def head(eb,t):
    return (f'<div style="display:flex;flex-direction:column;gap:8px"><p style="font-size:24px;line-height:1.2;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{TEAL}">{e(eb)}</p>'
            f'<h2 style="font-family:{SERIF};font-size:64px;font-weight:600;line-height:1.1;color:{INK}">{e(t)}</h2></div>')
def p(t,size=30,color=INK,extra=''):
    return f'<p style="font-size:{size}px;line-height:1.35;color:{color};{extra}">{rich(t)}</p>'
def h3(t,color=INK):
    return f'<h3 style="font-family:{SERIF};font-size:40px;font-weight:600;line-height:1.15;color:{color}">{e(t)}</h3>'
def pill(t,bg):
    return f'<div style="display:flex"><p style="font-size:24px;line-height:1.2;font-weight:600;background:{bg};color:{INK};padding:8px 16px;border-radius:24px">{e(t)}</p></div>'
def card(children,flex='1',bg=CARD,border=LINE,pad=32,gap=10,top=None,dashed=False,extra=''):
    b=f'border:1px {"dashed" if dashed else "solid"} {border};'
    if top: b+=f'border-top:6px solid {top};'
    return f'<div style="background:{bg};{b}border-radius:16px;padding:{pad}px;display:flex;flex-direction:column;gap:{gap}px;flex:{flex};{extra}">'+''.join(children)+'</div>'
def row(cells):  # cells: list of html cards
    return '<div style="display:flex;gap:24px;align-items:stretch">'+''.join(cells)+'</div>'
def fixed(children,w,bg=CARD,pad=22,justify='flex-start',border=True):
    bd=f'border:1px solid {LINE};' if border else ''
    return f'<div style="width:{w}px;flex:none;background:{bg};{bd}border-radius:16px;padding:{pad}px 28px;display:flex;flex-direction:column;justify-content:{justify};gap:6px">'+''.join(children)+'</div>'
def label(t): return f'<p style="font-size:24px;line-height:1.2;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:{MUTED}">{e(t)}</p>'
def slide(sid,eb,title,body,foot,num,notes,bg=PAPER,note=None):
    s=(f'<section id="{sid}" data-transition="fade" style="background:{bg};color:{INK};font-family:{SANS};padding:128px 128px 160px;display:flex;flex-direction:column;gap:32px">\n'
       +head(eb,title)+'\n'+body+'\n')
    if note: s+=p(note,24,MUTED)+'\n'
    s+=(f'<p style="position:absolute;left:128px;bottom:64px;width:1440px;font-size:24px;line-height:1.2;color:{MUTED};white-space:nowrap">{e(foot)}</p>'
        f'<p style="position:absolute;right:128px;bottom:64px;width:120px;font-size:24px;line-height:1.2;color:{MUTED};text-align:right">{num}</p>\n'
        f'<aside>{e(notes)}</aside>\n</section>\n')
    open(f'{D}/project/slides/{sid}.html','w').write(s)
def grid(cells,cols=2,gap=24): 
    return f'<div style="display:grid;grid-template-columns:{" ".join(["1fr"]*cols)};gap:{gap}px">'+''.join(cells)+'</div>'
def stack(items,gap=20): return f'<div style="display:flex;flex-direction:column;gap:{gap}px">'+''.join(items)+'</div>'
