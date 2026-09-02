# Monetization Plan — YouTube Partner Program

Goal: get `@showsforlittleones` into YPP and earning. This doc holds the
math and the production consequences. Update the numbers whenever YouTube
Studio's **Earn** tab is checked again.

## Where the channel actually stands

Snapshot from YouTube Studio, data as of **2026-08-20**:

| Requirement | Have | Need | % there |
|---|---|---|---|
| Subscribers | 1,012 | 500 | **met** |
| Public uploads, last 90d | 3 | 3 | **met** |
| Watch hours, last 365d | 4 | 3,000 | 0.13% |
| Shorts views, last 90d | 91,000 | 3,000,000 | 3.0% |

The subscriber and upload gates are done. Only **one** of the last two rows
has to clear. They are not equally far away.

## The two routes are not close to equal

**Watch hours: 0.13%.** 2,996 hours = 179,760 minutes still needed. A 5-minute
episode watched at a typical ~40% average view duration contributes ~2 minutes.
That is roughly **90,000 full long-form views inside a rolling 365 days**. The
channel has produced 4 watch hours to date. This route is not reachable from
here in any planning horizon that matters.

**Shorts views: 3.0%.** 91K per 90 days is ~1,010 views/day; the threshold
needs ~33,300/day. That is a 33× gap — large, but Shorts views do not scale
linearly. One Short that catches can do 500K on its own, which is 17% of the
whole requirement from a single upload. Long-form watch time has no equivalent
jump.

**The Shorts route is ~23× further along and is the only one with a
mechanism that can close the gap quickly. Produce for Shorts.**

This also matches the channel's own history: `docs/SHORTS_PLAYBOOK.md` calls
Shorts "the proven discovery format." The three long-form uploads produced
4 watch hours between them. That is the experiment's result.

## Be clear-eyed about what YPP pays here

Two things worth knowing before treating YPP as the finish line, both worth
confirming against the channel's own settings and YouTube's current terms:

- **Shorts RPM is low** — commonly quoted in the ~$0.05–0.15 per 1,000 views
  range. 3M Shorts views per quarter is therefore on the order of a few
  hundred dollars per quarter from Shorts alone, not a salary.
- **"Made for Kids" content carries restrictions.** Personalized ads are
  disabled on MFK videos, which cuts RPM materially, and channel memberships,
  Super Thanks and comments are unavailable. Check how this channel's videos
  are designated in Studio, because it changes the ceiling more than anything
  in this doc.

The realistic read: YPP acceptance is the unlock, and long-form watch time is
where the money eventually is — but the door opens through Shorts. Get in
first, then long-form becomes worth making again.

## Superseded in part — read `docs/CONTENT_STRATEGY.md` first

The 30-day analytics export (Aug 5 – Sep 1) revised two conclusions below:

- The real split is **habit content vs story content**, not long-form vs Shorts.
  Habit content wins in both formats; the story-format long-form got 4 views
  while the habit-format long-form got 12,749.
- Long-form is back in play. One long-form upload produced **152.7 watch
  hours** in 30 days. At that rate ~20 uploads clears the 3,000-hour gate,
  which is a shorter path than 3,000,000 Shorts views. Confirm against the Earn
  tab first — it read 4 qualified hours, which does not reconcile.

## Production consequences

1. **Shorts are the default format now.** 9:16, 1080x1920, 20–40s. Long-form
   is paused until the channel is monetized, or until a Short proves a concept
   worth expanding.
2. **Publish the water park episode anyway.** It keeps the 3-uploads-per-90-days
   gate satisfied and any watch hours it earns still count.
3. **Volume beats polish at this stage.** The threshold is a view count. More
   uploads is more chances at the one that catches.
4. **Repurposing is free.** A finished long-form episode contains 5+ minutes of
   generated footage. Re-cut vertical Shorts from it at **zero credits** — see
   `episodes/water-park-shorts/`. Do this for every future episode.

## Cost per Short — measured, not estimated

Real per-job costs from the credit ledger:

| Job | Credits |
|---|---|
| `nano_banana_pro` still | **2** |
| `kling3_0` **pro** video | **1.5 / second** (8s=12, 12s=18, 13s=19.5) |

So a purpose-built 30s Short of 5 clips x 6s:

```
5 stills  x 2            = 10
30s video x 1.5 (pro)    = 45
                         ---
                           55 credits
```

At **344 credits remaining**, that is about **6 purpose-built Shorts**.
Levers if that is too few:

- Test `mode: "std"` on one Short. If quality holds at Shorts size, it should
  roughly halve the video cost and take a Short to ~35 credits (~9–10 Shorts).
  Verify the actual charge in `transactions` before committing a batch.
- Shorter clips. 5 x 5s = 25s of video is 37.5 credits instead of 45.
- Reuse an established world (the water park exists now) so stills need less
  exploration and fewer retries.

Repurposed Shorts cost **0** and should always be exhausted first.

## Next actions

- [ ] Publish the three repurposed water park Shorts, spaced over several days
- [ ] Read the per-Short view counts after ~7 days — that is the real signal
- [ ] Cost-test one `std`-mode Short against a `pro` one
- [ ] Spend the remaining credits on purpose-built Shorts using the winning
      concepts from `docs/SHORTS_PLAYBOOK.md`
- [ ] Re-check the Earn tab and update the table at the top of this doc
