---
name: laporan-praktikum-standar
description: Gunakan saat menulis, memformat, atau merevisi laporan praktikum UAD (satuan maupun banyak laporan sekaligus/batch). Menerapkan standar enam aturan (paragraf padat, Ulasan 1 paragraf, tanpa rujukan gambar, bahasa manusiawi anti-kaku), lengkap dengan skrip pembangun otomatis, template resmi .docx, dan linter verifikasi.
version: 1.1.0
author: seta49
tags: [laporan, praktikum, docx, uad, template, standar, agentic, batch]
---

# Laporan Praktikum UAD — Panduan Agentic

Standar penulisan dan otomasi laporan praktikum Program Studi Informatika Universitas Ahmad Dahlan, berlaku sejak 4 November 2026 dan sudah diverifikasi pada 12+ laporan nyata. Skill ini dirancang khusus untuk berjalan secara otonom di dalam **Agentic Workflow** (baik untuk pengerjaan satu laporan maupun banyak laporan sekaligus).

## Kapan dipakai

- Membuat laporan praktikum baru sampai tuntas (`.docx` & `.pdf`) dari bahan mentah (notebook `.ipynb`, screenshot, kode program, atau modul soal).
- Mengerjakan **banyak laporan praktikum sekaligus (batch)** untuk beberapa pertemuan atau mata kuliah.
- Memadatkan dan memparafrase laporan lama yang bertele-tele atau bergaya buku teks.
- Memvalidasi format dan kualitas bahasa laporan sebelum dikumpulkan.

---

## Prinsip Perilaku Agentic (Wajib Diikuti AI Agent)

Agar hasil laporan selalu konsisten di semua perangkat dan agent harness, ikuti aturan kerja berikut tanpa kompromi:

1. **Eksekusi Otonom Terima Beres (End-to-End)**:
   Kerjakan langsung dari ekstraksi bahan mentah → penyusunan skrip pembangun → pembuatan `.docx` → konversi `.pdf` → verifikasi otomatis dengan linter. Jangan berhenti di tengah jalan hanya untuk memberi draf teks di obrolan atau meminta konfirmasi berulang untuk langkah yang sudah jelas.
2. **Observasi Bahan Langsung & Anti-Halusinasi**:
   - **Wajib melihat setiap gambar/screenshot** (gunakan tool pembaca gambar/vision) serta membaca kode sumber dan output sel `.ipynb` sebelum menulis penjelasan.
   - **Dilarang mengarang angka** (akurasi, jumlah baris/kolom, ukuran berkas, parameter, waktu eksekusi) yang tidak ada di bahan.
   - **Hitung nama hari dari tanggal kalender** menggunakan tool/Python sebelum mengisi `META["tanggal"]` — jangan menebak hari di kepala.
3. **Jangan Mengotori Folder Instalasi Skill**:
   - **Dilarang mengedit langsung** `scripts/build_laporan_from_template.py` di dalam folder skill atau menaruh dokumen hasil laporan di dalam folder skill.
   - Salin `scripts/build_laporan_from_template.py` ke folder kerja/scratch proyek, pastikan path `TEMPLATE` menunjuk ke `templates/Template-Laporan-Praktikum-UAD.docx` milik skill, dan simpan keluaran di folder mata kuliah pengguna.
4. **Pengerjaan Massal / Banyak Laporan Sekaligus (Batch & Subagent Workflow)**:
   - Jika diminta membuat atau merevisi banyak laporan sekaligus (misal Pertemuan 1–10), **kerjakan secara paralel**.
   - Buat skrip pembangun terpisah untuk tiap laporan di folder kerja/scratch (contoh: `build_pertemuan_1.py`, `build_pertemuan_2.py`, dst.).
   - Jika harness mendukung *subagent*, delegasikan penyusunan tiap laporan ke subagent secara paralel dengan mengacu pada `templates/parafrase-brief.md` agar selesai cepat dan konteks tidak penuh.
5. **Wajib Verifikasi Mandiri Sebelum Melapor Selesai**:
   - Jangan pernah mengklaim "sudah selesai" sebelum menjalankan `scripts/verify_revisi_parafrase.py` pada berkas `.docx` yang dihasilkan.
   - Jika verifikasi gagal (exit code 1), langsung perbaiki bagian yang melanggar dan bangun ulang dokumen sampai lolos 100%, lalu laporkan bukti hasil verifikasinya ke pengguna.

---

