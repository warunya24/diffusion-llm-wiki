# Cross-attention (how the text gets into the picture)

## One-line definition
Layers inside the U-Net that let each part of the image "look at" the words of the prompt and use the relevant ones.

## Intuition / analogy
While painting each region, the artist glances at the shopping list of words ("red", "cat", "sofa") and picks the word that matters for that spot.

## Details
- Stable Diffusion adds attention layers between the ResNet blocks of the U-Net; they merge the text representations into the latent so the next block can use the text information. [src: alammar-illustrated-sd]
- In latent diffusion, a separate domain-specific encoder turns the condition (e.g. a text prompt) into a representation, which cross-attention layers inject into the U-Net. [src: latent-diffusion]
- The same mechanism works for other conditions such as bounding boxes / layouts. [src: latent-diffusion]

## Key numbers
_(none yet)_

## Related
[clip-text-encoder](clip-text-encoder.md) · [u-net](u-net.md)
