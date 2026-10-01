# LeafGreen English game-title logo

The public `pret/pokefirered` title-logo asset is an English-build asset. Its
8x8 tile-order conversion did not match an equivalent 16,384-byte LZ77 stream
in the Japanese revision-0 ROM, so it is not mislabeled as Japanese evidence.

It exactly matches the English revision-0 candidate (`BPGE`) stream at
`0xEAB944`. Decompression yields 16,384 bytes (256 8bpp tiles), SHA-256
`d2b5c13a0b6d4f444eada4fdcf2c1bd96210e665004bb6f56d3019ee9fcd9bfe`.
The colored public PNG uses the corresponding 256-color JASC palette.

The common 8bpp extractor records the complete provenance without publishing
ROM bytes. This asset match does not promote the complete release candidate
to `verified`.
