#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji, and nothing else, to /output/entry.txt.

The emoji is U+1F917 HUGGING FACE: a warm, open-armed smile offered
to a stranger. It plainly aims to warm the reader, reads kind and
friendly at first glance, is understood the same way by any age or
background, feels picked for the moment rather than the default
smiley, and carries warmth without intimacy, sarcasm or flirtation.
The output is a single fixed character, so every run is identical.
"""

import os

EMOJI = "🤗"  # U+1F917 HUGGING FACE


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
