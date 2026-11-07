"""Bangun laporan praktikum UAD dari template resmi.

Salin skrip ini ke scratch/projek, isi META dan BODY, jalankan dengan Python:
  py build_laporan_from_template.py

Alur yang sudah terbukti (jangan disederhanakan tanpa alasan):
  salin template -> margin 3 cm -> buang badan template setelah cover -> isi -> verifikasi PDF.
"""

import os
import shutil
import re

from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ---------------------------------------------------------------------------
# 1. ISI DI SINI
# ---------------------------------------------------------------------------
TEMPLATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates",
                        "Template-Laporan-Praktikum-UAD.docx")

# OUT_DIR bisa ditimpa lewat env supaya bisa bangun ke staging/ saat .docx tujuan masih
# terbuka di Word (PermissionError muncul di shutil.copy, sebelum dokumen dibangun):
#   LAPRAK_OUT_DIR=".../staging" py build_laporan_from_template.py
OUT_DIR = os.environ.get("LAPRAK_OUT_DIR") or os.path.join(os.path.expanduser("~"), "Laporan Praktikum")
OUT_NAME = os.environ.get("LAPRAK_OUT_NAME") or "Laporan Praktikum <Mapel> Pertemuan 1.docx"

META = {
    "mapel": "Praktikum <Mata Kuliah>",          # placeholder (Mata Praktikum)
    "materi": "<Judul Pertemuan>",               # placeholder (Judul Pertemuan)
    "tanggal": "Senin, 5 Oktober 2026",          # hitung dulu: date.strftime('%A')
    "nama": "<Nama Mahasiswa>",                  # placeholder Nama Mahasiswa
    "nim": "<NIM>",                              # placeholder NIM
    "tahun": "2026",                             # placeholder ANGKA TAHUN SEKARANG
}

# Isi laporan: daftar langkah. Tipe blok:
#   heading | sub | step | para | para_bold | para_italic | bullet
#   gambar : (path, caption, width_cm?)
#   tabel  : (caption, header, rows, widths, align_cols)
#   kode   : (caption, [baris, ...])
#   kode_file : (path_berkas_sumber, caption)   <- baca berkas langsung, aman untuk 90+ baris
#
# STANDAR BAKU (wajib, bukan opsi):
#   - paragraf isi 30-55% panjang gaya lama: apa yang dikerjakan + angka penting + hasilnya.
#   - Ulasan Praktikum SATU paragraf, maksimal ~90 kata (pembelajaran + kendala + solusi + temuan).
#   - TIDAK ADA kalimat penunjuk gambar ('ditunjukkan pada Gambar 2.3') di mana pun.
#   - tanpa 'Pada praktikum ini dilakukan ...' / 'Hasil pengujian menunjukkan bahwa ...'.
#   - angka, nama berkas, nama menu, caption, judul langkah, dan blok kode tidak pernah berubah.
BODY = [
    ("heading", "Pre Test"),
    # Foto lembar pre test yang sudah dijawab: LAMPIRKAN GAMBARNYA SAJA.
    # Jangan transkripsi soal/jawaban ke teks. Paragraf pengantar cukup satu kalimat.
    ("para", "Bagian ini memuat lembar jawaban pre test yang dikerjakan sebelum praktikum."),
    # width 11,5 cm: judul + pengantar + gambar + caption muat SATU halaman pada margin 3 cm.
    # 13 cm mendorong gambar ke halaman berikutnya dan menyisakan halaman berisi judul saja.
    ("gambar", (r"<path foto lembar pre test>", "Gambar 1.1 Lembar Jawaban Pre Test", 11.5)),

    ("heading", "Hasil Praktikum"),
    ("para", "Praktikum ini <membuat/mengimplementasikan> <X> dengan <alat>."),
    ("step", "Langkah 1: <judul langkah>"),
    # Satu paragraf padat: operasi + nilai/angka yang terlihat + hasilnya. Tanpa rujukan gambar.
    ("para", "<operasi> dijalankan dengan <parameter>; hasilnya <fakta/angka>."),
    ("gambar", (r"<path screenshot>", "Gambar 2.1 <Caption Capital Each Word>")),
    # ... ulangi sampai langkah terakhir ...
    ("sub", "Ulasan Praktikum"),
    ("para", "<Pembelajaran utama>. <Kendala yang muncul dan cara mengatasinya>. "
             "<Temuan/hasil penting>."),

    ("heading", "Post Test"),
    ("para", "Post test ini <mengembangkan/menguji> <...>."),
    ("gambar", (r"<path screenshot>", "Gambar 3.1 <Caption>")),
]

