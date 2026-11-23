#!/usr/bin/env python3
"""Grounding + teaching-order checker for slides.html.

Checks per slide
  1. has data-wiki and every referenced wiki page exists
  2. GROUNDING: every number in the slide's visible text appears in one of the
     wiki pages that slide cites
  3. ORDER: a term listed in data-defines of slide j must not appear on any
     earlier slide i < j (beginners must not meet a term before it is explained)

Text inside elements with class "ui" (slider labels / controls) or "nocheck"
(step labels like "Step 2 ·") is ignored.
The quiz questions (JS array `const Q = [...]`) are checked as part of the quiz slide.

Usage: python tools/check_slides.py [slides.html]
"""
import re, sys, pathlib
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
SLIDES = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "slides.html"
NUM_RE = re.compile(r"\d+(?:[.,]\d+)*(?:e-?\d+)?")

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.slides = []; self.stack = []; self.skip = 0; self.cur = None
        self.in_script = False; self.script = ""
    def handle_starttag(self, tag, a):
        a = dict(a)
        if tag == "script": self.in_script = True
        if tag == "section" and "slide" in a.get("class", ""):
            self.cur = {"wiki": [x for x in a.get("data-wiki", "").split(",") if x],
                        "defines": [x.strip() for x in a.get("data-defines", "").split(",") if x.strip()],
                        "text": "", "title": ""}
            self.slides.append(self.cur)
        ui = bool({"ui", "nocheck"} & set(a.get("class", "").split()))
        self.stack.append((tag, ui))
        if ui: self.skip += 1
    def handle_endtag(self, tag):
        if tag == "script": self.in_script = False
        while self.stack:
            t, ui = self.stack.pop()
            if ui: self.skip -= 1
            if t == tag: break
        if tag == "section": self.cur = None
    def handle_data(self, d):
        if self.in_script: self.script += d; return
        if self.cur is not None and not self.skip:
            self.cur["text"] += " " + d
            if self.stack and self.stack[-1][0] == "h2" and not self.cur["title"]:
                self.cur["title"] = d.strip()

p = P(); p.feed(SLIDES.read_text())
m = re.search(r"const Q = \[(.*?)\n\];", p.script, re.S)
if m:
    quiz = next((s for s in p.slides if "quiz" in s["title"].lower() or "test yourself" in s["title"].lower()), None)
    if quiz: quiz["text"] += " " + m.group(1)

problems = []
def label(i, s): return f"slide {i+1} ({s['title'] or 'title'})"

# 1 + 2
for i, s in enumerate(p.slides):
    if not s["wiki"]:
        problems.append(f"{label(i,s)}: no data-wiki"); continue
    corpus = ""
    for w in s["wiki"]:
        f = ROOT / "wiki" / w
        if not f.exists():
            problems.append(f"{label(i,s)}: cites missing wiki page {w}")
        else:
            corpus += f.read_text().replace(",", "") + " "
    have = set(NUM_RE.findall(corpus))
    for n in sorted(set(NUM_RE.findall(s["text"].replace(",", "")))):
        if n not in have:
            problems.append(f"{label(i,s)}: number '{n}' not in cited wiki pages {s['wiki']}")

# 3
defined_at = {}
for j, s in enumerate(p.slides):
    for t in s["defines"]:
        defined_at.setdefault(t.lower(), j)
for i, s in enumerate(p.slides):
    low = s["text"].lower()
    for term, j in defined_at.items():
        if j > i and re.search(r"\b" + re.escape(term), low):
            problems.append(f"{label(i,s)}: uses '{term}' before it is defined on slide {j+1}")

print(f"check_slides: {len(p.slides)} slides, {sum(len(s['wiki']) for s in p.slides)} wiki refs, {len(defined_at)} tracked terms")
if problems:
    print(f"FAIL: {len(problems)} problem(s)")
    for x in problems: print("  -", x)
    sys.exit(1)
print("PASS")
