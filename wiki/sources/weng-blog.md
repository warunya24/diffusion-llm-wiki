# Source: Lilian Weng, "What are Diffusion Models?" (2021, updated 2024)
- **Citation:** L. Weng. *What are Diffusion Models?* Lil'Log, 2021-07-11 (updated 2022-08 and 2024-04). https://lilianweng.github.io/posts/2021-07-11-diffusion-models/
- **Raw capture:** [02-weng-blog.md](../../raw/02-weng-blog.md)
- **Type:** survey blog post (clear overview + math)

## Key takeaways
1. Diffusion is inspired by thermodynamics: slowly add noise, then learn to undo it.
2. Unlike a VAE, the "latent" (the noisy image) has the same size as the data.
3. Schedules: linear (DDPM) vs cosine (gentler at both ends).
4. DDIM makes sampling much faster by skipping steps.
5. Classifier-free guidance and latent diffusion are what modern text-to-image systems use.

## Feeds concept pages
[diffusion-model](../concepts/diffusion-model.md) · [forward-process](../concepts/forward-process.md) · [noise-schedule](../concepts/noise-schedule.md) · [sampling-steps](../concepts/sampling-steps.md) · [classifier-free-guidance](../concepts/classifier-free-guidance.md) · [latent-space](../concepts/latent-space.md) · [u-net](../concepts/u-net.md)
