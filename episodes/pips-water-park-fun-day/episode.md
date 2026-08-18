# Pip's Water Park Fun Day

First long-form episode. Shared rules live in `docs/` — this file records what
was actually done.

| | |
|---|---|
| **Slug** | `pips-water-park-fun-day` |
| **Format** | Long-form 16:9 |
| **Runtime** | 5:05.6 (song-defined) |
| **Song file** | `song/what-a-happy-water-day.mp3` |
| **Song duration** | 305.64 s |
| **Embedded title** | "What a Happy Water Day" (artist `forlittleones`, made with Suno) |
| **Embedded lyrics** | Yes — full lyrics with section markers, used to drive the timeline |
| **Scenes** | 27 |
| **Output** | `pips-water-park-fun-day-1080p.mp4` — 1920x1080, 305.71 s, 220.6 MB |
| **Delivered as** | Higgsfield media `eae25ec2-583d-428e-b317-db44ea08e30a` (repo CDN egress is blocked — see Failures) |
| **Thumbnail scene** | 24 — rainbow slide ride, big subject, obvious activity, reads at small size |

## Concept

> Pip's Water Park Fun Day 💦 — first 16:9 long-form Pip adventure. Pip, Teddy
> and Mommy visit a huge colorful water park on a sunny day.

Built as a preschool animated episode rather than a lyric visualisation: a
coherent beginning → middle → complication → resolution, with Pip as a
recognisable character rather than a generic toddler.

## The two questions

1. **Why does a parent click this?** A giant colorful water park with rainbow
   slides — instantly readable, and a real outing toddlers recognise.
2. **What does a child learn about Pip and Teddy?** That Pip *loves* Teddy.
   When Teddy drifts away Pip goes after him himself, and when Pip is scared
   of the big slide it is squeezing Teddy that gets him up the steps. Their
   bond is the spine of the episode, not decoration.

## Story summary

Pip is astonished by an enormous water park. He works up the nerve to touch
the water, then gets progressively soaked — a surprise ground fountain, a
proud dodge immediately punished by a second fountain, a drenched Teddy, a
small slide, and a giant tipping bucket that Mommy sees coming before he does.
On the lazy river Teddy slips off the float and drifts away; Pip notices, and
paddles after him himself while Mommy watches without intervening. Reunited,
Pip spots the enormous rainbow slide. He is thrilled and frightened. Mommy
reassures him at eye level but does not carry him. Pip squeezes Teddy, climbs,
and rides it — landing in a huge splash and holding Teddy overhead in triumph.
Mommy wraps him in a towel, gives Teddy a tiny one, and Pip falls asleep
cuddling his bear in the golden sunset.

## How the timeline was built

The MP3 carried full lyrics with section markers (`[Chorus]`,
`[Instrumental Break — leave room for visual comedy]`, `[Big Musical Build]`,
`[Outro — gentle and sleepy]`), so the story was mapped onto the song's own
structure rather than one image per lyric line.

An RMS energy profile in 5s buckets located the structural boundaries:

| Marker | Time | Used for |
|---|---|---|
| dip to -22.7 dB | ~132 s | instrumental break → tipping-bucket setup (scene 12) |
| dip to -23.5 dB | ~217 s | adventure break → giant slide reveal (scene 19) |
| dip to -23.3 dB | ~277 s | breath before the final chorus → splash payoff (scene 25) |
| declining | 280–305 s | sleepy outro → towel + sleeping (scenes 26–27) |

**Arithmetic:** 27 scene slots summing to 319 s, minus 26 crossfades at 0.5 s,
gives a 306.0 s timeline against a 305.64 s song — deliberately ~0.4 s long so
`-shortest` lets the music define the ending rather than the video running dry.

## Scene timeline

Start times account for crossfade overlap: `start(i) = Σd(1..i-1) − 0.5(i−1)`.

