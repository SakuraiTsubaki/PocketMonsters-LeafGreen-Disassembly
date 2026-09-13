#!/usr/bin/env python3
"""Verify mapped LeafGreen core modules against known retail targets.

This tool is analysis-only. It never writes to the supplied ROM.
Module ranges and expected hashes live in config/module_boundaries.json.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROM_SIZE = 16 * 1024 * 1024
ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "module_boundaries.json"


def sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def load_targets() -> dict:
    return json.loads(CONFIG.read_text(encoding="utf-8"))["targets"]


def identify(data: bytes, targets: dict) -> str | None:
    digest = sha1(data)
    for name, cfg in targets.items():
        if cfg["sha1"] == digest:
            return name
    return None


def scan(path: Path, targets: dict) -> int:
    data = path.read_bytes()
    print(f"ROM: {path}")
    print(f"size: {len(data)} (expected {ROM_SIZE})")
    print(f"sha1: {sha1(data)}")

    target = identify(data, targets)
    if target is None:
        print("target: UNKNOWN")
        return 2

    cfg = targets[target]
    print(f"target: {target}")
    for key, value in cfg.get("families", {}).items():
        print(f"{key}-family: {value}")

    failed = False
    for module, info in cfg["modules"].items():
        start = int(info["start"], 0)
        end = int(info["end"], 0)
        expected = info["sha1"]
        actual = sha1(data[start:end])
        ok = actual == expected
        failed |= not ok
        print(
            f"{module}: 0x{start:06X}-0x{end - 1:06X} "
            f"size=0x{end - start:X} sha1={actual} "
            f"{'OK' if ok else 'MISMATCH'}"
        )
    return 1 if failed else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("rom", nargs="+", type=Path)
    args = parser.parse_args()

    targets = load_targets()
    status = 0
    for i, path in enumerate(args.rom):
        if i:
            print()
        status = max(status, scan(path, targets))
    return status


if __name__ == "__main__":
    raise SystemExit(main())
