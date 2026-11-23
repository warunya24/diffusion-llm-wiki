# Text encoder (CLIP text model)

## One-line definition
The part that turns your prompt into numbers (vectors) that capture its meaning, so the image model can "read" it.

## Intuition / analogy
A translator that converts a sentence into a language the painter understands: lists of numbers.

## Details
- Stable Diffusion's text encoder (ClipText) outputs 77 token embeddings, each a vector of 768 numbers. [src: alammar-illustrated-sd]
- CLIP is trained on image–caption pairs: matching pairs are pushed toward high cosine similarity, mismatched pairs toward low similarity. [src: alammar-illustrated-sd]
- CLIP = Contrastive Language–Image Pre-training: an image encoder and a text encoder are trained together to predict which caption belongs to which image. [src: clip]
- The training data are (image, text) pairs collected from the internet. [src: clip]
- Because text and images share one vector space, CLIP can classify images zero-shot by comparing them with text such as "a photo of a dog". [src: clip]
- Limitations: weak at counting objects and at fine-grained categories (car models, flower species); sensitive to wording. [src: clip]

> ⚠️ Conflict (found at ingest #4): Alammar presents "400 million pairs" only as an *illustrative* number, while the CLIP paper states 400 million (image, text) pairs as the real dataset size. **We trust the original paper** [src: clip]; Alammar's caveat is about the exact data (web images + alt text), not the count. [src: alammar-illustrated-sd]

## Key numbers
- 77 tokens × 768 dimensions. [src: alammar-illustrated-sd]
- Trained on 400 million (image, text) pairs. [src: clip]
- Blog proxy task: choose the right caption out of 32,768 text snippets. [src: clip]

## Related
[cross-attention](cross-attention.md) · [stable-diffusion-pipeline](stable-diffusion-pipeline.md)
