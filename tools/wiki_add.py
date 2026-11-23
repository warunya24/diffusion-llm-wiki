#!/usr/bin/env python3
"""Append a bullet to a section of a wiki page (used during ingest so earlier
sources' bullets are never overwritten).
Usage: python tools/wiki_add.py wiki/concepts/x.md "Details" "- text [src: slug]"
"""
import re, sys, pathlib
path, sec, bullet = pathlib.Path(sys.argv[1]), sys.argv[2], sys.argv[3]
t = path.read_text()
m = re.search(r"(^##\s*" + re.escape(sec) + r".*?$)(.*?)(?=^##\s|\Z)", t, re.S | re.M)
if not m:
    sys.exit(f"section {sec} not found in {path}")
body = m.group(2).rstrip("\n") + "\n" + bullet + "\n\n"
path.write_text(t[: m.start(2)] + body + t[m.end(2):].lstrip("\n"))
print(f"added to {path}:{sec}")
