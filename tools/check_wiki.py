#!/usr/bin/env python3
"""Ingest/lint checker for the LLM Wiki.

Checks
  1. every [src: slug] points to an existing wiki/sources/<slug>.md
  2. every relative markdown link resolves
  3. every concept page has the 5 required sections
  4. every bullet in a concept page's "Details" section ends with a [src: ...] citation
  5. every number in "Key numbers" appears in the raw capture of a cited source
  6. (--full) no orphan pages: every page is linked from index.md
  7. (--full) every source page feeds >=1 concept; every concept has >=1 Related link

Usage: python tools/check_wiki.py [--full]
Exit code 0 = pass, 1 = problems found.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
SECTIONS = ["One-line definition", "Intuition", "Details", "Key numbers", "Related"]
SRC_RE = re.compile(r"\[src:\s*([a-z0-9\-]+)\s*\]")
LINK_RE = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)")
NUM_RE = re.compile(r"\d+(?:[.,]\d+)*(?:e-?\d+)?")

full = "--full" in sys.argv
problems = []

def rel(p):
    return str(p.relative_to(ROOT))

def section(text, name):
    m = re.search(r"^##\s*" + re.escape(name) + r".*?$(.*?)(?=^##\s|\Z)", text, re.S | re.M)
    return m.group(1) if m else None

def raw_for(slug):
    sp = WIKI / "sources" / f"{slug}.md"
    if not sp.exists():
        return ""
    m = re.search(r"\(\.\./\.\./raw/([^)]+)\)", sp.read_text())
    rp = ROOT / "raw" / m.group(1) if m else None
    return rp.read_text() if rp and rp.exists() else ""

def norm(n):
    return n.replace(",", "")

pages = [p for p in WIKI.rglob("*.md") if p.name not in ("CLAUDE.md",)]

for p in pages:
    t = p.read_text()
    # 1. citations
    for slug in SRC_RE.findall(t):
        if not (WIKI / "sources" / f"{slug}.md").exists():
            problems.append(f"{rel(p)}: citation [src: {slug}] has no source page")
    # 2. links
    for target in LINK_RE.findall(t):
        if target.startswith("http"):
            continue
        if not (p.parent / target).resolve().exists():
            problems.append(f"{rel(p)}: broken link -> {target}")

for p in sorted((WIKI / "concepts").glob("*.md")):
    t = p.read_text()
    # 3. sections
    for s in SECTIONS:
        if section(t, s) is None:
            problems.append(f"{rel(p)}: missing section '## {s}'")
    # 4. details bullets cited
    det = section(t, "Details") or ""
    for line in det.splitlines():
        if line.strip().startswith("- ") and not SRC_RE.search(line):
            problems.append(f"{rel(p)}: uncited Details bullet: {line.strip()[:70]}")
    # 5. key numbers grounded in raw captures
    kn = section(t, "Key numbers") or ""
    for line in kn.splitlines():
        if not line.strip().startswith("- "):
            continue
        slugs = SRC_RE.findall(line)
        if not slugs:
            problems.append(f"{rel(p)}: Key number without citation: {line.strip()[:70]}")
            continue
        body = SRC_RE.sub("", line)
        body = re.sub(r"\]\([^)]*\)", "]", body)  # drop link targets
        raw = " ".join(norm(raw_for(s)) for s in slugs)
        raw_nums = set(NUM_RE.findall(raw))
        for n in NUM_RE.findall(body):
            if norm(n) not in raw_nums:
                problems.append(f"{rel(p)}: number '{n}' not found in raw of {slugs}")

if full:
    index = (WIKI / "index.md").read_text() if (WIKI / "index.md").exists() else ""
    linked = {(WIKI / t).resolve() for t in LINK_RE.findall(index)}
    for p in pages:
        if p.name in ("index.md",) or p.resolve() in linked:
            continue
        problems.append(f"{rel(p)}: ORPHAN (not linked from index.md)")
    for p in sorted((WIKI / "sources").glob("*.md")):
        if "../concepts/" not in p.read_text():
            problems.append(f"{rel(p)}: source feeds no concept page")
    for p in sorted((WIKI / "concepts").glob("*.md")):
        if not LINK_RE.findall(section(p.read_text(), "Related") or ""):
            problems.append(f"{rel(p)}: no Related links")

n_c = len(list((WIKI / "concepts").glob("*.md")))
n_s = len(list((WIKI / "sources").glob("*.md")))
print(f"check_wiki: {n_s} source pages, {n_c} concept pages, mode={'full' if full else 'ingest'}")
if problems:
    print(f"FAIL: {len(problems)} problem(s)")
    for x in problems:
        print("  -", x)
    sys.exit(1)
print("PASS")
