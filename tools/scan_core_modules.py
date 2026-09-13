#!/usr/bin/env python3
"""Verify early LeafGreen core modules against known retail targets.

This tool is analysis-only. It never writes to the supplied ROM.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

ROM_SIZE = 16 * 1024 * 1024

TARGETS = {
    "japan": {
        "sha1": "5946f1b59e8d71cc61249661464d864185c92a5f",
        "dma3_manager": (0x000BFC, 0x001028, "8b2718bf8a170d9da2998e724a8ab51659d59f01"),
        "bg": (0x001028, 0x00292C, "ce1c4738712844bf006027cf67aa4bff59371994"),
        "malloc": (0x00292C, 0x002C28, "38aef8e169a52cee8f0fbbcb9a7252e79e318913"),
        "malloc_family": "A",
    },
    "usa": {
        "sha1": "574fa542ffebb14be69902d1d36f1ec0a4afd71e",
        "dma3_manager": (0x000BFC, 0x001028, "8b2718bf8a170d9da2998e724a8ab51659d59f01"),
        "bg": (0x001028, 0x00292C, "3e2b21fa70d2be1ed917d5ac1e843a16755342ed"),
        "malloc": (0x00292C, 0x002C28, "8d5f493a96aa8b573f77fc266961e6bebaba4d90"),
        "malloc_family": "A",
    },
    "europe_rev1": {
        "sha1": "7862c67bdecbe21d1d69ce082ce34327e1c6ed5e",
        "dma3_manager": (0x000C10, 0x00103C, "8b2718bf8a170d9da2998e724a8ab51659d59f01"),
        "bg": (0x00103C, 0x002940, "c835d551e0296848114f4907484b1a4f2c4699a7"),
        "malloc": (0x002940, 0x002C3C, "2b1091d7c57909bfcc056ef2bb45e1b20607299a"),
        "malloc_family": "A",
    },
    "germany": {
        "sha1": "0802d1fb185ee3ed48d9a22afb25e66424076dac",
        "dma3_manager": (0x000C0C, 0x001038, "8b2718bf8a170d9da2998e724a8ab51659d59f01"),
        "bg": (0x001038, 0x00293C, "7a2b1049975e4c6d41b003e74b08db6783090fd4"),
        "malloc": (0x00293C, 0x002BA8, "af19de3863a09c95dae346598dee448e7c6fe691"),
        "malloc_family": "B",
    },
    "france": {
        "sha1": "4b5758c14d0a07b70ef3ef0bd7fa5e7ce6978672",
        "dma3_manager": (0x000BF8, 0x001024, "8b2718bf8a170d9da2998e724a8ab51659d59f01"),
        "bg": (0x001024, 0x002928, "9dc2a474d6ada2bd7d51ea72158ce8f33cc027ce"),
        "malloc": (0x002928, 0x002B94, "bd5afaf2213afe3e24bab8282e745969639638e2"),
        "malloc_family": "B",
    },
    "italy": {
        "sha1": "a1dfea1493d26d1f024be8ba1de3d193fcfc651e",
        "dma3_manager": (0x000C0C, 0x001038, "8b2718bf8a170d9da2998e724a8ab51659d59f01"),
        "bg": (0x001038, 0x00293C, "e154f52450bd4f9983af3266c680e808d29bc786"),
        "malloc": (0x00293C, 0x002BA8, "ee3dfc9fa74136b33547c22d3f45e015d883ffea"),
        "malloc_family": "B",
    },
    "spain": {
        "sha1": "f9ebee5d228cb695f18ef2ced41630a09fa9eb05",
        "dma3_manager": (0x000BF8, 0x001024, "8b2718bf8a170d9da2998e724a8ab51659d59f01"),
        "bg": (0x001024, 0x002928, "452c5e2e8ea01df7580318df7a6e4e3c262e501a"),
        "malloc": (0x002928, 0x002B94, "a55729c5e882f6b760fefea670fdb4d83e710b57"),
        "malloc_family": "B",
    },
}


def sha1(data: bytes) -> str:
    return hashlib.sha1(data).hexdigest()


def identify(data: bytes) -> str | None:
    digest = sha1(data)
    for name, cfg in TARGETS.items():
        if cfg["sha1"] == digest:
            return name
    return None


def scan(path: Path) -> int:
    data = path.read_bytes()
    print(f"ROM: {path}")
    print(f"size: {len(data)} (expected {ROM_SIZE})")
    full_sha1 = sha1(data)
    print(f"sha1: {full_sha1}")

    target = identify(data)
    if target is None:
        print("target: UNKNOWN")
        return 2

    cfg = TARGETS[target]
    print(f"target: {target}")
    print(f"malloc-family: {cfg['malloc_family']}")

    failed = False
    for module in ("dma3_manager", "bg", "malloc"):
        start, end, expected = cfg[module]
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

    status = 0
    for i, path in enumerate(args.rom):
        if i:
            print()
        status = max(status, scan(path))
    return status


if __name__ == "__main__":
    raise SystemExit(main())
