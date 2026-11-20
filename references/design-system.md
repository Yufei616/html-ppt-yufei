# Design System & Layout Recipes

## 1. Theme source of truth

Choose one, in this order:

1. **Brand / PPT template provided** — reuse its colors and type identity. Do not substitute your own palette.
2. **A visual reference is provided** — sample the palette and type from the reference; ask for exact brand hex values when fidelity matters.
3. **Outline / notes / topic only** — propose a restrained palette (below) and pick one; don't interrogate the user.

When a brand kit exists, ask for its hex tokens once and record them at the top of the deck. Do not eyeball colors from a compressed screenshot.

### No theme? Pick a default

| Mood | Background | Ink | Accent | Secondary |
| --- | --- | --- | --- | --- |
| Editorial / warm | `#FAFAF7` | `#1A1A1A` | `#B8924C` | `#6B6B6B` |
| Corporate / cool | `#F7F8FA` | `#1F2937` | `#2563EB` | `#6B7280` |
| Technical / dark | `#0E1A2B` | `#F5F1E8` | `#36DD9F` | `#93A3B5` |

Use one accent plus neutrals. Do not mix warm and cool accents.

## 2. Tokens

```css
:root{
  --bg:#FAFAF7;
  --panel:#F5F1E8;
  --line:#E5E0D4;
  --ink:#1A1A1A;
  --muted:#6B6B6B;
  --gold:#B8924C;
  --gold-soft:#D8C29A;
  --dark:#0F172A;
  --serif:Georgia,"Times New Roman","Songti SC",serif;
  --sans:"Helvetica Neue","Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;
}
```

Never introduce a second accent hue. If no brand accent exists, use the accent from the default palette above.

## 3. Type scale (1280×720)

| Role | Size | Notes |
| --- | --- | --- |
| Kicker / eyebrow | 9–10 px | uppercase, `letter-spacing:.2em`, accent color |
| Page title | 32–36 px | 600 weight, 1.2 line-height |
| Lead | 13–14 px | muted, 1.6 line-height |
| Section head | 16–18 px | `01` index in accent |
| Body | 11–13 px | 1.6–1.7 line-height |
| Pull quote | 44–52 px | 600, 1.2; one idea only |
| Hero numeral | 110–150 px | serif, accent, `letter-spacing:-.02em` |
| Footer | 8–9 px | uppercase, muted |

Chinese titles benefit from `letter-spacing:.01em`; avoid faux italics on CJK.

## 4. Page chrome

- Margins: 72 px left/right, 44 px top, footer at 28 px from bottom.
- Kicker top-left; chapter marker top-right (`01 — THE PAIN`).
- Footer: brand + `12 / 19`, 9 px, uppercase, letter-spaced.
- Hairlines: 1 px `--line`; accent rules 1–2 px `--gold`.
- Generous whitespace is the style. Do not fill every corner.

## 5. Layout recipes

### Pain page
- Left 40%: quote mark, 2-line pull quote, one supporting note, tool chips.
- Right 60%: 4-row ledger, 1 px top borders, accent index numbers.
- Footer quote optional.

### Workflow / journey (dark)
- Full-bleed dark background with a faint 48 px grid.
- Horizontal axis at y≈440; 5 nodes at x≈150/385/620/855/1090.
- Cards alternate above/below; 1 px colored left border per role.
- Gate labels (`SPEC / GO / USE`) sit above the axis between nodes.
- Dashed coral feedback loop at y≈648.

### Product solution (bento)
- Row 1: 660×292 product mock (window chrome, 3 stats, bars + milestones) + 452 px feature ledger.
- Row 2: 660×172 two comparison cards + 452×172 2×2 roadmap.
- Mock data must say `UI Preview · 示意界面`.

### Chaotic files
- Left: 5 tilted file cards (298 px wide, rotations −6°…+5°) + large ghost `?` + red `5×` stamp.
- Right: 3 rows, 44 px outlined serif numerals, 24 px headings.
- Bottom: full-width dark root-cause strip.

### Pipeline
- Five outlined serif numerals above a 2 px accent rail.
- Captions below the rail; dots at each column center.
- Bottom: dark 6-column capability base with hairline separators.

### KPI
- Left 462×440 dark hero card: one hero number (serif, accent), label, comparison bars.
- Right: 3 rows × 146 px, big number + label + description + small visualization (bar / blocks / ring).
- Source line at y≈622.

### Comparison
- Two cards, identical internal structure; accent top border.
- Use bullets with accent dots; never a plain table.

## 6. Dark page contrasts

Use the dark page to break rhythm every 3–4 light pages. Keep:

- text `#F5F1E8`, secondary `#93A3B5`
- hairlines `rgba(255,255,255,.08)`
- nodes tinted with source accent colors
- one warm accent (gold) for gates and legends

Do not use frosted glass or blurred cards.

## 7. Finishing details

- Align all left edges to the 72 px margin.
- Use one accent per page for emphasis; everything else is ink/muted.
- Add hover only to interactive or list elements; transitions ≤ 0.25 s.
- Use `tabular-nums` for all numbers.
- No emoji icons. Use type, rules, numerals, and simple CSS shapes.
