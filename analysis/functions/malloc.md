# malloc module

## Scope

`malloc` follows `bg`, but unlike the immediately preceding core modules it is not one byte-layout family across all seven retail targets.

The same 12 semantic functions are present in every target, but the module splits into two verified layout families.

## Family A — Japan / USA / Europe Rev 1

| Target | Start | End exclusive | Size | SHA-1 |
|---|---:|---:|---:|---|
| Japan | `0x00292C` | `0x002C28` | `0x2FC` | `38aef8e169a52cee8f0fbbcb9a7252e79e318913` |
| USA | `0x00292C` | `0x002C28` | `0x2FC` | `8d5f493a96aa8b573f77fc266961e6bebaba4d90` |
| Europe Rev 1 | `0x002940` | `0x002C3C` | `0x2FC` | `2b1091d7c57909bfcc056ef2bb45e1b20607299a` |

Relative function offsets:

`000, 01C, 030, 0DC, 1BC, 1FC, 254, 270, 284, 298, 2AC, 2C0`

## Family B — Germany / France / Italy / Spain

| Target | Start | End exclusive | Size | SHA-1 |
|---|---:|---:|---:|---|
| Germany | `0x00293C` | `0x002BA8` | `0x26C` | `af19de3863a09c95dae346598dee448e7c6fe691` |
| France | `0x002928` | `0x002B94` | `0x26C` | `bd5afaf2213afe3e24bab8282e745969639638e2` |
| Italy | `0x00293C` | `0x002BA8` | `0x26C` | `ee3dfc9fa74136b33547c22d3f45e015d883ffea` |
| Spain | `0x002928` | `0x002B94` | `0x26C` | `a55729c5e882f6b760fefea670fdb4d83e710b57` |

Relative function offsets:

`000, 01C, 030, 0C8, 12C, 16C, 1C4, 1E0, 1F4, 208, 21C, 230`

Family B is exactly `0x90` bytes shorter than Family A.

## Function order

All targets retain this semantic order:

1. `PutMemBlockHeader`
2. `PutFirstMemBlockHeader`
3. `AllocInternal`
4. `FreeInternal`
5. `AllocZeroedInternal`
6. `CheckMemBlockInternal`
7. `InitHeap`
8. `Alloc`
9. `AllocZeroed`
10. `Free`
11. `CheckMemBlock`
12. `CheckHeap`

The exact per-target addresses are in `symbols/malloc.csv`.

## Assertion evidence

The USA, Japan, and Europe Rev 1 reference ROMs contain the ASCII path `gflib/malloc.c` used by the allocator's assertion/error-checking paths. The Germany, France, Italy, and Spain ROMs do not contain that string. The Family B code also contracts specifically through the allocator's internal/error-checking region.

This is strong ROM-level evidence that Family B was built with those assertion/debug paths omitted or otherwise compiled away. The precise historical build flag/toolchain cause is not yet asserted here; it should be documented only when independently verified.

## Reconstruction decision

Do **not** force a single byte-layout object for `malloc`.

Use one semantic allocator source where practical, but retain target-family build configuration so that:

- Family A reproduces the longer assertion-bearing layout;
- Family B reproduces the shorter localized-European layout;
- function identities remain shared while addresses are generated per target.

The next object begins immediately at each family's end and belongs to `text_printer`.
