from __future__ import annotations

import hashlib
import json
import struct
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ("en", "de", "fr", "it", "es")
ROM_SHA256 = {
    "en": "78d310d557ceebc593bd393acc52d1b19a8f023fec40bc200e6063880d8531fc",
    "de": "6ab7183caf8bf093f42351cf7c891722ecef85f2ded922f6d2491c6062fa3fc2",
    "fr": "cc0fa93f4631d0814afcd5a273edf28f2876e126e8ef0df4dd39dd6f36e53ed3",
    "it": "c71599a482c43df2104ce6be903393333d3ebacbf392ea5fcd8792dada8a5076",
    "es": "f8908e0bd32cf27077a26b557e1eea0ff06ce8059bee5dc7d799aab44a070d48",
}
OFFSETS = {
    "en": (0xE3958C, 0xE39DE8),
    "de": (0xE39580, 0xE39DDC),
    "fr": (0xE3958C, 0xE39DE8),
    "it": (0xE39584, 0xE39DE0),
    "es": (0xE3958C, 0xE39DE8),
}


class GlobalVersionSpriteSheetTests(unittest.TestCase):
    def test_reports_match_release_and_japanese_reference(self):
        jp = [
            json.loads((ROOT / "analysis" / f"leafgreen-jp-version-sprite-sheet-{sheet}.json").read_text())
            for sheet in range(2)
        ]
        for language in LANGUAGES:
            for sheet in range(2):
                report = json.loads(
                    (ROOT / "analysis" / f"leafgreen-{language}-version-sprite-sheet-{sheet}.json").read_text()
                )
                png = ROOT / "graphics" / "title" / f"{language}-version-sprite-sheet-{sheet}.png"
                self.assertEqual(report["rom_sha256"], ROM_SHA256[language])
                self.assertEqual(report["source_offset"], OFFSETS[language][sheet])
                self.assertEqual(report["compressed_sha256"], jp[sheet]["compressed_sha256"])
                self.assertEqual(report["decompressed_sha256"], jp[sheet]["decompressed_sha256"])
                self.assertEqual(report["decompressed_length"], 4096)
                self.assertEqual(report["tile_count"], 128)
                self.assertEqual(report["tiles_per_row"], 16)
                self.assertEqual(report["palette"], "grayscale-index-preview")
                self.assertFalse(report["raw_rom_bytes_included"])
                self.assertEqual(hashlib.sha256(png.read_bytes()).hexdigest(), report["png_sha256"])
                self.assertEqual(struct.unpack(">II", png.read_bytes()[16:24]), (256, 128))

    def test_manifest_outputs(self):
        manifest = json.loads((ROOT / "manifests" / "global-version-sprite-sheets.json").read_text())
        self.assertEqual(manifest["languages"], list(LANGUAGES))
        self.assertEqual({item["language"] for item in manifest["releases"]}, set(LANGUAGES))
        self.assertFalse(manifest["raw_rom_bytes_included"])
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(), output["sha256"])


if __name__ == "__main__":
    unittest.main()
