# Latent space (working on a compressed image)

## One-line definition
Instead of denoising the full-size picture, first compress it into a much smaller grid of numbers, run diffusion there, and decompress at the end.

## Intuition / analogy
Editing a small sketch of a painting and only painting the full canvas at the very end.

## Details
- Latent diffusion uses an autoencoder to compress images; the diffusion process runs in the smaller latent space, which lowers training and generation cost. [src: weng-blog]
- Stable Diffusion denoises a latent of shape (4, 64, 64); the autoencoder's decoder turns it into an RGB image of shape (3, 512, 512), running only once at the end. [src: alammar-illustrated-sd]
- Working in latent space is why Stable Diffusion is faster than earlier pixel-space diffusion models. [src: alammar-illustrated-sd]
- Motivation: training the strongest pixel-space diffusion models can take hundreds of GPU days, and sampling needs many sequential network passes. [src: latent-diffusion]
- Two stages: (1) a pretrained autoencoder compresses images into a latent that still looks the same to humans; (2) the diffusion model is trained in that latent space. [src: latent-diffusion]
- Compression factor f: values from 4 to 16 balance speed and quality; f = 4 and f = 8 gave the best results. Too much compression loses detail; too little trains slowly. [src: latent-diffusion]

## Key numbers
- Latent (4, 64, 64) → image (3, 512, 512). [src: alammar-illustrated-sd]
- Downsampling factor f = 4 to 16 works well; best at 4 and 8. [src: latent-diffusion]

## Related
[u-net](u-net.md) · [diffusion-model](diffusion-model.md)
[stable-diffusion-pipeline](stable-diffusion-pipeline.md)

