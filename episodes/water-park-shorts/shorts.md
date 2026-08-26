# Water Park Shorts — three vertical re-cuts

**Source:** `episodes/pips-water-park-fun-day/` (V2 clips)
**Canvas:** 1080x1920, 24 fps, h264 + aac
**Generation credits spent: 0**

## Why these exist

The channel's YPP blocker is Shorts views, not subscribers — see
`docs/MONETIZATION.md`. The watch-hours route is at 0.13% of its threshold and
the Shorts route is at 3.0%, so production pivots to Shorts. These three are the
free first move: existing water park footage, re-framed vertical and fast-cut,
with segments of the original Suno song underneath.

## What was built

| Short | Runtime | Shots | Song segment | Story |
|---|---|---|---|---|
| Pip Saves Teddy at the Water Park | 28.33s | 6 | 158.0–186.3s | Teddy drifts away, Pip paddles after him, relieved hug |
| Pip Goes Down the Big Water Slide | 33.00s | 7 | 214.0–247.0s | Slide reveal, nerves, count-in, climb, POV, ride, splash |
| The Big Bucket Splashes Pip | 30.00s | 6 | 76.0–106.0s | Fountain gag, proud dodge, sprayed anyway, bucket dump |

Full cut list with source job IDs, in-points and zooms: `edl.json`.
Titles, descriptions, tags and thumbnail beats: `metadata.md`.

## Method

Cut from the individual scene clips rather than the master, so no crossfade
lands mid-shot. Each segment skips the first ~1.5s of its clip (the start-image
hold before Kling's motion begins), then runs 3–7s. Hard cuts throughout — no
crossfades, which is the pacing difference between a Short and long-form.

Center crop to 9:16 and scale to 1080x1920 (lanczos). The rescue Short reuses
scene 17 twice at different punch-in zooms (1.0 then 1.25) so a single clip
yields two shots without reading as a jump cut.

Audio is a continuous segment of the original song with `afade` in 0.4s /
out 0.8s. The video is re-cut against it rather than synced to it — there is no
dialogue, so shot-level sync does not matter, but the musical section still
matches the mood of the scenes it came from.

## Problems hit and what fixed them

**Kling clips are 1928x1076, not 1920x1080.** The API job params report
1920x1080; the delivered files probe as 1928x1076. A hard-coded `crop=608:1080`
failed twice with `Invalid too big or non positive size`. Fixed by cropping with
expressions that read the real input height:
`crop=w=trunc(ih*9/16/Z/2)*2:h=trunc(ih/Z/2)*2`. Rule added to
`docs/PRODUCTION_WORKFLOW.md`.

**The Suno MP3 carries embedded cover art** (`0 mp3 audio`, `1 mjpeg video`).
Harmless here once the audio segment is pre-extracted with `-vn`, but worth
knowing before pointing a filter graph at an MP3 directly.

## Not verified

Nobody has looked at these frames. The session cannot download from the
Higgsfield CDN and has no working path to view a frame, which is the same
limitation recorded in `docs/PRODUCTION_WORKFLOW.md` under "Still QC before
animation". Specifically unverified:

- Whether the center crop keeps Pip and Mommy in frame on every shot. Any shot
  that staged action toward frame edge loses it — a 9:16 crop discards ~68% of
  the width.
- Whether the 1.25x punch-in on scene 17 is soft.
- Whether Mommy reads as adult-sized once the frame is this tight.

Watch them before publishing. If a shot crops badly, the fix is cheap: change
that segment's `zoom`, or swap the beat for another clip in `edl.json`.

## Output media

| Short | Higgsfield media ID |
|---|---|
| Pip Saves Teddy | `283cd429-e25a-4efc-a90a-8e66e2358171` |
| Big Water Slide | `16b66e33-8b7e-4159-8cec-4c07b2c6fa22` |
| Big Bucket Splash | `68ac18fa-40a6-4651-9403-4a2c68521d45` |

URL form: `https://d2ol7oe51mr4n9.cloudfront.net/user_3C5niICYToBtuRckDNTBnm68Okj/<id>.mp4`
