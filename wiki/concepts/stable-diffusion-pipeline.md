# The Stable Diffusion pipeline (big picture)

## One-line definition
What happens, in order, when you type a prompt: encode text → denoise a random latent many times while reading the text → decode the latent into a picture.

## Intuition / analogy
Order at a restaurant (text encoder takes the order), the chef cooks in many small stirs (U-Net loop), the waiter plates it (decoder).

## Details
- Stable Diffusion is a system of several models, not a single model. [src: alammar-illustrated-sd]
- Step 1, text encoder (ClipText): prompt → 77 × 768 token embeddings. [src: alammar-illustrated-sd]
- Step 2, image information creator (U-Net + scheduler): starts from random noise in latent space and refines it step by step, using the text embeddings. [src: alammar-illustrated-sd]
- Step 3, image decoder (autoencoder): turns the final latent into the full-size image once. [src: alammar-illustrated-sd]
- The paper's text-to-image model has 1.45B parameters and was trained on the LAION dataset. [src: latent-diffusion]
- The same latent-diffusion design also handles inpainting, super-resolution and layout-to-image. [src: latent-diffusion]

## Key numbers
- Text 77 × 768; latent (4, 64, 64); image (3, 512, 512); 50 or 100 steps by default. [src: alammar-illustrated-sd]
- Text-to-image latent diffusion model: 1.45B parameters. [src: latent-diffusion]

## Related
[clip-text-encoder](clip-text-encoder.md) · [u-net](u-net.md) · [cross-attention](cross-attention.md) · [latent-space](latent-space.md) · [sampling-steps](sampling-steps.md) · [classifier-free-guidance](classifier-free-guidance.md)
