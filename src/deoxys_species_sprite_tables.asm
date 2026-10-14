; BPGJ rev0 species 410 (Deoxys, Defense Forme) table evidence.
; Struct layout: data pointer, u16 size, u16 species tag.

gMonFrontPicTable = 0x081F466C
gMonBackPicTable  = 0x081F5B0C
gMonPaletteTable  = 0x081F68CC

gMonFrontPicTable_Deoxys: ; ROM 0x001F533C
    .4byte 0x08D3958C
    .2byte 0x0800
    .2byte 0x019A

gMonBackPicTable_Deoxys: ; ROM 0x001F67DC
    .4byte 0x08D39DE8
    .2byte 0x0800
    .2byte 0x019A

gMonPaletteTable_Deoxys: ; ROM 0x001F759C
    .4byte 0x08D39DC0
    .2byte 0x019A
    .2byte 0
