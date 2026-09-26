"""Render each page of a PDF to a PNG for visual inspection.

Usage: python render_pdf.py <pdf> [outdir] [dpi]
"""
import pathlib
import sys

import pymupdf


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: render_pdf.py <pdf> [outdir] [dpi]")
        return 1
    pdf = pathlib.Path(sys.argv[1])
    outdir = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else pdf.parent
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 150
    outdir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=dpi)
        out = outdir / f"{pdf.stem}_p{i + 1}.png"
        pix.save(out)
        print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
