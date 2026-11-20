# Viewer Specification

The template's viewer is part of the deliverable. Keep these behaviors when replacing slide content.

## 1. Structure

```html
<div class="stage">
  <div class="frame" id="p12" data-page="12 / 19">
    <section class="slide">…</section>
  </div>
  <!-- one frame per page -->
</div>

<div class="deck-ui">prev / next / overview / fullscreen / dots / counter</div>
<aside class="rail">…generated from slide DOM…</aside>
<div class="preview">…generated enlarged slide…</div>
```

- Base slide: 1280×720, absolute inside `.frame`.
- Scale: `min((vw - mx) / 1280, (vh - my) / 720)`. `mx` is 150 px normally, +160 px when the rail is visible; `my` is 100 px.
- `.frame.active` is the only visible page in deck mode.

## 2. Pagination

| Input | Behavior |
| --- | --- |
| Click on slide / stage | Next page |
| Wheel down / up | Next / previous, 520 ms lock |
| `→ ↓ Space PageDown` | Next |
| `← ↑ PageUp` | Previous |
| `Home` / `End` | First / last |
| Touch swipe | Horizontal, threshold 50 px |
| Prev/next buttons | Step one page |
| Dots | Jump to page |

Rules:

- Ignore clicks for 450 ms after a touch swipe.
- Ignore wheel events when `overview` is on, when `ctrlKey` is held, or when the target is inside `.rail`, `.preview`, or `.deck-ui`.
- At the first/last page, clamp instead of wrapping.

## 3. Thumbnail rail

- Fixed left, 160 px wide, one column, visible only in windowed mode (`body.rail-on`).
- Hidden in fullscreen, overview, print, and viewports < 980 px.
- Each thumb is a **clone of the real slide**, scaled to 136 px wide (`scale(.10625)`); remove `id` attributes and inline transforms from clones.
- Current page: `border-color: gold`, full opacity, 2 px left accent bar.
- Inactive: 60% opacity.
- Reserve 160 px of stage padding and subtract 160 px from fit width. Never let the rail cover the slide.

## 4. Hover preview

- On thumb `mouseenter`, show a fixed 472×265.5 px preview at `left:172px`.
- Preview slides are cached clones (one per page); toggle `.on`, never re-clone on every hover.
- Vertical position = thumb center, clamped to 16 px viewport margins.
- Preview is `pointer-events:none`; it disappears on `mouseleave`.
- Update the caption from `data-page`.

## 5. Overview

- `O` or the grid button toggles `body.overview`.
- All frames become visible in a flex-wrap grid; 3 columns ≥1100 px, 2 ≥640 px, otherwise 1.
- Compute thumbnails from both width and height so 2 rows fit on desktop.
- Clicking a thumbnail jumps to that page, stops propagation, and exits overview.
- `O` / `Esc` exits overview to the current page.
- Hide rail, arrows, dots, counter; show an overview hint.
- Wheel scrolls the overview; it must not flip pages.

## 6. Fullscreen / presenter mode

- `F` or the button calls `requestFullscreen()`.
- Fullscreen hides the rail, preview, and deck chrome through CSS, and fit math must stop reserving 160 px.
- Listen to `fullscreenchange` and refit.

## 7. Print / PDF

```css
@page { size: 13.333in 7.5in; margin: 0; }
@media print {
  body { overflow: visible; height: auto; display: block; }
  .frame { display: block !important; width: 1280px !important; height: 720px !important;
           page-break-after: always; animation: none !important; transform: none !important; }
  .slide { transform: none !important; box-shadow: none; }
  .deck-ui, .rail, .preview { display: none !important; }
}
```

If `body.overview` is active when printing, override overview layout back to the print layout.

## 8. Performance

- Fade only: `opacity 0 → 1`, ≤ 0.2 s.
- No `backdrop-filter`; use opaque translucent panels.
- Keep shadows small; avoid filter/mask animations.
- Only the active frame is displayed.
- Thumbnails and previews are cached DOM clones, not screenshots or iframes.
- Honor `prefers-reduced-motion: reduce` by disabling the fade and control transitions.

## 9. Acceptance checklist

- [ ] Only one page visible in windowed mode
- [ ] Click / wheel / keyboard / touch / arrows / dots all navigate
- [ ] Wheel over rail or controls does not flip pages
- [ ] Rail thumbnails match slides; current page highlighted
- [ ] Hover preview enlarges the hovered page
- [ ] Clicking a thumbnail jumps to it without double-advancing
- [ ] Overview opens, jumps, and exits
- [ ] Fullscreen hides chrome and rail
- [ ] No clipped text at 720 px
- [ ] Print produces one 16:9 page per slide
- [ ] No page scrollbars in deck mode
- [ ] < 980 px viewport hides the rail and still fits the slide
