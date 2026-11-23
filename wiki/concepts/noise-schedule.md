# Noise schedule

## One-line definition
The list that says how much noise is added at each step of the forward process.

## Intuition / analogy
A volume plan for the static: start very quiet, end very loud.

## Details
- DDPM uses a linear schedule: beta grows in a straight line from a tiny value to a larger value. [src: ddpm]
- The cosine schedule (Nichol & Dhariwal) changes the noise level more gently near the start and the end of the process. [src: weng-blog]

## Key numbers
- Linear schedule from beta_1 = 1e-4 to beta_T = 0.02 with T = 1000. [src: ddpm]
- Weng's summary of the DDPM linear schedule: 1e-4 to 0.02, T = 1000 (agrees with the paper). [src: weng-blog]

## Related
[forward-process](forward-process.md)
