# Source: Jay Alammar, "The Illustrated Stable Diffusion" (2022)
- **Citation:** J. Alammar. *The Illustrated Stable Diffusion*. 2022 (V2 Nov 2022). https://jalammar.github.io/illustrated-stable-diffusion/
- **Raw capture:** [03-alammar-illustrated-sd.md](../../raw/03-alammar-illustrated-sd.md)
- **Type:** illustrated beginner explainer (best source for the "big picture" and tensor shapes)

## Key takeaways
1. Stable Diffusion = 3 parts: text encoder → image information creator (U-Net + scheduler) → image decoder.
2. The text becomes 77 vectors of 768 numbers.
3. Diffusion happens on a small 4×64×64 latent; the decoder turns it into a 3×512×512 picture once at the end.
4. Interfaces usually run 50 or 100 denoising steps.
5. Text enters the U-Net through attention layers between its ResNet blocks.

## Feeds concept pages
[stable-diffusion-pipeline](../concepts/stable-diffusion-pipeline.md) · [clip-text-encoder](../concepts/clip-text-encoder.md) · [cross-attention](../concepts/cross-attention.md) · [latent-space](../concepts/latent-space.md) · [sampling-steps](../concepts/sampling-steps.md) · [noise-prediction-training](../concepts/noise-prediction-training.md)
