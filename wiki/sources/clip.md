# Source: CLIP (Radford et al., 2021) + OpenAI blog
- **Citation:** A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, et al. *Learning Transferable Visual Models From Natural Language Supervision*. ICML 2021. https://arxiv.org/abs/2103.00020 · Blog: https://openai.com/research/clip
- **Raw capture:** [04-clip.md](../../raw/04-clip.md)
- **Type:** research paper + official blog

## Key takeaways
1. CLIP learns by playing "which caption belongs to which image?" on internet data.
2. It trains an image encoder and a text encoder together, so matching text and images end up close in the same vector space.
3. Trained on 400 million (image, text) pairs.
4. Can classify images "zero-shot" just from text labels.
5. Weak at counting and very fine-grained categories.

## Feeds concept pages
[clip-text-encoder](../concepts/clip-text-encoder.md)
