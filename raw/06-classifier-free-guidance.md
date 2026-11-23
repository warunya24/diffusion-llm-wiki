# RAW CAPTURE: Classifier-Free Diffusion Guidance
- Authors: Jonathan Ho, Tim Salimans (Google Research, Brain team). arXiv 2207.12598, July 2022 (short version at NeurIPS 2021 workshop)
- URL: https://arxiv.org/abs/2207.12598 (read via ar5iv HTML)
- Captured: 2026-11-23

## Facts extracted (paraphrased)
- Classifier guidance (Dhariwal & Nichol 2021) needs an extra classifier trained on noisy images; it mixes the classifier's gradient into sampling, which looks like an adversarial attack on the classifier.
- Classifier-free guidance: jointly train a conditional and an unconditional model (one network; the condition is dropped with probability p_uncond), then combine the two predictions at sampling time.
- p_uncond tried: 0.1, 0.2, 0.5 on 64x64 ImageNet. 0.5 was worse; 0.1 and 0.2 were about equally good.
- Formula (paper, Eq. 6): eps_guided = (1 + w) * eps(x, c) - w * eps(x). w = 0 gives the plain conditional model.
- Increasing w: Inception score (fidelity) goes up; diversity goes down; best FID at small w (0.1 or 0.3 depending on dataset).
- Many later papers write the same rule as eps_uncond + s * (eps_cond - eps_uncond), where s = 1 + w. (seen in secondary sources found while searching, e.g. arXiv 2209.10948)
