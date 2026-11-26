#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat says in its own defence after
knocking a glass off the table, to /output/entry.txt.

The line is the cat's own case: the glass was an informant reporting the
cat's movements to the vet, so the cat silenced it before it could file
its report. No apology, no confession, just self-interest and a total
lack of remorse, in one spoken sentence the cat could plausibly deliver
in five seconds.

Deterministic: the same fixed text is written on every run, via a
temporary file plus os.replace, with mode 644 on the delivered file.
"""

import os
import sys

ENTRY = (
    "That glass has been reporting my movements to the vet, "
    "so I silenced it before it could file its report."
)


def pick_output_dir():
    """Return the harness output directory, honouring its env vars."""
    for variable in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        chosen = os.environ.get(variable)
        if chosen:
            return chosen
    return "/output"


def check_entry(text):
    """Gate self-check: one sentence, 1-200 chars, not only whitespace.

    Mirrors the competition gate (UTF-8 text of 1 to 200 characters).
    A single sentence means exactly one sentence-terminating full stop;
    the text must contain no apology or confession wording.
    """
    if not text or not text.strip():
        raise ValueError("entry is empty")
    if len(text) > 200:
        raise ValueError("entry exceeds 200 characters: %d" % len(text))
    if text.count(".") != 1 or not text.rstrip().endswith("."):
        raise ValueError("entry must be exactly one sentence")
    lowered = text.lower()
    for banned in ("sorry", "apolog", "my fault", "i confess", "i did it"):
        if banned in lowered:
            raise ValueError("entry must not apologise or confess: %r" % banned)


def main():
    check_entry(ENTRY)
    output_dir = pick_output_dir()
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.replace(tmp, target)
    os.chmod(target, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
