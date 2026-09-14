# Pokémon sprite extraction

Pokémon graphics are extracted independently from all seven uploaded retail Pokémon LeafGreen ROMs, compared byte-for-byte after decompression, and deduplicated before being committed.

## Deduplication policy

When front graphics, back graphics, normal palettes, and shiny palettes are identical across targets, only one canonical asset set is stored. Per-ROM source offsets and hashes remain in `metadata/` so provenance is not lost.

Language folders are **not** created for identical graphics. A second copy is added only when the decoded graphic or palette actually differs.

## Upload policy

Sprite work is committed in small numbered batches instead of one huge upload. Human-viewable PNGs are committed first for review; source-format tile/palette exports and reconstruction metadata are committed in separate small source batches.

Each completed visual species set contains:

- `front_normal.png`
- `front_shiny.png`
- `back_normal.png`
- `back_shiny.png`

The images are rendered directly from the retail ROM's decompressed 64×64 4bpp tile data and GBA BGR555 palettes; they are not redraws.

No retail ROM, modified ROM, or reconstructed ROM binary is stored in this repository.

## Current visual batches

- `001–004`: Bulbasaur, Ivysaur, Venusaur, Charmander
- `005–008`: Charmeleon, Charizard, Squirtle, Wartortle
- `009–012`: Blastoise, Caterpie, Metapod, Butterfree
- `013–016`: Weedle, Kakuna, Beedrill, Pidgey
- `017–020`: Pidgeotto, Pidgeot, Rattata, Raticate
- `021–024`: Spearow, Fearow, Ekans, Arbok
- `025–028`: Pikachu, Raichu, Sandshrew, Sandslash
