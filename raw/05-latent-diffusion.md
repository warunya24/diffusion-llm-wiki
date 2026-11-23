# RAW CAPTURE: Latent Diffusion Models (Stable Diffusion paper)
- Title: High-Resolution Image Synthesis with Latent Diffusion Models
- Authors: Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, Bjorn Ommer (LMU Munich & Heidelberg; Runway ML). CVPR 2022. arXiv 2112.10752
- URL: https://arxiv.org/abs/2112.10752 (read via ar5iv HTML)
- Captured: 2026-11-23

## Facts extracted (paraphrased)
- Pixel-space diffusion is expensive: training the strongest models can take hundreds of GPU days, and sampling needs many sequential network evaluations.
- Two stages: (1) pretrained autoencoder compresses images to a lower-dimensional latent space that is perceptually equivalent; (2) diffusion model trained in that latent space -> Latent Diffusion Models (LDMs).
- Downsampling factor f: f between 4 and 16 balances efficiency and quality; LDM-4 and LDM-8 are best for high-quality synthesis. Too large f loses detail; too small trains slowly.
- Conditioning: a domain-specific encoder tau_theta turns the condition (e.g. a text prompt) into an intermediate representation, injected into the UNet through cross-attention layers. Works for text, bounding boxes, etc.
- Text-to-image model: 1.45B parameters (LDM-KL-8) trained on LAION.
- Tasks: unconditional, class-conditional, text-to-image, layout-to-image, inpainting, super-resolution, semantic synthesis; new state of the art for inpainting and class-conditional synthesis with much lower compute than pixel-based DMs.
