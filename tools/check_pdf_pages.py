"""Fail unless every given PDF has exactly the expected number of pages (default 2)."""
import sys

import pymupdf

expected = 2
failed = False
for path in sys.argv[1:]:
    with pymupdf.open(path) as doc:
        n = doc.page_count
    print(f"{path}: {n} pages")
    failed |= n != expected
sys.exit(1 if failed else 0)
