Kalau males ribet install salin aja link ini terus minta agent mu pasangkan😹

# Laporan Praktikum UAD

Toolkit Python dan skill AI Agent untuk membuat serta memvalidasi laporan praktikum Program Studi Informatika Universitas Ahmad Dahlan sesuai **standar enam aturan** yang ditetapkan 4 November 2026 dan sudah diverifikasi pada 12+ laporan nyata.

Paket ini mencakup aturan gaya baku, template dokumen resmi (`.docx`), skrip pembangun dokumen otomatis, dan pemeriksa kualitas (linter parafrase) — sehingga laporan bisa disusun cepat dan rapi baik lewat bantuan AI coding agent maupun dijalankan langsung dari terminal.

Ramah untuk dipakai bersama: tidak ada nama, NIM, atau path pribadi di dalam paket ini.

---

## Isi paket

```
skill-laporan-praktikum-uad/
├── SKILL.md                                  aturan standar & instruksi untuk AI Agent
├── README.md                                 panduan penggunaan toolkit
├── templates/
│   ├── Template-Laporan-Praktikum-UAD.docx   template resmi (margin 3 cm, Calibri 11)
│   └── parafrase-brief.md                    brief gaya untuk memparafrase teks
└── scripts/
    ├── build_laporan_from_template.py        pembangun laporan (.docx)
    └── verify_revisi_parafrase.py            pemeriksa otomatis format & gaya
```

---

## Kebutuhan

- **Python 3.10+** dengan pustaka `python-docx`.
- **uv** (opsional, disarankan supaya tidak perlu repot setup virtualenv).
- **LibreOffice** (opsional, untuk konversi otomatis `.docx` ke `.pdf`).
- **AI Agent** (opsional, seperti Antigravity, Cursor, Claude Code, Windsurf, dsb.) jika ingin laporan disusun otomatis oleh agent.

---

## Cara pasang

### 1. Digunakan sebagai Skill AI Agent (Antigravity, Cursor, Claude, dll.)

Clone atau salin folder ini ke folder konfigurasi skills agent yang kamu gunakan:

**Google Antigravity:**
```powershell
# Windows (PowerShell)
Copy-Item -Recurse . "$env:USERPROFILE\.gemini\config\skills\laporan-praktikum-standar"
```

**Project / Workspace Agent (Cursor, Claude Code, dll.):**
Cukup letakkan folder atau rujuk berkas `SKILL.md` di root repository proyek praktikummu.

### 2. Digunakan secara Mandiri (Manual Python)

Cukup clone repo ini ke komputer lokal:

```bash
git clone https://github.com/seta49/skill-laporan-praktikum-uad.git
cd skill-laporan-praktikum-uad
```

---

## Cara pakai

**1. Isi `META` dan `BODY`** di `scripts/build_laporan_from_template.py`.

```python
META = {
    "mapel":   "Praktikum Pengolahan Bahasa Alami",
    "materi":  "Preprocessing 1",
    "tanggal": "Jumat, 16 Oktober 2026",
    "nama":    "Nama Mahasiswa",
    "nim":     "0000000000",
    "tahun":   "2026",
}

BODY = [
    ("heading", "Pre Test"),
    ("para", "Bagian ini memuat soal pre test beserta jawabannya."),
    ("gambar", ("img/hasil-01.png", "Gambar 2.1 Dataset Setelah Dimuat")),
    ("tabel",  ("Tabel 2.1 Kolom Dataset", ["Kolom", "Isi"],
                [["full_text", "isi tweet"], ["username", "nama akun"]],
                [6.0, 9.0], ["left", "left"])),
    ("kode",   ("Kode Program 2.1 Fungsi Pembersihan", ["def bersih(t):", "    return t"])),
]
```

**2. Jalankan:**

```bash
uv run --with python-docx python scripts/build_laporan_from_template.py
```

Tanpa `uv`, aktifkan dulu lingkungan Python yang punya `python-docx`, lalu
`python scripts/build_laporan_from_template.py`.

Skrip menyalin sendiri template resmi dari `templates/` ke `OUT_DIR` dengan nama `OUT_NAME`
(default `~/Laporan Praktikum`), jadi templatenya tidak perlu disalin manual. Ubah `OUT_DIR`/
`OUT_NAME` di bagian atas skrip, atau lewat variabel lingkungan `LAPRAK_OUT_DIR` dan
`LAPRAK_OUT_NAME`.

**3. Ubah ke PDF:**

