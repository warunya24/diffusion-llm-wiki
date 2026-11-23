# Source: DDPM (Ho, Jain & Abbeel, 2020)
- **Citation:** J. Ho, A. Jain, P. Abbeel. *Denoising Diffusion Probabilistic Models*. NeurIPS 2020. https://arxiv.org/abs/2006.11239
- **Raw capture:** [01-ddpm-paper.md](../../raw/01-ddpm-paper.md)
- **Type:** research paper (the paper that made diffusion models work well for images)

## Key takeaways
1. The forward (noising) process is fixed: no learning, just a schedule of noise amounts.
2. You can jump straight from a clean image to any noise level in one formula.
3. The neural network only has to predict **the noise** that was added. The loss is a simple mean squared error.
4. Generation = start from pure noise and remove predicted noise step by step (1000 steps in the paper).
5. Backbone network is a U-Net that is told the time step.

## Feeds concept pages
[diffusion-model](../concepts/diffusion-model.md) · [forward-process](../concepts/forward-process.md) · [noise-schedule](../concepts/noise-schedule.md) · [noise-prediction-training](../concepts/noise-prediction-training.md) · [reverse-process](../concepts/reverse-process.md) · [u-net](../concepts/u-net.md)
