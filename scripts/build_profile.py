"""Regenerate the GitHub profile artwork with Python 3; no dependencies."""
from build_hero import main as build_hero
from build_stack import main as build_stack
from build_capabilities import main as build_capabilities
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)

def combine_themes(stem):
    """Keep viewport selection outside GitHub's theme-query rewriting.

    Embedded SVG color-scheme inherits from its GitHub image element. Separate
    image files still provide the correct aspect ratio at mobile width.
    """
    source = ET.parse(ROOT/'assets'/f'{stem}-dark.svg').getroot()
    result = ET.Element(f'{{{NS}}}svg', {
        'width': source.attrib['width'], 'height': source.attrib['height'],
        'viewBox': source.attrib['viewBox'], 'role': 'img',
        'aria-labelledby': 'profile-title profile-desc',
    })
    for tag, ident in [('title','profile-title'), ('desc','profile-desc')]:
        el = ET.SubElement(result, f'{{{NS}}}{tag}', {'id': ident})
        el.text = source.find(f'{{{NS}}}{tag}').text
    css = ET.SubElement(result, f'{{{NS}}}style')
    css.text = '.profile-light{display:none}.profile-dark{display:inline}@media(prefers-color-scheme:light){.profile-light{display:inline}.profile-dark{display:none}}'
    for theme in ['dark', 'light']:
        raw = (ROOT/'assets'/f'{stem}-{theme}.svg').read_text()
        tree = ET.fromstring(raw)
        for ident in sorted({e.attrib['id'] for e in tree.iter() if 'id' in e.attrib}, key=len, reverse=True):
            raw = raw.replace(f'id="{ident}"', f'id="{theme}-{ident}"')
            raw = raw.replace(f'url(#{ident})', f'url(#{theme}-{ident})')
        tree = ET.fromstring(raw)
        group = ET.SubElement(result, f'{{{NS}}}g', {'class': f'profile-{theme}'})
        if 'fill' in tree.attrib:
            group.set('fill', tree.attrib['fill'])
        for child in tree:
            if child.tag not in [f'{{{NS}}}title', f'{{{NS}}}desc']:
                group.append(child)
    ET.ElementTree(result).write(ROOT/'assets'/f'{stem}.svg', encoding='unicode')

def make_static(stem):
    """Remove animation targets for browsers that do not pass motion into SVGs."""
    tree = ET.parse(ROOT/'assets'/f'{stem}.svg')
    for node in tree.iter():
        classes = node.get('class', '').split()
        if any(c in classes for c in ['signal', 'node-pulse']):
            node.set('class', ' '.join(c for c in classes if c not in ['signal','delayed','node-pulse']))
    tree.write(ROOT/'assets'/f'{stem}-static.svg', encoding='unicode')

if __name__ == '__main__':
    build_hero()
    build_stack()
    build_capabilities()
    for stem in ['hero', 'capabilities', 'stack']:
        combine_themes(stem)
        combine_themes(stem+'-mobile')
    make_static('hero')
    make_static('hero-mobile')
    print('Generated desktop and mobile profile artwork in assets/.')
