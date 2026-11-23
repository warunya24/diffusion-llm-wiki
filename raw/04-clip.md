# RAW CAPTURE: CLIP (paper + OpenAI blog)
- Paper: Radford, Kim, Hallacy, Ramesh, Goh, Agarwal, et al., "Learning Transferable Visual Models From Natural Language Supervision", arXiv 2103.00020, Feb 2021 (ICML 2021)
- Blog: OpenAI, "CLIP: Connecting text and images", https://openai.com/research/clip
- Captured: 2026-11-23

## Facts extracted (paraphrased)
- CLIP = Contrastive Language-Image Pre-training.
- Pre-training task: predict which caption goes with which image. Paper: trained from scratch on 400 million (image, text) pairs collected from the internet.
- CLIP jointly trains an image encoder and a text encoder to predict correct pairings in a batch.
- Blog: proxy task = for an image, pick which of 32,768 randomly sampled text snippets was really paired with it.
- Contrastive objective was 4x to 10x more efficient than an image-to-text (caption-generating) objective for zero-shot ImageNet.
- Best model: Vision Transformer, trained on 256 GPUs for 2 weeks.
- Zero-shot classification: write class names as text ("a photo of a dog") and pick the best-matching text. Matches original ResNet-50 ImageNet accuracy zero-shot without using its 1.28 million labelled examples.
- Limitations: weak at counting, fine-grained types (car models, flowers), out-of-distribution images (MNIST 88%), sensitive to wording.
