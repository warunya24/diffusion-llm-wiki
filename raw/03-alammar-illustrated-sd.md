# RAW CAPTURE: The Illustrated Stable Diffusion
- Author: Jay Alammar. Published 2022 (V2 Nov 2022, updated forward-diffusion images)
- URL: https://jalammar.github.io/illustrated-stable-diffusion/
- Captured: 2026-11-23

## Facts extracted (paraphrased)
- Stable Diffusion is a system of several components, not one model.
- Component 1: ClipText (text encoder). Input: text. Output: 77 token embeddings, each 768-dimensional.
- Component 2: UNet + Scheduler = "image information creator". Takes text embeddings + a random noise latent, refines it step by step. Steps often default to 50 or 100 in interfaces. Runs entirely in latent space, which is why it is faster than earlier pixel-space diffusion.
- Component 3: autoencoder decoder. Input: processed latent of shape (4, 64, 64). Output: RGB image of shape (3, 512, 512). Runs only once, at the end.
- Training data: take an image, add noise at different amounts (from none to total noise) -> many training examples per image.
- Noise predictor: given a noisy image + the step number, predict the noise; subtracting it moves the image toward the training-image distribution.
- Text conditioning: attention layers are added between the ResNet blocks of the UNet; they merge text representations into the latents.
- CLIP is trained on image-caption pairs; matching pairs pushed to high cosine similarity, mismatched ("negative") pairs to low. The article uses 400 million pairs as an illustrative figure and says CLIP was actually trained on web images with their alt tags.
