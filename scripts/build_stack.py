#!/usr/bin/env python3
"""Build self-contained, responsive engineering-stack illustrations."""

from html import escape
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
MODULES = [
    ("LANGUAGES", ["Core code"], "cyan", [
        ("Py", ["Python"]), ("TS", ["TypeScript"]),
        ("JS", ["JavaScript"]), ("SQL", ["SQL"]), ("C++", ["C++"]),
    ]),
    ("AI + AGENT TOOLS", ["Tool-using", "workflows"], "violet", [
        ("OA", ["OpenAI", "Agents SDK"]), ("CA", ["Claude", "Agent SDK"]),
        ("LG", ["LangGraph"]), ("LC", ["LangChain"]), ("MCP", ["MCP"]),
        ("CX", ["Codex"]), ("CC", ["Claude Code"]),
    ]),
    ("WEB + MOBILE", ["Product", "interfaces"], "cyan", [
        ("Re", ["React"]), ("Nx", ["Next.js"]), ("Nd", ["Node.js"]),
        ("RN", ["React Native"]), ("Ex", ["Expo"]), ("API", ["REST APIs"]),
    ]),
    ("SYSTEMS + DATA", ["Runtime &", "persistence"], "amber", [
        ("Dk", ["Docker"]), ("Lx", ["Linux"]), ("Gt", ["Git"]),
        ("GA", ["GitHub", "Actions"]), ("Sq", ["SQLite"]),
        ("Pg", ["PostgreSQL"]),
    ]),
    ("TEST + AUTOMATE", ["Quality", "engineering"], "violet", [
        ("Py", ["pytest"]), ("Pw", ["Playwright"]), ("CI", ["CI/CD"]),
        ("AST", ["AST codemods"]), ("Rt", ["Regression", "testing"]),
    ]),
]

PALETTES = {
    "dark": dict(bg="#070d18", panel="#0d1728", tile="#111f34", ink="#edf5ff",
                 muted="#a8b9ce", border="#293b54", grid="#183047",
                 cyan="#5ce1ff", violet="#a78bfa", amber="#ffce73"),
    "light": dict(bg="#f6f9ff", panel="#ffffff", tile="#edf3fc", ink="#152841",
                  muted="#526984", border="#cfdaea", grid="#d8e5f3",
                  cyan="#006c9f", violet="#7251b2", amber="#926000"),
}

# Local, commit-pinned Simple Icons artwork; see assets/icons/NOTICE.md.
# SDK/tool labels without an unambiguous project icon retain original monograms.
ICON_FILES = {
    "Python": "python", "TypeScript": "typescript", "JavaScript": "javascript",
    "C++": "cplusplus", "React": "react", "React Native": "react",
    "Next.js": "nextdotjs", "Node.js": "nodedotjs", "Expo": "expo",
    "Docker": "docker", "Linux": "linux", "Git": "git",
    "GitHub Actions": "githubactions", "SQLite": "sqlite",
    "PostgreSQL": "postgresql", "pytest": "pytest", "Playwright": "playwright",
}


def logo_paths(name):
    """Only embed SVG path geometry, never external links or active content."""
    filename = ICON_FILES.get(name)
    if not filename:
        return None
    path = ROOT / "assets" / "icons" / f"{filename}.svg"
    if not path.exists():
        return None
    root = ElementTree.parse(path).getroot()
    assert root.attrib.get("viewBox") == "0 0 24 24", path
    shapes = root.findall("{http://www.w3.org/2000/svg}path")
    if not shapes:
        return None
    return "".join(f'<path d="{escape(shape.attrib["d"], quote=True)}"/>' for shape in shapes)


def txt(x, y, value, size, fill, weight=400, extra=""):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" {extra}>{escape(value)}</text>')


def rect(x, y, width, height, radius, fill, stroke=None, extra=""):
    stroke_attr = f' stroke="{stroke}"' if stroke else ""
    return (f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
            f'rx="{radius}" fill="{fill}"{stroke_attr} {extra}/>')


def tile(x, y, width, height, glyph, names, accent, p, mobile):
    out = [rect(x, y, width, height, 9, p["tile"], p["border"])]
    glyph_size = 34 if mobile else 32
    gy = y + (height - glyph_size) / 2
    gx = x + 12
    out.append(rect(gx, gy, glyph_size, glyph_size, 7, accent, extra='fill-opacity="0.13"'))
    paths = logo_paths(" ".join(names))
    if paths:
        inset = (glyph_size - 24) / 2
        out.append(f'<g transform="translate({gx+inset} {gy+inset})" fill="{accent}">{paths}</g>')
    else:
        out.append(txt(gx + glyph_size / 2, gy + glyph_size / 2 + 6,
                       glyph, 15 if len(glyph) > 2 else 18, accent, 700,
                       'text-anchor="middle" font-family="ui-monospace, SFMono-Regular, Consolas, monospace"'))
    font_size = 25 if mobile else 24
    tx = gx + glyph_size + 10
    if len(names) == 1:
        out.append(txt(tx, y + height / 2 + 8, names[0], font_size, p["ink"], 500))
    else:
        out.append(txt(tx, y + height / 2 - 5, names[0], font_size, p["ink"], 500))
        out.append(txt(tx, y + height / 2 + 22, names[1], font_size, p["ink"], 500))
    return "".join(out)


