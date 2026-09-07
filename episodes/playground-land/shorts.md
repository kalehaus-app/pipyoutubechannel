# Playground Land — the first dubstep Short

**Runtime** 28.29s · **1080x1920** · **19 shots** · **9 source clips**
**Output** `0d86ec44-0345-4357-b16f-ad2bcd7a75a0`

## Why dubstep

The channel's songs kept coming back feeling slow. Measuring proved the tempo was
being honoured — the bath song came back at 118.5 BPM against a requested 118 —
so the problem was never that Suno ignored the number. Two real causes:

1. **Perceived speed comes from syllable rate, not BPM.** Sparse lyric lines leave
   the vocal strolling over a fast kick.
2. **"children's nursery rhyme" is a lullaby-adjacent genre token** that drags
   everything after it in the style field.

Switching genre outright to dubstep solved both at once. This track measured
**141.5 BPM**, the fastest the channel has produced.

## Beat-matched editing — the technique this episode introduces

A four-on-the-floor track gives the edit a grid. Read the tempo off the MP3, then
place every cut on a beat boundary. Full cut list: `edl.json`.

Method:

1. **Measure tempo** — autocorrelate an onset envelope over a plausible BPM range.
   141.5 BPM here, so beat = 0.424028s, bar = 1.696s.
2. **Map energy** — RMS in 1s buckets locates the drops. This track:
   verse 0-6.8s, **drop 1 at 6.8s** (energy +70%), breakdown 18-20s,
   **drop 2 at 20.4s** (loudest point), outro 25-28s.
3. **Vary the cut rate by section**, snapping section boundaries to bar lines:
   verse every 4 beats, drops every 3, breakdown held, outro long.
4. **Put the story beats where the music already wants them.** The "NO I don't
   wanna go" shot sits in the breakdown; "ONE more turn!" lands exactly on drop 2.
   The song does the emotional work for free.

## Drop the silent tail

The MP3 is 29.688s but the music ends at ~28.0s. The video is cut to 27.986s
(66 beats) so the Short loops without dead air. Trailing silence is where a
Shorts loop dies.

## Structure

| Section | Time | Shots | Cut rate |
|---|---|---|---|
| Verse | 0-6.8s | 4 | 4 beats · 1.70s |
| **DROP 1** | 6.8-18.7s | 9 | 3 beats · 1.27s |
| Breakdown | 18.7-20.4s | 1 | held |
| **DROP 2** | 20.4-25.4s | 3 | 3-4 beats |
| Outro | 25.4-28.0s | 2 | held 3 then 5 beats |

Fast through the drops, slow on the ending. A Short that cuts frantically through
its own warm ending has nowhere to land, and the ending is what earns the
subscribe.

## Failures

**None.** All 18 generations — 9 stills, 9 clips — passed first try. The
empty-playground casting ban ("no other children, no bystanders anywhere in the
background") was stated in every prompt and cost nothing.

## Not verified

No frame of this has been seen. The CDN is blocked from the session container and
no frame-viewing path exists. Unchecked: whether 1.27s reads as exciting or merely
frantic on a phone; whether an entirely empty playground looks odd; whether Mommy
reads as adult-sized throughout. All are cheap to fix — one shot is ~11 credits.

## Cost

9 stills x 2 + 9 clips x 6s x 1.5 = **99 credits**.
