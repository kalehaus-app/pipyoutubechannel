#!/usr/bin/env bash
# Prepare an ephemeral container for Pip video assembly.
# The session container ships without ffmpeg and is wiped between sessions,
# so run this before any normalize/assemble/mux step.
set -uo pipefail

need_install=0
command -v ffmpeg  >/dev/null 2>&1 || need_install=1
command -v ffprobe >/dev/null 2>&1 || need_install=1

if [ "$need_install" -eq 1 ]; then
    echo "==> installing ffmpeg (this takes a few minutes on a cold container)"
    SUDO=""
    [ "$(id -u)" -ne 0 ] && SUDO="sudo"

    # A bare `apt-get install` can fail on stale indexes with 404s on individual
    # .debs; refreshing first fixes it. Third-party PPAs may 403 behind the
    # egress proxy - harmless, the main archive is what matters.
    $SUDO apt-get update -qq
    $SUDO apt-get install -y ffmpeg || {
        echo "!! ffmpeg install failed" >&2
        exit 1
    }
fi

command -v ffmpeg >/dev/null 2>&1 || { echo "!! ffmpeg still missing" >&2; exit 1; }

echo "==> $(ffmpeg -version 2>/dev/null | head -1)"

fail=0
check() {
    if [ -z "$2" ]; then
        echo "!! MISSING: $1" >&2
        fail=1
    else
        echo "    ok: $1"
    fi
}

check "libx264 encoder" "$(ffmpeg -hide_banner -encoders 2>/dev/null | grep -w libx264)"
check "aac encoder"     "$(ffmpeg -hide_banner -encoders 2>/dev/null | grep -E '^ A....D aac ')"
check "xfade filter"    "$(ffmpeg -hide_banner -filters  2>/dev/null | grep -E '^ .S. xfade ')"
check "scale filter"    "$(ffmpeg -hide_banner -filters  2>/dev/null | grep -E ' scale ')"
check "python3"         "$(command -v python3)"

if [ "$fail" -ne 0 ]; then
    echo "==> environment INCOMPLETE" >&2
    exit 1
fi

echo "==> environment ready"
