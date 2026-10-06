#!/usr/bin/env python3
"""Operator Pack desk. Builds a design-partner packet. Does not sign evidence."""

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build_packet(buyer: str, site: str, out: Path) -> Path:
    out.mkdir(parents=True, exist_ok=True)
    cover = (
        f"Operator Pages — design-partner packet\n"
        f"Buyer: {buyer}\n"
        f"Site: {site}\n"
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\n"
        f"\n"
        f"This packet is a manifest, not a QuantumGuard receipt.\n"
        f"Seal it with the public QuantumGuard CLI (Ed25519, CONTRACT-v1).\n"
        f"Verdicts remain PASS / FAIL / INDETERMINATE. PQC is not claimed.\n"
        f"This product is not OpenMatter, S.5313, H.R.9129, or @QuantumGuard17.\n"
    )
    demo = (
        "RTP dual-verdict demo script\n"
        "1. Ingest a known-good ROS 2 telemetry sample. Expect ACCEPT only after QG PASS.\n"
        "2. Replay the same bytes. Verdict must match. No clock. No network.\n"
        "3. Flip one byte. Expect FAIL. Do not actuate.\n"
        "4. Omit the signature. Expect INDETERMINATE. Quarantine.\n"
        "A faithful twin of hijacked telemetry is still not evidence.\n"
    )
    files = {
        "COVER.txt": cover.encode(),
        "RTP-DEMO.txt": demo.encode(),
    }
    manifest = {
        "kind": "operator-pages.design-partner-packet",
        "version": 1,
        "buyer": buyer,
        "site": site,
        "sealed": False,
        "note": "SHA-256 only. Not an Ed25519 signature.",
        "files": [
            {"name": name, "sha256": sha256_bytes(blob)} for name, blob in files.items()
        ],
    }
    files["MANIFEST.json"] = json.dumps(manifest, indent=2).encode() + b"\n"
    for name, blob in files.items():
        (out / name).write_bytes(blob)
    print(f"wrote {out}")
    print("next: seal MANIFEST.json with quantumguard CLI; do not claim this desk signed it")
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Operator Pack desk")
    sub = parser.add_subparsers(dest="cmd", required=True)
    packet = sub.add_parser("packet", help="write a design-partner packet")
    packet.add_argument("--buyer", required=True)
    packet.add_argument("--site", required=True)
    packet.add_argument("--out", default="out")
    args = parser.parse_args()
    if args.cmd == "packet":
        build_packet(args.buyer, args.site, Path(args.out))


if __name__ == "__main__":
    main()
