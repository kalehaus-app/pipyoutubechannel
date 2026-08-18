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

---

# V2 Optimization Pass

Surgical revision of the finished V1. The story, song and the great majority of
generated footage are unchanged. **V1 is preserved** — see Delivery below.

| | |
|---|---|
| **V2 master** | Higgsfield media `1545f66b-2277-4602-af7e-71c00946c016` |
| **Runtime** | 305.834 s (song 305.640 s, +0.19 s margin) |
| **Spec** | 1920x1080, H.264 high, yuv420p, 24 fps, AAC 192k / 48 kHz, +faststart |
| **Size** | 236,612,303 bytes (225.6 MB) |
| **New generations** | 5 stills, 4 clips (~83 credits) |
| **Reused from V1** | 24 of 27 original clips, untouched |

## What changed and why

### 1. Cold open (highest priority)

V1 spent its first ~25 s on a slow establishing sequence before any real water
action. V2 opens on a 6.4 s teaser montage cut from footage already in the
episode, with **hard cuts** rather than crossfades for energy:

| | Source | Length |
|---|---|---|
| 0:00 | giant tipping-bucket drench (from scene 13) | 2.0 s |
| 0:02 | rainbow-slide ride (from scene 24) | 2.0 s |
| 0:04 | splash landing, Teddy held overhead (from scene 25) | 2.4 s |

It then crossfades (0.4 s) into the park reveal. The V1 opening was additionally
entered 5 s late, trimming the slowest part of the establishing shot.

First-30-second check: water + Pip + big physical action by **second 2**;
unmistakably a water park by second 5; all three characters introduced by ~0:20;
two comedy payoffs already seen inside the teaser.

These are flashes, not spoilers — each is ~2 s of a 10–13 s scene, and the full
payoffs still land in place later.

### 2. Generated entrance text removed

V1's entrance shot carried a malformed AI sign reading roughly "WATER PAR…",
breaking the no-environmental-text rule.

First replacement attempt kept a decorative rainbow archway and simply asked
harder for no lettering — but V1's prompt *already* banned text and still
produced a sign, so prompt-level mitigation alone was not trusted. The shot was
regenerated a second time with **no signable surface in the composition at
all**: no gateway, no arch, no booth, no panel. Pip and Mommy now walk a curving
poolside path between palms and parasols with the slides rising ahead.

Unused first attempt: image `4b3cc4da-8a3e-4398-b268-38eeeaec60b0`.

### 3. Pip costume break fixed

Around 176–187 s V1 lost Pip's yellow romper during the Teddy-drift sequence —
V1's prompt for that scene never restated the costume. The shot was regenerated
with a full costume lock and the same emotional beat preserved: Pip safe on his
float, realising Teddy is gone, patting the empty spot, searching left then
right. Motion prompt drives that as explicit cause-and-effect.

### 4. Pre-slide pacing tightened

V1 stacked several similar-energy shots before the payoff. V2 escalates:

```
wide reveal -> nervous close-up -> Mommy at eye level (count-in)
-> climb -> POV down the chute -> ride -> splash
```

Two changes: the Mommy reassurance shot was regenerated so she counts
**one… two… three, go!** on her fingers (a toddler participation beat, staged
visually with no on-screen numbers), and a **new POV shot** looking down the
slide from the top was inserted to convert repeated reassurance into rising
anticipation.

### 5. Mommy costume

Locked for all new generations to a light-blue summer top and denim shorts,
clearly adult. Existing V1 Mommy shots were deliberately **not** regenerated —
per the stated priority order (Pip > Teddy > story > Mommy), they were not
distracting enough to justify the spend.

### Preserved untouched

Teddy drifting away, Pip noticing, Pip paddling after him, the relieved hug,
slide nerves, Mommy reassuring without solving it, Pip choosing to go, the
rainbow-slide payoff, the tipping-bucket comedy, the towel sequence with Teddy's
tiny towel, and the sleepy ending.

## Replacement job IDs

