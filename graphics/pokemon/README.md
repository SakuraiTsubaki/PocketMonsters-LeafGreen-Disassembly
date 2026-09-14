# Pokémon sprite extraction — batch 001–004

This batch contains Pokémon #001–#004 from the seven uploaded retail Pokémon LeafGreen ROMs.

## Deduplication policy

All seven ROMs were parsed independently. For these four species, the decompressed front graphics, back graphics, normal palette, and shiny palette are byte-identical across USA, Europe Rev 1, German, French, Italian, Spanish, and Japanese targets.

Therefore only one canonical copy of each asset is stored here. `metadata/manifest.csv` records the source offset for every target ROM instead of duplicating the same asset seven times.

## Files per species

- `front.4bpp` — decompressed 64×64 4bpp front sprite tiles
- `back.4bpp` — decompressed 64×64 4bpp back sprite tiles
- `normal.gbapal` — 16-color normal palette in GBA BGR555 format
- `shiny.gbapal` — 16-color shiny palette in GBA BGR555 format
- `front_normal.png`
- `front_shiny.png`
- `back_normal.png`
- `back_shiny.png`

PNG files are human-viewable renderings generated directly from the extracted tile and palette data.

No ROM image or reconstructed ROM binary is included.
