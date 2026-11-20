#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Extract slide text from a PPTX into title + content Markdown.

Usage:
    python extract_pptx.py deck.pptx --pages 12-17 --out content.md
    python extract_pptx.py deck.pptx --pages 12,13,15
    python extract_pptx.py deck.pptx --pages all --include-notes

Requires: python-pptx
    pip install python-pptx
"""

import argparse
import io
import re
import sys

from pptx import Presentation


def parse_pages(spec, total):
    if not spec or spec.lower() == "all":
        return list(range(1, total + 1))

    pages = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = part.split("-", 1)
            start, end = int(start), int(end)
            if start > end:
                start, end = end, start
            pages.update(range(start, end + 1))
        else:
            pages.add(int(part))
    return sorted(p for p in pages if 1 <= p <= total)


def shape_text(shape):
    if not shape.has_text_frame:
        return ""
    lines = []
    for paragraph in shape.text_frame.paragraphs:
        text = "".join(run.text for run in paragraph.runs).strip()
        if not text:
            text = paragraph.text.strip()
        if text:
            lines.append(text)
    return "\n".join(lines)


def table_text(shape):
    rows = []
    for row in shape.table.rows:
        cells = [cell.text.strip().replace("\n", " / ") for cell in row.cells]
        rows.append(" | ".join(cells))
    if not rows:
        return ""
    header = rows[0]
    divider = " | ".join(["---"] * len(rows[0].split(" | ")))
    return "\n".join([header, divider] + rows[1:])


def ordered_shapes(slide):
    shapes = list(slide.shapes)

    def key(shape):
        return (
            shape.top if shape.top is not None else 0,
            shape.left if shape.left is not None else 0,
        )

    return sorted(shapes, key=key)


def extract_slide(slide, index, include_notes=False):
    out = ["## Slide %d" % index, ""]
    seen = set()

    for shape in ordered_shapes(slide):
        text = ""
        if shape.has_table:
            text = table_text(shape)
        else:
            text = shape_text(shape)

        if not text or text in seen:
            continue
        seen.add(text)
        out.append(text)
        out.append("")

    if include_notes and slide.has_notes_slide:
        notes = slide.notes_slide.notes_text_frame.text.strip()
        if notes:
            out.append("> Notes")
            out.extend("> " + line for line in notes.splitlines())
            out.append("")

    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description="Extract PPTX slides to Markdown.")
    parser.add_argument("pptx", help="path to .pptx")
    parser.add_argument("--pages", default="all", help="e.g. 12-17 or 12,14,16 (default: all)")
    parser.add_argument("--out", help="output .md path (default: stdout)")
    parser.add_argument("--include-notes", action="store_true", help="include speaker notes")
    args = parser.parse_args()

    presentation = Presentation(args.pptx)
    total = len(presentation.slides)
    pages = parse_pages(args.pages, total)
    if not pages:
        raise SystemExit("No matching slides in %s (total %d)" % (args.pptx, total))

    title = ""
    try:
        title = presentation.core_properties.title or ""
    except Exception:
        pass

    header = "# %s — slides %s" % (title or "Slide deck", ", ".join(map(str, pages)))
    body = [header, ""]

    for page in pages:
        body.append(extract_slide(presentation.slides[page - 1], page, args.include_notes))

    markdown = "\n".join(body).rstrip() + "\n"

    if args.out:
        with io.open(args.out, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(markdown)
        print("Wrote %s (%d slides)" % (args.out, len(pages)))
    else:
        if hasattr(sys.stdout, "buffer"):
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        sys.stdout.write(markdown)


if __name__ == "__main__":
    main()
