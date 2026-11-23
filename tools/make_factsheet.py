#!/usr/bin/env python3
"""NEW NODE (added after run 1): build a per-slide fact sheet from the wiki BEFORE
slides are written. The slide generator may only use the numbers and terms listed.
Usage: python tools/make_factsheet.py > process/factsheet.md
"""
import json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
plan = json.loads((ROOT / "process/slide-plan.json").read_text())
NUM_RE = re.compile(r"\d+(?:[.,]\d+)*(?:e-?\d+)?")
SRC = re.compile(r"\[src:[^\]]*\]|\]\([^)]*\)")
all_terms = [t for s in plan for t in s["defines"]]
defined = []
print("# Fact sheet: generated from the wiki before writing slides\n")
print("Rule: a slide may only use numbers in its *allowed numbers* list and terms in *allowed terms*.\n")
for s in plan:
    nums, facts = set(), []
    for w in s["wiki"]:
        f = ROOT / "wiki" / w
        for line in f.read_text().splitlines():
            if line.strip().startswith(("- ", "1.", "2.", "3.", "4.", "5.")) and NUM_RE.search(SRC.sub("", line)):
                clean = SRC.sub("", line).strip()
                facts.append(f"{clean}  ← `{w}`")
                nums |= set(NUM_RE.findall(clean.replace(",", "")))
    defined += s["defines"]
    blocked = [t for t in all_terms if t not in defined]
    print(f"## Slide {s['n']}: {s['title']}")
    print(f"- wiki pages: {', '.join(s['wiki'])}")
    print(f"- defines here: {', '.join(s['defines']) or '-'}")
    print(f"- allowed terms: {', '.join(defined) or '-'}")
    print(f"- NOT yet allowed: {', '.join(blocked) or '-'}")
    print(f"- allowed numbers: {', '.join(sorted(nums, key=lambda x: float(x.replace('e-','e-'))if re.fullmatch(r'[\d.]+(e-?\d+)?',x) else 0)) or '-'}")
    if facts:
        print("- numeric facts available:")
        for x in facts[:8]: print(f"  - {x}")
    print()
