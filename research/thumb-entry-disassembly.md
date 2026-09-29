# Japanese Thumb entry reachable disassembly

Starting at the proven Thumb transition target `0x080003a4`, conservative control-flow traversal records 116 reachable halfwords, 12 direct CFG edges, and 29 BL call sites. BL targets are recorded without following callees, and unreachable gaps are represented by explicit `.org` directives in the source.

The source halfwords in ascending address order have canonical SHA-256 `4c3848361250f0513a57eede916bef02730a8c54a0f53a98b8b0ac4a5ecb9cfb`. No return is reachable in this graph, so this is documented as a non-returning bootstrap path rather than a complete function boundary. Every emitted `.hword` is checked against its original little-endian ROM bytes.

