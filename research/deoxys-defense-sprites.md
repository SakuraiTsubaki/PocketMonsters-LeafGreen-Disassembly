# Japanese Deoxys Defense Forme sprites

Target: BPGJ rev0, SHA-256 `2957b392dc09fc8df45a660af5493368d7bd378d299862f4cc115998e9da0bf2`.

The two previously neutral Japanese version sprite sheets are identified as Deoxys front and back battle graphics. Their ROM `CompressedSpriteSheet` entries use tag `0x019A` (`SPECIES_DEOXYS`, species 410) and size `0x0800`. The front entry is at `0x1F533C` in the table beginning at `0x1F466C`; the back entry is at `0x1F67DC` in the table beginning at `0x1F5B0C`. The derived bases have 28 and 9 decoded Thumb literal references respectively.

The palette entry at `0x1F759C` points to the 16-color LZ77 stream at `0xD39DC0` and carries the same tag. The verified ROM palette is preserved as JASC-PAL and used to render the color PNG sheets. PNGs retain ROM tile order (16×8 tiles, 2× scale) and are not screenshots.

Pinned primary reconstruction source `pret/pokefirered@037335f4c725d7c9aecdac87066f2002b4bd7e14` confirms the role: the front/back tables index `SPECIES_DEOXYS`; the `LEAFGREEN` branch in `src/data/graphics/pokemon.h` selects `front_def.4bpp.lz` and `back_def.4bpp.lz`; and `src/decompress.c` consumes the tables through the Pokémon picture decompression path.

No compressed or decoded ROM binary is published. Only reproducible PNG/palette outputs, metadata, hashes, table evidence, and source-level evidence are retained.
