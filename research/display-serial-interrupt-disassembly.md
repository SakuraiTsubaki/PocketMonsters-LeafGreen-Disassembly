# Pokemon LeafGreen display and serial interrupt disassembly

`bpg-j-rev0-retail` is the Japanese origin reference. All 7 cataloged releases (Japanese, English, German, French, Italian, Spanish) contain exactly one HBlank, VCount and Serial handler matching the `frlg` profile. VCount records REG_VCOUNT and invokes m4aSoundVSync. Each handler sets both INTR_CHECK and gMain.intrCheck. Per-release evidence preserves ranges, hashes, validated literals and call order without ROM bytes or instruction halfwords.