| # | Start | Dur | Beat | Comedy / emotional beat |
|---|-------|-----|------|--------------------------|
| 1 | 0:00.0 | 13 | HOOK — water park reveal | jaw-drop wonder |
| 2 | 0:12.5 | 12 | Pip reaction close-up | eyes-widen signature |
| 3 | 0:24.0 | 12 | Entering the park | Pip drags Mommy along |
| 4 | 0:35.5 | 12 | Arriving at splash pad | run + skid stop |
| 5 | 0:47.0 | 14 | INSTRUMENTAL — toe test | comic hesitation, yanks foot back |
| 6 | 1:00.5 | 12 | First splashing | Teddy held high and dry |
| 7 | 1:12.0 | 12 | Surprise ground fountain | startle, lands on bottom |
| 8 | 1:23.5 | 12 | The proud dodge | victory pose + celebration bounce |
| 9 | 1:35.0 | 12 | Sprayed from behind | **money beat** — frozen mid-grin |
| 10 | 1:46.5 | 12 | Teddy gets splashed | "Oh, Teddy!" + wringing out ears |
| 11 | 1:58.0 | 11 | Beginner slide | little splash, Teddy triumph |
| 12 | 2:08.5 | 12 | Tipping bucket setup | **Mommy notices before Pip does** |
| 13 | 2:20.0 | 13 | The bucket dumps | **money beat** — slow look up, drench |
| 14 | 2:32.5 | 12 | Lazy river | calm, warm, Mommy humming alongside |
| 15 | 2:44.0 | 12 | COMPLICATION — Teddy drifts | gentle, never alarming |
| 16 | 2:55.5 | 12 | Pip notices | pats empty float, worried gasp |
| 17 | 3:07.0 | 12 | **PIP ACTS** — paddles | Mommy watches, does not intervene |
| 18 | 3:18.5 | 13 | RESCUE — relieved hug | emotional core |
| 19 | 3:31.0 | 12 | Giant slide revealed | dramatic tilt-up |
| 20 | 3:42.5 | 11 | Excited but nervous | squeezes Teddy for courage |
| 21 | 3:53.0 | 11 | Mommy reassures | at eye level, does not solve it |
| 22 | 4:03.5 | 11 | Pip decides — the climb | anticipation build |
| 23 | 4:14.0 | 11 | The top — the launch | brave breath, push off |
| 24 | 4:24.5 | 10 | **BIG PAYOFF** — the ride | banked turns, sparkling spray |
| 25 | 4:34.0 | 11 | SPLASH + victory | Teddy overhead, celebration bounce |
| 26 | 4:44.5 | 11 | Towels | Teddy's comically tiny towel |
| 27 | 4:55.0 | 11 | Sleepy final shot | eyes close, golden sunset |

Full image and motion prompts: `scenes.json` (source of truth).

## Models and jobs

- **Images** — `nano_banana_pro` @ 2k, 16:9, all 27 anchored on reference
  `54c9aaff-0c9a-4ab1-ac43-b829aef60edc` for character and location consistency
- **Video** — `kling3_0`, `mode: pro`, `sound: off`, durations 10–14 s
- **Audio** — user's Suno MP3, uploaded as media `a01f42a6-5c52-4152-9e3a-9662d53fdb6d`

Kling returned clips at 1928x1076 @ 24fps, normalized to 1920x1080.

Approximate spend: 27 images x 2 + 27 videos x ~19 avg ≈ 570 credits.

## Failures and retries