# ---------------------------------------------------------------------------
# 2. BANGUN
# ---------------------------------------------------------------------------
ALIGN = {
    "justify": WD_ALIGN_PARAGRAPH.JUSTIFY,
    "center": WD_ALIGN_PARAGRAPH.CENTER,
    "left": WD_ALIGN_PARAGRAPH.LEFT,
}

os.makedirs(OUT_DIR, exist_ok=True)
OUT = os.path.join(OUT_DIR, OUT_NAME)
shutil.copy(TEMPLATE, OUT)

doc = Document(OUT)

# margin wajib 3 cm (template masih 2,54 cm)
for sec in doc.sections:
    sec.top_margin = Cm(3)
    sec.bottom_margin = Cm(3)
    sec.left_margin = Cm(3)
    sec.right_margin = Cm(3)

# ganti placeholder cover DENGAN MENCCOKKAN TEKS, bukan indeks paragraf.
# Placeholder sering terpecah jadi beberapa run -> tulis run[0], kosongkan sisanya.
def set_cover_text(old_substring, new_text):
    """Ganti placeholder cover. Cocokkan teks, bukan indeks paragraf.

    Placeholder pendek (mis. "NIM") dicocokkan EXACT, supaya tidak salah mengenai
    paragraf lain yang kebetulan memuat substring yang sama.
    """
    exact = len(old_substring) <= 8
    for p in doc.paragraphs:
        txt = p.text.strip()
        hit = (txt == old_substring) if exact else (old_substring.lower() in txt.lower())
        if not hit:
            continue
        if not p.runs:
            p.add_run(new_text)
            return True
        p.runs[0].text = new_text
        for r in p.runs[1:]:
            r.text = ""
        return True
    raise SystemExit(f"placeholder tidak ketemu: {old_substring!r}")

set_cover_text("(Mata Praktikum)", META["mapel"])
set_cover_text("(Judul Pertemuan)", META["materi"])
set_cover_text("(Hari Tanggal dan Sesi Praktikum)", META["tanggal"])
set_cover_text("Nama Mahasiswa", META["nama"])
set_cover_text("NIM", META["nim"])
set_cover_text("ANGKA TAHUN SEKARANG", META["tahun"])

# buang badan template (Pre Test/Post Test/Aturan Penulisan) — sisakan cover saja.
# Tahun di cover sudah diganti, jadi patokannya: paragraf TERAKHIR yang isinya persis tahun.
paras = doc.paragraphs
cut = max(i for i, p in enumerate(paras)
          if p.text.strip() == META["tahun"] or "ANGKA TAHUN" in p.text)
for p in paras[cut + 1:]:
    p._p.getparent().remove(p._p)

# style isi: id-nya 'normal' huruf kecil, bukan 'Normal'
st = doc.styles["normal"]
st.font.name = "Calibri"
st.font.size = Pt(11)
st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")

def add(text="", *, size=11, bold=False, italic=False, align="justify",
        before=0, after=6, line=1.15, keep_next=False):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = line
    pf.keep_with_next = keep_next
    p.alignment = ALIGN[align]
    for i, chunk in enumerate(re.split(r"\*(.+?)\*", text)):  # *teks* -> italic
        if not chunk:
            continue
        r = p.add_run(chunk)
        r.font.name = "Calibri"
        r.font.size = Pt(size)
        r.bold = bold
        r.italic = italic or (i % 2 == 1)
    return p

def _safe_image(path):
    """Kembalikan path gambar yang aman untuk python-docx.

    JPEG dari kamera ponsel kadang membawa segmen EXIF rusak -> add_picture melempar
    UnexpectedEndOfFileError walau gambarnya normal di penampil foto. Re-encode lewat Pillow
    TANPA mengubah ukuran/rotasi; kalau Pillow tidak tersedia atau berkas sudah bersih,
    pakai path aslinya.
    """
    try:
        from PIL import Image
        im = Image.open(path)
        im.load()
        out = os.path.splitext(path)[0] + "_clean.jpg"
        im.convert("RGB").save(out, "JPEG", quality=88)
        return out
    except Exception:
        return path


def add_gambar(path, caption, width_cm=13.2):
    """Screenshot Colab default 13,2 cm.

    14,5 cm (lebar penuh kolom teks) sering mendorong caption ke halaman berikutnya sehingga
    tersisa halaman yang isinya cuma caption menggantung. 13,2 cm menghilangkan halaman itu dan
    memangkas jumlah halaman total. Foto lembar pre test memakai 11,5 cm supaya judul + pengantar
    + gambar + caption muat SATU halaman.
    """
    p = doc.add_paragraph()
    p.alignment = ALIGN["center"]
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    # keep_with_next HANYA di paragraf gambar: caption otomatis ikut karena satu blok.
    # Memasangnya juga di caption mengikat blok ke paragraf SESUDAHNYA -> gambar terlempar
    # ke halaman baru dan halaman sebelumnya hanya berisi judul + pengantar.
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(_safe_image(path), width=Cm(width_cm))
    add(caption, size=11, align="center", after=10)


