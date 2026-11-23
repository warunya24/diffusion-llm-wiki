# Source: Classifier-Free Diffusion Guidance (Ho & Salimans, 2022)
- **Citation:** J. Ho, T. Salimans. *Classifier-Free Diffusion Guidance*. arXiv 2207.12598, 2022 (short version: NeurIPS 2021 workshop). https://arxiv.org/abs/2207.12598
- **Raw capture:** [06-classifier-free-guidance.md](../../raw/06-classifier-free-guidance.md)
- **Type:** research paper

## Key takeaways
1. Classifier guidance needed a second network (a classifier trained on noisy images).
2. CFG: train one model that sometimes sees no condition; at sampling time mix "with prompt" and "without prompt" predictions.
3. Dropping the condition 10–20% of the time works well; 50% is worse.
4. Bigger guidance weight → images match the condition better but are less diverse.

## Feeds concept pages
[classifier-free-guidance](../concepts/classifier-free-guidance.md)
