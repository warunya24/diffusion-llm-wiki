# How does AI turn text into images? An LLM Wiki + teaching slides

Homework: build an LLM Wiki on a topic, then use it as the only knowledge source for a teaching HTML slideshow.

- 🎞️ **Slides:** `slides.html`
- 📚 **Wiki:** `wiki/index.md` (schema: `wiki/CLAUDE.md`, log: `wiki/log.md`)
- 🔁 **Workflow / graph:** `process/workflow.md`
- 🧾 **Run log:** `process/run-log.md` · 🤔 **Reflection:** `process/reflection.md`
- 🗂️ Raw source captures: `raw/`

## Folder layout
```
raw/        6 source capture notes (immutable)
wiki/       CLAUDE.md schema · index · log · sources/ (6) · concepts/ (12)
process/    discussion, workflow, slide plan, fact sheet, run log, reflection, check outputs
tools/      check_wiki.py · wiki_add.py · make_factsheet.py · check_slides.py · browser_check.py · build_site.py
slides.html teaching deck (16 slides, 3 interactive demos, quiz)
index.html  project home page
```

## Re-run the checks
```bash
python tools/check_wiki.py --full     # ingest / lint check
python tools/make_factsheet.py > process/factsheet.md
python tools/check_slides.py          # grounding + teaching-order check
python tools/browser_check.py         # render check (needs playwright + Chrome)
python tools/build_site.py            # render .md pages to .html for GitHub Pages
```

## Publish on GitHub Pages
Create a repo (e.g. `diffusion-llm-wiki`), upload all files, then Settings → Pages → Deploy from branch `main` / root.
Site: `https://warunya24.github.io/diffusion-llm-wiki/`
