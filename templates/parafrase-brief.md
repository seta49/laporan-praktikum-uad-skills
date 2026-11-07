# Brief parafrase laporan praktikum (untuk subagent / diri sendiri)

Berkas ini disalin apa adanya jadi `STYLE.md` di folder kerja, lalu ditunjuk dari setiap tugas
parafrase. Isinya aturan gaya yang sudah ditetapkan sebagai standar; jangan dilunakkan oleh
preferensi gaya penulis brief.

> **Status: standar tetap.** Sejak 4 Nov 2026 bentuk ini ditetapkan sebagai standar pembuatan
> laporan ke depan ("jadikan seperti ini standar pembuatan laporan kedepannya"). Kalau menulis
> laporan **baru**, gabungkan aturan gaya di bawah **dan** blok *versi padat* — jangan menulis gaya
> panjang dulu lalu memadatkannya. Kalau memadatkan laporan lama, blok versi padat dipakai sebagai
> lapisan kedua di atas folder hasil revisi.

## Yang WAJIB dihapus

1. **Semua kalimat penunjuk gambar/tabel/kode.** Bentuk yang harus hilang total:
   - `Tampilan proses normalisasi ditunjukkan pada Gambar 2.3.`
   - `Hasil visualisasi ditunjukkan pada Gambar 2.1.`
   - `… seperti tampak pada Gambar 2.1.`
   - `… seperti ditunjukkan pada Gambar 2.8.`
   - `… ditunjukkan pada Tabel 2.2, sedangkan potongan kodenya ditunjukkan pada Kode Program 2.1.`
   Kalimat yang isinya murni rujukan dibuang; kalau masih ada isi lain, buang klausa rujukannya saja
   dan sisakan pernyataan isinya.
2. **Frasa kaku berulang** → bahasa wajar:
   - `Pada praktikum ini dilakukan …` → `Praktikum ini …`
   - `Tahap awal praktikum dilakukan dengan …` → `Langkah pertama, …`
   - `Hasil pengujian menunjukkan bahwa …` → `Hasilnya, …` / langsung faktanya
   - `Kendala tersebut diatasi dengan …` → `Ini diatasi dengan …` / `Solusinya, …`
   - `Melalui praktikum ini dapat dipahami bahwa …` → `Dari sini kelihatan bahwa …`
   - `Berdasarkan hasil pengerjaan tersebut dapat disimpulkan bahwa …` → `Bisa disimpulkan, …`
   - `Selanjutnya dilakukan …` → `Setelah itu …`
   - `Sedangkan` / `Adapun` / `Oleh karena itu` / `Dalam hal ini` → `sementara` / `jadi` /
     `makanya` / `soalnya`
3. **`kecerdasan buatan` / `berbasis AI`** → sebut yang dilakukannya (`hapus latar otomatis`,
   `layanan daring`).

## Yang WAJIB dipertahankan persis

- Semua angka, satuan, ukuran berkas, durasi, akurasi, epoch, batch size, port, IP, path folder.
- Nama berkas, variabel, fungsi, menu/tombol, pustaka, perintah terminal (termasuk setiap karakter
  di dalam kutipan kode seperti `df.iloc[100:201, 10]`).
- Nama orang/akun/kontributor, judul video, kutipan teks.
- Urutan langkah dan sebab-akibat yang sudah ada. **Jangan menambah klaim, angka, atau kesimpulan
  baru.**
- Heading/sub-judul pendek (`A. Persiapan`, `Arsitektur Model`, `Hasil Praktikum`) → biarkan,
  **jangan ditambahi titik akhir** (`Langkah 1: Menyalakan Server Lokal.` salah).
- Caption `Gambar/Tabel/Kode Program x.y …` → tidak pernah disentuh.
- Baris pertanyaan pre test dan blok kode program → tidak ikut diparafrase sama sekali.
- **Paragraf pembuka tiap bagian tetap ikut diparafrase.** `Hasil Praktikum` pertama dan pengantar
  `Pre Test` letaknya dekat cover, bukan berarti bagian cover.

## Gaya

- Kalimat aktif, subjek jelas; hindari pasif berlapis (`dilakukan pengujian terhadap …`).
- Kata sehari-hari yang tetap sopan: `jadi`, `hasilnya`, `ternyata`, `caranya`, `makanya`,
  `kelihatan`, `soalnya`, `tetap`.
- **Batas slang:** `begini`, `bikin`, `banget`, `nggak`, `udah`, `kayak`, `doang` terlalu jauh untuk
  laporan praktikum walaupun terasa lebih "manusia". Pakai bentuk baku yang tetap luwes
  (`membuat`, `Urutannya, …`), bukan bentuk percakapan.
- **Bukan** `gw/lo`, dan tetap impersonal: tanpa `saya/aku/kami`.
- Panjang paragraf ≈ aslinya; jangan menambah/menggabung paragraf; variasikan pembuka kalimat.
- Ejaan baku (`praktik`, `analisis`, `objek`, `aktif`); tanpa karakter CJK.

## Format keluaran

Satu berkas Python, satu dict, kunci = indeks paragraf di JSON sumber:

```python
DATA = {
    37: "isi paragraf 37 hasil parafrase",
}
```

Satu paragraf = satu string, tanpa newline di dalamnya.

## Varian: versi padat (bentuk baku laporan baru)

Ini bukan opsi tambahan: **laporan baru ditulis langsung dengan aturan ini**, dan laporan lama yang
sudah bergaya manusiawi dipadatkan dengan blok yang sama. Salin blok di bawah ke dalam `STYLE.md`
**setelah** aturan di atas — jangan tulis ulang brief dari nol. Aturan di atas tetap berlaku; blok
ini yang menimpa panjang paragraf dan bentuk Ulasan.

```markdown
## Target panjang (menimpa aturan panjang di atas)
- Paragraf 30–55% dari panjang aslinya, tetap kalimat utuh (bukan fragmen).
- Satu paragraf = satu gagasan pokok: apa yang dikerjakan + angka penting + hasil akhirnya.
- Buang basa-basi pembuka dan penjelasan sebab-akibat yang sudah jelas dari faktanya.
- Ulasan Praktikum: SATU paragraf, maksimal 90 kata, memuat pembelajaran + kendala + solusi +
  temuan. Tanpa bullet.

## Format keluaran
```python
DATA = {37: "paragraf 37 versi padat"}

ULASAN = {
    "keep": 78,            # indeks paragraf pertama Ulasan
    "delete": [79, 80, 81],  # paragraf Ulasan lain yang dihapus
    "text": "satu paragraf ulasan gabungan",
}
```
```

Semua aturan "yang wajib dipertahankan persis" dan "batas slang" di atas **tidak berubah** di
versi padat — pemadatan tidak boleh menghilangkan angka, nama berkas, atau kutipan kode.
