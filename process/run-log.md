# Run log: one full execution of the workflow (2026-11-23)

The raw check outputs are saved next to this file:
`slides-check-run1.txt`, `slides-check-run2.txt`, `browser-check-run1.txt`, `browser-check-run2.txt`.
The wiki's own chronological log is in `wiki/log.md`.

## Summary table

| # | Node | Run | Result | What was found | Action |
|---|---|---|---|---|---|
| 1 | N0 Discuss | n/a | done | scope, 7 questions, 11 planned concepts, 6 sources | `00-discussion.md` |
| 2 | N2+C1 ingest #1 DDPM | 1 | ✅ PASS | n/a | n/a |
| 3 | N2+C1 ingest #2 Weng | 1 | ❌ FAIL (2) | placeholder `- (none yet)` read as an uncited fact | placeholders written as plain text |
| 4 | N2+C1 ingest #2 Weng | 2 | ✅ PASS | n/a | n/a |
| 5 | N2+C1 ingest #3 Alammar | 1 | ✅ PASS | n/a | n/a |
| 6 | N2+C1 ingest #4 CLIP | 1 | ✅ PASS | **conflict:** "400 million pairs" called *illustrative* by Alammar, stated as fact by the CLIP paper | ⚠️ conflict note, trust the paper |
| 7 | N2+C1 ingest #5 LDM | 1 | ✅ PASS | n/a | n/a |
| 8 | N2+C1 ingest #6 CFG | 1 | ✅ PASS | **conflict:** paper uses w, tools use s = 1 + w | ⚠️ conflict note (and a warning box on the slide) |
| 9 | N3 Lint (script) | 1 | ✅ PASS | 6 sources, 12 concepts, 0 orphans | n/a |
| 10 | N3 checker self-test | 1 | ✅ caught 3/3 | injected: orphan page, uncited bullet, fake number "860" | proves a PASS is meaningful |
| 11 | N3 Lint (manual) | 1 | ❌ 1 issue | "1000 steps" vs "50 or 100 steps" never explained | bridging bullet in `reverse-process` |
| 12 | N3 Lint (script) | 2 | ✅ PASS | n/a | n/a |
| 13 | N6+C2 slides | **1** | ❌ **FAIL (13)** | see below | fixed 7 slides; added N5 |
| 14 | N6+C2 slides | 2 | ✅ PASS | 16 slides, 31 wiki refs, 15 tracked terms | n/a |
| 15 | N7 browser (script) | 1 | ✅ PASS | 0 console errors, 0 overflow, 0 broken links | n/a |
| 16 | N7 browser (human look) | 1 | ❌ 2 issues | CFG demo: "guided" sat on "cond" at default s = 1; pipeline boxes cramped + hint text crowding footer | default s = 3, wider middle box, hint removed |
| 17 | N7 browser (human look) | 2 | ❌ 1 issue | CFG demo point clipped at top-right at s = 3 | rescaled diagram |
| 18 | N7 browser (script + look) | 3 | ✅ PASS | n/a | publish |

## Detail: slide check run 1 (C2): 13 problems

```
slide 3:  number '2020' not in cited wiki pages ['concepts/diffusion-model.md']
slide 6:  number '2' not in cited wiki pages            ← "Step 2" title (false positive)
slide 8:  number '3' not in cited wiki pages            ← "Step 3" title (false positive)
slide 10: number '48' not in cited wiki pages           ← I computed "48× fewer numbers" myself
slide 13: number '10' / '20' not in cited wiki pages    ← "10–20%" = my conversion of 0.1 / 0.2
slide 16: number '1000', '2021', '2022' not in cited wiki pages
slide 1:  uses 'diffusion model' before it is defined on slide 3
slide 2:  uses 'guidance scale' before it is defined on slide 13
slide 3:  uses 'forward process' before it is defined on slide 4
slide 3:  uses 'reverse process' before it is defined on slide 8
```

| Type | Count | Fix |
|---|---|---|
| Number not supported by the cited wiki page (made up / converted / cited the wrong page) | 7 | removed "48×", wrote 0.1 / 0.2 exactly as in the wiki, added the missing source pages to `data-wiki` |
| Term used before its definition | 4 | title gives a one-line definition; roadmap rephrased without jargon; slide 3 already defines forward/reverse in one line, so the definition moved there |
| False positive in the checker | 2 | step labels marked `class="nocheck"` |

## Detail: what the checker *cannot* catch (honest limits)
- A wrong claim that contains **no number** (e.g. "CLIP is trained on captions written by humans") passes C2. Only the wiki citations and a human read protect against that.
- Source pages have numbered takeaway lists ("1." to "5."), so small digits like 1 to 5 are always "allowed". A fake "3 steps" would pass.
- Layout problems passed the script but were obvious in the screenshots. This is why N7 includes a human look.
