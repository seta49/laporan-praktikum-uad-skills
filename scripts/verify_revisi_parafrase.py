"""Verifikasi hasil revisi massal gaya bahasa: asli (.docx) vs hasil revisi.

Pakai setelah menjalankan skrip penerap parafrase:

    uv run --with python-docx python verify_revisi_parafrase.py <asli.docx> <revisi.docx>

Yang diperiksa:
  1. Caption Gambar/Tabel/Kode Program identik dengan aslinya.
  2. Judul (Langkah N:, A.-F., Pre Test, dst.) identik dengan aslinya.
  3. Blok kode identik dengan aslinya.
  4. Frasa penunjuk gambar dan frasa template = 0.
  5. Tidak ada spasi ganda, spasi sebelum tanda baca di luar blok kode, atau '".".'
  6. STANDAR BAKU: Ulasan Praktikum tepat 1 paragraf dan <= 90 kata.
  7. STANDAR BAKU: paragraf isi 25-60% panjang paragraf asli yang bersesuaian
     (pakai --ratio kalau membandingkan dua versi yang sudah sama-sama padat).

Jumlah paragraf boleh berkurang, tetapi hanya sebanyak paragraf Ulasan yang digabung jadi satu.

Keluar dengan kode 1 kalau ada kegagalan, supaya bisa dipakai di pipeline.
"""

import re
import sys

import docx

REF_RE = re.compile(
    r"(?:ditunjukkan|ditampilkan|diperlihatkan|dirangkum|tampak)\s+(?:pada|di)\s+"
    r"(?:Gambar|Tabel|Kode Program)",
    re.IGNORECASE,
)
BAN_RE = re.compile(
    r"(Pada praktikum ini dilakukan|Tahap awal praktikum dilakukan|Hasil pengujian menunjukkan bahwa|"
    r"Kendala tersebut diatasi dengan|Melalui praktikum ini dapat dipahami bahwa|"
    r"Berdasarkan hasil pengerjaan tersebut|Selanjutnya dilakukan|Adapun |Oleh karena itu|"
    r"kecerdasan buatan|berbasis AI)",
    re.IGNORECASE,
)
CAP_RE = re.compile(r"^(Gambar|Tabel|Kode Program)\s+\d+\.\d+")
HEAD_RE = re.compile(
    r"^(Langkah \d+:|[A-F]\.\s|Pertanyaan \d+:|Jawaban:|Analisis Hasil|Alur Kerja Sistem|"
    r"Arsitektur Model|Pelatihan dan Evaluasi Model|Pre Test|Post Test|Hasil Praktikum|"
    r"Ulasan Praktikum)\s*$"
)


def is_code(text):
    return ("<?php" in text or "?>" in text or text.count("\n") >= 2
            or bool(re.match(r"^\s*\d+\s+\S", text) and text.count("\n") >= 1))


def collect(doc, pred):
    return [p.text for p in doc.paragraphs if pred(p.text)]


def prose_paragraphs(doc, min_len=40):
    """Paragraf isi saja: bukan caption, judul, blok kode, gambar, atau baris kosong."""
    out = []
    for p in doc.paragraphs:
        t = p.text.strip()
        if not t or "graphicData" in p._p.xml:
            continue
        if CAP_RE.match(t) or HEAD_RE.match(t) or is_code(p.text):
            continue
        if len(t) < min_len:
            continue
        out.append(t)
    return out


def check_ulasan(doc):
    """Ulasan Praktikum harus tepat 1 paragraf dan <= 90 kata."""
    idx = [i for i, p in enumerate(doc.paragraphs) if p.text.strip() == "Ulasan Praktikum"]
    if not idx:
        return None
    paras = []
    for p in doc.paragraphs[idx[0] + 1:]:
        t = p.text.strip()
        if t == "Post Test" or "graphicData" in p._p.xml:
            break
        if t:
            paras.append(t)
    kata = len(" ".join(paras).split())
    return len(paras), kata


