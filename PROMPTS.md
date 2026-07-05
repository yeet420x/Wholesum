# $WHOLESUM — image generation kit

Goal: the $ANSEM "Black Bull" format, but it's a **capybara** wearing the same face. No horns. Same dead-calm energy.

> Heads-up: the face in that artwork is a real person's (Ansem's) likeness, and he has publicly said he doesn't endorse coins using it — whether to use it is your call, same situation as the original $ANSEM art.

## How to use

1. Get the face reference: run `python extract_face.py` (needs `assets/blackbull.png` — the bull image saved from chat). It produces:
   - `assets/wholesum-face.png` — rectangular crop
   - `assets/wholesum-face-oval.png` — feathered oval on transparent background ← **use this one as the reference**
2. Feed the reference + a prompt below into your generator:
   - **Midjourney:** upload the oval face, then `--cref <image url> --cw 100 --ar 1:1`
   - **GPT-4o / Gemini / Flux (Krea, fal, etc.):** attach the oval face as a reference image and paste the prompt as-is
3. Generate square (1:1), at least 1024×1024.
4. Save the winner as `assets/wholesum.png` — the website picks it up automatically (until then it shows the "wholesum is being born" placeholder).

## Prompt 1 — the Black Bull parody (recommended)

This is the recognizable format; the site's pastel vibe makes the contrast funnier.

```
Hyper-realistic studio photograph of a capybara standing and facing the camera
against a pure black void background, dramatic low-key cinematic lighting.
The capybara's face is seamlessly replaced with the human face from the
reference image — same serene, unbothered, dead-calm expression, long dark
hair blending naturally into the capybara's brown fur. No horns. The body is
unmistakably a chubby, round capybara. Fur texture photorealistic, moody rim
lighting from above, dark and ominous yet strangely peaceful. Square format,
subject centered, styled exactly like a dramatic wildlife portrait.
```

## Prompt 2 — wholesome-core version (matches the site)

```
Soft dreamy pastel photograph of a capybara sitting peacefully in a field of
flowers under a pink-and-lavender sky, golden-hour glow, floating sparkles.
The capybara's face is seamlessly replaced with the human face from the
reference image, wearing a faint serene smile, long dark hair blending into
its fur. No horns. Cozy, heavenly, wholesome children's-book atmosphere; the
realistic human face makes it subtly uncanny. Square format, centered.
```

## Tweaks that help

- If the generator keeps drawing horns: add `absolutely no horns, no bull features, smooth round capybara head` to the end.
- If the face comes out cartoonish: add `the human face is photorealistic, matching the reference exactly`.
- If the body drifts toward "bull": add `short stubby legs, barrel-shaped capybara body, small round ears on top of the head`.
- For a hot-spring variant (peak capybara lore): swap the setting for `sitting neck-deep in a steaming natural hot spring, a yuzu orange floating on the water`.