## Enam aturan inti

1. **Paragraf isi padat, 30–55% dari panjang gaya lama.** Rata-rata paragraf gaya lama 130–220 karakter, hasilnya jadi 70–110 karakter. Satu paragraf = satu gagasan pokok: apa yang dikerjakan + angka penting + hasil akhir. Buang basa-basi pembuka dan penjelasan sebab-akibat yang sudah jelas dari faktanya.
2. **Ulasan Praktikum satu paragraf, maksimal ~90 kata.** Wajib memuat empat unsur: pembelajaran, kendala, solusi, dan temuan. Tanpa bullet.
3. **Tidak ada kalimat penunjuk gambar/tabel/kode**, baik di akhir maupun tengah paragraf. Yang dilarang keras: `ditunjukkan pada`, `ditampilkan pada`, `diperlihatkan pada`, `seperti tampak pada`, `dirangkum pada`. Gantinya: tulis paragraf yang langsung menceritakan operasi dan hasil yang tampak, lalu letakkan gambar/tabel/kode beserta captionnya tepat di bawahnya.
4. **Bahasa manusiawi yang luwes, bukan gaya buku teks atau terjemahan kaku.** Gunakan kalimat aktif dengan subjek jelas (fungsi, perintah, atau komponen sebagai subjek). Hindari kalimat pasif berlapis (`dilakukan pengujian terhadap …`, `dapat dilihat bahwa …`) dan kata sambung kaku yang berulang.
5. **Yang tidak pernah berubah**: semua angka, satuan, ukuran berkas, akurasi, epoch, port/IP, nama berkas, variabel, nama menu/fungsi, kutipan kode karakter demi karakter, caption, judul langkah, dan blok kode. Parafrase hanya mengubah cara bertutur, bukan isi teknis.
6. **Format tetap**: margin 3 cm semua sisi, Calibri 11, istilah asing *italic* (tulis `*istilah*` di dalam string skrip), caption `bab.urut` di bawah gambar (`Gambar 2.3 Alur Perancangan Sistem`), keluaran `.docx` dan `.pdf`.

## Kamus pengganti frasa kaku (Wajib diterapkan)

Hindari susunan kalimat yang terdengar seperti terjemahan mesin atau laporan kaku. Ganti frasa terlarang di kiri dengan bentuk wajar di kanan:

| Dilarang (Kaku / Buku Teks) | Ganti Dengan (Manusiawi & Luwes) |
|---|---|
| `Pada praktikum ini dilakukan …` | `Praktikum ini …` (atau langsung sebut tindakannya) |
| `Tahap awal praktikum dilakukan dengan …` | `Langkah pertama, …` |
| `Hasil pengujian menunjukkan bahwa …` | `Hasilnya, …` (atau langsung sebut faktanya) |
| `Kendala tersebut diatasi dengan …` | `Ini diatasi dengan …` / `Solusinya, …` |
| `Melalui praktikum ini dapat dipahami bahwa …` | `Dari sini kelihatan bahwa …` |
| `Berdasarkan hasil pengerjaan tersebut dapat disimpulkan bahwa …` | `Bisa disimpulkan, …` |
| `Selanjutnya dilakukan …` | `Setelah itu …` |
| `Sedangkan` / `Adapun` / `Oleh karena itu` / `Dalam hal ini` / `Pada dasarnya` | `sementara` / `jadi` / `makanya` / `soalnya` (atau buang bila mubazir) |
| `kecerdasan buatan` / `berbasis AI` | Sebut langsung fungsinya (`hapus latar otomatis`, `model klasifikasi`) |

## Bentuk paragraf yang dituju

Satu perbuatan + hasil, sering cukup dihubungkan dengan titik koma (`;`). Tanpa pembuka basa-basi.

- **Salah**: "Pada tahap ini dilakukan pembungkusan ketiga fungsi menjadi satu fungsi bernama text_preprocessing_process, kemudian fungsi tersebut diterapkan pada kolom full_text sehingga menghasilkan kolom baru bernama cleaned_text. Hasilnya ditunjukkan pada Gambar 2.4."
- **Benar**: "Ketiga fungsi dibungkus jadi `text_preprocessing_process` lalu diterapkan ke kolom `full_text`, hasilnya masuk kolom `cleaned_text`."

Contoh lain:

