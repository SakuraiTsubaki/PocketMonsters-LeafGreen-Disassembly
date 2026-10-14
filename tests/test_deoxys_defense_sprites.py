import hashlib
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
ROM_SHA = "2957b392dc09fc8df45a660af5493368d7bd378d299862f4cc115998e9da0bf2"


class DeoxysDefenseSpriteTests(unittest.TestCase):
    def test_species_tables(self):
        expected = {
            "front": (0xD3958C, 0x1F533C, 0x1F466C, 28),
            "back": (0xD39DE8, 0x1F67DC, 0x1F5B0C, 9),
        }
        for role, (source, entry, table, refs) in expected.items():
            report = json.loads((ROOT / "analysis" / f"leafgreen-jp-rev0-deoxys-{role}-table.json").read_text())
            self.assertEqual(report["source_sha256"], ROM_SHA)
            self.assertEqual(report["asset"]["source_offset"], source)
            item = report["entries"][0]
            self.assertEqual((item["entry_offset"], item["table_offset"]), (entry, table))
            self.assertEqual((item["size"], item["tag"]), (0x800, 410))
            self.assertEqual(len(item["table_thumb_references"]), refs)

    def test_palette_and_color_outputs(self):
        palette = json.loads((ROOT / "analysis/leafgreen-jp-rev0-deoxys-palette.json").read_text())
        self.assertEqual((palette["source_offset"], palette["color_count"]), (0xD39DC0, 16))
        self.assertEqual(palette["rom_sha256"], ROM_SHA)
        self.assertEqual(hashlib.sha256((ROOT / "graphics/pokemon/deoxys-normal-jp.pal").read_bytes()).hexdigest(), palette["palette_sha256"])
        for role in ("front", "back"):
            report = json.loads((ROOT / "analysis" / f"leafgreen-jp-rev0-deoxys-defense-{role}.json").read_text())
            png = ROOT / "graphics/pokemon" / f"deoxys-defense-{role}-jp.png"
            self.assertEqual(report["palette"], "jasc-pal")
            self.assertEqual(report["palette_sha256"], palette["palette_sha256"])
            self.assertEqual(hashlib.sha256(png.read_bytes()).hexdigest(), report["png_sha256"])

    def test_manifest(self):
        manifest = json.loads((ROOT / "manifests/deoxys-defense-sprites.json").read_text())
        self.assertFalse(manifest["raw_rom_bytes_included"])
        for output in manifest["outputs"]:
            self.assertEqual(hashlib.sha256((ROOT / output["path"]).read_bytes()).hexdigest(), output["sha256"])


if __name__ == "__main__":
    unittest.main()
