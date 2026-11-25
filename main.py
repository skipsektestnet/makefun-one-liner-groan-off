"""The One-Liner Groan-Off — emit the entry line to /output/entry.txt.

The joke works like a classic dad joke: the setup ("the smoke detector
and I have a lot in common") sounds like a sweet, heartfelt comparison,
and the punchline undercuts it — they both go off for no reason at
three in the morning. One sentence, setup first, punch at the very end.
"""

from pathlib import Path

JOKE = (
    "I told my wife the smoke detector and I have a lot in common: "
    "we both go off for no reason at three in the morning."
)

MAX_CHARS = 140
OUTPUT = Path("/output/entry.txt")

# The punchline must survive any future edit of the joke text: the whole
# gag hinges on the 3 a.m. false alarm, so the gate refuses a version
# that loses it, and refuses a version that does not end on the punch.
REQUIRED_PHRASE = "three in the morning"
TERMINATORS = ".!?"


def problems(line: str) -> list[str]:
    """Return every gate violation for a candidate entry line."""
    found = []
    if not line.strip():
        found.append("entry is blank")
    if len(line) > MAX_CHARS:
        found.append(f"{len(line)} chars exceeds {MAX_CHARS}-char limit")
    if "\n" in line or "\r" in line:
        found.append("entry must be a single line")
    if line != line.strip():
        found.append("leading or trailing whitespace")
    if any(ord(ch) < 32 for ch in line):
        found.append("contains a control character")
    if "  " in line:
        found.append("contains a double space")
    if REQUIRED_PHRASE not in line:
        found.append(f"missing punchline phrase {REQUIRED_PHRASE!r}")
    if not line or line[-1] not in TERMINATORS:
        found.append("must end on terminal punctuation (the punchline)")
    return found


def main() -> None:
    bad = problems(JOKE)
    if bad:
        raise ValueError("invalid entry: " + "; ".join(bad))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(JOKE, encoding="utf-8")
    print(f"wrote {OUTPUT} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