def build(theme, mobile=False):
    p = PALETTES[theme]
    width = 600 if mobile else 1200
    tile_height = 78 if mobile else 60
    columns = 2 if mobile else 3
    gap = 10 if mobile else 8
    top = 122 if mobile else 98
    module_gap = 18 if mobile else 12
    heights = []
    for _, _, _, skills in MODULES:
        rows = (len(skills) + columns - 1) // columns
        heights.append((86 if mobile else 20) + rows * tile_height + (rows - 1) * gap)
    height = top + sum(heights) + module_gap * (len(MODULES) - 1) + 38
    desc = "; ".join(f"{name}: {', '.join(' '.join(lines) for _, lines in skills)}"
                     for name, _, _, skills in MODULES)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
           f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="stack-title stack-desc">',
           '<title id="stack-title">Abhishek Pundir — engineering stack</title>',
           f'<desc id="stack-desc">{escape(desc)}</desc>',
           '<defs><pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">'
           f'<path d="M 30 0 L 0 0 0 30" fill="none" stroke="{p["grid"]}" stroke-width="0.65"/>'
           '</pattern></defs>',
           '<g font-family="Arial, Helvetica, sans-serif">',
           rect(0, 0, width, height, 18, p["bg"]),
           rect(0, 0, width, height, 18, 'url(#grid)', extra='opacity="0.34"')]

    if mobile:
        out.append(txt(28, 43, "ENGINEERING STACK", 32, p["ink"], 700, 'letter-spacing="0.5"'))
        out.append(txt(29, 82, "BUILD  /  TEST  /  SHIP", 21, p["muted"], 600,
                       'font-family="ui-monospace, SFMono-Regular, Consolas, monospace" letter-spacing="1.5"'))
        out.append(f'<path d="M 29 101 H 569" stroke="{p["border"]}"/>')
        out.append(f'<path d="M 29 101 H 112" stroke="{p["cyan"]}" stroke-width="3"/>')
    else:
        out.append(txt(38, 55, "ENGINEERING STACK", 33, p["ink"], 700, 'letter-spacing="1"'))
        out.append(txt(1159, 52, "BUILD  /  TEST  /  SHIP", 21, p["muted"], 600,
                       'text-anchor="end" font-family="ui-monospace, SFMono-Regular, Consolas, monospace" letter-spacing="2"'))
        out.append(f'<path d="M 38 75 H 1162" stroke="{p["border"]}"/>')
        out.append(f'<path d="M 38 75 H 169" stroke="{p["cyan"]}" stroke-width="3"/>')
        out.append(f'<path d="M 21 {top+24} V {height-56}" stroke="{p["border"]}" stroke-width="2"/>')

    y = top
    for idx, ((name, descriptor, color, skills), module_height) in enumerate(zip(MODULES, heights), 1):
        accent = p[color]
        if mobile:
            x, panel_width = 20, 560
            out.append(rect(x, y, panel_width, module_height, 14, p["panel"], p["border"]))
            out.append(f'<path d="M 37 {y+17} V {y+56}" stroke="{accent}" stroke-width="3" stroke-linecap="round"/>')
            out.append(txt(50, y+31, f"0{idx}", 17, accent, 700,
                           'font-family="ui-monospace, SFMono-Regular, Consolas, monospace"'))
            out.append(txt(85, y+32, name, 22, p["ink"], 700, 'letter-spacing="0.4"'))
            out.append(txt(50, y+60, " ".join(descriptor), 23, p["muted"], 400))
            tx, ty, tw = 32, y + 74, 263
        else:
            x, panel_width = 38, 1124
            out.append(rect(x, y, panel_width, module_height, 13, p["panel"], p["border"]))
            out.append(f'<path d="M 21 {y+24} H 38" stroke="{accent}" stroke-width="2"/>')
            out.append(f'<circle cx="21" cy="{y+24}" r="4.5" fill="{p["bg"]}" stroke="{accent}" stroke-width="2"/>')
            out.append(f'<path d="M 53 {y+20} V {y+module_height-20}" stroke="{accent}" stroke-width="3" stroke-linecap="round"/>')
            out.append(txt(69, y+33, f"0{idx}", 16, accent, 700,
                           'font-family="ui-monospace, SFMono-Regular, Consolas, monospace" letter-spacing="1"'))
            out.append(txt(105, y+33, name, 19, p["ink"], 700, 'letter-spacing="0.4"'))
            for line_idx, line in enumerate(descriptor):
                out.append(txt(69, y+74+line_idx*28, line, 24, p["muted"], 400))
            out.append(f'<path d="M 307 {y+15} V {y+module_height-15}" stroke="{p["border"]}"/>')
            tx, ty, tw = 321, y + 10, 271
        for number, (glyph, names) in enumerate(skills):
            row, col = divmod(number, columns)
            out.append(tile(tx + col*(tw+gap), ty + row*(tile_height+gap),
                            tw, tile_height, glyph, names, accent, p, mobile))
        y += module_height + module_gap

    out.append(f'<path d="M {28 if mobile else 38} {height-17} H {width-28 if mobile else width-38}" stroke="{p["border"]}"/>')
    for i, key in enumerate(["cyan", "violet", "amber"]):
        out.append(rect(width-71+i*13, height-21, 7, 7, 1.5, p[key]))
    out.append('</g></svg>')
    return "\n".join(out)


def main():
    for theme in PALETTES:
        for mobile in (False, True):
            suffix = f"mobile-{theme}" if mobile else theme
            path = ROOT / "assets" / f"stack-{suffix}.svg"
            path.write_text(build(theme, mobile), encoding="utf-8")
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
