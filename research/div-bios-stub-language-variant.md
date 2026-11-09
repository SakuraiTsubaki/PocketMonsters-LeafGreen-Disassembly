# LeafGreen Div BIOS stub language variant

`leafgreen-jp-rev0` is the Japanese origin reference and does not contain the four-byte `Div` libagbsyscall wrapper. The wrapper is present in 6 of 7 cataloged builds: every English, German, French, Italian, and Spanish release, at exactly -4 bytes from the independently verified `LZ77UnCompVram` anchor. The source therefore applies only to those global builds. Per-release evidence preserves both presence and absence without publishing ROM bytes or promoting release status.
