---
name: laporan-praktikum-standar
description: Gunakan saat menulis atau memformat laporan praktikum UAD. Standar enam aturan (paragraf padat, Ulasan 1 paragraf, tanpa rujukan gambar), lengkap dengan skrip pembangun, template resmi, dan pemeriksa otomatis.
version: 1.0.0
author: seta49
tags: [laporan, praktikum, docx, uad, template, standar]
---

# Laporan Praktikum UAD — Standar Baku

Standar penulisan laporan praktikum Program Studi Informatika Universitas Ahmad Dahlan, berlaku
sejak 4 November 2026 dan sudah diverifikasi pada 12+ laporan nyata. Skill ini generik: tidak
memuat nama, NIM, atau path pribadi siapa pun.

## Kapan dipakai

- Mau membuat laporan praktikum baru dari bahan mentah (notebook, screenshot, kode program).
- Mau membetulkan laporan lama yang paragrafnya bertele-tele.
- Mau cek format laporan sebelum dikumpulkan.

## Enam aturan inti

1. **Paragraf isi padat, 30–55% dari panjang gaya lama.** Rata-rata paragraf gaya lama 130–220
   karakter, hasilnya jadi 70–110 karakter. Satu paragraf = satu gagasan: apa yang dikerjakan +
   angka penting + hasil akhir. Buang basa-basi pembuka dan sebab-akibat yang sudah jelas dari
   faktanya.
2. **Ulasan Praktikum satu paragraf, maksimal ~90 kata.** Wajib memuat empat unsur: pembelajaran,
   kendala, solusi, dan temuan. Tanpa bullet.
3. **Tidak ada kalimat penunjuk gambar/tabel/kode**, baik di akhir maupun tengah paragraf. Yang
   dilarang: `ditunjukkan pada`, `ditampilkan pada`, `seperti tampak pada`, `dirangkum pada`.
   Gantinya: paragraf yang menceritakan operasi dan hasil yang tampak, lalu gambar/tabel/kode
   dengan captionnya.
4. **Bahasa manusiawi, bukan bahasa buku teks.** Kalimat aktif, subjek jelas. Dilarang:
   `Pada praktikum ini dilakukan …`, `Hasil pengujian menunjukkan bahwa …`,
   `Kendala tersebut diatasi dengan …`, `Melalui praktikum ini dapat dipahami bahwa …`, serta
   `kecerdasan buatan` / `berbasis AI`.
5. **Yang tidak pernah berubah**: angka, nama berkas, nama menu/fungsi, kutipan kode karakter demi
   karakter, caption, judul langkah, dan blok kode. Parafrase mengubah cara bertutur, bukan isi.
6. **Format tetap**: margin 3 cm semua sisi, Calibri 11, istilah asing *italic*, caption `bab.urut`
   di bawah gambar (contoh `Gambar 2.3 Alur Perancangan Sistem`), keluaran `.docx` dan `.pdf`.

## Bentuk paragraf yang dituju

Satu perbuatan + hasil, sering cukup dengan titik koma. Tanpa pembuka.

- Salah: "Pada tahap ini dilakukan pembungkusan ketiga fungsi menjadi satu fungsi bernama
  text_preprocessing_process, kemudian fungsi tersebut diterapkan pada kolom full_text sehingga
  menghasilkan kolom baru bernama cleaned_text."
- Benar: "Ketiga fungsi dibungkus jadi text_preprocessing_process lalu diterapkan ke kolom
  full_text, hasilnya masuk kolom cleaned_text."

Contoh lain:

- "df.head(5) mengambil lima baris teratas dan menyimpannya ke df2, jadi preprocessing berjalan
  pada lima tweet saja."
- "Token dipisah dengan explode() dan dihitung value_counts(); efisiensi muncul 5 kali, indonesia
  3 kali, danantara, berkomitmen, serta asik 2 kali."

Batas slang: `begini`, `bikin`, `banget`, `nggak`, `udah`, `kayak`, `doang` terlalu jauh untuk
laporan. Pakai bentuk baku yang tetap luwes. Bukan `gw/lo`, dan tetap impersonal — tanpa
`saya/aku/kami`.

## Susunan berkas

Cover → Pre Test → Hasil Praktikum → Ulasan Praktikum → Post Test.

- **Pre Test**: paragraf pengantar singkat, lalu `Pertanyaan 1` sampai `Pertanyaan N` (tebal)
  dengan `Jawaban` di bawahnya. Kalau ada foto lembar jawaban, cukup lampirkan gambarnya — soal dan
  jawaban tidak perlu diketik ulang.
- **Hasil Praktikum**: sub-bab huruf `A.`, `B.`, `C.` sesuai tahapan. Satu gambar = satu paragraf
  penjelas pendek tepat sebelumnya. Dua gambar bertumpuk di bawah satu paragraf menurunkan nilai.