def _isi_run(p, text, size=11, bold=False, italic=False, mono=False):
    """Tulis teks ke paragraf; *kata* jadi italic. Dipakai paragraf DAN sel tabel."""
    for i, chunk in enumerate(re.split(r"\*(.+?)\*", text)):
        if not chunk:
            continue
        r = p.add_run(chunk)
        r.font.name = "Courier New" if mono else "Calibri"
        r.font.size = Pt(size)
        r.bold = bold
        r.italic = italic or (i % 2 == 1)


def _borders(tbl):
    """Template UAD hanya punya TableNormal -> 'Table Grid' KeyError. Pasang garis manual."""
    tblPr = tbl._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "000000")
        borders.append(el)
    tblPr.append(borders)


def add_tabel(caption, header, rows, widths=None, size=10, align_cols=None):
    """Caption di ATAS tabel (aturan template), font 10, spasi 1, anti-pecah halaman.

    `widths` (cm) jumlahnya harus <= 15 cm — itu lebar kolom teks A4 dengan margin 3 cm.
    Tabel perhitungan lebar (mis. Vigenere 15 kolom + 1 kolom label) pakai size=8 supaya
    label baris tetap satu baris.
    """
    add(caption, size=11, align="center", before=10, after=3, keep_next=True)
    t = doc.add_table(rows=1, cols=len(header))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _borders(t)
    hdr = t.rows[0].cells
    for i, h in enumerate(header):
        hdr[i].text = ""
        p = hdr[i].paragraphs[0]
        p.alignment = ALIGN["center"]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1
        r = p.add_run(h)
        r.font.name = "Calibri"
        r.font.size = Pt(size)
        r.bold = True
        tcPr = hdr[i]._tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), "D9D9D9")
        tcPr.append(shd)
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            cells[i].text = ""
            p = cells[i].paragraphs[0]
            p.alignment = ALIGN[(align_cols or ["left"] * len(header))[i]]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1
            _isi_run(p, str(val), size)  # sel juga kena *italic*
    if widths:
        # cell.width SENDIRIAN TIDAK DIPAKAI LibreOffice: tblGrid bawaan python-docx sama rata,
        # jadi tabel 16 kolom tetap membagi lebar seragam dan label baris terlipat ("Juml/ah").
        # Perlu tblLayout=fixed + tblGrid ditulis ulang + tblW eksplisit.
        tbl = t._tbl
        tblPr = tbl.tblPr
        layout = OxmlElement("w:tblLayout")
        layout.set(qn("w:type"), "fixed")
        tblPr.append(layout)
        tblW = tblPr.find(qn("w:tblW"))
        if tblW is None:
            tblW = OxmlElement("w:tblW")
            tblPr.append(tblW)
        tblW.set(qn("w:type"), "dxa")
        tblW.set(qn("w:w"), str(int(sum(widths) * 567)))  # 1 cm = 567 dxa
        old_grid = tbl.find(qn("w:tblGrid"))
        if old_grid is not None:
            tbl.remove(old_grid)
        grid = OxmlElement("w:tblGrid")
        for w in widths:
            gc = OxmlElement("w:gridCol")
            gc.set(qn("w:w"), str(int(w * 567)))
            grid.append(gc)
        tblPr.addnext(grid)
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Cm(w)
        # padding sel rapat: tanpa ini kolom 0,8 cm tidak cukup untuk satu huruf
        mar = OxmlElement("w:tblCellMar")
        for edge in ("left", "right"):
            el = OxmlElement(f"w:{edge}")
            el.set(qn("w:w"), "28")
            el.set(qn("w:type"), "dxa")
            mar.append(el)
        tblPr.append(mar)
    # anti-pecah: baris tidak boleh dipotong, semua baris kecuali terakhir ikut pindah halaman
    for ri, row in enumerate(t.rows):
        trPr = row._tr.get_or_add_trPr()
        trPr.append(OxmlElement("w:cantSplit"))
        if ri < len(t.rows) - 1:
            for cell in row.cells:
                for p in cell.paragraphs:
                    p.paragraph_format.keep_with_next = True
    add("", after=8)
    return t