def main(orig_path, rev_path, ratio=(0.25, 0.60)):
    o = docx.Document(orig_path)
    r = docx.Document(rev_path)
    fails = []

    for label, pred in (
        ("caption", lambda t: bool(CAP_RE.match(t.strip()))),
        ("judul", lambda t: bool(HEAD_RE.match(t.strip()))),
        ("blok kode", is_code),
    ):
        a, b = collect(o, pred), collect(r, pred)
        if a != b:
            fails.append(f"{label} berubah ({len(a)} -> {len(b)})")
            for x, y in zip(a, b):
                if x != y:
                    fails.append(f"    ASLI: {x[:90]!r}\n    REV : {y[:90]!r}")

    # Jumlah paragraf boleh berkurang, tapi hanya sebanyak paragraf Ulasan yang digabung.
    n_o, n_r = len(o.paragraphs), len(r.paragraphs)
    ul_o = check_ulasan(o)
    boleh_turun = (ul_o[0] - 1) if ul_o else 0
    if n_r > n_o or (n_o - n_r) > boleh_turun:
        fails.append(f"jumlah paragraf berubah {n_o} -> {n_r} "
                     f"(boleh turun maksimal {boleh_turun} karena penggabungan Ulasan)")
    if len(o.inline_shapes) != len(r.inline_shapes):
        fails.append(f"jumlah gambar berubah {len(o.inline_shapes)} -> {len(r.inline_shapes)}")

    teks = "\n".join(p.text for p in r.paragraphs)
    prose = "\n".join(p.text for p in r.paragraphs if not is_code(p.text))

    n_ref = len(REF_RE.findall(teks))
    if n_ref:
        fails.append(f"masih ada {n_ref} frasa penunjuk gambar")
        for p in r.paragraphs:
            if REF_RE.search(p.text):
                fails.append(f"    {p.text[:120]!r}")

    n_ban = len(BAN_RE.findall(prose))
    if n_ban:
        fails.append(f"masih ada {n_ban} frasa template")
        for m in BAN_RE.finditer(prose):
            fails.append(f"    …{prose[max(0, m.start() - 40):m.end() + 40]!r}")

    if "  " in prose:
        fails.append("ada spasi ganda di prosa")
    # Spasi sebelum titik itu normal kalau titiknya mengawali nama metode ('.loc[]',
    # '.iloc[]'). Selain pola itu, spasi sebelum tanda baca berarti ada sisa penggabungan
    # kalimat yang malas.
    for m in re.finditer(r"\s+[.,;]", prose):
        tanda = prose[m.end() - 1]
        sisa = prose[m.end():m.end() + 1]
        if tanda == "." and sisa and sisa.isalpha() and sisa.islower():
            continue
        fails.append(
            "ada spasi sebelum tanda baca di prosa: "
            f"…{prose[max(0, m.start() - 45):m.end() + 25]!r}"
        )
        break
    if '.”.' in teks or '"."' in teks:
        fails.append("ada titik dobel setelah tanda kutip")

    # --- standar baku: Ulasan 1 paragraf, <= 90 kata ---
    ul = check_ulasan(r)
    if ul:
        n_par, n_kata = ul
        if n_par != 1:
            fails.append(f"Ulasan Praktikum {n_par} paragraf (standar: 1)")
        if n_kata > 90:
            fails.append(f"Ulasan Praktikum {n_kata} kata (standar: <= 90)")

    # --- standar baku: paragraf isi dipadatkan ---
    po, pr = prose_paragraphs(o), prose_paragraphs(r)
    if po and pr:
        lo, hi = ratio
        la = sum(len(t) for t in po) / len(po)
        lb = sum(len(t) for t in pr) / len(pr)
        rasio = lb / la if la else 1
        if not (lo <= rasio <= hi):
            fails.append(
                f"rasio panjang paragraf {rasio:.2f} di luar {lo}-{hi} "
                f"(rata-rata {la:.0f} -> {lb:.0f} karakter)"
            )

    if fails:
        print(f"GAGAL {rev_path}")
        for f in fails:
            print("  -", f)
        return 1

    ul = check_ulasan(r)
    ekor = f" | Ulasan {ul[0]} paragraf/{ul[1]} kata" if ul else " | tanpa Ulasan"
    print(f"OK {rev_path} | {len(r.paragraphs)} paragraf | {len(r.inline_shapes)} gambar | "
          f"{len(collect(r, lambda t: bool(CAP_RE.match(t.strip()))))} caption utuh{ekor}")
    return 0


if __name__ == "__main__":
    argv = sys.argv[1:]
    rentang = (0.25, 0.60)
    if "--ratio" in argv:
        i = argv.index("--ratio")
        try:
            rentang = (float(argv[i + 1]), float(argv[i + 2]))
        except (IndexError, ValueError):
            sys.exit("--ratio butuh dua angka, mis. --ratio 0.30 0.60")
        del argv[i:i + 3]
    if len(argv) != 2:
        sys.exit("pemakaian: verify_revisi_parafrase.py <asli.docx> <revisi.docx> "
                 "[--ratio lo hi]")
    sys.exit(main(argv[0], argv[1], rentang))
