#!/usr/bin/env bash
# First step whenever the user uploads a Suno MP3.
# Prints duration, embedded tags (title/lyrics if Suno wrote them) and stream
# info, so the scene plan is built against the real track length.
#
#   bash scripts/inspect_audio.sh episodes/<slug>/song/song.mp3
set -uo pipefail

if [ $# -lt 1 ]; then
    echo "usage: $0 <song.mp3>" >&2
    exit 1
fi

song="$1"
[ -f "$song" ] || { echo "!! not found: $song" >&2; exit 1; }
command -v ffprobe >/dev/null 2>&1 || { echo "!! ffprobe missing - run scripts/setup_env.sh" >&2; exit 1; }

echo "==> $song"

dur=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$song")
printf '    duration : %s s' "$dur"
python3 -c "
import sys
d = float(sys.argv[1])
print('  (%d:%05.2f)' % (int(d // 60), d % 60))
" "$dur" 2>/dev/null || echo

echo "    size     : $(ffprobe -v error -show_entries format=size -of default=nw=1:nk=1 "$song") bytes"

echo "--- stream ---"
ffprobe -v error -select_streams a:0 \
    -show_entries stream=codec_name,sample_rate,channels,bit_rate \
    -of default=nw=1 "$song"

echo "--- tags ---"
tags=$(ffprobe -v error -show_entries format_tags -of default=nw=1 "$song")
if [ -z "$tags" ]; then
    echo "(no embedded tags - title/lyrics must come from the user's concept)"
else
    echo "$tags"
fi
