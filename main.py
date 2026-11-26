#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun bounty u-suroto-two-sentence-horror-acea9253.

Writes one two-sentence horror story to /output/entry.txt.
The story is fixed, so every run writes exactly the same text:
deterministic, no network, no randomness, no clock.
"""

import os
from pathlib import Path

STORY = (
    "The shelter said the dog I adopted had been returned twice "
    "for barking at empty rooms. "
    "Last night he stood at the foot of my bed and barked at it "
    "for an hour, and I was lying in it the whole time."
)


def check_story(text: str) -> None:
    """The sealed gate's rules, checked before anything is written:
    UTF-8 text of 1 to 400 characters, not only white space,
    told in exactly two sentences."""
    assert 1 <= len(text) <= 400, f"story is {len(text)} chars, gate allows 1-400"
    assert text.strip(), "story must not be only white space"
    assert text.count(".") == 2, "story must be exactly two sentences"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    text = STORY.strip()
    check_story(text)
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {out_path} ({len(text)} chars, 2 sentences)")


if __name__ == "__main__":
    main()
