# Habit Shorts — batch 01

Five 9:16 Shorts, 5 shots x 6s = **30.0s** each, hard cuts, 1080x1920.

## Why these five topics

Chosen strictly by the rule in `docs/CONTENT_STRATEGY.md`, derived from the
30-day analytics export: within videos published Aug 1-20, six topics averaged
24,089 views and eight averaged 161 — a 150x gap where the only variable was
the topic. Winners are **a concrete physical activity with visible mess and a
face the toddler pulls**. Losers are abstract (feelings) or tidy.

| Short | Mess | Resistance | Nearest proven neighbour |
|---|---|---|---|
| Wash Your Hair | foam, water | fear of water on the face | Bath Time (94,486) |
| Potty Time | — | the whole topic | highest-volume toddler search topic |
| Out of the Bath | splash | "five more minutes" | Bath Time (94,486) |
| Eat Your Broccoli | — | outright refusal | No More Candy (17,767) |
| Sticky Hands | jam everywhere | — | Blow Your Nose (11,906) |

Runtime is pinned at 30s because every proven winner is 29-31s, and both the
too-short (20-23s) and too-long (36s, 50s) attempts underperformed.

## Structure

Each Short follows `docs/SHORTS_PLAYBOOK.md`: open on the activity already
visible, one clear action per shot, Pip does it imperfectly, one Teddy beat,
warm ending. Hard cuts rather than crossfades — the winners are fast-paced and
a 6s shot does not need easing.

Shot-by-shot beats and every job ID: `jobs.json`.
Titles, descriptions, sing-along lyrics, thumbnail beats: `metadata.md`.

## Audio — not yet attached

These are delivered **silent**. `generate_audio` on Higgsfield is
speech-only — its own tool description says there is no standalone music model
and instructs against substituting a speech model — so the songs must come from
Suno as usual.

Lyrics for all five are written and ready in `docs/CONTENT_STRATEGY.md`.
Once each MP3 exists, muxing is a single ffmpeg pass and costs **zero credits**:

```
-map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart
```

Trim or extend the song to 30.0s rather than re-cutting the video, so the shot
rhythm stays intact.

## Costume and casting locks used

Three prompt prefixes, applied verbatim per shot so the model could not drift:

- **Standard** — Pip in the sunny-yellow romper with 'Pip' in red bubble letters
- **Bath** — no romper; Pip always covered chest-down in thick white bubble foam,
  head-and-shoulders framing only, per the bath-scene guidance in
  `docs/HIGGSFIELD_REFERENCE.md`
- **Towel** — Pip fully wrapped in an enormous fluffy hooded bath towel

Every prompt states: exactly one adult, one toddler, one bear; Mommy clearly a
full-grown adult much taller and older than Pip; no written text except 'Pip' on
the romper; no flat signable surfaces.

## Failures and fixes

**Shot 105 failed** (`87bdaf29-08b7-4253-9740-16e319bedcc3`). The Wash Your Hair
finale originally described water sheeting down over Pip with his head tipped all
the way back. Replaced by **106**, the same emotional beat framed as a
head-and-shoulders portrait *after* the rinse rather than during it — Pip beaming
with freshly rinsed curls. Retried that index only; the other 24 stills were
untouched.

**Rule to carry forward:** frame bath finales after the water, not mid-pour.
Added alongside the existing bath guidance.

No Kling preset interceptions occurred — `declined_preset_id`
`24bae836-2c4a-48e0-89b6-49fcc0b21612` was passed preemptively on all 25
submissions, which is the practice recorded in `docs/HIGGSFIELD_REFERENCE.md`.

## Not verified

Nobody has looked at these frames. The CDN is blocked from the session container
and no frame-viewing path exists — the same limitation recorded under "Still QC
before animation" in `docs/PRODUCTION_WORKFLOW.md`. Specifically unchecked:

- whether Mommy reads as a full-grown adult in every shot she appears in
- whether the bath shots kept Pip covered as instructed
- whether the romper survived in all the non-bath shots
- whether any environmental text appeared

Watch each Short before publishing. Reshooting one bad shot costs ~11 credits
(2 for the still, 9 for a 6s pro clip) and only that index needs redoing.

## Cost

| Item | Credits |
|---|---:|
| 26 stills @ 2 (25 + 1 retry) | 52 |
| 25 clips @ 6s x 1.5 (pro) | 225 |
| **Total** | **~277** |
