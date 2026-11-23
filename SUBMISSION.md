**Title:** NTHU <student ID> EECS<year> Warunya Kumpunya: How does AI turn text into images? (Diffusion Models)

---

### 1. LLM Wiki topic and short introduction
**Topic:** How does AI turn text into images? (Diffusion models)

A small knowledge base that explains how text-to-image models like Stable Diffusion work, for a beginner who knows what a neural network and a loss function are.
It follows the LLM Wiki pattern: **raw sources** (immutable capture notes) → **wiki** (LLM-maintained source + concept pages, every claim cited) → **schema** (`CLAUDE.md`, the rules for ingest / query / lint).
I used "discuss first, then generate": before any page was generated, I agreed on the audience, 7 guiding questions, the concept pages and the source list (`process/00-discussion.md`).

- 6 sources ingested: DDPM (Ho et al. 2020), Lilian Weng's "What are Diffusion Models?", Jay Alammar's "The Illustrated Stable Diffusion", CLIP (Radford et al. 2021 + OpenAI blog), Latent Diffusion (Rombach et al. 2022), Classifier-Free Guidance (Ho & Salimans 2022)
- 12 concept pages: diffusion model, forward process, noise schedule, noise-prediction training, U-Net, reverse process, sampling steps, latent space, CLIP text encoder, cross-attention, classifier-free guidance, Stable Diffusion pipeline

### 2. LLM Wiki link
<https://warunya24.github.io/diffusion-llm-wiki/wiki/index.html>

### 3. Teaching HTML slides link
<https://warunya24.github.io/diffusion-llm-wiki/slides.html>
(16 slides, 3 interactive demos (noise slider with the real DDPM schedule, denoising animation, guidance-scale demo), a 5-question quiz; each slide's footer links to the wiki pages it uses)

Project home: <https://warunya24.github.io/diffusion-llm-wiki/>

### 4. Loop / graph
Collect sources → **Ingest one source → Ingest check** (repeat ×6) → **Lint** → Slide plan → **Fact sheet** (new in v2) → Generate slides (query wiki) → **Grounding + order check** → **Render check** → Publish

- **Repeated:** ingest + ingest check once per source; slide check until it passes (only failing slides regenerated); render check until the slides look right.
- **Checks / regeneration points:** after every ingest (citations, links, every number must exist in the raw source); lint (orphans + manual contradiction read); fact sheet before writing slides; after generation (every number on a slide must be in the cited wiki pages; no term before its definition); browser render (console errors, overflow, broken links, plus a human look).
- **Why:** the wiki is the only knowledge source for the slides, so it is checked first and most strictly. Errors are cheapest to fix at the earliest node that could know about them. Scripts check mechanical things; a human checks layout and teaching quality.

Full diagram and explanation: <https://warunya24.github.io/diffusion-llm-wiki/process/workflow.html>

### 5. One real run: check record
| Node | Runs | Problems | Example |
|---|---|---|---|
| Ingest check | 7 | 2 + 2 source conflicts noted | CLIP "400 million pairs": "illustrative" in Alammar vs. fact in the CLIP paper → trust the paper |
| Lint | 2 (+ checker self-test 3/3) | 1 | "1000 steps" vs "50 or 100 steps" never explained → added bridging explanation (DDIM) |
| **Slide check** | 2 | **13 → 0** | "48× fewer numbers" was the AI's own arithmetic; "forward process" used before its slide |
| Render check | 3 | 3 (found only by looking) | guidance demo point hidden under another point at the default setting |

Full log: <https://warunya24.github.io/diffusion-llm-wiki/process/run-log.html>

### 6. Reflection
- **Most error-prone node:** slide generation (13 problems in run 1). The wiki facts were correct, but when turning them into teaching text the AI added its own numbers (48×, 10–20%), used terms before teaching them, and under-cited summary slides.
- **Where I moved the check:** from after generation to **before** it. A new **fact-sheet node** lists, for each slide, the allowed numbers (from its wiki pages) and the terms that are not yet allowed. Earlier, I had already moved number checking to **ingest time**, which is why the 2 source conflicts were caught in the wiki and became a teaching point instead of a slide error.
- **Did I change the graph?** Yes (v1 → v2): added the fact-sheet node; the slide check now regenerates only failing slides; added a human look to the render check because the script said PASS while a demo was visibly broken; and fixed checker false positives so the checks stay trustworthy.

Full reflection: <https://warunya24.github.io/diffusion-llm-wiki/process/reflection.html>
