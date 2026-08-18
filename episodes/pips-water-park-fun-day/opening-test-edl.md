# Opening re-edit experiment (free — no generation credits)

Question: **can better editing of footage we already own make the opening
materially more engaging?**

Full 5:05 master was NOT modified. No image or video credits were spent.
Every frame below already existed in V1/V2.

| Deliverable | Length | Media ID |
|---|---|---|
| Fast-cut opening test | 30.000 s | `4f5584db-545a-4a89-a501-a82ce74f4f9d` |
| Current V2 opening (baseline) | 30.000 s | `c2194a16-2147-403a-82da-398b70102433` |

Both 1920x1080, 24 fps, H.264 + AAC, original Suno MP3 from 0:00.

## Edit decision list — 13 shots, 2.31 s average

| # | In–out | Src clip | Source in | Len | Beat |
|---|--------|----------|-----------|-----|------|
| 1 | 0:00.0–0:02.0 | 13 `802dd576` | 7.0 | 2.0 | tipping bucket drenches Pip |
| 2 | 0:02.0–0:04.0 | 24 `40523850` | 2.5 | 2.0 | rainbow-slide ride |
| 3 | 0:04.0–0:06.0 | 25 `2581892b` | 2.0 | 2.0 | splash landing, Teddy overhead |
| 4 | 0:06.0–0:09.0 | 1 `9a1db6d0` | 1.0 | 3.0 | wide reveal — Pip, Mommy, Teddy, park |
| 5 | 0:09.0–0:12.0 | 2 `6c2d6a05` | 2.0 | 3.0 | Pip excited, squeezes Teddy |
| 6 | 0:12.0–0:15.0 | 4 `f4bc083e` | 1.5 | 3.0 | runs at the water, skids to a stop |
| 7 | 0:15.0–0:16.5 | 5 `55b9d750` | 3.0 | 1.5 | toe touches water, yanks back |
| 8 | 0:16.5–0:18.0 | 6 `6f4bc518` | 1.0 | 1.5 | both feet stomp, big splash |
| 9 | 0:18.0–0:20.5 | 7 `510546d8` | 0.8 | 2.5 | ground fountain erupts, Pip startles |
| 10 | 0:20.5–0:21.5 | 7 `510546d8` | 4.5 | 1.0 | **punch-in 1.35x** — giggle reaction |
| 11 | 0:21.5–0:24.0 | 8 `13a5b7a6` | 1.0 | 2.5 | Pip dodges the spray |
| 12 | 0:24.0–0:26.5 | 8 `13a5b7a6` | 5.5 | 2.5 | **punch-in 1.35x** — proud celebration |
| 13 | 0:26.5–0:30.0 | 9 `5574d952` | 1.5 | 3.5 | reversal: second spray gets him |

**All hard cuts.** No crossfades anywhere in the 30 s.

Punch-ins are a centre crop to 1422x800 (16:9) re-scaled to 1920x1080 — 1.35x,
used twice only, to get closer coverage out of clips we already own without
generating anything.

## What was removed

- The entrance / walk-in shot is **gone entirely**. It carried the malformed
  "WATER PAR…" signage in V1 and is not load-bearing for the story. The
  sequence now reads: sees the park → gets excited → runs at the water.
- V2's slow 6 s reveal push-in is trimmed to 3 s.
- The second Pip close-up is dropped (V2 had two similar ones back to back).

## Structural comparison

| | V2 opening | Fast-cut test |
|---|---|---|
| Shots in first 30 s | 4 | 13 |
| Average shot length | ~7.5 s | 2.31 s |
| Transitions | crossfades | all hard cuts |
| First physical-comedy payoff | ~0:02 (teaser), then none until ~1:12 | 0:02, and again at 0:18, 0:21, 0:24, 0:27 |
| Entrance/sign shot | present | removed |

## Predictor comparison — NOT obtained

The V2 opening scored hook 34 / engagement 31 / overall 43 / sustain 82,
peaking at t=2 s. The intent was to score the new 16 s cut the same way.

`media_confirm` began failing with "Something went wrong" immediately after the
two 30 s files confirmed, and kept failing across three attempts and two fresh
upload slots. Unconfirmed media is not served (403), so the predictor could not
ingest the new clip. This is a Higgsfield API fault, not a problem with the
edit — the 30 s test itself is confirmed and playable.

Worth re-running when the API recovers, but the user's own judgement on the two
30 s files is the better signal anyway; the predictor was only ever a secondary
proxy.
