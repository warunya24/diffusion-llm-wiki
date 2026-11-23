# RAW CAPTURE: Lilian Weng blog
- Title: What are Diffusion Models?
- Author: Lilian Weng (Lil'Log). Published 2021-07-11; updated 2021-09-19, 2022-08-27 (CFG, GLIDE, unCLIP, Imagen), 2022-08-31 (latent diffusion), 2024-04-13 (distillation, consistency models, architecture)
- URL: https://lilianweng.github.io/posts/2021-07-11-diffusion-models/
- Captured: 2026-11-23

## Facts extracted (paraphrased)
- Diffusion models are inspired by non-equilibrium thermodynamics: a Markov chain slowly adds random noise to data, and a model learns to reverse it to build samples from noise.
- Unlike VAE or flow models, the procedure is fixed and the latent has the SAME dimensionality as the data.
- Forward: add Gaussian noise over T steps, each with variance beta_t; after enough steps x_T is close to an isotropic Gaussian.
- "Nice property": with alpha_t = 1 - beta_t and alpha-bar_t = product, x_t = sqrt(abar_t) x_0 + sqrt(1 - abar_t) eps (jump to any step directly).
- Reverse: a network learns each reverse step as a Gaussian; training uses a variational lower bound (like a VAE).
- DDPM simplified loss: predict the added noise with mean squared error.
- Noise schedules: linear (DDPM) 1e-4 to 0.02 with T = 1000; cosine schedule (Nichol & Dhariwal) changes noise more gently near the start and end.
- DDIM: deterministic when eta = 0; can skip steps (strided subset), so far fewer steps than DDPM with good quality.
- Other speedups: progressive distillation, consistency models.
- Classifier guidance uses gradients of a separate classifier; classifier-free guidance trains one network with the condition randomly dropped, then combines conditional and unconditional predictions at sampling time. GLIDE preferred CFG over CLIP guidance.
- Latent diffusion: autoencoder compresses images; diffusion runs in the smaller latent space; denoiser is a time-conditioned U-Net with cross-attention.
- U-Net: downsampling path (more channels, lower resolution), upsampling path, skip connections between them. DiT is a transformer alternative.
