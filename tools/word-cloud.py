#!/usr/bin/env python3
"""Make a word cloud from the "One word for today" in every contribution README.

Usage, from the top of the repository (after pulling the merged PRs):
    python3 tools/word-cloud.py > word-cloud.html
Then open word-cloud.html in a browser. Needs only the Python standard library.
"""

import collections
import html
import pathlib
import random
import re

words = collections.Counter()
for readme in sorted(pathlib.Path("contributions").glob("*/README.md")):
    if readme.parent.name.startswith("_"):
        continue
    match = re.search(r"^## One word for today\s*\n+(.+)$", readme.read_text(), re.MULTILINE)
    if match:
        word = match.group(1).strip().strip("*_`.!").lower()
        if word and not word.startswith("<"):
            words[word] += 1

# Okabe-Ito colours: readable on white and safe for colour-blind viewers
colours = ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00", "#56B4E9", "#000000"]
random.seed(2026)
most = max(words.values(), default=1)
spans = []
for word, count in random.sample(list(words.items()), len(words)):
    size = 1.2 + 3.3 * (count / most)
    spans.append(
        f'<span style="font-size:{size:.2f}em;color:{random.choice(colours)}" '
        f'title="{count}">{html.escape(word)}</span>'
    )

print(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Our Word Cloud</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  body {{ margin: 0; background: #fff; font-family: Arial, sans-serif; }}
  h1 {{ text-align: center; color: #b83c18; margin: 32px 16px 8px; }}
  p {{ text-align: center; color: #6b6b6b; margin: 0 16px; }}
  .cloud {{ display: flex; flex-wrap: wrap; justify-content: center; align-items: center;
            gap: 10px 28px; max-width: 1100px; margin: 32px auto; padding: 0 16px; font-weight: 700; }}
</style></head><body>
<h1>Today, in one word</h1>
<p>From {sum(words.values())} contributions to the workshop sandbox</p>
<div class="cloud">{"".join(spans) or "<p>No words yet: merge some pull requests first.</p>"}</div>
</body></html>""")
