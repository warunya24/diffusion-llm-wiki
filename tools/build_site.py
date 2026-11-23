#!/usr/bin/env python3
"""Render every wiki/*.md (and process/*.md) to a sibling .html page so the whole
project can be browsed on GitHub Pages (a .nojekyll file disables Jekyll).
Usage: python tools/build_site.py
"""
import re, pathlib, html, markdown
ROOT = pathlib.Path(__file__).resolve().parent.parent
CSS = """body{font-family:'Segoe UI',system-ui,sans-serif;max-width:860px;margin:40px auto;padding:0 20px;
line-height:1.6;color:#1d2533;background:#fbfaf7}a{color:#1f63b5}code{background:#eef1f5;padding:1px 5px;border-radius:4px}
pre{background:#eef1f5;padding:12px;border-radius:8px;overflow:auto}blockquote{border-left:4px solid #e0a030;
background:#fff6e5;margin:12px 0;padding:8px 14px}table{border-collapse:collapse}td,th{border:1px solid #d5dae2;padding:6px 10px}
.top{font-size:14px;color:#667;border-bottom:1px solid #e3e6ea;padding-bottom:8px;margin-bottom:18px}
.src{display:inline-block;background:#eaf2fd;color:#1f63b5;border-radius:12px;padding:0 8px;font-size:13px}"""

def render(md_path):
    text = md_path.read_text()
    text = re.sub(r"\]\(([^)#\s]+)\.md(#[^)]*)?\)", lambda m: f"]({m.group(1)}.html{m.group(2) or ''})", text)
    rel_wiki = pathlib.Path("../" * (len(md_path.relative_to(ROOT).parts) - 1))
    def src(m):
        slug = m.group(1)
        href = (rel_wiki / "wiki" / "sources" / f"{slug}.html").as_posix()
        return f'<a class="src" href="{href}">src: {slug}</a>'
    body = markdown.markdown(text, extensions=["tables", "fenced_code"])
    body = re.sub(r"\[src:\s*([a-z0-9\-]+)\s*\]", src, body)
    home = (rel_wiki / "index.html").as_posix()
    widx = (rel_wiki / "wiki" / "index.html").as_posix()
    title = html.escape(text.splitlines()[0].lstrip("# ").strip())
    out = (f"<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
           f"<title>{title}</title><style>{CSS}</style></head><body><div class='top'><a href='{home}'>🏠 Project home</a> · "
           f"<a href='{widx}'>📚 Wiki index</a> · <a href='{(rel_wiki / 'slides.html').as_posix()}'>🎞️ Slides</a> · "
           f"<a href='{md_path.name}'>view .md source</a></div>{body}</body></html>")
    md_path.with_suffix(".html").write_text(out)

n = 0
for p in list((ROOT / "wiki").rglob("*.md")) + list((ROOT / "process").glob("*.md")) + list((ROOT / "raw").glob("*.md")):
    render(p); n += 1
(ROOT / ".nojekyll").write_text("")
print(f"rendered {n} markdown pages to HTML")
