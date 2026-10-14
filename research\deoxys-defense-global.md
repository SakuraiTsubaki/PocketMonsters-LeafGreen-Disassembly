# Global Deoxys Defense Forme sprites

The English, German, French, Italian, and Spanish rev0 releases were checked independently against their pinned ROM SHA-256 identities. In every release, the compressed sheets at the recorded offsets resolve to species 410 (`SPECIES_DEOXYS`) entries with size `0x0800` in the runtime front- and back-pic tables. The front tables have 28 or 29 decoded Thumb references depending on the localization; every back table has 9.

All five releases decode to the same Defense Forme pixels as Japanese rev0: front SHA-256 `71462d4b3254d963c16d42eb89327c4eb007da0a98a3ec1a903d089f65dce6df` and back SHA-256 `de5a2254b3d9fba115ab66ee7e0a7432c13e02dd70cd31b07d4f3887f490d26b`. Their 16-color palette also decodes identically. The repository preserves a color PNG and JASC palette for every verified release, plus release-specific compression and table reports; shared image hashes are expected evidence, not deduplication assumptions.

Together with the separate Japanese rev0 and English rev1 evidence, this covers every catalogued LeafGreen retail ROM currently available to the project. No ROM bytes or decoded binary sheets are published.
