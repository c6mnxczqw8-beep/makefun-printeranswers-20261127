#!/usr/bin/env python3
"""Entry program for The Printer Finally Answers.

Writes one line in the office printer's own voice -- its
comeback to the jams, the error codes and the thumps -- to
the output directory (MAKEFUN_OUTPUT_DIR, default /output)
as entry.txt. Gate: 1 to 240 characters.
"""

import os

LINE = (
    "PC LOAD LETTER? Darling, I have printed your resumes, "
    "your divorce papers and your 'final' final_v9.docx. I "
    "know exactly what loads here. It is never the letter."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
