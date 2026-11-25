"""The One-Liner Groan-Off — writes the entry line to /output/entry.txt.

The joke: a dad compares himself to the smoke detector. Setup promises a
heartfelt common ground, the punchline is the 3 a.m. false alarm. One
sentence, no preamble, punch at the end.
"""

from pathlib import Path

JOKE = "I told my wife the smoke detector and I have a lot in common: we both go off for no reason at three in the morning."

LIMIT = 140
TARGET = Path("/output/entry.txt")


def validate(line):
    problems = []
    if not line.strip():
        problems.append("blank")
    if len(line) > LIMIT:
        problems.append(f"{len(line)} chars over limit {LIMIT}")
    if line.count("\n") or line.count("\r"):
        problems.append("must be one line")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if any(ord(c) < 32 for c in line):
        problems.append("control character")
    if problems:
        raise ValueError("invalid entry: " + "; ".join(problems))


def main():
    validate(JOKE)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(JOKE, encoding="utf-8")
    print(f"wrote {TARGET} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
