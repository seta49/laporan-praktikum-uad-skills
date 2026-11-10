<div align="center">

# 📄 Laporan Praktikum UAD Skills

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Output](https://img.shields.io/badge/Output-.DOCX%20%26%20.PDF-2B579A?style=flat-square&logo=microsoftword&logoColor=white)](templates/Template-Laporan-Praktikum-UAD.docx)
[![Informatika UAD](https://img.shields.io/badge/Format-Informatika%20UAD-003366?style=flat-square)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![AI Ready](https://img.shields.io/badge/AI%20Agent-Antigravity%20%7C%20Claude%20%7C%20ChatGPT-8A2BE2?style=flat-square)](#-cara-pasang)

<p align="center">
  Toolkit Python dan skill AI Agent buat bikin dan ngecek laporan praktikum Informatika <b>Universitas Ahmad Dahlan</b> biar formatnya langsung rapi tanpa pusing mikirin margin dan layout.
</p>

<p align="center">
  <a href="#-cara-pasang"><b>📦 Cara Pasang</b></a> •
  <a href="#-bagian-yang-perlu-diubah"><b>⚙️ Bagian yang Diubah</b></a> •
  <a href="#-cara-menjalankan"><b>🚀 Cara Jalanin</b></a> •
  <a href="SKILL.md"><b>📖 Panduan SKILL.md</b></a>
</p>

</div>

> 💡 **Males ribet pasang manual?**  
> Salin link repo ini (`https://github.com/seta49/laporan-praktikum-uad-skills`) terus suruh AI agent kamu yang pasangkan! 😹

---

## 📦 Cara Pasang

Pilih AI agent yang lagi kamu pakai:

### ⚡ Google Antigravity

* **Lewat Chat Prompt (Paling Gampang):**  
  Tinggal paste prompt ini ke chat Antigravity:
  ```text
  Tolong pasang skill laporan praktikum UAD dari https://github.com/seta49/laporan-praktikum-uad-skills ke konfigurasi skills saya.
  ```

* **Lewat Terminal / CMD:**
  ```powershell
  # Windows (PowerShell)
  git clone https://github.com/seta49/laporan-praktikum-uad-skills.git "$env:USERPROFILE\.gemini\config\skills\laporan-praktikum-standar"
  ```
  ```bash
  # Linux / macOS
  git clone https://github.com/seta49/laporan-praktikum-uad-skills.git ~/.gemini/config/skills/laporan-praktikum-standar
  ```

---

### 🟣 Claude (Claude Code & Web)

* **Lewat Claude Code (CMD / Terminal):**  
  Buka terminal di folder project kamu, terus jalanin:
  ```bash
  claude "Ambil dan pasang skill dari https://github.com/seta49/laporan-praktikum-uad-skills ke .claude/skills/laporan-praktikum-standar"
  ```
  Atau clone manual ke folder skills Claude:
  ```bash
  git clone https://github.com/seta49/laporan-praktikum-uad-skills.git .claude/skills/laporan-praktikum-standar
  ```

* **Lewat Claude Desktop / Web:**
  1. Bikin **Project** baru di Claude.
  2. Upload file [`SKILL.md`](SKILL.md) dan [`templates/Template-Laporan-Praktikum-UAD.docx`](templates/Template-Laporan-Praktikum-UAD.docx) ke **Project Knowledge**.
  3. Pas chat, minta Claude susun atau cek laporan mengacu ke dokumen yang udah di-upload tadi.

---

### 🟢 ChatGPT (Web & Custom GPTs)

* **Lewat Custom GPT / Project (Biar Nempel Terus):**
  1. Buka ChatGPT > **Explore GPTs** > **Create** (atau menu **Projects**).
  2. Upload [`SKILL.md`](SKILL.md) dan [`templates/Template-Laporan-Praktikum-UAD.docx`](templates/Template-Laporan-Praktikum-UAD.docx) ke bagian **Knowledge**.
  3. Isi kolom **Instructions** dengan:
     > Jadikan file SKILL.md sebagai acuan utama penulisan laporan praktikum UAD. Selalu terapkan aturan penulisan yang ada (paragraf padat, Ulasan 1 paragraf, tanpa frasa penunjuk gambar, dan layout rapi).

* **Lewat Chat Prompt Langsung:**  
  Copy prompt ini di awal chat sebelum kirim draft atau materi praktikum:
  ```text
  Bantu aku bikin laporan praktikum Informatika UAD. Ikuti aturan ini:
  1. Paragraf isi padat dan to the point, 1 paragraf = 1 inti bahasan.
  2. Ulasan Praktikum wajib 1 paragraf, maksimal 90 kata (pembelajaran + kendala + solusi + temuan).
  3. DILARANG pakai kalimat penunjuk gambar/tabel (contohnya 'ditunjukkan pada', 'seperti tampak pada').
  4. Pakai kalimat aktif dan bahasa wajar, jangan kaku kayak buku teks.
  5. Nilai teknis, angka, kode program, dan caption bab.urut jangan diubah pas diparafrase.
  ```

---

### 🛠️ Harness Lain (Cursor, Windsurf, Roo Code / Cline, Aider)

* **Lewat Prompt Agent di IDE (Cursor Composer, Windsurf, Roo Code):**
  ```text
  Pelajari aturan dan pakai skill dari https://github.com/seta49/laporan-praktikum-uad-skills buat nyusun laporan praktikum di project ini.
  ```

* **Lewat File Rules Project:**  
  Clone repo ini ke dalam folder project praktikum kamu:
  ```bash
  git clone https://github.com/seta49/laporan-praktikum-uad-skills.git .skills/laporan-praktikum-standar
  ```
  Terus arahkan file rules bawaan IDE kamu:
  * **Cursor**: Tulis di `.cursor/rules/laprak.mdc` atau `.cursorrules`:
    ```text
    Ikuti seluruh aturan format dan gaya penulisan di .skills/laporan-praktikum-standar/SKILL.md
    ```
  * **Windsurf**: Tambahkan aturan di `.windsurfrules`.
  * **Roo Code / Cline**: Tambahkan aturan di `.clinerules`.
  * **Aider / CLI Agent**: Masukkan file context pas manggil agent:
    ```bash
    aider --read .skills/laporan-praktikum-standar/SKILL.md
    ```

---

### 💻 Pakai Mandiri (Python Langsung)

Kalau mau pakai script Python-nya langsung tanpa AI Agent, clone aja reponya:

```bash
git clone https://github.com/seta49/laporan-praktikum-uad-skills.git
cd laporan-praktikum-uad-skills
```

---

## ⚙️ Bagian yang Perlu Diubah

Kamu cuma perlu edit file [`scripts/build_laporan_from_template.py`](scripts/build_laporan_from_template.py) di dua variabel ini:

### 1. `META` — Data Diri & Praktikum

```python
META = {
    "mapel":   "Praktikum Pengolahan Bahasa Alami",
    "materi":  "Preprocessing 1",
    "tanggal": "Jumat, 16 Oktober 2026",
    "nama":    "Nama Mahasiswa",
    "nim":     "0000000000",
    "tahun":   "2026",
}
```

### 2. `BODY` — Isi Laporan

```python
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

---

## 🚀 Cara Menjalankan

Kalau `META` dan `BODY` udah diisi, tinggal generate file laporan (`.docx`) pakai perintah ini:

```bash
# Pakai uv (otomatis install library yang dibutuhin, anti ribet)
uv run --with python-docx python scripts/build_laporan_from_template.py

# Atau pakai python biasa (pastikan python-docx sudah terinstall)
python scripts/build_laporan_from_template.py
```

File `.docx` bakal otomatis dibuat di folder `~/Laporan Praktikum/`.

---

<div align="center">
  <sub>Aturan penulisan lengkap, daftar blok, dan panduan gaya ada di <a href="SKILL.md">SKILL.md</a>.</sub>
</div>
