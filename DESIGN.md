# The profile as an engineering artifact

This profile combines a visual introduction with the detail needed to understand my skills and work. The layout and diagrams are original, generated with Python's standard library, and stored alongside the content. Selected technology symbols come from Simple Icons; [source, licenses, and attribution](assets/icons/NOTICE.md) are retained locally.

## Design

- **Identity:** an engineering console illustrates the relationship between agents, tool calls, traces, differences, and verification. It is an illustrative process, not a live service monitor.
- **Capabilities:** three small diagrams represent AI evaluation, developer tooling, and product engineering.
- **Stack:** named tools are grouped by their role in a system. There are no invented proficiency scores or language percentages presented as skill ratings.
- **Depth:** ordinary Markdown preserves selectable text, working links, project evidence, and expandable background information.

## Build

```sh
python3 scripts/build_profile.py
```

Edit the corresponding generator for hero, capabilities, or stack artwork, then regenerate the SVGs. Edit `README.md` for the profile's text, links, and background. Generated SVGs require no network requests, external fonts, scripts, or remote widgets.

Every dense panel has a desktop and mobile composition in light and dark themes. The builder combines both palettes into each final SVG. A viewport-only `<picture>` selects the composition, and the SVG inherits GitHub's color scheme. This avoids GitHub's theme handler rewriting compound theme/viewport source queries. The hero keeps essential information visible and supplies dedicated still variants under `prefers-reduced-motion: reduce`, in addition to its internal CSS safeguard.

## Research references

These implementations informed the approach; their artwork and profile text were not copied:

- [DenverCoder1](https://github.com/DenverCoder1/DenverCoder1): organize substantial technical breadth into clear groups.
- [Andrew6rant](https://github.com/Andrew6rant/Andrew6rant): maintain a coherent engineering-console theme.
- [aw-snap/live-readme](https://github.com/aw-snap/live-readme): make the implementation of a profile part of the engineering story.
- [Platane/snk](https://github.com/Platane/snk): generate self-contained animated SVG artifacts.
- [GitHub theme-aware images](https://github.blog/developer-skills/github/how-to-make-your-images-in-markdown-on-github-adjust-for-dark-mode-and-light-mode/): use supported picture/source markup.
- [MDN: SVG as an image](https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/SVG_as_an_image): design within image rendering restrictions.
