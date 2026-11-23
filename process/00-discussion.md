# Step 0: "Discuss first, then generate"

Before generating any wiki page, I discussed the scope with the AI and agreed on the decisions below.
Only after this did ingest start.

## Topic
**How does AI turn text into images? (Diffusion models)**
Why this topic: it is the core technology behind my Generative AI final project (an AI song cover art generator),
so this wiki doubles as background research for that project.

## Audience
A classmate who knows what a neural network and a loss function are, but has never studied image generation.

## Questions the wiki must be able to answer
1. What does "diffusion" mean here? Why add noise to images on purpose?
2. How does the model learn? What exactly does the neural network predict?
3. How does a picture come out of pure noise?
4. Why is it fast enough to run on one GPU? (latent space)
5. How does the *text* get into the picture? (text encoder + cross-attention)
6. Why does a prompt get followed strongly? What is the "guidance scale"?
7. What happens, step by step, when I type a prompt into Stable Diffusion?

## Agreed concept pages (planned before ingest)
| Concept | Answers question |
|---|---|
| diffusion-model | 1 |
| forward-process, noise-schedule | 1 |
| noise-prediction-training | 2 |
| reverse-process | 3 |
| u-net | 2, 3 |
| sampling-steps | 3, 7 |
| latent-space | 4 |
| clip-text-encoder | 5 |
| cross-attention | 5 |
| classifier-free-guidance | 6 |
| stable-diffusion-pipeline | 7 (the "big picture" page) |

## Source plan (at least 5; we used 6)
| # | Source | Type | Why |
|---|---|---|---|
| 1 | Ho, Jain & Abbeel (2020), *Denoising Diffusion Probabilistic Models* | paper | the original DDPM math |
| 2 | Lilian Weng (2021, updated 2024), *What are Diffusion Models?* | blog | a clear overview of all concepts |
| 3 | Jay Alammar (2022), *The Illustrated Stable Diffusion* | blog | beginner-friendly pictures & shapes |
| 4 | Radford et al. (2021), *CLIP*, paper + OpenAI blog | paper/blog | how text is understood |
| 5 | Rombach et al. (2022), *Latent Diffusion Models* | paper | why it runs in latent space; cross-attention |
| 6 | Ho & Salimans (2022), *Classifier-Free Diffusion Guidance* | paper | the guidance scale |

## Ground rules we agreed on
- Explain in plain English first, math second (math is optional "for the curious").
- No number on any slide unless it is in the wiki with a source.
- If sources disagree, show the conflict instead of hiding it.