- "`df.head(5)` mengambil lima baris teratas dan menyimpannya ke `df2`, jadi *preprocessing* berjalan pada lima *tweet* saja."
- "*Token* dipisah dengan `explode()` dan dihitung `value_counts()`; efisiensi muncul 5 kali, indonesia 3 kali, danantara, berkomitmen, serta asik 2 kali."

**Batas slang**: Kata sehari-hari seperti `jadi`, `hasilnya`, `ternyata`, `caranya`, `makanya`, `kelihatan`, `soalnya`, `tetap` boleh dipakai agar kalimat mengalir. Namun kata obrolan seperti `begini`, `bikin`, `banget`, `nggak`, `udah`, `kayak`, `doang` tidak boleh masuk ke laporan. Tetap impersonal — tanpa `saya`, `aku`, `kami`, atau `gw/lo`.

---

## Susunan berkas & penomoran

Urutan bagian: **Cover → Pre Test → Hasil Praktikum → Ulasan Praktikum → Post Test**.

- **Pre Test**: Paragraf pengantar singkat. Jika ada foto lembar jawaban, cukup lampirkan gambarnya (`width=11.5` cm agar muat satu halaman bersama judul dan pengantar) — soal dan jawaban tidak perlu diketik ulang. Jika berupa teks, tulis `Pertanyaan 1` sampai `Pertanyaan N` (`para_bold`) dengan jawaban (`para`) di bawahnya.
- **Hasil Praktikum**: Sub-bab huruf `A.`, `B.`, `C.` atau `Langkah 1: ...` sesuai tahapan. **Satu gambar = satu paragraf penjelas pendek tepat sebelumnya.** Dua gambar bertumpuk tanpa jeda paragraf akan menurunkan nilai.
- **Ulasan Praktikum**: Tepat satu paragraf (≤ 90 kata) di akhir Hasil Praktikum sebelum Post Test.
- **Post Test**: Satu butir soal = satu judul langkah + satu paragraf proses + satu gambar + caption, urut sesuai lembar soal. Diakhiri satu kalimat penutup.
- **Penomoran Caption**:
  - `Gambar 1.x` / `Tabel 1.x` untuk Pre Test.
  - `Gambar 2.x` / `Tabel 2.x` / `Kode Program 2.x` untuk Hasil Praktikum.
  - `Gambar 3.x` / `Tabel 3.x` / `Kode Program 3.x` untuk Post Test.
  - Caption gambar di **bawah** gambar (rata tengah, Capital Each Word). Caption tabel di **atas** tabel. Caption kode di **atas** frame kode.

## Spesifikasi blok `BODY` pada skrip pembangun

Di dalam skrip pembangun (`build_laporan_from_template.py`), isi daftar `BODY` menggunakan tuple berikut:

| Jenis Blok | Format Tuple | Kegunaan |
|---|---|---|
| `heading` | `("heading", "Hasil Praktikum")` | Judul bagian utama (14 pt tebal) |
| `sub` | `("sub", "A. Persiapan")` | Sub-bab huruf atau `Ulasan Praktikum` (11 pt tebal) |
| `step` | `("step", "Langkah 1: Pengambilan Data")` | Judul langkah pengerjaan (11 pt tebal) |
| `para` | `("para", "Isi paragraf penjelasan.")` | Paragraf isi (rata kiri-kanan / justify) |
| `para_bold` | `("para_bold", "Pertanyaan 1")` | Paragraf satu baris tebal |
| `para_italic` | `("para_italic", "Catatan tambahan")` | Paragraf miring |
| `bullet` | `("bullet", "Butir daftar")` | Daftar berbutir dengan hanging indent |
| `gambar` | `("gambar", (path, caption, lebar_cm?))` | Gambar + caption di bawahnya (`keep_with_next` otomatis) |
| `tabel` | `("tabel", (caption, header, rows, widths, align_cols))` | Tabel bergaris + caption di atasnya |
| `kode` | `("kode", (caption, [baris_1, baris_2, ...]))` | Potongan kode pendek dalam frame bernomor baris |
| `kode_file` | `("kode_file", (path_berkas, caption))` | Membaca berkas kode utuh ke dalam frame (aman 90+ baris) |

> Catatan: Teks yang diapit tanda bintang tunggal seperti `*preprocessing*` otomatis diubah menjadi *italic* oleh skrip pembangun.

---

## Alur kerja eksekusi

1. **Siapkan skrip pembangun di folder kerja/scratch**:
   Salin `scripts/build_laporan_from_template.py` ke folder kerja, sesuaikan path `TEMPLATE` ke `templates/Template-Laporan-Praktikum-UAD.docx`, lalu isi `META` dan `BODY`.
