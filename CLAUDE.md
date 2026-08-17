# CLAUDE.md — Pip Production System

Permanent production repo for the YouTube channel **Shows for Little Ones**
(`@showsforlittleones`) — original AI-generated toddler videos starring
**Pip**, **Teddy**, and **Mommy**.

## The deal

The user does one manual creative step: they write and generate an original
song in Suno. Then they upload the MP3 and give a short concept, e.g.:

> Pip's Water Park Fun Day. MP3 attached. Build this as a 16:9 Pip & Teddy adventure.

Everything after that is yours. Do not bury the user in planning questions.
Take initiative and deliver a finished MP4.

## Default pipeline

1. `ffprobe` the MP3 — duration, embedded title, embedded lyrics
2. Read the concept; pick Shorts (9:16) or Long-form (16:9)
3. Write a scene plan sized to the **real** song duration
4. Generate start images (Higgsfield, batched)
5. Poll with `jobs_wait`; retry failures intelligently
6. Animate each start image (`kling3_0`, sound `off`)
7. Poll again; retry failures
8. Normalize + assemble + crossfade (`scripts/assemble.py`)
9. Mux the user's MP3 as the sole audio bed
10. Verify runtime / resolution / file size
11. Write the episode package under `episodes/<slug>/`
12. Report the final path plus metadata

Detailed rules live in `docs/`. Do not duplicate them into episode files.

| Topic | File |
|---|---|
| Who Pip, Teddy and Mommy are; hard casting rules | `docs/CHARACTER_BIBLE.md` |
| Step-by-step production + ffmpeg recipes | `docs/PRODUCTION_WORKFLOW.md` |
| Long-form story beats | `docs/LONG_FORM_STORY_ENGINE.md` |
| Shorts format | `docs/SHORTS_PLAYBOOK.md` |
| **Verified** Higgsfield model IDs and params | `docs/HIGGSFIELD_REFERENCE.md` |
| Titles, descriptions, tags | `docs/METADATA_GUIDE.md` |

## Environment (read this first each session)

The container is **ephemeral and ships without ffmpeg**. Before any assembly:

```bash
bash scripts/setup_env.sh
```

It installs ffmpeg/ffprobe and verifies `libx264`, `aac` and the `xfade`
filter. Takes a few minutes on a cold container. Verified working on
ffmpeg 7:6.1.1 (Ubuntu 24.04).

## Non-negotiables

These exist because breaking them produces unusable video:

- **One adult, one toddler.** Never two Pips, never two Mommies, no random
  background children or bystanders unless the story truly requires them.
- **Mommy is a full-grown adult** and must be visibly much larger than Pip.
  She must never read as another child. This is the single most common
  failure mode — state it explicitly in every prompt containing both.
- **No on-screen text** except `Pip` in red bubble letters on the romper.
  No signs, labels, captions, logos or invented lettering.
- **Clips are generated silent** (`sound: "off"`). The user's Suno MP3 is the
  only audio. Never replace or loop their song.
- **Never reproduce** another channel's characters, lyrics, audio, shot
  sequences or thumbnail compositions. Structural principles only.

## Cost discipline

Generation spends real credits. Before a large batch, sanity-check the scene
plan. Do not silently re-run a whole batch to fix one scene — retry only the
failed indices. Never pass `use_unlim: true` on your own initiative.

## Repo conventions

- Episode assets go in `episodes/<slug>/`; start from `episodes/_TEMPLATE/`.
- Large media is gitignored. Commit `episode.md`, `metadata.md` and
  `manifest.json` — the prompts and job IDs are the valuable part, and they
  let a later session reproduce or extend an episode.
- Every episode records failed generations and what fixed them, so the next
  episode starts smarter.
