#!/usr/bin/env python3
"""
Generate a QR code PNG for the landing URL.

Default URL:
  https://greenpeace-cl.github.io/hazte-socio/

Example:
  python3 scripts/generate_qr.py
  python3 scripts/generate_qr.py --out assets/qr.png --url https://example.com
"""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_URL = "https://greenpeace-cl.github.io/hazte-socio/"
DEFAULT_OUT = "assets/qr-hazte-socio.png"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a QR code PNG.")
    p.add_argument("--url", default=DEFAULT_URL, help=f"Target URL (default: {DEFAULT_URL})")
    p.add_argument("--out", default=DEFAULT_OUT, help=f"Output PNG path (default: {DEFAULT_OUT})")
    p.add_argument("--box-size", type=int, default=12, help="Pixels per QR module (default: 12)")
    p.add_argument("--border", type=int, default=4, help="Border modules (default: 4)")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    try:
        import qrcode
        from qrcode.constants import ERROR_CORRECT_M
    except Exception as e:  # pragma: no cover
        raise SystemExit(
            "Missing dependency. Install first:\n"
            "  python3 -m pip install -r requirements.txt\n"
        ) from e

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_M,
        box_size=args.box_size,
        border=args.border,
    )
    qr.add_data(args.url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(out_path)

    print(f"Saved: {out_path}")
    print(f"URL:   {args.url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
