# string_util module

## Scope

`string_util` immediately follows the sprite engine. It implements bounded name copying, generic string copy/append/compare helpers, decimal/hex conversion, placeholder expansion, Braille conversion, padding/multibyte helpers, color control-code generation, and (international builds only) extended-control-code comparison/conversion helpers.

`src/sloopsvc.o` appears between `sprite` and `string_util` in the modern reference linker order, but it contributes no retail LeafGreen `.text` for these targets; `StringCopy_Nickname` begins immediately after `sprite` in all seven ROMs.

## Verified boundaries

| Target | Start | End exclusive | Size | SHA-1 | Family |
|---|---:|---:|---:|---|---|
| Japan | `0x008870` | `0x008EAC` | `0x63C` | `81c3bc783ed9e0d48a8fe4d303b9bb97a093db17` | JP |
| USA | `0x008CF4` | `0x009480` | `0x78C` | `7e954b2f681f9900665a30af03f5c7a8aa4a001f` | INTL |
| Europe Rev 1 | `0x008D08` | `0x009494` | `0x78C` | `0ff3dd406378019ba1c2598b4b12912ffb2803a5` | INTL |
| Germany | `0x008C74` | `0x009400` | `0x78C` | `a163447431caa6017d521561a9798cdf1be28e0c` | INTL |
| France | `0x008C60` | `0x0093EC` | `0x78C` | `d5a35b4714ebd7ed685e69f0175954f19bb01091` | INTL |
| Italy | `0x008C74` | `0x009400` | `0x78C` | `19c7cbd1514150935686d9f26872a50ca382cb40` | INTL |
| Spain | `0x008C60` | `0x0093EC` | `0x78C` | `389737282a30385cbcc7b18fe2fd98ef5c203d31` | INTL |

The international builds share the same relative function layout. Japan is exactly `0x150` bytes shorter.

## Language-family split

The first three bounded-copy helpers expose the retail language constants directly:

- Japan `StringCopy_Nickname` / `StringGet_Nickname`: limit `5`.
- International `StringCopy_Nickname` / `StringGet_Nickname`: limit `10`.
- Japan `StringCopy_PlayerName`: limit `5`.
- International `StringCopy_PlayerName`: limit `7`.

Despite those immediate-value differences, the first three routines preserve the same sizes and `StringCopy` begins at relative offset `0x90` in both families.

The decisive size difference comes at the end. The Japanese retail object ends immediately after `WriteColorChangeControlCode`. The international family additionally contains:

- `GetExtCtrlCodeLength`
- `SkipExtCtrlCode`
- `StringCompareWithoutExtCtrlCodes`
- `ConvertInternationalString`
- `StripExtCtrlCodes`

Those international-only routines occupy exactly `0x150` bytes, matching the module-size delta.

## Link boundary evidence

The international next-module entry is `IsWirelessAdapterConnected`. On USA it begins at ROM offset `0x009480` (`0x08009480`), where the Thumb code follows the expected wireless-adapter check sequence (playback guard, wireless mode setup, RFU initialization/check, cleanup on failure). The same entry signature locates the corresponding boundary in all targets:

- Japan `0x008EAC`
- USA `0x009480`
- Europe Rev 1 `0x009494`
- Germany / Italy `0x009400`
- France / Spain `0x0093EC`

This independently fixes the end of `string_util` and the start of `link`.

## Reconstruction decision

Use one semantic `string_util` source with target-family conditionals/configuration, not seven copied source files. The Japanese build must omit the international-only tail and use Japanese name-length constants; international targets retain the full helper set.

Exact function addresses are recorded in `symbols/string_util.csv`. Retail ROM ranges are evidence only and must not become final build inputs or `incbin` dependencies.
