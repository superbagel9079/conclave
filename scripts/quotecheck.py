"""Check that a lens quote appears verbatim in the input, whitespace collapsed.

Usage: python scripts/quotecheck.py "<quote>" <file-or-dir> [...]
Prints each file that contains the quote. Exit 0 if found, 1 if not.
"""
import os
import re
import sys


def collapse(text):
    return re.sub(r"\s+", " ", text).strip()


def files(paths):
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, names in os.walk(p):
                dirs[:] = [d for d in dirs if not d.startswith(".")]
                for n in sorted(names):
                    yield os.path.join(root, n)
        else:
            yield p


def find(quote, paths):
    q = collapse(quote)
    if not q:
        return []
    hits = []
    for f in files(paths):
        try:
            with open(f, encoding="utf-8") as fh:
                if q in collapse(fh.read()):
                    hits.append(f)
        except (UnicodeDecodeError, OSError):
            continue  # binary or unreadable file: cannot hold a text quote
    return hits


def main(argv):
    if len(argv) < 3:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    missing = [p for p in argv[2:] if not os.path.exists(p)]
    if missing:
        print("not found: " + ", ".join(missing), file=sys.stderr)
        return 2
    hits = find(argv[1], argv[2:])
    for h in hits:
        print(h)
    return 0 if hits else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
