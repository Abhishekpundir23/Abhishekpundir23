"""Draw original capability panels with only the Python standard library."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]

def make(theme, mobile=False):
    dark = theme == 'dark'
    bg, panel, line, fg, muted = ('#070d18','#0d1728','#22344c','#edf5ff','#a1b4cd') if dark else ('#f6f9ff','#ffffff','#c9d9e8','#11213a','#4d6480')
    colors = ['#5ce1ff','#a78bfa','#ffce73'] if dark else ['#006c9f','#7545be','#9a6200']
    w, h = (600, 990) if mobile else (1200, 372)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">', '<title id="title">Engineering capabilities</title>', '<desc id="desc">AI agent evaluation, developer infrastructure, and product engineering: three connected areas of my work.</desc>', f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="22" fill="{bg}" stroke="{line}"/>']
    cards = [
        ('01','AI evaluation', ['Trace behavior.', 'Reproduce failures.', 'Test what changed.']),
        ('02','Developer tooling', ['Transform code.', 'Automate the checks.', 'Keep changes reviewable.']),
        ('03','Product engineering', ['Design the workflow.', 'Build across platforms.', 'Handle the edge cases.']),
    ]
    for i, (num, title, copy) in enumerate(cards):
        x,y,cw,ch = (20,20+i*320,560,310) if mobile else (20+i*393,20,374,332)
        c = colors[i]
        out += [f'<g transform="translate({x} {y})">',f'<rect width="{cw}" height="{ch}" rx="16" fill="{panel}" stroke="{line}"/>',f'<text x="22" y="35" fill="{c}" font-family="monospace" font-size="20">{num} / ENGINEERING</text>']
        # Each miniature diagram expresses the capability rather than a generic decoration.
        if i == 0:
            out += [f'<path d="M36 104H104L132 76H204L240 118H{cw-35}" fill="none" stroke="{c}" stroke-width="2.5"/>',f'<path d="M104 104L140 140H214" fill="none" stroke="{c}" stroke-width="2" stroke-dasharray="5 6" opacity=".5"/>']
            for px,py in [(36,104),(104,104),(204,76),(240,118),(cw-35,118)]:
                out += [f'<circle cx="{px}" cy="{py}" r="6" fill="{bg}" stroke="{c}" stroke-width="2"/>']
        elif i == 1:
            out += [f'<path d="M68 88V128M68 110H132M132 82V142M132 90H200M132 132H200" stroke="{c}" stroke-width="2" fill="none"/>']
            for px,py in [(55,70),(120,67),(120,123),(196,77),(196,120)]:
                out += [f'<rect x="{px}" y="{py}" width="26" height="20" rx="4" fill="{bg}" stroke="{c}" stroke-width="2"/>']
            out += [f'<path d="M{cw-108} 112L{cw-93} 127L{cw-62} 91" stroke="{c}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>']
        else:
            out += [f'<rect x="36" y="69" width="{cw-126}" height="78" rx="7" fill="{bg}" stroke="{c}" stroke-width="2"/>',f'<path d="M36 86H{cw-90}" stroke="{c}" stroke-width="1"/>',f'<path d="M53 102H145M53 115H112M53 128H136" stroke="{c}" stroke-width="3" opacity=".6"/>',f'<rect x="{cw-126}" y="83" width="56" height="78" rx="7" fill="{panel}" stroke="{c}" stroke-width="2"/>',f'<path d="M{cw-107} 149H{cw-88}" stroke="{c}" stroke-width="2"/>']
        out += [f'<text x="22" y="202" fill="{fg}" font-family="Arial, Helvetica, sans-serif" font-weight="700" font-size="{29 if mobile else 28}">{escape(title)}</text>']
        for j,s in enumerate(copy):
            out += [f'<text x="22" y="{238+j*29}" fill="{muted}" font-family="Arial, Helvetica, sans-serif" font-size="{25 if mobile else 23}">{escape(s)}</text>']
        out += ['</g>']
    out += ['</svg>']
    return '\n'.join(out)+'\n'

def main():
    for theme in ['dark','light']:
        for mobile in [False,True]:
            name = f'capabilities-{"mobile-" if mobile else ""}{theme}.svg'
            (ROOT/'assets'/name).write_text(make(theme,mobile))

if __name__ == '__main__':
    main()