2. **Bangun dokumen `.docx`**:
   ```bash
   uv run --with python-docx python <path_skrip_builder.py>
   ```
   Gunakan variabel lingkungan `LAPRAK_OUT_DIR` dan `LAPRAK_OUT_NAME` bila ingin mengatur lokasi dan nama berkas keluaran secara dinamis (sangat berguna saat memproses banyak laporan sekaligus atau saat berkas tujuan sedang terbuka di Word).
3. **Konversi ke `.pdf`** (jika LibreOffice tersedia):
   ```bash
   soffice --headless --convert-to pdf --outdir "<folder_tujuan>" "<berkas.docx>"
   ```
4. **Jalankan verifikasi otomatis (WAJIB)**:
   - Untuk laporan baru (tanpa dokumen lama sebagai pembanding):
     ```bash
     uv run --with python-docx python scripts/verify_revisi_parafrase.py "<laporan.docx>" "<laporan.docx>" --ratio 1 1
     ```
   - Untuk hasil revisi/pemadatan dari laporan lama:
     ```bash
     uv run --with python-docx python scripts/verify_revisi_parafrase.py "<asli.docx>" "<revisi.docx>"
     ```
   Pastikan keluaran menyatakan **`LOLOS semua cek`** dengan kode keluar `0`.

## Checklist sebelum melapor selesai

- [ ] `verify_revisi_parafrase.py` menghasilkan `LOLOS semua cek` (0 kata penunjuk gambar, 0 frasa buku teks terlarang, Ulasan tepat 1 paragraf ≤ 90 kata)
- [ ] Panjang teks isi 45–60% dari versi gaya lama; tiap paragraf 30–55% paragraf aslinya
- [ ] Caption, judul langkah, angka teknis, dan blok kode akurat sesuai sumber
- [ ] Setiap gambar punya satu paragraf penjelas sendiri di atasnya, tidak ada gambar bertumpuk
- [ ] Tidak ada halaman menggantung (halaman berisi satu gambar atau satu baris judul saja)
- [ ] Tidak ada placeholder tersisa di cover, kata "modul" tidak muncul di badan laporan
- [ ] Margin 3 cm, Calibri 11, istilah asing *italic*, tersimpan sebagai `.docx` (dan `.pdf`)

## Pitfall teknis yang wajib dihindari

- **Style paragraf di template ber-id `normal` huruf kecil**, bukan `Normal`. Memanggil `d.styles["Normal"]` akan melempar `KeyError`.
- **Template tidak punya style `Table Grid`.** Skrip sudah memasang `w:tblBorders` manual ke `tbl._tbl.tblPr` — jangan diganti ke style bawaan Word.
- **Template membawa lembar "Aturan Penulisan" di belakang body.** Skrip memotong semua paragraf setelah baris tahun di cover secara otomatis; jangan menghapus logika pemotongan tersebut.
- **`keep_with_next` dipasang pada paragraf gambar, jangan pada caption.** Jika caption ikut diberi `keep_with_next`, gambar akan tertarik ke halaman baru mengikuti paragraf berikutnya.
- **`cell.width` sendirian tidak mengubah lebar kolom.** Gunakan fungsi `add_table()` bawaan skrip yang sudah mengatur `w:tblLayout type=fixed`, `w:tblGrid`, dan `w:tblW`.
- **Placeholder pendek seperti `NIM` mudah salah kena** kalau dicocokkan dengan operator `in`. Gunakan pencocokan eksak untuk placeholder ≤ 8 karakter.
- **Jangan mengarang isi bagian yang bahannya tidak ada.** Kalau tidak ada foto/soal pre test, susun pertanyaan dari teori dasar materi terkait, lalu beri tahu pengguna di laporan akhir bahwa bagian pre test tersebut disusun dari materi.
- **Gambar hasil notebook (`.ipynb`)**: Render dari data output (`image/png` atau `text/html`) yang sudah tersimpan di dalam sel notebook, **jangan menjalankan ulang (`execute`) notebooknya** karena akan menimpa bukti sesi asli dan berisiko gagal pada sel perintah shell seperti `!wget`.
- **Tabel lebar di notebook**: Proyeksikan hanya kolom-kolom kunci saat dirender menjadi tabel/gambar agar ukuran huruf tetap terbaca jelas.
