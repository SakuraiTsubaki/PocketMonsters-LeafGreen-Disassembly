# LeafGreen localized European game-title logos

The English revision-0 asset establishes the title-logo layout: a 256-entry
GBA BGR555 palette immediately precedes a BIOS-LZ77 stream that expands to
256 8bpp tiles. The German, French, Italian, and Spanish retail ROMs preserve
that structure while providing localized logo pixels.

Each ROM is gated by its cataloged SHA-256. The common palette and 8bpp tools
reproduce these localized assets:

| Language | Game code | Palette | Tiles |
| --- | --- | ---: | ---: |
| German | BPGD | `0xEAA060` | `0xEAA260` |
| French | BPGF | `0xEAA0A0` | `0xEAA2A0` |
| Italian | BPGI | `0xEAA07C` | `0xEAA27C` |
| Spanish | BPGS | `0xEAA0D8` | `0xEAA2D8` |

Reports and the consolidated manifest preserve all source-range, decoded,
palette, and PNG hashes without retaining raw ROM bytes.
