# Source: Latent Diffusion Models (Rombach et al., 2022), the Stable Diffusion paper
- **Citation:** R. Rombach, A. Blattmann, D. Lorenz, P. Esser, B. Ommer. *High-Resolution Image Synthesis with Latent Diffusion Models*. CVPR 2022. https://arxiv.org/abs/2112.10752
- **Raw capture:** [05-latent-diffusion.md](../../raw/05-latent-diffusion.md)
- **Type:** research paper

## Key takeaways
1. Pixel-space diffusion is very expensive (hundreds of GPU days to train).
2. Fix: compress images with an autoencoder first, then do diffusion on the small latent.
3. Compression factor 4 to 16 is the sweet spot; 4 and 8 are best.
4. Any condition (text, boxes…) is encoded by a separate encoder and injected via cross-attention.
5. Same idea works for text-to-image, inpainting, super-resolution, and more.

## Feeds concept pages
[latent-space](../concepts/latent-space.md) · [cross-attention](../concepts/cross-attention.md) · [stable-diffusion-pipeline](../concepts/stable-diffusion-pipeline.md)
