# Log (append-only)

## [2026-11-23] setup
- Agreed scope, audience, 7 guiding questions and concept list (see `process/00-discussion.md`).
- Wrote schema `wiki/CLAUDE.md` and checker `tools/check_wiki.py`.

## [2026-11-23] ingest #1: raw/01-ddpm-paper.md
- Created source page `ddpm` and 6 concept pages.
- Ingest check: PASS on first run.

## [2026-11-23] ingest #2: raw/02-weng-blog.md
- Created source page `weng-blog`; new concepts `sampling-steps`, `latent-space`, `classifier-free-guidance`; added bullets to diffusion-model, forward-process, noise-schedule, u-net.
- Ingest check run 1: **FAIL (2)**. Placeholder line "- (none yet)" in Key numbers was parsed as an uncited fact.
- Fix: placeholders are written as plain text `_(none yet)_`, not as bullets. Ingest check run 2: PASS.
- Ingest check: PASS.

## [2026-11-23] ingest #3: raw/03-alammar-illustrated-sd.md
- Created source page `alammar-illustrated-sd`; new concepts `clip-text-encoder`, `cross-attention`, `stable-diffusion-pipeline`; added tensor shapes to `latent-space`, step defaults to `sampling-steps`.
- Ingest check: PASS.

## [2026-11-23] ingest #4: raw/04-clip.md
- Created source page `clip`; added 4 Details bullets + 2 Key numbers to `clip-text-encoder`.
- **Conflict found during ingest:** Alammar calls "400 million pairs" illustrative; the CLIP paper states 400 million as the real size. Wrote a ⚠️ Conflict note; trust the paper.
- Ingest check: PASS.

## [2026-11-23] ingest #5: raw/05-latent-diffusion.md
- Created source page `latent-diffusion`; added motivation, two-stage design and factor f to `latent-space`; conditioning encoder to `cross-attention`; 1.45B model to `stable-diffusion-pipeline`.
- Ingest check: PASS.

## [2026-11-23] ingest #6: raw/06-classifier-free-guidance.md
- Created source page `classifier-free-guidance-paper`; added 4 Details + 2 Key numbers to `classifier-free-guidance`.
- **Conflict found during ingest:** paper formula (1+w)·cond − w·uncond vs common form uncond + s·(cond − uncond). Same rule with s = 1 + w. Wrote ⚠️ Conflict note so slides don't mix up w and s.
- Ingest check: PASS.

## [2026-11-23] lint #1
- `check_wiki.py --full`: PASS (6 sources, 12 concepts, 0 orphans).
- Checker self-test on a temp copy with 3 injected faults (orphan page, uncited bullet, invented number "860"): all 3 caught → a PASS is meaningful.
- **Manual contradiction pass found 1 issue the script cannot see:** pages say "1000 steps" (DDPM) and "50 or 100 steps" (Stable Diffusion tools) with no explanation. Added a bridging bullet to `reverse-process` linking to `sampling-steps`.
- Re-run `--full`: PASS.

## [2026-11-23] query: slide generation (16 slides)
- Slides generated from `process/slide-plan.json` using only wiki pages (each slide declares `data-wiki`).
- Slide check run 1: **FAIL (13)**: 7 unsupported numbers, 4 terms used before definition, 2 checker false positives. Details in `process/run-log.md`.
- Fixed 7 slides; slide check run 2: PASS.
- Workflow changed (v2): added fact-sheet node `tools/make_factsheet.py` before slide generation.

## [2026-11-23] render check
- Browser script: PASS (0 console errors, 0 overflow, 0 broken links). Human look at screenshots: 3 layout issues over 2 rounds, fixed. Final: PASS.
