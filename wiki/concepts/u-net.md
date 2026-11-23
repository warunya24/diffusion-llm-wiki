# U-Net (the noise-predicting network)

## One-line definition
The neural network inside a diffusion model that looks at a noisy image and outputs a same-sized "noise map".

## Intuition / analogy
A "U" shape: squeeze the picture down to understand *what* is in it, then expand it back up to say *where* the noise is.

## Details
- DDPM uses a U-Net similar to PixelCNN++, with group normalization. [src: ddpm]
- The same weights are used for every time step; the step number is given to the network as a sinusoidal embedding (like positions in a Transformer). [src: ddpm]
- Self-attention is used at the 16x16 feature-map resolution. [src: ddpm]
- Structure: a downsampling path (lower resolution, more channels), an upsampling path, and skip connections that carry fine details across. [src: weng-blog]
- A newer alternative backbone is the Diffusion Transformer (DiT), which works on patches of the latent. [src: weng-blog]

## Key numbers
- Self-attention at 16x16 resolution. [src: ddpm]

## Related
[noise-prediction-training](noise-prediction-training.md)
[forward-process](forward-process.md) · [latent-space](latent-space.md)