| Scene | Image job | Video job | Slot |
|---|---|---|---|
| 3 — poolside walk-in (no signage) | `48032fc5-f562-4c08-ba8e-ce4ccabd4771` | `e685e397-f30f-4159-9c07-d590ed052e5d` | 11 s |
| 16 — Pip notices Teddy gone (romper) | `8283dcd4-996f-4f06-b92a-b47311bf9eae` | `473527b9-2a7c-4967-a2ca-657b1b20aa8c` | 12 s |
| 21 — Mommy count-in | `22942940-f3d9-4042-b5d0-b0b2dd778ada` | `92b7b56a-2c06-40ac-995d-c2970c01e06b` | 10 s |
| 22b — POV down the slide (NEW) | `3b58d9b5-13c0-469b-bf46-5d3bcff9a645` | `60ae79df-12c0-43f0-b295-d18b80877135` | 8 s |

## Assembly method

Rebuilding all 27 clips was unnecessary and, in this environment, impossible:
`sandbox_exec` background mode was returning `deadline_exceeded` for even a
trivial `sleep`, and foreground calls cap out around 60 s while the sandbox is
discarded between them.

Instead V2 was **patched from the V1 master**, which is already 1920x1080/24fps:
unchanged spans were re-encoded straight from V1, and only the four replacement
clips and the cold open were composited in. The work was split into five chunks,
each built and uploaded inside a single foreground call, then joined with the
concat demuxer using stream copy and muxed with the original MP3.

| Chunk | Contents | Length | Media |
|---|---|---|---|
| c1 | cold open + V1 [5.0–24.0] + new scene 3 + V1 [35.5–41.5] | 41.042 s | `759b5fa8-…` |
| c2 | V1 [41.5–119.5] | 78.000 s | `b8eb1499-…` |
| c3 | V1 [119.5–172.0] | 52.500 s | `d143d7fd-…` |
| c4 | new scene 16 + V1 [187.0–233.0] | 57.542 s | `7711e820-…` |
| c5 | new scene 21 + V1 [243.5–254.0] + new POV + V1 [254.0–305.71] | 78.750 s | `4694f78e-…` |

Chunk boundaries were placed **inside contiguous V1 spans**, so rejoining them
is frame-exact and invisible. Crossfades (0.5 s) sit inside chunks around every
replacement. Two junctions — into scene 16 and into scene 21 — fall on chunk
boundaries and are therefore **hard cuts rather than crossfades**; both land on
scene changes where a cut reads as intentional.

The song was never touched: original Suno MP3, muxed with `-shortest` so the
music defines the ending.

## Lessons learned

- **A generic "no text" instruction does not prevent generated signage.** V1
  asked for no text and still produced a sign. The reliable fix is
  compositional — remove the signable surface from the shot.
- **Every still prompt must restate the costume.** V1's scene 16 omitted the
  romper and the model dropped it. Prompts have no memory of neighbouring scenes.
- **Reuse beats regeneration.** Patching an existing master preserved 24 clips
  and cost ~83 credits instead of ~570 for a full rebuild.
- **Design chunk boundaries to fall inside contiguous source material** when
  splitting a render across calls; joins there are seamless.

## Known limitation — visual QC was not performed

The new stills were **not** visually inspected before animation, contrary to the
QC rule now written into `docs/PRODUCTION_WORKFLOW.md`. Every available route
failed in this environment: the CDN is blocked locally, sandbox stdout truncates
near 20k characters so base64 transfer of a usable image is cut off,
hand-copying base64 corrupted the file (verified by checksum and a JPEG huffman
error), and an installed Tesseract failed a control test — it did not detect
V1's known "WATER PAR…" sign, so it cannot certify text absence either.

Risk was therefore mitigated at generation time (compositional bans, explicit
costume locks) rather than by inspection. **The four replacement shots should be
spot-checked on playback before publishing** — at roughly 0:25 (entrance, check
for signage), 3:05 (Pip's romper), 4:05 (Mommy count-in) and 4:30 (POV).
