# Production Workflow

From "MP3 + one-line concept" to a finished MP4.

## 0. Environment

```bash
bash scripts/setup_env.sh
```

The container ships **without ffmpeg** and is wiped between sessions. Do this
before any assembly step or you will lose work to a missing binary.

## 1. Inspect the song first — always

Never plan against a guessed duration.

```bash
bash scripts/inspect_audio.sh path/to/song.mp3
```

or directly:

```bash
ffprobe -v error -show_entries format_tags -show_entries format=duration song.mp3
```

Pull out duration, embedded title, and embedded lyrics if present.

Then decide how the visuals bind to the audio:

- **Lyrics narrate actions** → align scenes tightly to the lyric lines
- **Thematic / instrumental** → build around musical sections, chorus
  returns and major beats

The song defines the runtime. Do not loop the song to fit the video; size the
video to the song.

## 2. Pick the format

| | Shorts | Long-form |
|---|---|---|
| Aspect | 9:16 | 16:9 |
| Canvas | 1080x1920 | 1920x1080 |
| Runtime | 20–40s | 2:45–5:00 |
| Shape | one literal activity | full story arc |

See `docs/SHORTS_PLAYBOOK.md` and `docs/LONG_FORM_STORY_ENGINE.md`.

## 3. Scene plan

Write the plan before spending a single credit. Per scene:

scene number · song timestamp · duration · story purpose · start-image
composition · motion/action · comedy beat · Pip emotion · Teddy involvement ·
Mommy involvement · which model

Scene durations should **vary**. Do not force everything into identical 10s
blocks — it reads as stitched clips rather than a story. Kling caps at 15s per
clip, so a scene slot longer than 15s needs multiple clips.

Save the plan into `episodes/<slug>/episode.md` as you go.

## 4. Start images

Full model details, IDs and the NSFW workaround: `docs/HIGGSFIELD_REFERENCE.md`.

Batch up to 12 with `generate_image_batch`, giving each request an `index`
equal to its scene number. Then poll:

```
jobs_wait(jobs=[{index, job_id}, ...], timeout_seconds=15)
```

`timeout_seconds` maxes out at 15, so a slow batch needs repeated calls. When
`all_terminal` is false, wait `poll_after_seconds` and call again.

**Retry only the failed indices.** Because indices are stable you can
re-submit exactly the scenes that failed and slot the new job IDs back into
the plan. Never re-run a whole batch to fix one image.

## 5. Animate

`kling3_0`, `mode: "pro"`, `sound: "off"`, duration ≤ 15, start image =
the image **job ID**:

```
medias: [{ role: "start_image", value: "<IMAGE_JOB_ID>" }]
```

### Motion prompt rules

Describe subject movement, camera movement if needed, expression changes,
one or two clear physical comedy beats, environment reactions, and an ending
pose that transitions well.

One clear action per clip. Do not ask a 15-second clip to perform five
unrelated actions.

Bad:

> Pip plays, laughs, runs, eats, falls down, gets up, finds Teddy, Mommy hugs
> him, they leave.

Good:

> Pip cautiously steps beneath the fountain while hugging Teddy. He dodges the
> first water jet with a proud grin, turns to celebrate toward Mommy, then a
> second gentle jet unexpectedly sprays the top of his curly hair. Pip freezes
> in surprise, Teddy dangling from one hand, then bursts into laughter. Smooth
> playful camera push-in.

If Kling returns a preset recommendation, re-submit with the returned
`declined_preset_id`. Do not drop the scene.

## 6. Download clips

Clip URLs come back from `jobs_wait` / `show_generation_by_ids`. Save into
`episodes/<slug>/clips/` named by scene: `s01.mp4`, `s02.mp4`, …

### The CDN egress block — read before planning assembly

Both Higgsfield result CDNs are **blocked by the session's egress policy**:

```
d8j0ntlcm91z4.cloudfront.net   403 on CONNECT   (generation results)
d2ol7oe51mr4n9.cloudfront.net  403 on CONNECT   (uploaded media)
```

A `CONNECT tunnel failed, response 403` is the org policy, not a bad URL.
Never disable TLS verification, never route around it, never retry blindly.

**This means clips cannot be downloaded into the session container, so
`scripts/assemble.py` cannot run locally.** Plan for it from the start.

### Assembling in the Higgsfield sandbox instead

`sandbox_exec` runs a Linux box on Higgsfield's side with ffmpeg, ffprobe,
ImageMagick and python3 preinstalled, and it reaches the media natively. Its
own tool description directs you to use it for ffmpeg work. Nothing blocked
transits this container.

Getting the user's MP3 in: `media_upload` returns a presigned URL on
`fast-and-furious-input-prod-*.s3.amazonaws.com`, which **is** permitted. PUT
the bytes, then `media_confirm`. The sandbox then curls it from the media URL.

Getting the master out: call `media_upload` for the output **before** starting
the build, and append the `curl -X PUT --upload-file` to the *same* command.

Sandbox gotchas that matter:

- It is discarded ~10 s after a call returns. Chain everything with `&&`, or
  use `background: true` and poll.
- **Poll at least every 60 s** or the background process dies with the sandbox.
- The tool call itself may time out even with `background: true` — the job
  usually survives. Check `~/.bg/*.log` before assuming failure.
- `timeout_seconds` caps at 120.

Because the final MP4 lives on a blocked CDN, it cannot be pulled back into
the repo from this environment. Deliver the Higgsfield media URL and keep the
manifest committed so the render is reproducible.

## 7. Assemble

```bash
python3 scripts/assemble.py episodes/<slug>/manifest.json
```

The script normalizes every clip to the target canvas, fps and pixel format,
loops short clips to fill their slot, crossfades scene to scene, and muxes the
MP3. Manifest schema and options: `scripts/assemble.py --help`, and
`episodes/_TEMPLATE/manifest.json`.

What it does under the hood, if you need to do it by hand:

**Normalize** each clip:

```
scale=W:H:force_original_aspect_ratio=increase,crop=W:H,setsar=1,fps=24,format=yuv420p
```

**Crossfade** between scenes:

```
xfade=transition=fade:duration=0.5
```

offset by the cumulative timeline. Every `xfade` input must share width,
height, pixel format and frame rate — mismatches are the usual cause of
cryptic filter errors.

**Loop to fill** when a clip is shorter than its slot: repeat copies,
crossfade them, offset by `clip_duration - 0.5`, trim to the slot. Prefer
generating enough unique scenes over obvious loops.

**Mux** the user's MP3 as the only audio:

```
-map 0:v -map 1:a -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart
```

Build the video at least as long as the song and let `-shortest` let the song
define the end.

**Master video settings:** H.264 / `libx264`, CRF ~20, preset `slow`,
`yuv420p`, `+faststart`.

## 8. Verify before declaring done

```bash
ffprobe -v error -show_entries format=duration,size -show_entries stream=width,height,codec_name,r_frame_rate -of default=noprint_wrappers=1 out.mp4
```

Check runtime matches the song, resolution is exactly 1920x1080 or 1080x1920,
there is one audio stream, and the file size is sane. Actually look at the
numbers — do not report success on the basis that ffmpeg exited 0.

If delivering through chat, aim under ~30 MB. GitHub's normal file limit is
100 MB; large renders stay gitignored.

## 9. Episode package

Create `episodes/<slug>/episode.md` and `metadata.md` from
`episodes/_TEMPLATE/`. Record title, concept, runtime, song file, aspect
ratio, story summary, scene timeline, final scene prompts, model/job notes,
**failed generations and what fixed them**, and the output filename.

That failure log is the point: it is how the next episode avoids repeating
this episode's dead ends.
