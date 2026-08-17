# <Episode Title>

Copy this folder to `episodes/<episode-slug>/` and fill it in as you produce.
Do not restate the shared rules here — they live in `docs/`. This file records
what was *actually done* for this episode.

| | |
|---|---|
| **Slug** | `<episode-slug>` |
| **Format** | Long-form 16:9 / Short 9:16 |
| **Runtime** | `M:SS` (must match the song) |
| **Song file** | `song/<file>.mp3` |
| **Song duration** | `NN.NN s` (from `scripts/inspect_audio.sh`) |
| **Embedded title / lyrics** | yes / no — paste if present |
| **Output** | `renders/<file>.mp4` |
| **Thumbnail scene** | scene N — why it reads well at small size |

## Concept

The user's original one-line request, verbatim, then a sentence on how it was
interpreted.

## The two questions

1. **Why does a parent click this?**
2. **What does a child learn about Pip or Teddy?**

Both must have a real answer. See `docs/LONG_FORM_STORY_ENGINE.md`.

## Story summary

One short paragraph: beginning, middle, end.

## Scene timeline

| # | Time | Dur | Purpose | Comedy beat | Pip | Teddy | Mommy |
|---|------|-----|---------|-------------|-----|-------|-------|
| 1 | 0:00 | 8s | visual hook | | | | |
| 2 | 0:08 | 10s | Pip wants… | | | | |

## Scene prompts

### Scene 1 — <label>

- **Model**: `soul_2` (soul_id …) / `nano_banana_pro` (+ ref `54c9aaff…`)
- **Image job**: `<job-id>`
- **Video job**: `<job-id>`

**Start image prompt**

> …

**Motion prompt**

> …

## Model / job notes

Which model each scene used and why, plus anything surprising.

## Failures and retries

**This section is the point of the file.** Record what failed, the error, and
what fixed it, so the next episode does not rediscover it.

| Scene | What happened | Fix |
|---|---|---|
| | | |

## Assembly

```bash
bash scripts/setup_env.sh
python3 scripts/assemble.py episodes/<slug>/manifest.json
bash scripts/helpers/verify_output.sh episodes/<slug>/renders/<file>.mp4 episodes/<slug>/song/<file>.mp3
```

Final verified numbers: runtime, resolution, file size.
