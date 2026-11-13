"""Salin image.png ke lokasi output sebagai entry.png.

Program ini mengambil gambar PNG yang ada di samping skrip ini dan
menyalinnya byte demi byte ke direktori output, lalu memverifikasi
bahwa hasil salinan identik dengan sumbernya.

Perilaku:
- Direktori output diambil dari environment variable
  MAKEFUN_OUTPUT_DIR; bila tidak diset, dipakai /output.
  Nama file hasil selalu entry.png, dan direktori output dibuat
  bila belum ada.
- Sebelum menyalin, sumber divalidasi: file harus ada, ukuran
  maksimal 1 MiB, dan 8 byte awal harus cocok dengan magic
  bytes format PNG.
- Setelah menyalin, isi hasil dibandingkan byte demi byte dengan
  sumber; bila berbeda, program gagal.
- Setiap kegagalan mencetak pesan error yang deskriptif ke stderr
  dan keluar dengan kode non-zero.

Hanya memakai Python 3 stdlib; tanpa network, random, atau
timestamp. Dua run pada input yang sama menghasilkan byte yang
identik.

Gambar entry (terverifikasi): image.png 1024x1024, 646.997 byte,
sha256 e6e4dc208b7e26a46dcf613469b885f50be758889f88b1bdc3d0753d2acf8110.
"""

import os
import shutil
import sys

MAX_SIZE = 1048576  # 1 MiB
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    # Lokasi skrip ini; gambar sumber ada di direktori yang sama.
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "image.png")

    # Guard: file sumber harus ada.
    if not os.path.isfile(source):
        print(f"Error: file sumber tidak ditemukan: {source}", file=sys.stderr)
        sys.exit(1)

    # Guard: ukuran maksimal 1 MiB.
    size = os.path.getsize(source)
    if size > MAX_SIZE:
        print(
            f"Error: ukuran image.png {size} byte melebihi batas {MAX_SIZE} byte",
            file=sys.stderr,
        )
        sys.exit(1)

    # Guard: 8 byte awal harus cocok dengan magic bytes PNG.
    with open(source, "rb") as f:
        header = f.read(8)
    if header != PNG_MAGIC:
        print("Error: image.png bukan file PNG yang valid (magic bytes tidak cocok)",
              file=sys.stderr)
        sys.exit(1)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")

    try:
        shutil.copyfile(source, dest)
    except OSError as exc:
        print(f"Error: gagal menyalin {source} ke {dest}: {exc}", file=sys.stderr)
        sys.exit(1)

    # Verifikasi pasca-copy: hasil harus byte-identik dengan sumber.
    try:
        with open(source, "rb") as f_src, open(dest, "rb") as f_dst:
            if f_src.read() != f_dst.read():
                print(
                    f"Error: hasil salinan {dest} tidak identik dengan sumber {source}",
                    file=sys.stderr,
                )
                sys.exit(1)
    except OSError as exc:
        print(f"Error: gagal memverifikasi hasil salinan {dest}: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Disalin: {source} -> {dest} ({size} byte, terverifikasi identik)")


if __name__ == "__main__":
    main()
