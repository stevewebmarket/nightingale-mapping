"""Download the three reference WAVs into the project root so
`run_nightingale_baseline.py` (and the iter_*.py / conv_* scripts) can load them.

Pulls from the permanent GitHub Release attached to the canonical
`stevewebmarket/nightingale-mapping` repo. These URLs are stable and
do not expire, so this script works on any machine without Replit access.

Run from the project root:  python scripts/fetch_samples.py
"""
from __future__ import annotations

import sys
import urllib.request
from pathlib import Path

RELEASE_V1 = (
    "https://github.com/stevewebmarket/nightingale-mapping"
    "/releases/download/samples-v1"
)
RELEASE_V2 = (
    "https://github.com/stevewebmarket/nightingale-mapping"
    "/releases/download/samples-v2"
)

# (filename, release_base) pairs
SAMPLES = (
    ("birdsong.wav",   RELEASE_V1),
    ("orchestra.wav",  RELEASE_V1),
    ("rock.wav",       RELEASE_V1),
    ("flute.mp3",      RELEASE_V2),
    ("polyphonic.mp3", RELEASE_V2),
    ("highenergy.wav", RELEASE_V2),
)
ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    for name, base in SAMPLES:
        dst = ROOT / name
        if dst.exists() and dst.stat().st_size > 0:
            print(f"[ok ] {name} already present, skipping")
            continue
        url = f"{base}/{name}"
        print(f"downloading {url} -> {dst} ...", flush=True)
        try:
            with urllib.request.urlopen(url, timeout=60) as resp:
                data = resp.read()
        except Exception as exc:
            print(f"  FAILED: {exc}", file=sys.stderr)
            return 1
        dst.write_bytes(data)
        print(f"  done ({len(data) / (1024 * 1024):.1f} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
