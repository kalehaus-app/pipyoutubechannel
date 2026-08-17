#!/usr/bin/env bash
# Final QC before declaring an episode done. Checks the things that actually
# go wrong: wrong canvas, missing audio, runtime drift against the song.
#
#   bash scripts/helpers/verify_output.sh renders/final.mp4 [song.mp3]
set -uo pipefail

[ $# -lt 1 ] && { echo "usage: $0 <final.mp4> [song.mp3]" >&2; exit 1; }
out="$1"
[ -f "$out" ] || { echo "!! not found: $out" >&2; exit 1; }

get() { ffprobe -v error -select_streams "$1" -show_entries "$2" -of default=nw=1:nk=1 "$out" | head -1; }

dur=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$out")
size=$(ffprobe -v error -show_entries format=size -of default=nw=1:nk=1 "$out")
w=$(get v:0 stream=width); h=$(get v:0 stream=height)
vcodec=$(get v:0 stream=codec_name); acodec=$(get a:0 stream=codec_name)
fps=$(get v:0 stream=r_frame_rate)

echo "==> $out"
echo "    ${w}x${h}  ${vcodec}  ${fps}fps"
echo "    audio: ${acodec:-NONE}"
printf '    runtime: %s s   size: %.1f MB\n' "$dur" "$(echo "$size" | awk '{print $1/1048576}')"

fail=0
if [ "$w" = "1920" ] && [ "$h" = "1080" ]; then echo "    ok: long-form canvas"
elif [ "$w" = "1080" ] && [ "$h" = "1920" ]; then echo "    ok: shorts canvas"
else echo "    !! unexpected canvas ${w}x${h}"; fail=1
fi

[ -z "$acodec" ] && { echo "    !! no audio stream - the MP3 was not muxed"; fail=1; }
[ "$vcodec" != "h264" ] && { echo "    !! video is $vcodec, expected h264"; fail=1; }

if [ $# -ge 2 ] && [ -f "$2" ]; then
    song=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$2")
    echo "    song: ${song} s"
    awk -v a="$dur" -v b="$song" 'BEGIN{
        d = a - b; if (d < 0) d = -d;
        if (d > 1.0) { printf "    !! runtime differs from song by %.2fs\n", d; exit 1 }
        printf "    ok: runtime matches song (%.2fs diff)\n", d
    }' || fail=1
fi

awk -v s="$size" 'BEGIN{ if (s/1048576 > 100) print "    !! over 100 MB - do not commit to git" }'

[ $fail -ne 0 ] && { echo "==> FAILED QC"; exit 1; }
echo "==> passed QC"
