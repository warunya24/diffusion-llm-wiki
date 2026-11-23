# Sampling steps (and why fewer steps can work)

## One-line definition
How many denoising passes the model makes to produce one image; smarter samplers can skip most of the original steps.

## Intuition / analogy
Walking down a staircase of 1000 steps vs. taking the same staircase two or three steps at a time: you reach the bottom much faster.

## Details
- DDIM generalises the DDPM reverse process; with its parameter eta = 0 the process becomes deterministic (same noise in → same image out). [src: weng-blog]
- DDIM can follow a strided subset of the steps, so it needs far fewer steps than DDPM while keeping good quality. [src: weng-blog]
- Other ways to speed up: progressive distillation and consistency models. [src: weng-blog]
- In Stable Diffusion interfaces the number of steps often defaults to 50 or 100. [src: alammar-illustrated-sd]

## Key numbers
- DDPM training uses T = 1000 steps. [src: weng-blog]
- Typical default in Stable Diffusion tools: 50 or 100 steps. [src: alammar-illustrated-sd]

## Related
[reverse-process](reverse-process.md) · [noise-schedule](noise-schedule.md)
