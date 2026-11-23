#!/usr/bin/env python3
"""Render node check: open slides.html in headless Chrome, screenshot every slide,
report JS console errors, slides whose content overflows the screen, and broken footer links.
Usage: python tools/browser_check.py [outdir]
"""
import sys, pathlib
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent
out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/shots"); out.mkdir(exist_ok=True)
errs, issues = [], []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": 1280, "height": 720})
    pg.on("console", lambda m: m.type == "error" and errs.append(m.text))
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto((ROOT / "slides.html").as_uri())
    n = pg.evaluate("document.querySelectorAll('.slide').length")
    for i in range(n):
        pg.evaluate(f"show({i})"); pg.wait_for_timeout(400)
        pg.screenshot(path=str(out / f"slide{i+1:02d}.png"))
        over = pg.evaluate("""() => { const s=document.querySelector('.slide.active'), f=s.querySelector('.wiki-foot');
           const lim = f ? f.getBoundingClientRect().top : innerHeight; let worst=0;
           s.querySelectorAll(':scope > *:not(.wiki-foot)').forEach(e=>{worst=Math.max(worst,e.getBoundingClientRect().bottom)});
           return Math.round(worst - lim); }""")
        if over > 0: issues.append(f"slide {i+1}: content overlaps footer by {over}px")
        for href in pg.evaluate("[...document.querySelectorAll('.slide.active .wiki-foot a')].map(a=>a.getAttribute('href'))"):
            if not (ROOT / href).exists(): issues.append(f"slide {i+1}: broken wiki link {href}")
    b.close()
print(f"browser_check: {n} slides screenshotted to {out}")
print("console errors:", errs or "none")
print("layout/link issues:", issues or "none")
sys.exit(1 if errs or issues else 0)
