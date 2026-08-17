# Shows for Little Ones — Pip Production System

Production repo for the YouTube channel **[@showsforlittleones](https://www.youtube.com/@showsforlittleones)** —
original AI-generated toddler videos starring **Pip**, **Teddy**, and **Mommy**.

## How a video gets made

The only manual creative step is the song. You write and generate an original
track in Suno, upload the MP3 into a Claude Code session, and give a one-line
concept:

> Pip's Water Park Fun Day. MP3 attached. Build this as a 16:9 Pip & Teddy adventure.

Claude then inspects the audio, designs the story and scene plan, generates
every start image through Higgsfield, animates each scene, retries failures,
assembles the clips, muxes your MP3 as the audio bed, and exports the finished
MP4 plus an episode package.

## Two content engines

| | Shorts | Long-form |
|---|---|---|
| Aspect | 9:16 (1080x1920) | 16:9 (1920x1080) |
| Runtime | 20–40s | 2:45–5:00 |
| Content | Pip + Mommy daily-life routine, one literal activity | Pip's Little Adventures, full story arc |
| Role | proven discovery format | primary growth direction |

## Layout

```
docs/         permanent rules — character bible, workflow, story engine,
              verified Higgsfield parameters, metadata patterns
episodes/     one folder per episode; _TEMPLATE/ to copy from
scripts/      setup, audio inspection, assembly, QC
references/   approved character reference assets
```

## Quick start in a session

```bash
bash scripts/setup_env.sh                      # installs ffmpeg (container ships without it)
bash scripts/inspect_audio.sh episodes/<slug>/song/song.mp3
# ... generate images + clips ...
python3 scripts/assemble.py episodes/<slug>/manifest.json
bash scripts/helpers/verify_output.sh episodes/<slug>/renders/final.mp4 episodes/<slug>/song/song.mp3
```

## Notes

- Generated clips are silent by design; your Suno MP3 is the only audio and is
  never replaced or looped.
- Large media (`*.mp4`, `*.mp3`, images) is gitignored. The committed
  `episode.md` / `metadata.md` / `manifest.json` carry the prompts and job IDs,
  which is what lets a later session reproduce or extend an episode.
- Everything is original. Pip, Teddy and Mommy are their own world — no other
  channel's characters, lyrics, audio, shot sequences or thumbnails.

Start with **[CLAUDE.md](CLAUDE.md)**.