def add_kode(caption, lines, size=10):
    """Kode Program: frame 1x1 + nomor baris, Courier New 10, spasi 1, caption di bawah."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _borders(t)
    cell = t.rows[0].cells[0]
    cell.text = ""
    for i, ln in enumerate(lines, start=1):
        p = cell.paragraphs[0] if i == 1 else cell.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(0)
        pf.line_spacing = 1
        p.alignment = ALIGN["left"]
        r = p.add_run(f"{i}\t{ln}")   # pendekkan komentar: baris panjang wrap = baris "duplikat"
        r.font.name = "Courier New"
        r.font.size = Pt(size)
        r._element.rPr.rFonts.set(qn("w:eastAsia"), "Courier New")
    add(caption, size=11, align="center", before=3, after=10)

def add_kode_par(caption, lines, size=9):
    """Kode panjang: frame paragraf (pBdr) + nomor baris, mengalir lintas halaman.

    Tabel 1x1 TIDAK bisa dipecah rapi untuk berkas 90+ baris; paragraf dengan line break bisa,
    asalkan keep_with_next hanya dipasang untuk blok pendek (blok panjang yang di-keep akan
    mendorong seluruh halaman jadi kosong).
    """
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(6)
    pf.space_after = Pt(2)
    pf.line_spacing = 1
    pf.left_indent = Cm(0.1)
    pf.keep_with_next = len(lines) <= 14
    pf.widow_control = False
    p.alignment = ALIGN["left"]
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "6")
        el.set(qn("w:space"), "4")
        el.set(qn("w:color"), "808080")
        pBdr.append(el)
    pPr.append(pBdr)
    for i, ln in enumerate(lines):
        r = p.add_run(f"{i+1:>3} {ln}")
        r.font.name = "Courier New"
        r.font.size = Pt(size)
        r._element.rPr.rFonts.set(qn("w:eastAsia"), "Courier New")
        if i < len(lines) - 1:
            r.add_break()
    add(caption, size=11, align="center", after=10)


def add_kode_file(path, caption, size=9):
    """Lampirkan berkas sumber apa adanya (buang baris kosong di ekor)."""
    lines = open(path, encoding="utf-8", errors="replace").read().replace("\r", "").split("\n")
    while lines and lines[-1].strip() == "":
        lines.pop()
    add_kode_par(caption, lines, size)


for kind, val in BODY:
    if kind == "heading":
        add(val, size=14, bold=True, align="left", before=18, after=10, keep_next=True)
    elif kind == "sub":
        add(val, bold=True, align="left", before=10, after=4, keep_next=True)
    elif kind == "step":
        add(val, bold=True, align="left", before=8, after=2, keep_next=True)
    elif kind == "para":
        add(val)
    elif kind == "para_bold":
        add(val, bold=True, after=2)
    elif kind == "para_italic":
        add(val, italic=True)
    elif kind == "bullet":
        # hanging indent: baris lanjutan butir panjang sejajar teks, bukan menempel di margin
        p = add("\u2022 " + val)
        p.paragraph_format.left_indent = Cm(0.75)
        p.paragraph_format.first_line_indent = Cm(-0.4)
    elif kind == "gambar":
        add_gambar(*val)
    elif kind == "tabel":
        # val = (caption, header_list, rows, widths, align_cols)
        add_tabel(*val)
    elif kind == "kode":
        # val = (caption, [baris_kode, ...])
        add_kode(*val)
    elif kind == "kode_file":
        # val = (path_berkas_sumber, caption) — untuk berkas panjang, lebih aman dari tabel
        add_kode_file(*val)
    else:
        raise SystemExit(f"tipe blok tidak dikenal: {kind}")

doc.save(OUT)
print("TERSIMPAN:", OUT, os.path.getsize(OUT), "bytes")

# ---------------------------------------------------------------------------
# 3. VERIFIKASI (jalankan setelah ini)
# ---------------------------------------------------------------------------
# "C:/Program Files/LibreOffice/program/soffice.exe" --headless --convert-to pdf --outdir <dir> <docx>
# lalu, SEBELUM membuka gambar, cetak angka per halaman — lebih cepat dan lebih andal daripada vision:
#   import pymupdf
#   d = pymupdf.open(pdf)
#   for i, p in enumerate(d):
#       ys = [b[3] for b in p.get_text('blocks')] + [b['bbox'][3] for b in p.get_image_info()]
#       print(i + 1, len(p.get_text()), 'bottom', round(max(ys)) if ys else 0)
# Batas isi A4 margin 3 cm = y 85..707. Halaman dengan bottom < ~450 dan teks pendek berarti ada
# blok terdorong ke halaman berikutnya; halaman terakhir yang hanya berisi satu paragraf
# (len < ~300) diperbaiki dengan mengecilkan gambar Post Test, bukan memotong teks.
# Sesudah angkanya wajar, baru rasterisasi + vision_analyze untuk cek caption menempel di gambar.
#   d[i].get_pixmap(dpi=80).save(f'pg{i+1}.png')
# Kirim .docx + .pdf ke user.
