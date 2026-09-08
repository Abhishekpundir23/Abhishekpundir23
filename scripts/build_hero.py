"""Generate self-contained, responsive GitHub profile hero artwork.

Run from any directory. Only the four hero SVG assets are written.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTES = {
    'dark': {'bg':'#070d18','panel':'#0d1728','inner':'#091120','fg':'#edf5ff','muted':'#a0b2cb','fine':'#24364e','grid':'#142137','cyan':'#5ce1ff','violet':'#a78bfa','amber':'#ffce73','green':'#70e3bd'},
    'light': {'bg':'#f6f9ff','panel':'#ffffff','inner':'#f2f6fc','fg':'#12233e','muted':'#506580','fine':'#ccdaeb','grid':'#e0eaf5','cyan':'#006c9f','violet':'#7046bd','amber':'#976400','green':'#087758'},
}

def txt(x, y, text, size, fill, weight=400, family='Arial, Helvetica, sans-serif', **attrs):
    extra = ' '.join(f'{k.replace("_", "-")}="{escape(str(v), quote=True)}"' for k,v in attrs.items())
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" {extra}>{escape(text)}</text>'

def rect(x,y,w,h,fill,stroke=None,rx=12,**attrs):
    extra = ' '.join(f'{k.replace("_", "-")}="{v}"' for k,v in attrs.items())
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"'+(f' stroke="{stroke}"' if stroke else '')+f' {extra}/>'

def path(d,stroke,width=1,**attrs):
    extra = ' '.join(f'{k.replace("_", "-")}="{v}"' for k,v in attrs.items())
    return f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'

def icon(kind,x,y,color,scale=1):
    shapes = {
        'agent': '<rect x="3" y="6" width="22" height="18" rx="5"/><path d="M14 2v4M9 12v3m10-3v3M10 20h8M0 13h3m22 0h3"/>',
        'tools': '<path d="m9 6-6 8 6 8m10-16 6 8-6 8M16 3l-4 22"/>',
        'trace': '<path d="M4 4v20m0-16h8m-8 6h14M4 20h20"/><circle cx="15" cy="8" r="2"/><circle cx="21" cy="14" r="2"/>',
        'diff': '<path d="M3 8h9m-4-4v8m9 8h9M14 3v22"/>',
        'verify': '<path d="M14 2 25 7v8c0 6-11 11-11 11S3 21 3 15V7Z"/><path d="m8 14 4 4 8-8"/>',
    }
    return f'<g transform="translate({x} {y}) scale({scale})" stroke="{color}" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round">{shapes[kind]}</g>'

def node(x,y,w,h,label,sub,kind,color,p,mobile=False):
    size = 25 if mobile else 18
    subtitle = 24 if mobile else 12
    s = rect(x,y,w,h,p['inner'],p['fine'],12)
    s += path(f'M{x+12} {y+1}H{x+w-12}',color,1.5,stroke_opacity='.75')
    s += icon(kind,x+14,y+15,color,1.15 if mobile else .82)
    s += txt(x+(58 if mobile else 49),y+31,label,size,p['fg'],600)
    s += txt(x+15,y+h-15,sub,subtitle,p['muted'])
    return s

def start(w,h,p,mobile):
    title='Abhishek Pundir — Software Engineer and AI Systems'
    desc='Engineering console illustration showing an agent using tools, recording a trace, comparing a change and verifying behavior. A small illustrative log compares an argument with its baseline; it is not live telemetry.'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" role="img" aria-labelledby="title desc">
<title id="title">{title}</title><desc id="desc">{desc}</desc>
<defs>
 <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{p['grid']}" stroke-width=".7"/></pattern>
 <linearGradient id="edge" x1="0" y1="0" x2="{w}" y2="{h}" gradientUnits="userSpaceOnUse"><stop stop-color="{p['cyan']}" stop-opacity=".6"/><stop offset=".5" stop-color="{p['fine']}"/><stop offset="1" stop-color="{p['violet']}" stop-opacity=".45"/></linearGradient>
 <clipPath id="bounds"><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="22"/></clipPath>
</defs>
<style>
.signal {{stroke-dasharray: 5 250; stroke-linecap: round; animation: stream 16s linear infinite;}}
.signal.delayed {{animation-delay:-8s;}}
.node-pulse {{animation: breathe 16s ease-in-out infinite;}}
@keyframes stream {{to {{stroke-dashoffset:-510;}}}}
@keyframes breathe {{0%,100% {{opacity:.45}} 50% {{opacity:.9}}}}
@media (prefers-reduced-motion: reduce) {{.signal,.node-pulse {{animation:none !important;}} .signal {{stroke-dasharray:none;opacity:.45;}}}}
</style>
<g clip-path="url(#bounds)">
{rect(0,0,w,h,p['bg'],rx=0)}
<rect width="{w}" height="{h}" fill="url(#grid)" opacity=".6"/>
'''

def finish(w,h):
    return f'</g><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="22" stroke="url(#edge)"/></svg>\n'

def terminal(x,y,w,h,p,mobile=False):
    s=rect(x,y,w,h,p['inner'],p['fine'],10)
    if mobile:
        s+=txt(x+20,y+36,'ILLUSTRATIVE TRACE DIFF',20,p['muted'],600,letter_spacing='1')
        s+=path(f'M{x+20} {y+53}H{x+w-20}',p['fine'])
        mono='Menlo, Consolas, monospace'
        lines=[('trace','tool: search_docs',p['cyan']),('−','limit: 3',p['muted']),('+','limit: 5',p['amber']),('check','schema → valid',p['green'])]
        for i,(prefix,value,color) in enumerate(lines):
            yy=y+88+i*36
            s+=txt(x+20,yy,prefix,24,color,500,family=mono)
            s+=txt(x+113,yy,value,24,p['fg'],family=mono)
    else:
        s+=txt(x+16,y+23,'ILLUSTRATIVE TRACE DIFF',10,p['muted'],600,letter_spacing='1.4')
        s+=path(f'M{x+16} {y+33}H{x+w-16}',p['fine'])
        mono='Menlo, Consolas, monospace'
        lines=[('trace','tool: search_docs',p['cyan']),('diff','limit: 3 → 5',p['amber']),('check','schema → valid',p['green'])]
        for i,(prefix,value,color) in enumerate(lines):
            yy=y+55+i*20
            s+=txt(x+16,yy,prefix,13,color,500,family=mono)
            s+=txt(x+82,yy,value,13,p['fg'],family=mono)
        s+=icon('diff',x+w-61,y+56,p['fine'],1.1)
    return s

def desktop(theme):
    p=PALETTES[theme]; w,h=1200,500
    s=start(w,h,p,False)
    s+=path('M52 50H75',p['cyan'],3)
    s+=txt(88,55,'ENGINEERING / AI SYSTEMS',12,p['muted'],600,letter_spacing='2.5')
    s+=txt(48,153,'Abhishek',77,p['fg'],700,letter_spacing='-3.4')
    s+=txt(48,230,'Pundir',77,p['fg'],700,letter_spacing='-3.4')
    s+=rect(295,218,12,12,p['cyan'],rx=1)
    s+=txt(52,276,'Software Engineer',25,p['fg'],600)
    s+=txt(52,308,'AI Systems',25,p['cyan'],600)
    s+=txt(52,359,'Developer tools · Agent evaluation',18,p['muted'])
    s+=txt(52,387,'Reproducible builds · Software quality',18,p['muted'])
    s+=path('M52 421H452',p['fine'])
    for xx,label,color in [(52,'BUILD',p['cyan']),(179,'COMPARE',p['violet']),(339,'VERIFY',p['green'])]:
        s+=rect(xx,441,5,5,color,rx=1)
        s+=txt(xx+14,448,label,12,p['muted'],600,letter_spacing='1.5')
    s+=rect(510,32,658,436,p['panel'],p['fine'],18)
    s+=txt(536,65,'ILLUSTRATIVE WORKFLOW',12,p['muted'],600,letter_spacing='1.8')
    s+=path('M536 81H1142',p['fine'])
    # Five-stage route: left-to-right first row, down, then left.
    route='M710 148H742M896 148H928M1005 188V247M928 283H896'
    s+=path(route,p['fine'],2)
    s+=path(route,p['cyan'],2.5,**{'class':'signal'})
    s+=path('M724 144l5 4-5 4M910 144l5 4-5 4M1001 220l4 5 4-5M914 279l-5 4 5 4',p['muted'],1.3)
    s+=node(556,112,154,76,'Agent','task + context','agent',p['cyan'],p)
    s+=node(742,112,154,76,'Tools','CLI + APIs','tools',p['cyan'],p)
    s+=node(928,112,154,76,'Trace','record actions','trace',p['violet'],p)
    s+=node(928,247,154,76,'Diff','compare runs','diff',p['amber'],p)
    s+=node(742,247,154,76,'Verify','check behavior','verify',p['green'],p)
    # A restrained source marker fills the circuit's negative space.
    s+=path('M564 232H588M576 220V244',p['fine'],1)
    s+=txt(556,276,'TRACEABLE',12,p['muted'],600,letter_spacing='1.5')
    s+=txt(556,297,'BY DESIGN',12,p['muted'],600,letter_spacing='1.5')
    s+=terminal(536,343,606,105,p)
    return s+finish(w,h)

def mobile(theme):
    p=PALETTES[theme]; w,h=600,1174
    s=start(w,h,p,True)
    s+=path('M34 43H57',p['cyan'],3)
    s+=txt(72,50,'ENGINEERING / AI SYSTEMS',18,p['muted'],600,letter_spacing='1.1')
    s+=txt(30,137,'Abhishek',73,p['fg'],700,letter_spacing='-3')
    s+=txt(30,213,'Pundir',73,p['fg'],700,letter_spacing='-3')
    s+=rect(263,202,11,11,p['cyan'],rx=1)
    s+=txt(34,264,'Software Engineer · AI Systems',26,p['fg'],600)
    s+=txt(34,310,'Developer tools · Agent evaluation',24,p['muted'])
    s+=txt(34,344,'Reproducible builds · Software quality',24,p['muted'])
    s+=rect(24,382,552,763,p['panel'],p['fine'],18)
    s+=txt(46,421,'ILLUSTRATIVE WORKFLOW',21,p['muted'],600,letter_spacing='1')
    s+=path('M46 440H554',p['fine'])
    # A five-stage serpentine circuit preserves the complete sequence.
    route='M260 503H340M446 549V591M340 637H260M154 683V770H196'
    s+=path(route,p['fine'],2.5)
    s+=path(route,p['cyan'],3,**{'class':'signal'})
    s+=path('M291 497l7 6-7 6M440 569l6 7 6-7M309 631l-7 6 7 6M179 764l7 6-7 6',p['muted'],1.6)
    s+=node(46,457,214,92,'Agent','task + context','agent',p['cyan'],p,True)
    s+=node(340,457,214,92,'Tools','CLI + APIs','tools',p['cyan'],p,True)
    s+=node(340,591,214,92,'Trace','record actions','trace',p['violet'],p,True)
    s+=node(46,591,214,92,'Diff','compare runs','diff',p['amber'],p,True)
    s+=node(196,724,214,92,'Verify','check behavior','verify',p['green'],p,True)
    s+=terminal(46,844,508,274,p,True)
    return s+finish(w,h)

def main():
    assets=ROOT/'assets'
    assets.mkdir(exist_ok=True)
    for theme in ('dark','light'):
        (assets/f'hero-{theme}.svg').write_text(desktop(theme))
        (assets/f'hero-mobile-{theme}.svg').write_text(mobile(theme))

if __name__ == '__main__':
    main()
