# Fact sheet: generated from the wiki before writing slides

Rule: a slide may only use numbers in its *allowed numbers* list and terms in *allowed terms*.

## Slide 1: Title
- wiki pages: index.md, concepts/diffusion-model.md
- defines here: diffusion model
- allowed terms: diffusion model
- NOT yet allowed: forward process, reverse process, noise schedule, noise prediction, u-net, ddim, sampling steps, latent space, autoencoder, clip, text encoder, cross-attention, classifier-free guidance, guidance scale
- allowed numbers: 3.17, 10, 2020
- numeric facts available:
  - - [ddpm: DDPM paper (2020)  ← `index.md`
  - - DDPM reached FID 3.17 on unconditional CIFAR10 (lower FID = better image quality).  ← `concepts/diffusion-model.md`

## Slide 2: The questions we will answer
- wiki pages: index.md
- defines here: -
- allowed terms: diffusion model
- NOT yet allowed: forward process, reverse process, noise schedule, noise prediction, u-net, ddim, sampling steps, latent space, autoencoder, clip, text encoder, cross-attention, classifier-free guidance, guidance scale
- allowed numbers: 2020
- numeric facts available:
  - - [ddpm: DDPM paper (2020)  ← `index.md`

## Slide 3: The big idea
- wiki pages: concepts/diffusion-model.md, sources/ddpm.md
- defines here: forward process, reverse process
- allowed terms: diffusion model, forward process, reverse process
- NOT yet allowed: noise schedule, noise prediction, u-net, ddim, sampling steps, latent space, autoencoder, clip, text encoder, cross-attention, classifier-free guidance, guidance scale
- allowed numbers: 01, 1, 2, 3, 3.17, 4, 5, 10, 1000, 2006.11239, 2020
- numeric facts available:
  - - DDPM reached FID 3.17 on unconditional CIFAR10 (lower FID = better image quality).  ← `concepts/diffusion-model.md`
  - - **Citation:** J. Ho, A. Jain, P. Abbeel. *Denoising Diffusion Probabilistic Models*. NeurIPS 2020. https://arxiv.org/abs/2006.11239  ← `sources/ddpm.md`
  - - **Raw capture:** [01-ddpm-paper.md  ← `sources/ddpm.md`
  - 1. The forward (noising) process is fixed: no learning, just a schedule of noise amounts.  ← `sources/ddpm.md`
  - 2. You can jump straight from a clean image to any noise level in one formula.  ← `sources/ddpm.md`
  - 3. The neural network only has to predict **the noise** that was added. The loss is a simple mean squared error.  ← `sources/ddpm.md`
  - 4. Generation = start from pure noise and remove predicted noise step by step (1000 steps in the paper).  ← `sources/ddpm.md`
  - 5. Backbone network is a U-Net that is told the time step.  ← `sources/ddpm.md`

## Slide 4: Forward process (interactive)
- wiki pages: concepts/forward-process.md, concepts/noise-schedule.md
- defines here: noise schedule
- allowed terms: diffusion model, forward process, reverse process, noise schedule
- NOT yet allowed: noise prediction, u-net, ddim, sampling steps, latent space, autoencoder, clip, text encoder, cross-attention, classifier-free guidance, guidance scale
- allowed numbers: 0, 1e-4, 0.02, 1, 1000
- numeric facts available:
  - - The forward process q adds Gaussian noise over T steps. The amount per step is set by a variance schedule beta_1 … beta_T.  ← `concepts/forward-process.md`
  - - Shortcut: any noisy version x_t can be computed directly from the clean image x_0 in one formula (no need to loop through all earlier steps).  ← `concepts/forward-process.md`
  - - Shortcut formula: x_t = sqrt(alpha-bar_t) * x_0 + sqrt(1 - alpha-bar_t) * noise, where alpha-bar_t multiplies together (1 - beta) of all earlier steps.  ← `concepts/forward-process.md`
  - - T = 1000 steps in the DDPM experiments.  ← `concepts/forward-process.md`
  - - Linear schedule from beta_1 = 1e-4 to beta_T = 0.02 with T = 1000.  ← `concepts/noise-schedule.md`
  - - Weng's summary of the DDPM linear schedule: 1e-4 to 0.02, T = 1000 (agrees with the paper).  ← `concepts/noise-schedule.md`

## Slide 5: Shortcut formula
- wiki pages: concepts/forward-process.md, concepts/noise-schedule.md
- defines here: -
- allowed terms: diffusion model, forward process, reverse process, noise schedule
- NOT yet allowed: noise prediction, u-net, ddim, sampling steps, latent space, autoencoder, clip, text encoder, cross-attention, classifier-free guidance, guidance scale
- allowed numbers: 0, 1e-4, 0.02, 1, 1000
- numeric facts available:
  - - The forward process q adds Gaussian noise over T steps. The amount per step is set by a variance schedule beta_1 … beta_T.  ← `concepts/forward-process.md`
  - - Shortcut: any noisy version x_t can be computed directly from the clean image x_0 in one formula (no need to loop through all earlier steps).  ← `concepts/forward-process.md`
  - - Shortcut formula: x_t = sqrt(alpha-bar_t) * x_0 + sqrt(1 - alpha-bar_t) * noise, where alpha-bar_t multiplies together (1 - beta) of all earlier steps.  ← `concepts/forward-process.md`
  - - T = 1000 steps in the DDPM experiments.  ← `concepts/forward-process.md`
  - - Linear schedule from beta_1 = 1e-4 to beta_T = 0.02 with T = 1000.  ← `concepts/noise-schedule.md`
  - - Weng's summary of the DDPM linear schedule: 1e-4 to 0.02, T = 1000 (agrees with the paper).  ← `concepts/noise-schedule.md`

## Slide 6: Training: guess the noise
- wiki pages: concepts/noise-prediction-training.md
- defines here: noise prediction
- allowed terms: diffusion model, forward process, reverse process, noise schedule, noise prediction
- NOT yet allowed: u-net, ddim, sampling steps, latent space, autoencoder, clip, text encoder, cross-attention, classifier-free guidance, guidance scale
- allowed numbers: 1, 1000
- numeric facts available:
  - - The step t is drawn uniformly from 1 to T, with T = 1000.  ← `concepts/noise-prediction-training.md`

## Slide 7: U-Net
- wiki pages: concepts/u-net.md
- defines here: u-net
- allowed terms: diffusion model, forward process, reverse process, noise schedule, noise prediction, u-net
- NOT yet allowed: ddim, sampling steps, latent space, autoencoder, clip, text encoder, cross-attention, classifier-free guidance, guidance scale
- allowed numbers: 16
- numeric facts available:
  - - Self-attention is used at the 16x16 feature-map resolution.  ← `concepts/u-net.md`
  - - Self-attention at 16x16 resolution.  ← `concepts/u-net.md`

## Slide 8: Reverse process (animation)
- wiki pages: concepts/reverse-process.md
- defines here: -
- allowed terms: diffusion model, forward process, reverse process, noise schedule, noise prediction, u-net
- NOT yet allowed: ddim, sampling steps, latent space, autoencoder, clip, text encoder, cross-attention, classifier-free guidance, guidance scale
- allowed numbers: 1, 50, 100, 1000
- numeric facts available:
  - - At every step from T down to 1, the predicted noise is removed and a small amount of fresh noise is added (except at the last step).  ← `concepts/reverse-process.md`
  - - Why do tools use only 50 or 100 steps if DDPM used 1000? Faster samplers such as DDIM can skip along a strided subset of steps with good quality (see sampling-steps).  ← `concepts/reverse-process.md`
  - - DDPM runs the full 1000 steps to make one image.  ← `concepts/reverse-process.md`

## Slide 9: Fewer steps: DDIM
- wiki pages: concepts/sampling-steps.md, concepts/reverse-process.md
- defines here: ddim, sampling steps
- allowed terms: diffusion model, forward process, reverse process, noise schedule, noise prediction, u-net, ddim, sampling steps
- NOT yet allowed: latent space, autoencoder, clip, text encoder, cross-attention, classifier-free guidance, guidance scale
- allowed numbers: 0, 1, 50, 100, 1000
- numeric facts available:
  - - DDIM generalises the DDPM reverse process; with its parameter eta = 0 the process becomes deterministic (same noise in → same image out).  ← `concepts/sampling-steps.md`
  - - In Stable Diffusion interfaces the number of steps often defaults to 50 or 100.  ← `concepts/sampling-steps.md`
  - - DDPM training uses T = 1000 steps.  ← `concepts/sampling-steps.md`
  - - Typical default in Stable Diffusion tools: 50 or 100 steps.  ← `concepts/sampling-steps.md`
  - - At every step from T down to 1, the predicted noise is removed and a small amount of fresh noise is added (except at the last step).  ← `concepts/reverse-process.md`
  - - Why do tools use only 50 or 100 steps if DDPM used 1000? Faster samplers such as DDIM can skip along a strided subset of steps with good quality (see sampling-steps).  ← `concepts/reverse-process.md`
  - - DDPM runs the full 1000 steps to make one image.  ← `concepts/reverse-process.md`

## Slide 10: Latent space
- wiki pages: concepts/latent-space.md
- defines here: latent space, autoencoder
- allowed terms: diffusion model, forward process, reverse process, noise schedule, noise prediction, u-net, ddim, sampling steps, latent space, autoencoder
- NOT yet allowed: clip, text encoder, cross-attention, classifier-free guidance, guidance scale
- allowed numbers: 1, 2, 3, 4, 8, 16, 64, 512
- numeric facts available:
  - - Stable Diffusion denoises a latent of shape (4, 64, 64); the autoencoder's decoder turns it into an RGB image of shape (3, 512, 512), running only once at the end.  ← `concepts/latent-space.md`
  - - Two stages: (1) a pretrained autoencoder compresses images into a latent that still looks the same to humans; (2) the diffusion model is trained in that latent space.  ← `concepts/latent-space.md`
  - - Compression factor f: values from 4 to 16 balance speed and quality; f = 4 and f = 8 gave the best results. Too much compression loses detail; too little trains slowly.  ← `concepts/latent-space.md`
  - - Latent (4, 64, 64) → image (3, 512, 512).  ← `concepts/latent-space.md`
  - - Downsampling factor f = 4 to 16 works well; best at 4 and 8.  ← `concepts/latent-space.md`

## Slide 11: CLIP text encoder
- wiki pages: concepts/clip-text-encoder.md
- defines here: clip, text encoder
- allowed terms: diffusion model, forward process, reverse process, noise schedule, noise prediction, u-net, ddim, sampling steps, latent space, autoencoder, clip, text encoder
- NOT yet allowed: cross-attention, classifier-free guidance, guidance scale
- allowed numbers: 77, 400, 768, 32768
- numeric facts available:
  - - Stable Diffusion's text encoder (ClipText) outputs 77 token embeddings, each a vector of 768 numbers.  ← `concepts/clip-text-encoder.md`
  - - 77 tokens × 768 dimensions.  ← `concepts/clip-text-encoder.md`
  - - Trained on 400 million (image, text) pairs.  ← `concepts/clip-text-encoder.md`
  - - Blog proxy task: choose the right caption out of 32,768 text snippets.  ← `concepts/clip-text-encoder.md`

## Slide 12: Cross-attention
- wiki pages: concepts/cross-attention.md, concepts/u-net.md
- defines here: cross-attention
- allowed terms: diffusion model, forward process, reverse process, noise schedule, noise prediction, u-net, ddim, sampling steps, latent space, autoencoder, clip, text encoder, cross-attention
- NOT yet allowed: classifier-free guidance, guidance scale
- allowed numbers: 16
- numeric facts available:
  - - Self-attention is used at the 16x16 feature-map resolution.  ← `concepts/u-net.md`
  - - Self-attention at 16x16 resolution.  ← `concepts/u-net.md`

## Slide 13: Classifier-free guidance (interactive)
- wiki pages: concepts/classifier-free-guidance.md
- defines here: classifier-free guidance, guidance scale
- allowed terms: diffusion model, forward process, reverse process, noise schedule, noise prediction, u-net, ddim, sampling steps, latent space, autoencoder, clip, text encoder, cross-attention, classifier-free guidance, guidance scale
- NOT yet allowed: -
- allowed numbers: 0, 0.1, 0.2, 0.3, 0.5, 1
- numeric facts available:
  - - Paper's formula: guided noise = (1 + w) × noise_with_prompt − w × noise_without_prompt; w = 0 means no extra guidance.  ← `concepts/classifier-free-guidance.md`
  - - p_uncond tested: 0.1, 0.2, 0.5; 0.1 and 0.2 worked equally well, 0.5 was worse.  ← `concepts/classifier-free-guidance.md`
  - - Best FID at w = 0.1 or 0.3 (depends on dataset).  ← `concepts/classifier-free-guidance.md`

## Slide 14: Pipeline
- wiki pages: concepts/stable-diffusion-pipeline.md
- defines here: -
- allowed terms: diffusion model, forward process, reverse process, noise schedule, noise prediction, u-net, ddim, sampling steps, latent space, autoencoder, clip, text encoder, cross-attention, classifier-free guidance, guidance scale
- NOT yet allowed: -
- allowed numbers: 1, 1.45, 2, 3, 4, 50, 64, 77, 100, 512, 768
- numeric facts available:
  - - Step 1, text encoder (ClipText): prompt → 77 × 768 token embeddings.  ← `concepts/stable-diffusion-pipeline.md`
  - - Step 2, image information creator (U-Net + scheduler): starts from random noise in latent space and refines it step by step, using the text embeddings.  ← `concepts/stable-diffusion-pipeline.md`
  - - Step 3, image decoder (autoencoder): turns the final latent into the full-size image once.  ← `concepts/stable-diffusion-pipeline.md`
  - - The paper's text-to-image model has 1.45B parameters and was trained on the LAION dataset.  ← `concepts/stable-diffusion-pipeline.md`
  - - Text 77 × 768; latent (4, 64, 64); image (3, 512, 512); 50 or 100 steps by default.  ← `concepts/stable-diffusion-pipeline.md`
  - - Text-to-image latent diffusion model: 1.45B parameters.  ← `concepts/stable-diffusion-pipeline.md`

## Slide 15: Quiz
- wiki pages: concepts/noise-prediction-training.md, concepts/forward-process.md, concepts/latent-space.md, concepts/classifier-free-guidance.md, concepts/clip-text-encoder.md
- defines here: -
- allowed terms: diffusion model, forward process, reverse process, noise schedule, noise prediction, u-net, ddim, sampling steps, latent space, autoencoder, clip, text encoder, cross-attention, classifier-free guidance, guidance scale
- NOT yet allowed: -
- allowed numbers: 0, 0.1, 0.2, 0.3, 0.5, 1, 2, 3, 4, 8, 16, 64, 77, 400, 512, 768, 1000, 32768
- numeric facts available:
  - - The step t is drawn uniformly from 1 to T, with T = 1000.  ← `concepts/noise-prediction-training.md`
  - - The forward process q adds Gaussian noise over T steps. The amount per step is set by a variance schedule beta_1 … beta_T.  ← `concepts/forward-process.md`
  - - Shortcut: any noisy version x_t can be computed directly from the clean image x_0 in one formula (no need to loop through all earlier steps).  ← `concepts/forward-process.md`
  - - Shortcut formula: x_t = sqrt(alpha-bar_t) * x_0 + sqrt(1 - alpha-bar_t) * noise, where alpha-bar_t multiplies together (1 - beta) of all earlier steps.  ← `concepts/forward-process.md`
  - - T = 1000 steps in the DDPM experiments.  ← `concepts/forward-process.md`
  - - Stable Diffusion denoises a latent of shape (4, 64, 64); the autoencoder's decoder turns it into an RGB image of shape (3, 512, 512), running only once at the end.  ← `concepts/latent-space.md`
  - - Two stages: (1) a pretrained autoencoder compresses images into a latent that still looks the same to humans; (2) the diffusion model is trained in that latent space.  ← `concepts/latent-space.md`
  - - Compression factor f: values from 4 to 16 balance speed and quality; f = 4 and f = 8 gave the best results. Too much compression loses detail; too little trains slowly.  ← `concepts/latent-space.md`

## Slide 16: Summary
- wiki pages: index.md, concepts/stable-diffusion-pipeline.md, concepts/sampling-steps.md, sources/clip.md, sources/latent-diffusion.md, sources/classifier-free-guidance-paper.md
- defines here: -
- allowed terms: diffusion model, forward process, reverse process, noise schedule, noise prediction, u-net, ddim, sampling steps, latent space, autoencoder, clip, text encoder, cross-attention, classifier-free guidance, guidance scale
- NOT yet allowed: -
- allowed numbers: 0, 1, 1.45, 2, 3, 4, 04, 5, 05, 06, 8, 10, 16, 20, 50, 64, 77, 100, 400, 512, 768, 1000, 2020, 2021, 2022, 2103.00020, 2112.10752, 2207.12598
- numeric facts available:
  - - [ddpm: DDPM paper (2020)  ← `index.md`
  - - Step 1, text encoder (ClipText): prompt → 77 × 768 token embeddings.  ← `concepts/stable-diffusion-pipeline.md`
  - - Step 2, image information creator (U-Net + scheduler): starts from random noise in latent space and refines it step by step, using the text embeddings.  ← `concepts/stable-diffusion-pipeline.md`
  - - Step 3, image decoder (autoencoder): turns the final latent into the full-size image once.  ← `concepts/stable-diffusion-pipeline.md`
  - - The paper's text-to-image model has 1.45B parameters and was trained on the LAION dataset.  ← `concepts/stable-diffusion-pipeline.md`
  - - Text 77 × 768; latent (4, 64, 64); image (3, 512, 512); 50 or 100 steps by default.  ← `concepts/stable-diffusion-pipeline.md`
  - - Text-to-image latent diffusion model: 1.45B parameters.  ← `concepts/stable-diffusion-pipeline.md`
  - - DDIM generalises the DDPM reverse process; with its parameter eta = 0 the process becomes deterministic (same noise in → same image out).  ← `concepts/sampling-steps.md`

