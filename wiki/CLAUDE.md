# CLAUDE.md: Schema for the "Text-to-Image Diffusion" LLM Wiki

This file is the operating manual for the AI that maintains this wiki.
Read it before every **ingest**, **query**, or **lint** operation.

## Purpose
A small knowledge base that explains **how AI turns text into images (diffusion models)**,
written for a beginner who knows basic ML (what a neural network and a loss function are)
but has never studied generative models.

## Layers
| Layer | Folder | Rule |
|---|---|---|
| Raw sources | `raw/` | Capture notes of each source (URL, date read, facts extracted). **Never edited after ingest.** |
| Wiki | `wiki/` | LLM-maintained pages. Every factual claim must cite a source page. |
| Schema | `wiki/CLAUDE.md` | This file. Changed only when the workflow changes (record why in `log.md`). |

## Page types
- `wiki/sources/<slug>.md`: one page per ingested source: citation, 3–6 key takeaways, which concept pages it feeds.
- `wiki/concepts/<slug>.md`: one page per idea. Fixed sections:
  1. **One-line definition** (plain English, no symbols)
  2. **Intuition / analogy**
  3. **Details** (bullets; each bullet ends with a citation like `[src: ddpm]`)
  4. **Key numbers** (only numbers that appear in a source page)
  5. **Related** (links to other concept pages)
- `wiki/index.md`: table of contents. Every page must be linked here.
- `wiki/log.md`: append-only, chronological record of every ingest / lint / query.

## Citation rule
- A citation looks like `[src: <source-slug>]` and must match a file in `wiki/sources/`.
- If two sources disagree, write **both** and add a `> ⚠️ Conflict:` note explaining which one we trust and why.
- Numbers (dimensions, step counts, dataset sizes) are copied **only** from sources, never from model memory.

## Operations
### Ingest `<raw file>`
1. Read the raw capture note.
2. Create/update `wiki/sources/<slug>.md`.
3. Create or update the concept pages it touches (add bullets with citations; do not delete other sources' bullets).
4. Add cross-links in **Related**.
5. Update `index.md` and append to `log.md`.
6. Run `python tools/check_wiki.py` → fix until it passes (**ingest check**).

### Query `<question>`
Answer only from wiki pages; cite the pages used. If the wiki can't answer, say so and propose a source to ingest.

### Lint
Run `python tools/check_wiki.py --full`, then manually look for contradictions between concept pages.

## Slide generation rules (for the teaching deck)
- Every content slide declares the wiki pages it uses (`data-wiki="concepts/x.md,..."`).
- A term may not appear on a slide before the slide that defines it.
- Any number on a slide must appear in one of the wiki pages that slide cites.
- Run `python tools/check_slides.py` after generating; regenerate only the failing slides.
