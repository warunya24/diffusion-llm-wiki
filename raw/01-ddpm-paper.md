# RAW CAPTURE: DDPM paper
- Title: Denoising Diffusion Probabilistic Models
- Authors: Jonathan Ho, Ajay Jain, Pieter Abbeel (UC Berkeley), NeurIPS 2020
- URL: https://arxiv.org/abs/2006.11239  (read via ar5iv HTML version)
- Captured: 2026-11-23

## Facts extracted (paraphrased, not copied)
- A diffusion model is a parameterized Markov chain trained with variational inference so that, after a finite number of steps, it produces samples that look like the data.
- Forward process q: a FIXED chain that adds Gaussian noise over T steps with a variance schedule beta_1..beta_T. The betas are constants, so q has nothing to learn.
- Closed form: any noisy x_t can be computed directly from x_0 using alpha-bar_t (product of 1-beta).
- Experiments: T = 1000; betas increase linearly from 1e-4 (beta_1) to 0.02 (beta_T).
- Reverse process p_theta: learned chain that starts from a standard Gaussian and uses Gaussian transitions.
- Parameterization: the network eps_theta(x_t, t) predicts the noise contained in x_t.
- Simplified objective L_simple: mean squared error between the true noise eps and the predicted noise; t sampled uniformly from 1..T. Drops the weighting of the full bound.
- Algorithm 1 (training): repeat: take a data image x_0, pick random t, sample noise eps, gradient step on ||eps - eps_theta(sqrt(abar_t) x_0 + sqrt(1-abar_t) eps, t)||^2.
- Algorithm 2 (sampling): start from x_T ~ N(0,I); for t = T..1 remove predicted noise and add a little fresh noise (except the last step); return x_0.
- Backbone: U-Net similar to unmasked PixelCNN++, group normalization, weights shared across time, time step given by Transformer sinusoidal position embedding, self-attention at 16x16 resolution.
- Result: unconditional CIFAR10 Inception score 9.46, FID 3.17 (state of the art at the time); 256x256 LSUN quality similar to ProgressiveGAN.
