"""Download the reference audio clips into the project root so the
M3 / M5 / M6 scripts can load them.

Pulls from the permanent GitHub Releases attached to the canonical
`stevewebmarket/nightingale-mapping` repo. These URLs are stable and
do not expire, so this script works on any machine with network.

Run from the project root:  python scripts/fetch_samples.py
"""
from __future__ import annotations

import sys
import urllib.request
from pathlib import Path

REPO = "https://github.com/stevewebmarket/nightingale-mapping"

# (filename, release-tag) pairs.
SAMPLES = (
    ("birdsong.wav",         "samples-v1"),
    ("orchestra.wav",        "samples-v1"),
    ("rock.wav",             "samples-v1"),
    ("flute.mp3",            "samples-v2"),
    ("polyphonic.mp3",       "samples-v2"),
    ("highenergy.wav",       "samples-v2"),
    ("twinkle_box.mp3",      "samples-v3"),
    ("twinkle_harmonica.wav","samples-v3"),
    ("twinkle_people.m4a",   "samples-v3"),
)
ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    for name, tag in SAMPLES:
        dst = ROOT / name
        if dst.exists() and dst.stat().st_size > 0:
            print(f"[ok ] {name} already present, skipping")
            continue
        url = f"{REPO}/releases/download/{tag}/{name}"
        print(f"downloading {url} -> {dst} ...", flush=True)
        try:
            with urllib.request.urlopen(url, timeout=60) as resp:
                data = resp.read()
        except Exception as exc:
            print(f"  FAILED: {exc}", file=sys.stderr)
            return 1
        dst.write_bytes(data)
        print(f"  done ({len(data) / (1024 * 1024):.2f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
