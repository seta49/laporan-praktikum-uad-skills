Kalau males/gk tau cara install, salin aja link ini terus minta agent mu pasangkan😹

# Laporan Praktikum UAD

Toolkit Python dan skill AI Agent untuk membuat serta memvalidasi laporan praktikum Program Studi Informatika Universitas Ahmad Dahlan sesuai standar baku enam aturan. Aturan lengkap gaya penulisan dapat dibaca di [`SKILL.md`](SKILL.md).

---

## Cara pasang

### 1. Google Antigravity

**Lewat Chat Prompt (Praktis):**
Salin prompt ini dan kirimkan langsung di chat Antigravity:
```text
Tolong pasang skill laporan praktikum UAD dari https://github.com/seta49/skill-laporan-praktikum-uad ke konfigurasi skills saya.
```

**Lewat Terminal / CMD:**
```powershell
# Windows (PowerShell)
git clone https://github.com/seta49/skill-laporan-praktikum-uad.git "$env:USERPROFILE\.gemini\config\skills\laporan-praktikum-standar"
```
```bash
# Linux / macOS
git clone https://github.com/seta49/skill-laporan-praktikum-uad.git ~/.gemini/config/skills/laporan-praktikum-standar
```

---

### 2. Claude (Claude Code & Claude Desktop / Web)

**Lewat Claude Code (CMD / Terminal):**
Jalankan Claude Code langsung dari terminal dengan prompt instalasi di folder proyek praktikummu:
```bash
claude "Ambil dan pasang skill dari https://github.com/seta49/skill-laporan-praktikum-uad ke .claude/skills/laporan-praktikum-standar"
```
Atau clone manual ke folder skills Claude:
```bash
git clone https://github.com/seta49/skill-laporan-praktikum-uad.git .claude/skills/laporan-praktikum-standar
```

**Lewat Claude Desktop / Web:**
1. Buat **Project** baru di Claude.
2. Unggah berkas `SKILL.md` dan `templates/Template-Laporan-Praktikum-UAD.docx` ke bagian **Project Knowledge**.
3. Di obrolan, minta Claude membuat atau memvalidasi laporan mengacu pada standar di knowledge base tersebut.

---

### 3. ChatGPT (Web & Custom GPTs)

**Lewat Custom GPT / Project (Direkomendasikan):**
1. Buka ChatGPT > **Explore GPTs** > **Create** (atau gunakan menu **Projects**).
2. Unggah berkas `SKILL.md` dan `templates/Template-Laporan-Praktikum-UAD.docx` ke bagian **Knowledge**.
3. Pada kolom **Instructions**, masukkan:
   > Gunakan berkas `SKILL.md` sebagai acuan mutlak penulisan laporan praktikum UAD. Selalu terapkan standar enam aturan (paragraf padat, Ulasan 1 paragraf, tanpa penunjuk gambar, bahasa manusiawi, format tetap).

**Lewat Chat Prompt Langsung:**
Salin prompt singkat ini sebelum memberikan draf atau data praktikum:
```text
Posisikan dirimu sebagai asisten penyusun laporan praktikum Informatika UAD. Ikuti standar baku berikut:
1. Paragraf isi padat (30–55% dari gaya biasa), 1 paragraf = 1 gagasan teknis.
2. Ulasan Praktikum wajib 1 paragraf, maksimal ~90 kata (pembelajaran + kendala + solusi + temuan).
3. DILARANG menggunakan kata penunjuk gambar/tabel (seperti 'ditunjukkan pada', 'seperti tampak pada').
4. Gunakan kalimat aktif dan bahasa manusiawi, hindari basa-basi buku teks.
5. Nilai teknis, angka, blok kode, dan caption bab.urut tidak boleh diubah saat diparafrase.
```

---

### 4. Harness Lain (Cursor, Windsurf, Roo Code / Cline, Aider, dll.)

**Lewat Prompt Agent di IDE (Cursor Composer, Windsurf Cascade, Roo Code):**
Ketik prompt berikut di chat agent IDE:
```text
Pelajari aturan dan gunakan skill dari https://github.com/seta49/skill-laporan-praktikum-uad untuk menyusun laporan praktikum di project ini.
```

**Lewat Rules File di Proyek:**
Clone repositori ini ke folder proyek praktikum:
```bash
git clone https://github.com/seta49/skill-laporan-praktikum-uad.git .skills/laporan-praktikum-standar
```
Lalu hubungkan ke konfigurasi rules harness yang kamu gunakan:
- **Cursor**: Buat file `.cursor/rules/laprak.mdc` atau tambahkan ke `.cursorrules`:
  ```text
  Ikuti seluruh aturan format dan gaya penulisan di .skills/laporan-praktikum-standar/SKILL.md
  ```
- **Windsurf**: Tambahkan instruksi serupa ke `.windsurfrules`.
- **Roo Code / Cline**: Tambahkan instruksi ke `.clinerules`.
- **Aider / Generic Agent**: Jalankan agent dengan menyertakan context file:
  ```bash
  aider --read .skills/laporan-praktikum-standar/SKILL.md
  ```

---

### 5. Digunakan secara Mandiri (Manual Python)

Cukup clone repo ini ke komputer lokal:

```bash
git clone https://github.com/seta49/skill-laporan-praktikum-uad.git
cd skill-laporan-praktikum-uad
```

---

## Bagian yang Perlu Diubah

Buka berkas `scripts/build_laporan_from_template.py`, lalu sesuaikan dua bagian ini:

### 1. `META` (Identitas & Mata Kuliah)

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

### 2. `BODY` (Konten Laporan)

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

### Menjalankan Skrip

Setelah `META` dan `BODY` diisi, jalankan skrip pembangun dokumen:

```bash
uv run --with python-docx python scripts/build_laporan_from_template.py
```

*(Atau jalankan `python scripts/build_laporan_from_template.py` jika lingkungan Python lokalmu sudah terpasang `python-docx`).*
