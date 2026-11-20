---
name: html-ppt-editorial
description: Use when turning an existing PPT/PPTX or outline into a redesigned 16:9 HTML slide deck — preserving the source theme colors and content while rebuilding layouts, with a left thumbnail rail, hover preview, click/wheel navigation, overview mode, presenter fullscreen, and print-to-PDF. Triggers include "HTML PPT", "网页版 PPT", "HTML 幻灯片", "重新设计版式", "缩略图侧栏", "演讲者模式", "HTML deck", "slides to HTML".
---

# HTML PPT Editorial

Turn source slides into an editorial-style HTML deck: **keep the theme and content, rebuild the layout**. The viewer shell in `assets/deck-template.html` is part of the deliverable — never regress its navigation, thumbnail rail, overview, or print behavior.

## Workflow

1. **Extract.** Run `python scripts/extract_pptx.py deck.pptx --pages 12-17 --out content.md`. Read the output and confirm slide titles, body copy, quotes, footers, and page numbers.
2. **Extract the theme.** Read `ppt/theme/theme1.xml` and count `srgbClr` values in the target slides. Do not guess brand colors. See `references/design-system.md`.
3. **Choose a layout rhythm.** Plan a different composition for each page before writing HTML. Use the pattern table below; do not reuse the source PPT's grid.
4. **Build.** Copy `assets/deck-template.html`, replace the `<section class="slide">` bodies (the template ships with six), keep the viewer CSS + script intact. Update each frame's `data-page` and the footer page numbers when the count changes; the viewer's total/counter adapts automatically. Regenerate thumbnails from the slide DOM — no screenshots needed.
5. **Verify.** Walk the checklist in `references/viewer-spec.md`: single-page display, click/wheel/keyboard/touch, rail hover preview, overview, fullscreen, print PDF, no overflow.
6. **Deliver.** Give the HTML path, page count, and controls. If asked, also deliver the title+content Markdown.

## Hard rules

- 16:9, **one PPT page = one HTML slide**, 1280×720 base, scaled to fit the window.
- Single HTML file, offline, system font stack, no CDN.
- Preserve source colors and text; never invent facts, numbers, or conclusions.
- **Never mirror the source layout.** The source's 2×2 cards / three columns are not a design.
- One visual focus per page. Vary page types across the deck.
- Mark mock UI data as `示意` / `UI Preview`.
- Keep every slide's content inside 1280×720; clipped text is a failure.
- Dark full-bleed pages are a rhythm tool, not the default — keep them to roughly ⅓ of pages or fewer.

## Theme tokens

Extract per deck, then define them once in `:root`:

```css
--bg:#FAFAF7;      /* page background */
--panel:#F5F1E8;   /* light panel */
--ink:#1A1A1A;     /* primary text */
--muted:#6B6B6B;   /* secondary text */
--line:#E5E0D4;    /* hairlines */
--gold:#B8924C;    /* accent */
```

Use a serif (Georgia) for large numerals and an editorial sans for Chinese copy. See `references/design-system.md` for spacing, type scale, and six layout recipes.

## Viewer contract — do not regress

| Feature | Required behavior |
| --- | --- |
| Display | One slide at a time; no vertical stack; centered and scaled |
| Pagination | Click anywhere → next; wheel down/up → next/prev with a ~520 ms lock; keyboard arrows/space/PageUp/PageDown/Home/End; touch swipe |
| Controls | Round prev/next buttons, dots + `01 / 06`, fullscreen (`F`), overview (`O`) |
| Thumbnail rail | Left, one column, only in windowed (non-presenter) mode; real rendered miniatures; current page highlighted; hover shows a larger preview to the right; click jumps |
| Overview | Grid of all pages (3/2/1 columns by viewport), click to open, `O` / `Esc` to leave; wheel scrolls the grid, never flips pages |
| Presenter mode | Fullscreen hides the rail, preview, and deck chrome; `Esc`/browser exits |
| Print | `13.333in × 7.5in` pages, one slide per page, all slides visible, chrome hidden, transforms reset |
| Performance | ≤ 0.2 s fade only; no `backdrop-filter` blur; no large moving shadows; honor `prefers-reduced-motion` |

Implementation details, dimensions, and math are in `references/viewer-spec.md`.

## Layout recipes

| Page intent | Composition |
| --- | --- |
| Pain / problem | Massive pull quote + numbered ledger; tools as small chips |
| Workflow | Dark full-bleed journey map; alternating nodes above/below an axis; gate labels; dashed feedback loop |
| Product solution | Bento grid: product mock in a window frame + feature ledger + two comparison cards + roadmap cells |
| Chaotic source material | Tilted file-card collage + oversized outlined numerals |
| Pipeline | Five-step rail with outlined numerals + dark capability base |
| KPI / impact | Hero number card (dark) + bars/blocks/ring for supporting metrics |
| Comparison | Side-by-side cards, never a plain table |

Five or six different recipes per deck is normal. Repeat only when consecutive pages are intentionally a series.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| Rebuilding the PPT's own grid | Choose a new composition per page first |
| Theme colors eyeballed | Extract `srgbClr` values from theme/slides |
| Text clipped at 720 px | Budget header/body/footer heights before writing |
| Rail overlays slide | Reserve 160 px left padding and subtract it in the fit math |
| Wheel over the rail flips pages | Ignore wheel events inside `.rail`, `.preview`, `.deck-ui` |
| Overview click advances twice | Stop propagation on thumbnail clicks |
| Animating a full-screen blur | Use a short opacity fade only |
| Print includes controls | Force all frames visible, hide `.deck-ui`, `.rail`, `.preview` |
| Copying company content into a public repo | Sanitize names, sources, and internal data first |

## Files

```
html-ppt-editorial/
├── SKILL.md
├── assets/deck-template.html   # working 6-page deck; copy and rewrite slide bodies
├── references/design-system.md # colors, type, spacing, layout recipes
├── references/viewer-spec.md   # interaction + print + performance spec
├── scripts/extract_pptx.py     # PPTX → title/content Markdown
├── examples/demo-content.md    # sample extracted content
└── docs/requirements.md        # original design brief
```

Read both references before building. Start from the template; do not rebuild the viewer from scratch.