- **Ulasan Praktikum**: satu paragraf, di akhir Hasil Praktikum sebelum Post Test.
- **Post Test**: satu butir soal = satu judul langkah + satu paragraf proses + satu gambar +
  caption, urut sesuai lembar soal. Diakhiri satu kalimat penutup.

## Penomoran

- `Gambar 1.x` untuk Pre Test, `Gambar 2.x` untuk Hasil Praktikum, `Gambar 3.x` untuk Post Test.
- Caption di **bawah** gambar, rata tengah, Capital Each Word. Caption tabel di **atas** tabel.
- Kode program dalam frame, Courier New 10, bernomor baris, caption `Kode Program 2.x`.

## Checklist sebelum dikumpulkan

- [ ] Panjang teks isi 45–60% dari versi gaya lama; tiap paragraf 30–55% paragraf aslinya
- [ ] Ulasan tepat 1 paragraf, ≤ 90 kata, keempat unsur ada
- [ ] `ditunjukkan pada` / `ditampilkan pada` / `dirangkum pada` = 0
- [ ] Caption, judul langkah, dan blok kode identik dengan sumber
- [ ] Setiap gambar punya paragraf penjelas sendiri, tidak ada yang bertumpuk
- [ ] Tidak ada halaman menggantung (halaman berisi satu gambar atau satu paragraf saja)
- [ ] Tidak ada placeholder tersisa di cover, kata "modul" tidak muncul di badan laporan
- [ ] Margin 3 cm, Calibri 11, istilah asing italic
- [ ] Tersimpan sebagai `.docx` dan `.pdf`

## Alur kerja

1. Isi `META` (mapel, materi, tanggal, nama, nim, tahun) dan `BODY` di
   `scripts/build_laporan_from_template.py`, lalu jalankan dengan
   `uv run --with python-docx python scripts/build_laporan_from_template.py`.
   Skrip menyalin sendiri template resmi dari `templates/` ke `OUT_DIR` dengan nama `OUT_NAME`
   (default `~/Laporan Praktikum`) — templatenya tidak perlu disalin manual. Env `LAPRAK_OUT_DIR`
   dan `LAPRAK_OUT_NAME` bisa menimpa keduanya.
2. Konversi ke PDF: `soffice --headless --convert-to pdf --outdir <folder> <docx>`.
3. Verifikasi: `python scripts/verify_revisi_parafrase.py <asli.docx> <revisi.docx>`. Skrip
   membandingkan **dua** berkas: caption/judul/blok kode harus identik, frasa penunjuk gambar dan
   frasa template = 0, Ulasan 1 paragraf ≤90 kata, dan rasio panjang paragraf 25–60% terhadap acuan
   (atur lewat `--ratio lo hi`). Untuk laporan baru tanpa versi acuan, bandingkan berkas dengan
   dirinya sendiri: `... laporan.docx laporan.docx --ratio 1 1`.

## Pitfall

- **Style paragraf di template ber-id `normal` huruf kecil**, bukan `Normal`. `d.styles["Normal"]`
  melempar KeyError.
- **Template tidak punya style `Table Grid`.** Pasang `w:tblBorders` manual ke `tbl._tbl.tblPr`.
- **Template membawa lembar "Aturan Penulisan" di belakang body.** Hapus semua paragraf setelah
  baris tahun di cover, kalau tidak lembar aturan ikut terkumpul.
- **`keep_with_next` dipasang pada paragraf gambar, jangan pada caption.** Caption yang ikut
  di-keep mengikat blok ke paragraf sesudahnya sehingga gambar terlempar ke halaman baru.
- **`cell.width` sendirian tidak mengubah lebar kolom.** Setel `w:tblLayout type=fixed`, tulis ulang
  `w:tblGrid`, set `w:tblW` eksplisit.
- **Placeholder pendek seperti `NIM` mudah salah kena** kalau dicocokkan dengan `in`. Cocokkan exact
  untuk placeholder ≤ 8 karakter.
- **Hitung hari dari tanggalnya** sebelum menulis baris tanggal, jangan mengandalkan ingatan.
- **Jangan mengarang isi bagian yang bahannya tidak ada.** Kalau tidak ada lembar pre test, isi
  dengan pertanyaan yang diturunkan dari teori pendukung bahan, lalu sebutkan di pesan akhir bahwa
  pertanyaan itu disusun sendiri.
- **Gambar hasil notebook: render dari `text/html` yang sudah tersimpan**, jangan jalankan ulang
  notebooknya. Eksekusi ulang menukar bukti sesi asli dengan keluaran mesin, dan sel `!wget` jadi
  SyntaxError.
- **Tabel lebar di notebook** perlu proyeksi kolom kunci saat dirender, jangan mengecilkan font
  sampai tak terbaca.
