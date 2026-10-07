import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_reports_and_pngs(self):
  hashes=[]
  for i in range(2):
   r=json.loads((ROOT/f'analysis/leafgreen-jp-version-sprite-sheet-{i}.json').read_text());p=ROOT/f'graphics/title/jp-version-sprite-sheet-{i}.png'
   self.assertEqual(r['rom_sha256'],'2957b392dc09fc8df45a660af5493368d7bd378d299862f4cc115998e9da0bf2');self.assertEqual(r['decompressed_length'],4096);self.assertEqual(r['tile_count'],128);self.assertEqual(r['tiles_per_row'],16);self.assertEqual(r['palette'],'grayscale-index-preview');self.assertFalse(r['raw_rom_bytes_included']);self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),r['png_sha256']);hashes.append(r['decompressed_sha256'])
  self.assertEqual(len(set(hashes)),2)
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/jp-version-sprite-sheets.json').read_text());self.assertFalse(m['raw_rom_bytes_included']);self.assertEqual(m['palette_status'],'unverified-not-published')
  for o in m['outputs']:self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256'])
if __name__=='__main__':unittest.main()

