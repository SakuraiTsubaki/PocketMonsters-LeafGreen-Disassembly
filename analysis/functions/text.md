# text module

## Scope

`text` follows `window_8bpp` and ends where the sprite engine begins at `ResetSpriteData`. The module contains the core font dispatchers, down-arrow/text-state handling, string measurement, text cursor/keypad helpers, and glyph decompression/width functions.

## Verified boundaries

| Target | Start | End exclusive | Size | SHA-1 | Family |
|---|---:|---:|---:|---|---|
| japan | `0x005348` | `0x00668C` | `0x1344` | `9dbf6d2c61378de79f2cfe7bf252158db3685ad0` | JP |
| usa | `0x00537C` | `0x006B10` | `0x1794` | `1ab3000917f4b7ec589f46c76cd630a1e4856c0b` | INTL |
| europe_rev1 | `0x005390` | `0x006B24` | `0x1794` | `2892dc2eb454c8785a154a68ad6489aa0ffcb583` | INTL |
| germany | `0x0052FC` | `0x006A90` | `0x1794` | `3c43ffb93e1984a1de10191c35c918e561bce36c` | INTL |
| france | `0x0052E8` | `0x006A7C` | `0x1794` | `7181a9c549c5b6b0de6582b1966c0cc6cac6a306` | INTL |
| italy | `0x0052FC` | `0x006A90` | `0x1794` | `946114b37abf606f005d117886f161b5e8160fee` | INTL |
| spain | `0x0052E8` | `0x006A7C` | `0x1794` | `6dc73b75069bec2aed5814761e1452b6d63036a7` | INTL |

The six international targets have the same `0x1794`-byte function layout. Japan is `0x1344` bytes, exactly `0x450` bytes shorter.

## Function layout

There are 38 semantic functions in both families. International targets share one relative-offset table. Japan preserves the same function order but has its own offsets after the early text-renderer section. Exact absolute addresses are in `symbols/text.csv`.

Key structural split:

- Functions 1–14 (`FontFunc_Small` through `RenderText`) begin at the same relative offsets in both families.
- Japanese `RenderText` ends earlier, shifting later functions.
- Japanese glyph decompressors are compiled around the Japanese font data path and omit the international dual-language branches.
- Width helpers become especially small in the Japanese build: e.g. the small-font and normal-copy width paths reduce to fixed Japanese widths where applicable.
- The final function is `DecompressGlyph_Bold`; the following bytes are `ResetSpriteData`, the start of `sprite`.

## Boundary evidence

For the USA retail target, `ResetSpriteData` is at ROM offset `0x006B10` (`0x08006B10` in GBA ROM address space). Its Thumb instruction prefix was matched directly in all seven reference ROMs, locating the corresponding `sprite` start at:

- Japan `0x00668C`
- USA `0x006B10`
- Europe Rev 1 `0x006B24`
- Germany / Italy `0x006A90`
- France / Spain `0x006A7C`

This independently fixes the end of `text` for every target.

## Reconstruction decision

Treat `text` as one semantic module with two build families rather than seven source copies:

- `JP`: Japanese retail compile layout.
- `INTL`: shared international function layout, with target-specific relocation/data addresses resolved by the linker and target data.

Do not use a retail ROM or an `incbin` of this module in the final build. The ROM ranges above are analysis evidence only; the reconstruction target is source plus font/text assets in the repository.
