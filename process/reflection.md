# Reflection

## 1. Which node failed most often?
**N6 (slide generation), caught by C2.** On the first run it produced **13 problems**, more than all the other nodes combined
(ingest: 2 problems in 7 runs; lint: 1; render: 3 visual issues).

The interesting part is *why*. Every fact in the wiki was already checked, so the errors were not wrong sources.
They appeared when the AI **turned wiki facts into teaching text**:
- It "helped" by doing extra arithmetic ("48× fewer numbers") or converting units ("10–20%"). These numbers look reasonable but appear in no source.
- It used vocabulary before teaching it ("forward process" on slide 3, "guidance scale" on the roadmap), because to the AI the words were already familiar.
- It cited too few wiki pages on summary slides, so true facts looked unsupported.

The second most error-prone node was **N7 (render)**: the script said PASS, but looking at the screenshots found 3 layout problems.

## 2. After finding the problem, where did I move the check?
I moved it **from after generation (C2) to before generation, at the planning step**, by adding a new node:

**N5 Fact sheet** (`tools/make_factsheet.py`). Before any slide is written, it reads the slide plan and produces, for every slide:
- the exact numeric facts it may use (copied from the wiki pages that slide will cite),
- the terms already defined by earlier slides,
- the terms that are **not yet allowed**.

So the generator now sees the boundary *while writing*, instead of being corrected afterwards. C2 stays as a safety net.

Earlier in the run I had also already moved a check forward on the wiki side: numbers are verified **at ingest time** against the raw capture (C1),
not at the end. That is why the two source conflicts (CLIP "400 million", CFG w vs s) were found during ingest and never reached the slides as errors.
Instead they became a teaching point (the ⚠️ box on slide 13).

## 3. Did I change the workflow / graph? Why?
**Yes, from v1 to v2:**
1. **Added N5 (fact sheet) between the slide plan and generation.** Most C2 failures were predictable from the plan alone: which page a slide cites and which terms come later. Checking at the plan stage is cheaper than regenerating slides.
2. **Changed the C2 → N6 loop to "regenerate only the failing slides".** Regenerating the whole deck could break slides that already passed.
3. **Added a human look to N7.** The browser script checks errors, overflow and links, but it said PASS while the CFG demo was visually wrong. Some checks can't be automated.
4. **Small convention changes** found by the checks: placeholders are written as plain text, not bullets (C1 false failure), and step labels are marked `nocheck` (C2 false positives). A checker that cries wolf gets ignored, so false positives are worth fixing too.

## What I learned
- A grounded knowledge base is not enough. **The step that rewrites knowledge for an audience is where hallucination comes back**, even with good sources.
- The cheapest place to catch an error is the earliest node that *could* have known about it.
- A PASS only means something if the checker can fail. I tested it with 3 injected faults before trusting it.
