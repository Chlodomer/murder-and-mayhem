# Murder & Mayhem in Merovingian Tours

A SimCity-style 3D simulation of the violent dispute between **Sichar and Chramnesind** (Tours, A.D. 585–588), as recorded by Gregory of Tours, *Histories* VII.47 & IX.19.

**[▶ Play it here](https://chlodomer.github.io/murder-and-mayhem/)**

## What it is

A single-file Three.js scene that plays the whole affair as 14 cinematic scenes across six acts — the Christmas killing at Manthelan, the church brawl, Austregisel's plunder, Sichar's night raid on Auno's farmstead, Bishop Gregory's failed peace offer, the false rumor of Sichar's death, Chramnesind's arson, the tribunal settlement, the strange friendship, and the fatal dinner of 588.

- Isometric low-poly Touraine: walled Tours on the Loire, Manthelan, two villas, lakes, hills, woods
- Scripted scene engine with English narration + the original Latin
- Cinematic camera: drone descents through clouds, hard cuts, orbits, tracking shots, slow-motion kills
- Sword-and-shield combat, horses, fire and smoke, weather and a full day/night cycle
- Character voices, sound effects, and music generated with the ElevenLabs API
- Retro game chrome: vengeance meter, church treasury, newspaper headlines, CRT intro

## Run locally

Any static server works:

```sh
python3 -m http.server 8642
# open http://localhost:8642
```

## Controls

Drag to orbit · wheel to zoom · space to pause · ←/→ scenes · diamond dots jump anywhere · 1×/2×/4× speed · SND toggle

## Credits

Source text: Gregory of Tours, *Decem Libri Historiarum* VII.47 & IX.19 (MGH SS rer. Merov. I).
Audio (voices, SFX, music) generated with the ElevenLabs API — regeneration scripts in `sfx/`.
Built with [Three.js](https://threejs.org/).