```bash
soffice --headless --convert-to pdf --outdir "<folder tujuan>" "<berkas.docx>"
```

**4. Periksa hasilnya:**

```bash
uv run --with python-docx python scripts/verify_revisi_parafrase.py "<asli.docx>" "<revisi.docx>"
```

Skrip ini membandingkan **dua** berkas: berkas acuan dengan berkas hasil. Yang diperiksa: caption,
judul langkah, dan blok kode identik; frasa penunjuk gambar dan frasa template nol; Ulasan
Praktikum 1 paragraf ≤ 90 kata; dan panjang paragraf isi 25–60% dari acuan (atur sendiri lewat
`--ratio lo hi`). Untuk laporan baru yang tidak punya versi acuan, bandingkan berkas dengan
dirinya sendiri dan setel rasionya:

```bash
uv run --with python-docx python scripts/verify_revisi_parafrase.py "laporan.docx" "laporan.docx" --ratio 1 1
```

Kalau argumennya kurang, skrip berhenti dengan pesan `pemakaian: verify_revisi_parafrase.py
<asli.docx> <revisi.docx> [--ratio lo hi]` dan keluar dengan kode 1.

---

## Jenis blok yang bisa dipakai di `BODY`

| Blok | Bentuk | Kegunaan |
|---|---|---|
| `heading` | `("heading", "Hasil Praktikum")` | judul bagian, 14 pt tebal |
| `sub` | `("sub", "A. Persiapan")` | sub-bab huruf, 11 pt tebal |
| `step` | `("step", "1. Pengambilan Data")` | judul langkah, 11 pt tebal |
| `para` | `("para", "Isi paragraf.")` | paragraf isi, rata kiri-kanan |
| `para_bold` | `("para_bold", "Teks tebal")` | label seperti `Pertanyaan 1` |
| `para_italic` | `("para_italic", "Teks miring")` | catatan miring |
| `bullet` | `("bullet", "Butir daftar")` | daftar berbutir dengan hanging indent |
| `gambar` | `("gambar", (path, caption, lebar_cm?))` | gambar + caption di bawahnya |
| `tabel` | `("tabel", (caption, header, rows, widths, align_cols))` | tabel bergaris + caption di atas |
| `kode` | `("kode", (caption, [baris, ...]))` | potongan kode pendek dalam frame |
| `kode_file` | `("kode_file", (path_berkas, caption))` | berkas kode utuh, aman 90+ baris |

Tanda `*miring*` di dalam teks otomatis jadi italic — dipakai untuk istilah asing.

---

## Hal yang sering bikin gagal

- **Template punya lembar "Aturan Penulisan" di belakang.** Skrip sudah memotongnya otomatis
  setelah baris tahun. Kalau kamu menyunting `.docx` manual, pastikan lembar itu tidak ikut.
- **Jangan menaruh laporan hasil kerja di dalam folder skill.** Simpan laporan di folder mata
  kuliah; folder skill hanya untuk paket ini.
- **`TEMPLATE` di skrip memakai path relatif** terhadap lokasi skrip, jadi paket ini bisa
  dipindah ke folder mana pun tanpa mengubah kode.
- **`OUT_DIR` bisa ditimpa** lewat variabel lingkungan `LAPRAK_OUT_DIR` — berguna kalau berkas
  tujuan sedang terbuka di Word dan terkunci:

  ```bash
  LAPRAK_OUT_DIR="./staging" python scripts/build_laporan_from_template.py
  ```

- **Berkas `.docx` yang sedang dibuka Word tidak bisa ditimpa.** Tutup dulu Word, atau bangun ke
  folder lain lewat `LAPRAK_OUT_DIR` di atas.

---

## Ringkasan standarnya

1. Paragraf isi padat, 30–55% dari gaya lama — satu paragraf satu gagasan.
2. Ulasan Praktikum satu paragraf, maksimal ~90 kata, memuat pembelajaran + kendala + solusi + temuan.
3. Tidak ada kalimat penunjuk gambar (`ditunjukkan pada`, `ditampilkan pada`, dan sejenisnya).
4. Bahasa manusiawi, bukan bahasa buku teks.
5. Angka, nama berkas, kutipan kode, caption, dan judul langkah tidak boleh berubah.
6. Margin 3 cm, Calibri 11, istilah asing italic, caption `bab.urut`, keluaran `.docx` + `.pdf`.

Detail lengkap tiap aturan ada di `SKILL.md`.
