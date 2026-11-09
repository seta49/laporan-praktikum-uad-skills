<div align="center">

# 📄 Laporan Praktikum UAD — Standar Baku

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Output](https://img.shields.io/badge/Output-.DOCX%20%26%20.PDF-2B579A?style=flat-square&logo=microsoftword&logoColor=white)](templates/Template-Laporan-Praktikum-UAD.docx)
[![Standard](https://img.shields.io/badge/Standard-Informatika%20UAD-003366?style=flat-square)](SKILL.md)
[![Agent Ready](https://img.shields.io/badge/AI%20Agent-Antigravity%20%7C%20Claude%20%7C%20GPT-8A2BE2?style=flat-square)](#-cara-pasang)

<p align="center">
  Toolkit Python dan skill AI Agent untuk membuat serta memvalidasi laporan praktikum Program Studi Informatika <b>Universitas Ahmad Dahlan</b> sesuai standar baku enam aturan.
</p>

<p align="center">
  <a href="#-cara-pasang"><b>📦 Cara Pasang</b></a> •
  <a href="#-bagian-yang-perlu-diubah"><b>⚙️ Konfigurasi</b></a> •
  <a href="#-cara-menjalankan"><b>🚀 Eksekusi</b></a> •
  <a href="SKILL.md"><b>📖 Panduan SKILL.md</b></a>
</p>

</div>

> 💡 **Males ribet pasang manual?**  
> Salin aja tautan repo ini (`https://github.com/seta49/skill-laporan-praktikum-uad`) lalu minta AI agent pilihanmu buat pasangkan otomatis! 😹

---

## 📦 Cara Pasang

Pilih platform atau AI agent yang kamu gunakan:

### ⚡ Google Antigravity

* **Lewat Chat Prompt (Praktis):**  
  Kirim prompt ini langsung di obrolan Antigravity:
  ```text
  Tolong pasang skill laporan praktikum UAD dari https://github.com/seta49/skill-laporan-praktikum-uad ke konfigurasi skills saya.
  ```

* **Lewat Terminal / CMD:**
  ```powershell
  # Windows (PowerShell)
  git clone https://github.com/seta49/skill-laporan-praktikum-uad.git "$env:USERPROFILE\.gemini\config\skills\laporan-praktikum-standar"
  ```
  ```bash
  # Linux / macOS
  git clone https://github.com/seta49/skill-laporan-praktikum-uad.git ~/.gemini/config/skills/laporan-praktikum-standar
  ```

---

### 🟣 Claude (Claude Code & Web)

* **Lewat Claude Code (CMD / Terminal):**  
  Jalankan Claude Code langsung dari terminal dengan prompt instalasi di folder proyekmu:
  ```bash
  claude "Ambil dan pasang skill dari https://github.com/seta49/skill-laporan-praktikum-uad ke .claude/skills/laporan-praktikum-standar"
  ```
  Atau clone langsung ke folder skills Claude:
  ```bash
  git clone https://github.com/seta49/skill-laporan-praktikum-uad.git .claude/skills/laporan-praktikum-standar
  ```

* **Lewat Claude Desktop / Web:**
  1. Buat **Project** baru di Claude.
  2. Unggah berkas [`SKILL.md`](SKILL.md) dan [`templates/Template-Laporan-Praktikum-UAD.docx`](templates/Template-Laporan-Praktikum-UAD.docx) ke **Project Knowledge**.
  3. Minta Claude menyusun atau memvalidasi laporan mengacu pada berkas knowledge tersebut.

---

### 🟢 ChatGPT (Web & Custom GPTs)

* **Lewat Custom GPT / Project (Direkomendasikan):**
  1. Buka ChatGPT > **Explore GPTs** > **Create** (atau menu **Projects**).
  2. Unggah [`SKILL.md`](SKILL.md) dan [`templates/Template-Laporan-Praktikum-UAD.docx`](templates/Template-Laporan-Praktikum-UAD.docx) ke bagian **Knowledge**.
  3. Masukkan arahan singkat di **Instructions**:
     > Gunakan berkas `SKILL.md` sebagai acuan mutlak penulisan laporan praktikum UAD. Selalu terapkan standar enam aturan (paragraf padat, Ulasan 1 paragraf, tanpa penunjuk gambar, bahasa manusiawi, format tetap).

* **Lewat Chat Prompt Langsung:**  
  Salin prompt ini di awal obrolan sebelum memberikan draf atau data praktikum:
  ```text
  Posisikan dirimu sebagai asisten penyusun laporan praktikum Informatika UAD. Ikuti standar baku berikut:
  1. Paragraf isi padat (30–55% dari gaya biasa), 1 paragraf = 1 gagasan teknis.
  2. Ulasan Praktikum wajib 1 paragraf, maksimal ~90 kata (pembelajaran + kendala + solusi + temuan).
  3. DILARANG menggunakan kata penunjuk gambar/tabel (seperti 'ditunjukkan pada', 'seperti tampak pada').
  4. Gunakan kalimat aktif dan bahasa manusiawi, hindari basa-basi buku teks.
  5. Nilai teknis, angka, blok kode, dan caption bab.urut tidak boleh diubah saat diparafrase.
  ```

---

### 🛠️ Harness Lain (Cursor, Windsurf, Roo Code / Cline, Aider)

* **Lewat Prompt Agent di IDE (Cursor Composer, Windsurf Cascade, Roo Code):**
  ```text
  Pelajari aturan dan gunakan skill dari https://github.com/seta49/skill-laporan-praktikum-uad untuk menyusun laporan praktikum di project ini.
  ```

* **Lewat File Rules Proyek:**  
  Clone repositori ini ke folder proyek praktikum:
  ```bash
  git clone https://github.com/seta49/skill-laporan-praktikum-uad.git .skills/laporan-praktikum-standar
  ```
  Lalu tautkan ke konfigurasi rule masing-masing harness:
  * **Cursor**: Tulis di `.cursor/rules/laprak.mdc` atau `.cursorrules`:
    ```text
    Ikuti seluruh aturan format dan gaya penulisan di .skills/laporan-praktikum-standar/SKILL.md
    ```
  * **Windsurf**: Tambahkan instruksi ke `.windsurfrules`.
  * **Roo Code / Cline**: Tambahkan instruksi ke `.clinerules`.
  * **Aider / CLI Agent**: Sertakan saat menjalankan agent:
    ```bash
    aider --read .skills/laporan-praktikum-standar/SKILL.md
    ```

---

### 💻 Penggunaan Mandiri (Python CLI)

Jika ingin menjalankan tanpa AI Agent, clone langsung ke komputermu:

```bash
git clone https://github.com/seta49/skill-laporan-praktikum-uad.git
cd skill-laporan-praktikum-uad
```

---

## ⚙️ Bagian yang Perlu Diubah

Kamu hanya perlu menyunting berkas [`scripts/build_laporan_from_template.py`](scripts/build_laporan_from_template.py) pada dua variabel utama:

### 1. `META` — Identitas & Informasi Praktikum

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

### 2. `BODY` — Struktur Isi Laporan

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

Setelah `META` dan `BODY` disesuaikan, bangun berkas laporan (`.docx`) menggunakan:

```bash
# Menggunakan uv (direkomendasikan, otomatis unduh pustaka)
uv run --with python-docx python scripts/build_laporan_from_template.py

# Atau menggunakan Python biasa (jika python-docx sudah terpasang)
python scripts/build_laporan_from_template.py
```

Dokumen keluaran akan otomatis tersimpan di folder tujuan (default: `~/Laporan Praktikum/`).

---

<div align="center">
  <sub>Aturan penulisan lengkap, struktur blok dokumen, dan panduan parafrase tersedia di <a href="SKILL.md">SKILL.md</a>.</sub>
</div>
