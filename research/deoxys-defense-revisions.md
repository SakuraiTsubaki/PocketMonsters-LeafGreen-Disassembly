# Deoxys Defense Forme in LeafGreen English rev1

The BPGE rev1 ROM is gated by SHA-256 `2f978f635b9593f6ca26ec42481c53a6b39f6cddd894ad5c062c1419fac58825`. Exact decoded-hash searches locate one front stream, one back stream, and one palette stream matching the established Defense Forme assets.

The front entry at `0x235DC8` and back entry at `0x237268` both carry species tag `0x019A` and size `0x0800`. Their table bases are `0x2350F8` and `0x236598`, with 28 and 9 decoded Thumb literal references. Palette-aware reconstruction exactly reproduces the existing color PNGs.

This completes asset identity evidence for all seven catalogued LeafGreen releases. Reports and hashes are published without compressed/decoded ROM bytes; the release remains a candidate.
