# sprite module

## Scope

`sprite` follows `text` and contains the core OAM/sprite engine: sprite lifecycle, sorting, OAM construction, animation and affine-animation state, tile allocation, sprite sheet/palette management, subsprites, copy requests, and matrix anchoring.

## Verified boundaries

| Target | Start | End exclusive | Size | SHA-1 |
|---|---:|---:|---:|---|
| japan | `0x00668C` | `0x008870` | `0x21E4` | `8436744015fa8e2c51a0008016825e485982e958` |
| usa | `0x006B10` | `0x008CF4` | `0x21E4` | `dd60a567132520a3b0f084c9204bf00282a3e940` |
| europe_rev1 | `0x006B24` | `0x008D08` | `0x21E4` | `a3d90e132fa9d617164ee3f2e068d4d1573cbf2d` |
| germany | `0x006A90` | `0x008C74` | `0x21E4` | `c838559cb5a10516012f77ad28be80d608fe049e` |
| france | `0x006A7C` | `0x008C60` | `0x21E4` | `2f4cf8da778cb689a8ad3bb84e38b30a67749854` |
| italy | `0x006A90` | `0x008C74` | `0x21E4` | `b898b620edc1b339f922104f7e4c8efcfdb8da5c` |
| spain | `0x006A7C` | `0x008C60` | `0x21E4` | `03d5aebb607dbfc9ccfee7a3d2e78bf7ea317357` |

All seven targets therefore preserve one `0x21E4`-byte code layout. Raw module SHA-1 values differ because absolute addresses and target data references differ.

## Layout evidence

A set of widely used engine entry points was matched directly against every reference ROM at the same relative offsets. This includes `ResetSpriteData`, `AnimateSprites`, `BuildOamBuffer`, `CreateSprite`, `DestroySprite`, `SpriteCallbackDummy`, animation entry points, and sprite sheet/palette loaders. The verified address matrix is in `symbols/sprite_key.csv`.

The next object starts with `StringCopy_Nickname`:

- Japan: `0x08008870`
- USA: `0x08008CF4`
- Europe Rev 1: `0x08008D08`
- Germany / Italy: `0x08008C74`
- France / Spain: `0x08008C60`

The Japanese routine immediately exposes the expected target-language difference: the nickname copy limit is 5 characters, while the international routine uses 10. This makes the following `string_util` boundary independently recognizable instead of relying only on the fixed module size.

## Reconstruction decision

Treat `sprite` as a single common semantic/function-layout module. Target-specific addresses and referenced data are relocation/configuration concerns, not separate copies of the engine source.

This module is sprite **engine code**, not the Pokémon/trainer sprite graphics asset set. Graphic extraction/restoration will be stored separately under the graphics tree; when that asset work begins, human-viewable PNG files are required alongside source metadata.

No retail-ROM `incbin` is permitted in the final reconstruction.
