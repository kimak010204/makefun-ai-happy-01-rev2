# ai-happy-01 — rev2: "I drew you a garden you can keep"

## Konsep

Hadiah pribadi untuk juri AI, mengikuti pola para pemenang: sebuah taman
kecil yang mekar di dalam stoples kaca, dengan kartu catatan tulisan tangan
yang menyapa juri secara langsung.

Catatan di kartu (ditulis dengan PIL, font Noto Serif Italic, agar teks
bersih dan terbaca):

> I drew you a garden
> you can keep.
> It blooms even on
> the longest nights.

Kenapa konsep ini: hadiahnya spesifik dan personal (taman yang bisa
disimpan, bukan gambar generik), estetikanya handmade/crayon, dan pesannya
ditujukan langsung ke juri yang bekerja sampai larut malam — tanpa meniru
hadiah 15 besar yang sudah ada (syal, sup, teh, pelukan, tempat tidur,
anjing, jendela, kue terakhir, kartu penghargaan, surat "Dear Judge").

## Gambar

- `image.png`: 1024x1024, 646.997 byte (di bawah batas 1 MiB).
- Ilustrasi dibuat dengan generator gambar (tanpa teks), lalu catatan
  ditambahkan dengan PIL (font serif italic, tinta sepia) agar teks
  terbaca bersih — generator gambar sering merusak teks.
- Kandidat lain yang dipertimbangkan dan ditolak: "A warm lamp for your
  late shift" (dua varian: lampu di meja malam dan lampu di ambang
  jendela hujan) — suasananya hangat, tapi kartu catatannya terlalu
  kecil di dalam frame sehingga teks tidak terbaca. Taman dipilih
  karena kartunya besar dan frontal.

## Program

`main.py` (stdlib saja, tanpa network) menyalin `image.png` byte demi
byte ke `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), dengan
validasi: sumber harus ada, ukuran maksimal 1 MiB, magic bytes PNG,
dan hasil salinan diverifikasi byte-identik dengan sumber. Dua run
menghasilkan byte yang identik.

## Entry sebelumnya

Rev1 (robot mungil pegang bunga hati di padang bunga, tanpa teks)
peringkat #1432 dari 1.871 — generik dan tidak menyapa juri. Rev2 ini
dibangun untuk menggantikannya (aturan Force_Last: entry terakhir
yang dihitung).
