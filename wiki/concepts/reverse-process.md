# Reverse process (generating an image)

## One-line definition
Start from pure random noise and repeatedly subtract the noise the network predicts, until a clean image appears.

## Intuition / analogy
A sculptor removing a thin layer of stone each pass; after many passes a statue appears.

## Details
- Generation starts from a sample of standard Gaussian noise x_T. [src: ddpm]
- At every step from T down to 1, the predicted noise is removed and a small amount of fresh noise is added (except at the last step). [src: ddpm]
- Why do tools use only 50 or 100 steps if DDPM used 1000? Faster samplers such as DDIM can skip along a strided subset of steps with good quality (see sampling-steps). [src: weng-blog] [src: alammar-illustrated-sd]

## Key numbers
- DDPM runs the full 1000 steps to make one image. [src: ddpm]

## Related
[noise-prediction-training](noise-prediction-training.md) · [forward-process](forward-process.md) · [diffusion-model](diffusion-model.md)
[sampling-steps](sampling-steps.md) · [stable-diffusion-pipeline](stable-diffusion-pipeline.md)

