# Global version-specific 4bpp sprite sheets

The Japanese `BPGJ` release remains the origin reference. This result extends the same two version-specific sprite sheets to the official English, German, French, Italian, and Spanish revision-0 releases without treating those releases as interchangeable ROMs.

Each verified local ROM was scanned for valid BIOS-LZ77 streams that decode to 4,096 bytes. FireRed and LeafGreen each contain 54 such streams in the full ROM; 52 decoded hashes are shared between the games. The two remaining LeafGreen streams exactly match the two previously extracted Japanese LeafGreen sheets by compressed and decompressed SHA-256. That cross-version comparison establishes the asset correspondence without relying on filenames or visual similarity alone.

| Language | Release | Sheet 0 | Sheet 1 |
| --- | --- | ---: | ---: |
| English | BPGE rev 0 | `0xE3958C` | `0xE39DE8` |
| German | BPGD rev 0 | `0xE39580` | `0xE39DDC` |
| French | BPGF rev 0 | `0xE3958C` | `0xE39DE8` |
| Italian | BPGI rev 0 | `0xE39584` | `0xE39DE0` |
| Spanish | BPGS rev 0 | `0xE3958C` | `0xE39DE8` |

Sheet 0 decodes to SHA-256 `71462d4b3254d963c16d42eb89327c4eb007da0a98a3ec1a903d089f65dce6df`; sheet 1 decodes to `de5a2254b3d9fba115ab66ee7e0a7432c13e02dd70cd31b07d4f3887f490d26b` in every language. The language-specific paths are retained so every published PNG has direct ROM provenance even though Git can deduplicate identical content.

Each output is 128 4bpp tiles rendered in ROM tile order as a 16×8 tile sheet and enlarged 2× to a 256×128 PNG. The deterministic grayscale index preview is intentional: the matching runtime palette has not yet been proven. Raw compressed or decoded ROM bytes are not stored.
