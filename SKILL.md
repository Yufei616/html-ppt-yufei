---
name: html-ppt-yufei
description: Use when building a 16:9 HTML presentation from any source — selected PPT/PPTX pages, a PPT template or brand kit, an outline, notes, screenshots, or pasted content. The focus is presentation craft — narrative, theme, layout rhythm, and a self-contained viewer with thumbnail rail, overview, presenter mode, and PDF export — not PPT data conversion. Triggers include "HTML PPT", "网页版 PPT", "HTML 幻灯片", "PPT 模板", "大纲做成 PPT", "outline to slides", "重新设计版式", "缩略图侧栏", "演讲者模式".
---

# HTML PPT — Presentation First

Build the **presentation**, not a PPT converter. The output is always a single-file 16:9 HTML deck with a polished viewer; the input may be a PPT, a template, an outline, notes, or raw content. Extraction is an optional helper, never the center of the work.

The viewer shell in `assets/deck-template.html` is part of the deliverable — never regress its navigation, thumbnail rail, overview, presenter mode, or print behavior.

## Input modes

| Input | Content | Theme |
| --- | --- | --- |
| PPTX, whole deck or selected pages | Extract text with `scripts/extract_pptx.py`; confirm the Markdown | Extract colors/fonts from theme + slides |
| PPT template / brand kit | Author content to fit the template's story | Extract the template's theme; keep its identity |
| Outline / notes / Markdown | Structure into a narrative first; confirm the outline | Propose 2–3 palettes, or use the user's brand |
| Screenshots / existing HTML / PDF | Reconstruct the content; do not copy the layout | Derive from the source or propose |
| Just a topic | Draft an outline, confirm, then build | Propose |

Ask only for what is missing. Do not block on a PPTX when the user already gave an outline.

## Workflow

1. **Clarify the frame.** Content source, audience, page count, language, and whether a theme/brand exists. If the user already supplied these, proceed without re-asking.
2. **Get the content.**
   - PPTX: `python scripts/extract_pptx.py deck.pptx --pages 12-17 --out content.md`, then confirm titles, body copy, quotes, footers, and page numbers.
   - Outline/notes: turn it into a slide-by-slide outline (title + one key message per page) and confirm it.
   - Vague idea: draft the narrative structure first; do not jump into layout.
3. **Decide the theme source.**
   - Template/brand provided: extract and reuse it.
   - Source deck has a strong identity: reuse its tokens.
   - No theme: propose a restrained palette and type pairing; pick one default rather than asking a dozen questions.
4. **Plan the rhythm.** Assign a different composition to each page before writing HTML. Use the layout recipes below; never mirror the source deck's grids.
5. **Build.** Copy `assets/deck-template.html`, replace the `<section class="slide">` bodies, keep the viewer CSS + script intact. Update `data-page` and footer numbers when the count changes; the counter adapts automatically. Thumbnails are generated from the DOM — no screenshots.
6. **Verify.** Walk the checklist in `references/viewer-spec.md`: single-page display, click/wheel/keyboard/touch, rail hover preview, overview, fullscreen, print PDF, no overflow.
7. **Deliver.** Give the HTML path, page count, and controls. Deliver the title+content Markdown when content was extracted or outlined.

## Presentation craft

The deck is judged on how it presents, not on how faithfully it reproduces a source file.

- One idea per page; the title should state the takeaway, not a category.
- Build a narrative arc: context → tension → solution → proof → next step. See `references/presentation-craft.md`.
- Vary density: a hero statement, a diagram, a comparison, a data page, a quiet quote.
- Vary composition: at least 4 layout types in a 6–10 page deck.
- Prefer diagrams, timelines, big numbers, and annotated mockups over bullet walls.
- Body copy 11–13 px at 1280×720; if it needs 9 px, the slide is doing too much.
- Dark full-bleed pages are a rhythm tool — roughly ⅓ of pages or fewer.
- Keep one accent color for emphasis; everything else is ink and muted neutrals.

## Hard rules

- 16:9, **one slide per HTML page**, 1280×720 base, scaled to fit the window.
- Single HTML file, offline, system font stack, no CDN.
- If content was extracted: preserve facts, numbers, quotes, and attribution.
- If content was authored from an outline: you may write connective copy, but mark any invented example metrics as `示意` / `UI Preview`.
- If a template/brand is provided: keep its colors and type identity.
- **Never mirror the source layout.** The source's 2×2 cards / three columns are not a design.
- One visual focus per page; clipped text is a failure.
- Dark pages are not the default.
- Sanitize company names and internal data before putting a demo in a public repo.

## Theme tokens

Define once in `:root`, whatever the source:

```css
--bg:#FAFAF7;      /* page background */
--panel:#F5F1E8;   /* light panel */
--ink:#1A1A1A;     /* primary text */
--muted:#6B6B6B;   /* secondary text */
--line:#E5E0D4;    /* hairlines */
--gold:#B8924C;    /* accent */
```

Use a serif (Georgia) for large numerals and an editorial sans for Chinese copy. See `references/design-system.md` for extraction methods, spacing, type scale, and layout recipes.

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

Details and math: `references/viewer-spec.md`.

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
| Template showcase | Follow the template's composition rules, but keep the page rhythm varied |

Five or six different recipes per deck is normal. Repeat only for an intentional series.

## Common mistakes

| Mistake | Fix |
| --- | --- |
| Treating every request as "extract PPT pages" | Identify the input mode first; outline and template jobs are first-class |
| Blocking because there is no PPTX | If there is an outline, build from the outline |
| Chasing extraction fidelity and forgetting the presentation | Spend the effort on hierarchy, pacing, and layout |
| Rebuilding the PPT's own grid | Choose a new composition per page first |
| Theme colors eyeballed | Extract `srgbClr` values when a source/template exists |
| Text clipped at 720 px | Budget header/body/footer heights before writing |
| Rail overlays slide | Reserve 160 px left padding and subtract it in the fit math |
| Wheel over the rail flips pages | Ignore wheel events inside `.rail`, `.preview`, `.deck-ui` |
| Overview click advances twice | Stop propagation on thumbnail clicks |
| Animating a full-screen blur | Use a short opacity fade only |
| Print includes controls | Force all frames visible, hide `.deck-ui`, `.rail`, `.preview` |

## Files

```
html-ppt-yufei/
├── SKILL.md
├── assets/deck-template.html      # working 6-page deck; copy and rewrite slide bodies
├── references/design-system.md    # theme extraction, type, spacing, layout recipes
├── references/presentation-craft.md # narrative, pacing, slide roles
├── references/viewer-spec.md      # interaction + print + performance spec
├── scripts/extract_pptx.py        # optional: PPTX → title/content Markdown
├── examples/demo-content.md       # one input mode: extracted PPT content
└── docs/requirements.md           # original design brief
```

Read the references before building. Start from the template; do not rebuild the viewer from scratch.
