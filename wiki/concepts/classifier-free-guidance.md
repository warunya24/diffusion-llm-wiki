# Classifier-free guidance (CFG, the "guidance scale")

## One-line definition
A trick that makes the image follow the prompt more strongly by comparing "what the model would draw with the prompt" vs "without the prompt" and pushing further in that direction.

## Intuition / analogy
Ask an artist to draw "anything", then "a cat". The difference between the two drawings is "cat-ness". Guidance exaggerates that difference.

## Details
- Older classifier guidance used the gradients of a separate classifier to steer the noise prediction. [src: weng-blog]
- Classifier-free guidance trains one network with the condition randomly dropped, so it learns both conditional and unconditional predictions, then combines them while sampling. [src: weng-blog]
- GLIDE found classifier-free guidance worked better than CLIP guidance. [src: weng-blog]
- Problem with classifier guidance: it needs an extra classifier trained on noisy images, and mixing in its gradient resembles an adversarial attack on that classifier. [src: classifier-free-guidance-paper]
- CFG trains a single network on both tasks: the condition is replaced by "empty" with probability p_uncond during training. [src: classifier-free-guidance-paper]
- Paper's formula: guided noise = (1 + w) × noise_with_prompt − w × noise_without_prompt; w = 0 means no extra guidance. [src: classifier-free-guidance-paper]
- Larger w → higher fidelity (Inception score rises) but less diversity; the best FID came at small w. [src: classifier-free-guidance-paper]

> ⚠️ Conflict (found at ingest #6): the paper writes (1 + w)·cond − w·uncond, but most later papers and tools write uncond + s·(cond − uncond). These are the **same rule** with s = 1 + w. So a tool's "guidance scale" s is *not* the paper's w (s = 1 means no extra guidance). [src: classifier-free-guidance-paper]

## Key numbers
- p_uncond tested: 0.1, 0.2, 0.5; 0.1 and 0.2 worked equally well, 0.5 was worse. [src: classifier-free-guidance-paper]
- Best FID at w = 0.1 or 0.3 (depends on dataset). [src: classifier-free-guidance-paper]

## Related
[reverse-process](reverse-process.md) · [stable-diffusion-pipeline](stable-diffusion-pipeline.md) · [clip-text-encoder](clip-text-encoder.md)
