# Diffusion model

## One-line definition
A generative model that learns to turn random noise into a realistic image by removing noise a little at a time.

## Intuition / analogy
Imagine slowly dropping ink into clear water until it is completely cloudy. A diffusion model is trained to *run that movie backwards*: from a cloudy glass back to the clean picture.

## Details
- A diffusion model is a chain of small steps (a Markov chain), trained so that after a fixed number of steps it outputs samples that look like the training data. [src: ddpm]
- It has two halves: a fixed forward process that adds noise, and a learned reverse process that removes it. [src: ddpm]
- The idea is inspired by non-equilibrium thermodynamics: slowly add random noise to data, then learn to reverse that process. [src: weng-blog]
- Unlike VAEs or flow models, the noising procedure is fixed and the hidden variables have the same size as the image itself. [src: weng-blog]

## Key numbers
- DDPM reached FID 3.17 on unconditional CIFAR10 (lower FID = better image quality). [src: ddpm]

## Related
[forward-process](forward-process.md) · [reverse-process](reverse-process.md) · [noise-prediction-training](noise-prediction-training.md)
