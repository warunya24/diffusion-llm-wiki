# Training by predicting noise

## One-line definition
The model is trained with one simple game: "here is a noisy image, guess exactly which noise was added".

## Intuition / analogy
A teacher splashes a known pattern of paint on a photo and asks the student to point out the splash. Because the teacher made the splash, the correct answer is always known, so there are no human labels needed.

## Details
- The network eps_theta(x_t, t) receives the noisy image and the step number t and predicts the noise inside it. [src: ddpm]
- Loss = mean squared error between the real noise and the predicted noise (called L_simple). [src: ddpm]
- Training loop: pick a training image, pick a random step t, sample noise, make the noisy image, take a gradient step on the loss. [src: ddpm]
- One training image gives many training examples, because noise can be added at many different amounts (from none to total noise). [src: alammar-illustrated-sd]

## Key numbers
- The step t is drawn uniformly from 1 to T, with T = 1000. [src: ddpm]

## Related
[forward-process](forward-process.md) · [reverse-process](reverse-process.md) · [u-net](u-net.md)
