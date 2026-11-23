# Forward process (adding noise)

## One-line definition
The fixed recipe that destroys an image by adding a little Gaussian noise at every step until only noise is left.

## Intuition / analogy
Like turning up TV static one notch at a time: after enough notches you can no longer see the show.

## Details
- The forward process q adds Gaussian noise over T steps. The amount per step is set by a variance schedule beta_1 … beta_T. [src: ddpm]
- The betas are fixed constants, so the forward process has **nothing to learn**. [src: ddpm]
- Shortcut: any noisy version x_t can be computed directly from the clean image x_0 in one formula (no need to loop through all earlier steps). [src: ddpm]
- After enough steps, x_T is almost pure isotropic Gaussian noise (no trace of the picture left). [src: weng-blog]
- Shortcut formula: x_t = sqrt(alpha-bar_t) * x_0 + sqrt(1 - alpha-bar_t) * noise, where alpha-bar_t multiplies together (1 - beta) of all earlier steps. [src: weng-blog]

## Key numbers
- T = 1000 steps in the DDPM experiments. [src: ddpm]

## Related
[noise-schedule](noise-schedule.md) · [reverse-process](reverse-process.md) · [diffusion-model](diffusion-model.md)
