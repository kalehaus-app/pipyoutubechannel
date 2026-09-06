# Shorts Playbook — Pip + Mommy Daily Life

9:16, usually 20–40 seconds. This is the **proven discovery format** for the
channel. It works; do not quietly replace it with vague nursery-rhyme ideas.

## Format

- One literal, instantly recognisable toddler activity
- Pip + Mommy (Teddy wherever he fits)
- A healthy habit or daily routine
- Lots of physical comedy
- Simple original song
- Fast visual pacing — short scenes, quick cuts

## What has already worked

Sunscreen with Mommy · Try New Foods with Mommy · Buckle Up with Mommy ·
Shoes On with Mommy · Getting Ready with Mommy · Brush Teeth · Wash Hands ·
Haircut · Doctor Visit

The pattern: an everyday thing a toddler has actually just done or is about to
do, with a parent, done slightly wrong and very cheerfully.

## Titles stay boringly literal

A parent scrolling must understand the video in one glance. Clever titles lose
to obvious ones. See `docs/METADATA_GUIDE.md`.

## Scene shape

With only 20–40 seconds, every scene needs to earn its place:

- Open on the activity already visible — no wind-up
- Each scene: one clear action, ideally one comedy beat
- Pip does the thing imperfectly (too much sunscreen, wrong feet, big face)
- Give Teddy a small parallel moment where it fits — Teddy gets sunscreen too,
  Teddy gets his own seat belt
- End warm: a hug, a bounce, a proud grin

Because scenes are short, a Short is usually 3–6 clips. Keep durations varied
rather than six identical 5-second blocks.

## Assembly

Same pipeline as long-form, different canvas: **1080x1920**. Crossfades can be
shorter than long-form (0.3–0.5s) to keep the pacing snappy.

## Pacing spec — revised after batch 01

The first habit-Shorts batch was built as 5 shots x 6s = 30s. Watching it back,
that reads slow: a 6-second hold is an eternity to a toddler and it is the same
complaint that produced the V3 fast-cut pass on the water park episode.

**Target ~2.5-3.5s per shot, 12-14 shots in a 35-40s Short.** Roughly double the
cut rate of a 5x6s build.

### How to get there without doubling generation cost

Generate **7 clips at 6s** (42s of source), then cut 13 shots from it using
wide/punch-in alternation — each clip yields a wide segment and a tighter
segment from a different moment. The framing change reads as a second camera,
not a jump cut, provided the zoom step is large enough (1.0 -> 1.25-1.30) and
the action continues across the cut.

Source clips arrive at 1076x1928, so punch in with expressions rather than
fixed pixels:

```
crop=w=trunc(iw/Z/2)*2:h=trunc(ih/Z/2)*2,
scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=24,format=yuv420p
```

### Vary the rate — do not cut everything at 2.9s

Fast through the comedy and the mess; **hold the final warm beat long**. A
Short that cuts frantically through its own ending has no landing. Batch 01's
Out of the Bath runs twelve shots at 2.3-3.2s and then holds the towel snuggle
for 6.0s.

### At least two shots must be genuine motion

Not "a reaction with a camera push-in" — actual movement across the frame:
running, spinning, splashing, something zooming. Reaction shots are where the
character work happens, but a Short built only from reactions feels static
however fast it is cut.

### Size the video to the song, never the reverse

Suno songs come back around 35-40s, not 30. Plan 7 clips so there is enough
source to fill one, rather than trimming the song and losing its ending. The
song defines the runtime — the same rule as long-form.
