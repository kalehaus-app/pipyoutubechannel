#!/usr/bin/env python3
"""Assemble Pip episode clips into a finished MP4 with the user's Suno MP3.

Takes a manifest describing the scene order, normalizes every clip to one
canvas/fps/pixel format, loops short clips to fill their slot, crossfades
scene to scene, and muxes the MP3 as the sole audio bed.

    python3 scripts/assemble.py episodes/<slug>/manifest.json

Manifest (paths are relative to the manifest file's own directory):

    {
      "title":     "Pip's Water Park Fun Day",
      "aspect":    "16:9",              // or "9:16"
      "fps":       24,
      "crossfade": 0.5,                 // seconds between scenes
      "audio":     "song/song.mp3",
      "output":    "renders/final.mp4",
      "scenes": [
        {"n": 1, "clip": "clips/s01.mp4", "duration": 12.0},
        {"n": 2, "clip": "clips/s02.mp4"}          // natural clip duration
      ]
    }

Clips are expected to be silent; any audio they carry is discarded.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CANVAS = {"16:9": (1920, 1080), "9:16": (1080, 1920)}

# Kling clips land near but not exactly on the target canvas (16:9 comes back
# around 1928x1076), so every clip is rescaled and cropped rather than trusted.
NORMALIZE = (
    "scale={w}:{h}:force_original_aspect_ratio=increase,"
    "crop={w}:{h},setsar=1,fps={fps},format=yuv420p"
)


def run(cmd: list[str]) -> None:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        # ffmpeg puts the actual reason in the last few stderr lines.
        tail = "\n".join(proc.stderr.strip().splitlines()[-15:])
        raise SystemExit(f"!! ffmpeg failed:\n  {' '.join(cmd)}\n{tail}")


def probe_duration(path: Path) -> float:
    proc = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True,
    )
    if proc.returncode != 0:
        raise SystemExit(f"!! cannot probe {path}\n{proc.stderr.strip()}")
    try:
        return float(proc.stdout.strip())
    except ValueError:
        raise SystemExit(f"!! no duration reported for {path}")


def normalize_scene(src: Path, dst: Path, slot: float, w: int, h: int,
                    fps: int, xfade: float) -> None:
    """Render `src` to exactly `slot` seconds on the target canvas.

    A clip shorter than its slot is looped. Looping is done with -stream_loop
    plus a hard trim so the seam count doesn't matter; prefer generating enough
    unique scenes over relying on this.
    """
    src_dur = probe_duration(src)
    vf = NORMALIZE.format(w=w, h=h, fps=fps)

    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error"]
    if src_dur < slot - 0.05:
        loops = int(slot // src_dur) + 1
        print(f"    clip is {src_dur:.2f}s for a {slot:.2f}s slot "
              f"-> looping x{loops + 1}")
        cmd += ["-stream_loop", str(loops)]
    cmd += ["-i", str(src), "-t", f"{slot:.3f}", "-vf", vf, "-an",
            "-c:v", "libx264", "-crf", "18", "-preset", "medium",
            "-pix_fmt", "yuv420p", str(dst)]
    run(cmd)


def build_video(scenes: list[Path], durations: list[float], xfade: float,
                fps: int, dst: Path) -> None:
    """Crossfade the normalized scenes into one continuous video."""
    if len(scenes) == 1:
        shutil.copy(scenes[0], dst)
        return

    cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error"]
    for s in scenes:
        cmd += ["-i", str(s)]

    # Each xfade consumes `xfade` seconds of overlap, so the offset for the
    # next transition is the running total minus the fades already spent.
    steps, prev, offset = [], "[0:v]", 0.0
    for i in range(1, len(scenes)):
        offset += durations[i - 1] - xfade
        label = f"[v{i}]" if i < len(scenes) - 1 else "[out]"
        steps.append(
            f"{prev}[{i}:v]xfade=transition=fade:"
            f"duration={xfade}:offset={offset:.3f}{label}"
        )
        prev = label

    cmd += ["-filter_complex", ";".join(steps), "-map", "[out]",
            "-r", str(fps), "-c:v", "libx264", "-crf", "20", "-preset", "slow",
            "-pix_fmt", "yuv420p", str(dst)]
    run(cmd)


def mux(video: Path, audio: Path, dst: Path) -> None:
    """Attach the user's MP3 as the only audio stream.

    -shortest lets whichever of song/visuals ends first define the end; the
    video is built at least as long as the song, so the song defines it.
    """
    dst.parent.mkdir(parents=True, exist_ok=True)
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
         "-i", str(video), "-i", str(audio),
         "-map", "0:v", "-map", "1:a", "-c:v", "copy",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
         "-shortest", "-movflags", "+faststart", str(dst)])


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Assemble Pip episode clips into a finished MP4.")
    ap.add_argument("manifest", type=Path)
    ap.add_argument("--keep-temp", action="store_true",
                    help="keep normalized intermediates for debugging")
    args = ap.parse_args()

    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            raise SystemExit(f"!! {tool} not found - run scripts/setup_env.sh")

    m = json.loads(args.manifest.read_text())
    root = args.manifest.parent

    aspect = m.get("aspect", "16:9")
    if aspect not in CANVAS:
        raise SystemExit(f"!! aspect must be one of {list(CANVAS)}")
    w, h = CANVAS[aspect]
    fps = int(m.get("fps", 24))
    xfade = float(m.get("crossfade", 0.5))

    scenes = m.get("scenes") or []
    if not scenes:
        raise SystemExit("!! manifest has no scenes")

    audio = root / m["audio"]
    if not audio.exists():
        raise SystemExit(f"!! song not found: {audio}")
    song_dur = probe_duration(audio)

    print(f"==> {m.get('title', args.manifest.stem)}")
    print(f"    {aspect} {w}x{h} @ {fps}fps, {len(scenes)} scenes")
    print(f"    song {song_dur:.2f}s")

    tmp = Path(tempfile.mkdtemp(prefix="pip-assemble-"))
    try:
        normalized, durations = [], []
        for i, sc in enumerate(scenes):
            clip = root / sc["clip"]
            if not clip.exists():
                raise SystemExit(f"!! scene {sc.get('n', i + 1)}: missing {clip}")
            slot = float(sc["duration"]) if sc.get("duration") else probe_duration(clip)
            print(f"  [{sc.get('n', i + 1):>2}] {clip.name} -> {slot:.2f}s")
            dst = tmp / f"n{i:03d}.mp4"
            normalize_scene(clip, dst, slot, w, h, fps, xfade)
            normalized.append(dst)
            durations.append(slot)

        timeline = sum(durations) - xfade * (len(durations) - 1)
        print(f"==> timeline {timeline:.2f}s vs song {song_dur:.2f}s")
        if timeline < song_dur - 0.5:
            print(f"    !! visuals are {song_dur - timeline:.2f}s SHORT of the "
                  f"song; -shortest will cut the song off early")

        silent = tmp / "silent.mp4"
        build_video(normalized, durations, xfade, fps, silent)

        out = root / m.get("output", "renders/final.mp4")
        mux(silent, audio, out)

        size_mb = out.stat().st_size / 1024 / 1024
        print(f"==> {out}  ({probe_duration(out):.2f}s, {size_mb:.1f} MB)")
    finally:
        if args.keep_temp:
            print(f"    intermediates: {tmp}")
        else:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