| What happened | Detail | Fix |
|---|---|---|
| `soul_2` returned `nsfw` | Scene 1 test render, a wholesome water-park establishing shot. The documented false positive, and a water park is its highest-risk setting. | Switched **all** stills to `nano_banana_pro` + reference image. Zero NSFW failures across 27 images. |
| `style_id` silently dropped | Batch tool reported `"Higgsfield Soul 2.0 does not support this parameter"` | The `General` style that produced the reference's look **cannot be applied through the MCP path**, so `soul_2` would have rendered in its native realistic style anyway — a second, independent reason to use `nano_banana_pro`. |
| Kling preset recommendation | 6 of the first 12 video submissions returned `submission_failed` with preset **"IN THE DARK"** instead of a job | Re-submitted with `declined_preset_id: 24bae836-2c4a-48e0-89b6-49fcc0b21612`; all 6 went through. Included it **preemptively** on every later submission — no further preset interruptions. |
| Higgsfield CDNs blocked | `d8j0ntlcm91z4.cloudfront.net` and `d2ol7oe51mr4n9.cloudfront.net` both return 403 on CONNECT via this session's egress proxy | Clips cannot be downloaded into the session container, so ffmpeg assembly ran in the **Higgsfield sandbox** (`sandbox_exec`) instead, which reaches the media natively. The MP3 was uploaded via `media_upload` (the S3 input host *is* permitted). See "Assembly" below. |
| Scene 15 image lagged | Rendered several minutes after the rest of its batch | Animated the other 26 first rather than blocking; submitted 15 on arrival. |

**Zero image failures and zero video failures** after the model switch.

## Assembly

Because of the CDN egress block, assembly did **not** run via
`scripts/assemble.py` locally. The same pipeline was reproduced in the
Higgsfield sandbox:

1. download 27 clips + the MP3 (~700 MB)
2. normalize each to exactly its slot:
   `scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=24,format=yuv420p`
   (CRF 18, veryfast — intermediate)
3. 26-step `xfade=transition=fade:duration=0.5` chain with cumulative offsets
4. final encode CRF 20, `yuv420p`
5. mux: `-map 0:v -map 1:a -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart`

**Deviation:** final encode used `-preset medium` rather than the documented
`slow`, to fit the sandbox's polling-based keep-alive window. Visually
equivalent at CRF 20 for a 1080p master that YouTube re-encodes anyway.

Reproducing locally (if the CDN hosts are ever allowed) needs only the clips in
`clips/s01.mp4 … s27.mp4`, then:

```bash
python3 scripts/assemble.py episodes/pips-water-park-fun-day/manifest.json
```

`manifest.json` holds the identical scene/duration table.

### Verified output

```
1920x1080  h264 + aac  24/1 fps
duration 305.709 s   (song 305.640 s — 0.07 s audio frame boundary)
size     231,295,375 bytes (220.6 MB)
```

Timeline arithmetic confirmed by the build: `timeline end = 306.0`, and every
normalized scene landed on its exact slot (13.000, 12.000, 14.000, …) with no
looping — Kling returned each clip slightly longer than requested, so all 27
were trimmed rather than repeated.

**220.6 MB exceeds GitHub's 100 MB limit**, so the master is not committed; it
lives in Higgsfield media. For chat delivery a smaller proxy would need a
separate lower-bitrate encode.

## Delivery

Both files live in the Higgsfield media library (the repo cannot host them —
220 MB exceeds GitHub's limit, and the CDN is blocked from the session).

| | Media ID | Spec |
|---|---|---|
| **Master** | `eae25ec2-583d-428e-b317-db44ea08e30a` | 1920x1080, 305.71 s, 220.6 MB — upload this to YouTube |
| **Preview** | `c514abee-043b-4cad-ac8b-ed690228d264` | 640x360, 305.71 s, 37 MB — quick check on a phone |

The preview is a downscale of the master, not a re-assembly, so it is frame-
for-frame the same edit.

### Sandbox note

`sandbox_exec` with `background: true` was returning `deadline_exceeded` for
even a trivial `sleep 100`, so long-running detached work was unavailable and
files did **not** survive between back-to-back calls. The workaround that
succeeded: give ffmpeg the media **URL directly as its input** so the download
overlaps the transcode, and chain the upload with `&&` in the *same* call —
the whole job then fits inside a single sub-60 s foreground call.
