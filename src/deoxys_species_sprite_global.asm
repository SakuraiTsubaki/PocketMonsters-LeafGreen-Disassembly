; Global rev0 species 410 (Deoxys, Defense Forme) table evidence.
; Struct layout: data pointer, u16 size, u16 species tag.

; language  front table  front entry  front data  back table  back entry  back data  palette data
; English   0x08235088   0x08235D58   0x08E3958C  0x08236528  0x082371F8  0x08E39DE8 0x08E39DC0
; German    0x08234F58   0x08235C28   0x08E39580  0x082363F8  0x082370C8  0x08E39DDC 0x08E39DB4
; French    0x0822F494   0x08230164   0x08E3958C  0x08230934  0x08231604  0x08E39DE8 0x08E39DC0
; Italian   0x0822E12C   0x0822EDFC   0x08E39584  0x0822F5CC  0x0823029C  0x08E39DE0 0x08E39DB8
; Spanish   0x082307F4   0x082314C4   0x08E3958C  0x08231C94  0x08232964  0x08E39DE8 0x08E39DC0

; Every listed species entry has size 0x0800 and tag 0x019A.
; The decoded front, back, and palette payloads are identical across these
; five releases even where their compressed streams begin at different offsets.
