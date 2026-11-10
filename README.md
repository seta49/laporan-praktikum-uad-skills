<div align="center">

# 📄 Laporan Praktikum UAD Skills

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Output](https://img.shields.io/badge/Output-.DOCX%20%26%20.PDF-2B579A?style=flat-square&logo=microsoftword&logoColor=white)](templates/Template-Laporan-Praktikum-UAD.docx)
[![Informatika UAD](https://img.shields.io/badge/Format-Informatika%20UAD-003366?style=flat-square)](SKILL.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Agentic Workflow](https://img.shields.io/badge/Workflow-Agentic%20%26%20Batch-8A2BE2?style=flat-square)](#-keunggulan)

<p align="center">
  Skill <b>Agentic Workflow</b> dan toolkit Python buat bikin, memformat, dan ngecek laporan praktikum Informatika <b>Universitas Ahmad Dahlan</b> secara otomatis — dari bahan mentah langsung jadi <code>.docx</code> & <code>.pdf</code> siap kumpul.
</p>

<p align="center">
  <a href="#-keunggulan"><b>✨ Keunggulan</b></a> •
  <a href="#-cara-pasang"><b>📦 Cara Pasang</b></a> •
  <a href="#-contoh-prompt-agentic"><b>🤖 Cara Pakai di Agent</b></a> •
  <a href="#-bagian-yang-perlu-diubah-mode-manual"><b>⚙️ Mode Manual</b></a> •
  <a href="SKILL.md"><b>📖 Panduan SKILL.md</b></a>
</p>

</div>

> 💡 **Males ribet pasang manual?**  
> Salin link repo ini (`https://github.com/seta49/laporan-praktikum-uad-skills`) terus suruh AI agent kamu yang pasangkan! 😹

---

## ✨ Keunggulan

Skill ini dirancang khusus buat jalan di **Agentic Workflow** (seperti Antigravity, Claude Code, Cursor, Windsurf, Roo Code), jadi kamu nggak perlu lagi ngetik laporan dari nol atau ngatur-ngatur layout Word manual:

* 🤖 **Full Otonom (Terima Beres)**: Cukup taruh bahan mentah (file `.ipynb`, kodingan, screenshot, atau soal praktikum) di folder kerja. Agent bakal otomatis baca tiap gambar & kode, nulis pembahasannya, nge-build `.docx` sesuai template resmi prodi, sampai convert ke `.pdf`.
* ⚡ **Bisa Bikin Banyak Laprak Sekaligus (Batch Processing)**: Punya tugas beberapa pertemuan sekaligus atau mau merombak banyak laprak lama dalam satu waktu? Tinggal perintah sekali, agent bakal nge-spawn subagent / skrip paralel buat ngerjain semuanya sekaligus.
* 🗣️ **Bahasa Natural & Anti-Kaku**: Sudah tertanam aturan gaya bahasa yang luwes dan manusiawi — bebas kalimat pasif ala terjemahan mesin, bebas basa-basi buku teks, dan tanpa kalimat penunjuk gambar (`ditunjukkan pada Gambar...`).
* ✅ **Auto-Verification (Linter Bawaan)**: Agent nggak bakal asal klaim selesai sebelum hasil `.docx`-nya lolos pengecekan skrip verifikasi otomatis (`verify_revisi_parafrase.py`).

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
  2. Upload file [`SKILL.md`](SKILL.md), [`templates/parafrase-brief.md`](templates/parafrase-brief.md), dan [`templates/Template-Laporan-Praktikum-UAD.docx`](templates/Template-Laporan-Praktikum-UAD.docx) ke **Project Knowledge**.
  3. Pas chat, minta Claude susun atau cek laporan mengacu ke dokumen yang udah di-upload tadi.

---

### 🟢 ChatGPT (Web & Custom GPTs)

* **Lewat Custom GPT / Project (Biar Nempel Terus):**
  1. Buka ChatGPT > **Explore GPTs** > **Create** (atau menu **Projects**).
  2. Upload [`SKILL.md`](SKILL.md), [`templates/parafrase-brief.md`](templates/parafrase-brief.md), dan [`templates/Template-Laporan-Praktikum-UAD.docx`](templates/Template-Laporan-Praktikum-UAD.docx) ke bagian **Knowledge**.
  3. Isi kolom **Instructions** dengan:
     > Jadikan file SKILL.md dan parafrase-brief.md sebagai acuan utama penulisan laporan praktikum UAD. Gunakan bahasa Indonesia aktif yang luwes (bukan gaya terjemahan kaku), paragraf padat, Ulasan 1 paragraf (≤90 kata), dan tanpa frasa penunjuk gambar.

* **Lewat Chat Prompt Langsung:**  
  Copy prompt ini di awal chat sebelum kirim draft atau materi praktikum:
  ```text
  Bantu aku bikin laporan praktikum Informatika UAD. Ikuti aturan ini:
  1. Paragraf isi padat (30–55% dari gaya biasa), 1 paragraf = 1 inti bahasan (apa yang dikerjakan + angka penting + hasil).
  2. Ulasan Praktikum wajib 1 paragraf, maksimal 90 kata (pembelajaran + kendala + solusi + temuan), tanpa bullet.
  3. DILARANG pakai kalimat penunjuk gambar/tabel (seperti 'ditunjukkan pada', 'ditampilkan pada', 'seperti tampak pada').
  4. Pakai kalimat aktif yang mengalir wajar. Hindari kalimat pasif berlapis dan kata sambung kaku ('adapun', 'oleh karena itu', 'dalam hal ini', 'pada praktikum ini dilakukan').
  5. Nilai teknis, angka, kode program, dan caption bab.urut jangan diubah atau dikarang.
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
    Ikuti seluruh aturan format, gaya bahasa, dan alur verifikasi di .skills/laporan-praktikum-standar/SKILL.md
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

## 🤖 Contoh Prompt Agentic

Begitu skill ini terpasang di agent kamu, tinggal perintah lewat chat:

**1. Bikin Laporan Baru dari Bahan Mentah:**
```text
Buatkan laporan praktikum dari notebook dan screenshot di folder Pertemuan-3 ini sampai jadi docx dan pdf. Nama: Budi Santoso, NIM: 2200018000.
```

**2. Bikin Banyak Laporan Sekaligus (Batch Processing):**
```text
Di folder ini ada bahan Pertemuan 1 sampai Pertemuan 5. Tolong buatkan semua laporan praktikumnya sekaligus secara paralel pakai skill laporan praktikum UAD, lalu verifikasi semuanya.
```

**3. Padatkan & Rapikan Banyak Laporan Lama:**
```text
Tolong parafrase dan padatkan semua file .docx laporan di folder ini biar sesuai standar laporan praktikum UAD, pastikan semuanya lolos cek verify_revisi_parafrase.py.
```

---

## ⚙️ Bagian yang Perlu Diubah (Mode Manual)

Kalau kamu jalanin script-nya secara manual tanpa bantuan AI Agent, kamu cuma perlu edit file [`scripts/build_laporan_from_template.py`](scripts/build_laporan_from_template.py) di dua variabel ini:

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

### Cara Menjalankan Manual

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
