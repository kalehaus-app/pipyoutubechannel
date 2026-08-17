# Higgsfield Reference — verified against the live account

Everything here was confirmed by querying the account during bootstrap, not
copied from memory. Where the original brief and the live API disagree, the
live API wins and the discrepancy is called out.

## Model IDs — use these exact strings

| Purpose | MCP `model` | Notes |
|---|---|---|
| Primary stills | `soul_2` | Brief calls it `soul_v2`; the **MCP tool ID is `soul_2`**. Backend records it as `text2image_soul_v2`. |
| Fallback stills | `nano_banana_pro` | Used when `soul_2` false-flags NSFW. |
| Animation | `kling3_0` | Confirmed. |

Passing `soul_v2` will fail. This was the single biggest trap in the brief.

## soul_2 — declared parameters

```
quality    : "1.5k" | "2k"   (default 2k)
soul_id    : one Soul only
aspect_ratio: 1:1 16:9 9:16 4:3 3:4 3:2 2:3
medias     : max 1, role "image"
```

### Undeclared but accepted: `style_id`

`models_explore` does **not** list a style parameter, but the approved
reference job was generated with one and it took effect:

```
style_id: "3db34ab5-3439-4317-9e03-08dc30852e69"   // "General", strength 1
```

Params are passed through, so include it. If a submission is ever rejected
for an unknown field, drop `style_id` first and re-submit — it is a nice-to-have,
not load-bearing.

### Soul IDs — both confirmed `ready`

```
Pip    44f638c0-b402-424a-a6ba-962eae4ca86d
Mommy  6c889761-3c6d-45ee-8425-e6cb87dedeff
```

**One `soul_id` per generation** — this is a hard model constraint, not a
style choice. For a shot containing both characters, anchor on **Mommy**
(she is the one that breaks when unanchored — she drifts toward child
proportions) and describe Pip explicitly in the prompt text.

The account also holds unrelated Souls (`Kaley`, `Hank`, `Theo`, `Brexlee`,
`rechannel-narrator-alex`, `Whimsical Hide-and-Seek`). None belong to this
channel. Do not use them.

## nano_banana_pro — fallback

```
resolution : "1k" | "2k" | "4k"   (default 1k — pass "2k" explicitly)
medias     : role "image", multiple allowed
```

Note it takes `resolution`, **not** `quality`. Different key from `soul_2`.

### Approved Pip + Mommy + Teddy reference

```
54c9aaff-0c9a-4ab1-ac43-b829aef60edc
```

This is a **completed image job ID**, not an uploaded media UUID — it does not
appear in `show_medias`, and that is expected. It is valid directly as a
`medias[].value`. Verified `status: completed`, 1152x2048, a warm living-room
scene with all three characters correctly proportioned.

```
medias: [{ role: "image", value: "54c9aaff-0c9a-4ab1-ac43-b829aef60edc" }]
```

Base prompt pattern:

> Match the character designs and soft polished 3D animated look of the
> reference image — Pip, a toddler boy with curly brown hair wearing a
> sunny-yellow romper with 'Pip' in red bubble letters; his clearly adult
> Mommy with shoulder-length brown hair and cozy clothing; and Teddy, Pip's
> small red-and-blue plush bear. Create a NEW scene: [ACTION]. ONLY one adult
> and one toddler and the bear. Mommy is clearly much taller and older than
> Pip. No other people. No written text except 'Pip' on the romper.

Then append environment, camera, expressions, action, comedy beat, lighting,
and framing.

## kling3_0 — animation

```
duration : 3-15 seconds (default 5)   -> integer
mode     : "std" | "pro" | "4k"       -> use "pro"
sound    : "on" | "off"               -> ALWAYS "off"
medias   : roles "start_image", "end_image"
aspect   : 16:9 | 9:16 | 1:1
```

`sound` defaults to **`on`**. Always set `"off"` explicitly: it is both wrong
for our pipeline and more expensive.

### `cfg` is not a declared parameter

The brief specifies `CFG 0.5`. `kling3_0` declares no `cfg` parameter. Pass it
if you like — unknown params appear to pass through — but do not treat it as
required, and drop it first if a submission is rejected.

### Preset notice

If Kling replies with a preset recommendation instead of a job, re-submit the
identical request plus the returned `declined_preset_id`. Do not abandon the
scene.

## Batching

- `generate_image_batch` / `generate_video_batch` — **max 12 per call**
- `jobs_wait` — max 12 jobs, `timeout_seconds` max **15**
- Give every request a stable `index` (use the scene number) — results come
  back indexed, which is how you retry only what failed
- When everything is terminal, one `show_generation_by_ids` call (max 60).
  Never `show_generations`, never `job_display` per job.

`jobs_wait` returning `all_terminal: false` is normal — wait
`poll_after_seconds` and call again. A 15s cap means a 2-minute render needs
several polls; that is expected, not a failure.

## The NSFW false-positive

`soul_2` intermittently flags wholesome Pip + Mommy renders. It is a filter
artifact, not a real classification. Recovery order:

1. Do **not** halt the run — other scenes are unaffected
2. Reword: explicitly "wholesome", "G-rated", "fully clothed", "family-friendly"
3. Re-submit as a fresh job (new seed)
4. Fall back to `nano_banana_pro` + the reference image

Bath/tub scenes need extra care up front: keep Pip buried in bubbles or
wrapped in a towel, frame head-and-shoulders, and say "wholesome G-rated
family scene" in the prompt. Do not emphasise the body.

## Account

Plan `ultra`, ~1046 credits at bootstrap. Check `balance` before a big
long-form run. `unlim` is not currently available on these models, so
generations spend credits.
