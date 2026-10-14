import hashlib, json, unittest
from pathlib import Path

ROOT=Path(__file__).parents[1]
class Tests(unittest.TestCase):
 def test_english_rev1_assets_tables_and_palette(self):
  sha='2f978f635b9593f6ca26ec42481c53a6b39f6cddd894ad5c062c1419fac58825';release='en-rev1'
  pal=json.loads((ROOT/f'analysis/leafgreen-{release}-deoxys-palette.json').read_text());self.assertEqual(pal['rom_sha256'],sha);self.assertEqual(pal['palette_sha256'],'479c76fdaf9a0ca458fa37a514b9bbf20d9dc3c7b82d813ea743e4830a58f197')
  for role,offset,table,refs in (('front',0xE3958C,0x2350F8,28),('back',0xE39DE8,0x236598,9)):
   asset=json.loads((ROOT/f'analysis/leafgreen-{release}-deoxys-defense-{role}.json').read_text());e=json.loads((ROOT/f'analysis/leafgreen-{release}-deoxys-{role}-table.json').read_text())['entries'][0]
   self.assertEqual(asset['rom_sha256'],sha);self.assertEqual(asset['source_offset'],offset);self.assertEqual(asset['palette'],'jasc-pal');self.assertEqual((e['table_offset'],e['size'],e['tag']),(table,0x800,410));self.assertEqual(len(e['table_thumb_references']),refs)
 def test_manifest(self):
  m=json.loads((ROOT/'manifests/deoxys-defense-revisions.json').read_text());self.assertFalse(m['raw_rom_bytes_included'])
  for o in m['outputs']:self.assertEqual(hashlib.sha256((ROOT/o['path']).read_bytes()).hexdigest(),o['sha256'])
if __name__=='__main__':unittest.main()
