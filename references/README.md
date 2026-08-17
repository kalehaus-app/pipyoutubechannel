# References

Approved character reference assets. These are **Higgsfield job IDs**, which
is what the generation tools consume — the binaries are not committed (media
is gitignored, and this environment's egress proxy blocks the asset CDN).

Pass one as a media input:

```
medias: [{ role: "image", value: "<job-id>" }]
```

## Pip + Mommy + Teddy — 9:16 living room (canonical)

```
54c9aaff-0c9a-4ab1-ac43-b829aef60edc
```

- 1152x2048 (9:16), `text2image_soul_v2`, style `General`, anchored on the
  Mommy Soul
- Warm living room, all three characters, correct adult/toddler proportions
- This is the reference named in the original channel brief and the one to use
  for `nano_banana_pro` fallback renders

## Pip + Mommy + Teddy — 16:9 backyard

```
47e100ab-77c9-45eb-a177-62e5e8cbe8de
```

- 2752x1536 (16:9), `nano_banana_pro`, generated from the 9:16 reference above
- Sunlit backyard, Pip in his Teddy-overhead victory pose, Mommy kneeling
- Added because long-form is 16:9 and the only prior reference was portrait

## Souls

| Character | Soul ID | Status |
|---|---|---|
| Pip | `44f638c0-b402-424a-a6ba-962eae4ca86d` | ready |
| Mommy | `6c889761-3c6d-45ee-8425-e6cb87dedeff` | ready |

Teddy is **not** a Soul — describe him in prompt text.

Other Souls in the account (`Kaley`, `Hank`, `Theo`, `Brexlee`,
`rechannel-narrator-alex`, `Whimsical Hide-and-Seek`) are unrelated to this
channel. Do not use them.

## Style

```
style_id: 3db34ab5-3439-4317-9e03-08dc30852e69   // "General", strength 1
```

See `docs/HIGGSFIELD_REFERENCE.md` for the full verified parameter set.
