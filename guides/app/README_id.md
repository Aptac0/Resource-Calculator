# RSS STORE APTAC - Kalkulator Sumber Daya

**[Español](README_es.md) | [English](README_en.md) | [Português](README_pt.md) | [Tiếng Việt](README_vi.md) | [Bahasa Indonesia](README_id.md) | [Français](README_fr.md)**

Aplikasi desktop untuk mengekstrak sumber daya kerajaan dari tangkapan layar secara otomatis menggunakan OCR dengan pembuatan nama panggilan pintar.

---

## 📖 Daftar Isi

1. [Panduan Singkat](#-panduan-singkat)
2. [Cara Mengambil Tangkapan Layar](#-cara-mengambil-tangkapan-layar)
3. [Format Masukan](#-format-masukan)
4. [Tombol dan Fungsi](#-tombol-dan-fungsi)
5. [Hasil dan File Tersimpan](#-hasil-dan-file-tersimpan)
6. [Pemecahan Masalah](#-pemecahan-masalah)
7. [Sistem Pembaruan](#-sistem-pembaruan)

---

## 🚀 Panduan Singkat

### Langkah demi Langkah

1. **Buka aplikasi**
   - Jalankan `RSS STORE APTAC.exe`
   - Pilih bahasa di menu utama

2. **Tambahkan gambar**
   - Klik tombol `Tambah Gambar`
   - Pilih tangkapan layar Anda
   - Gambar dimuat ke dalam daftar

3. **Konfigurasi kerajaan**
   - Pilih `Kerajaan` dari dropdown
   - Kerajaan yang tersedia diperbarui dari server

4. **Isi angka**
   - `Nomor awal`: nomor akun pertama (misalnya 1)
   - `Nomor akhir`: nomor akun terakhir (misalnya 30)
   - `Nomor diblokir` (opsional): akun yang dilewati (misalnya 3,5,7)

5. **Atur level**
   - `Level Kota`: level Pasar (1–25)
   - `Level Gudang`: level Penyimpanan (1–25)

6. **Proses sumber daya**
   - Klik tombol sumber daya yang Anda butuhkan:
     - `Sumber Daya Total`: Total per akun
     - `Sumber Daya Akun`: Nilai bersih
     - `Sumber Daya Tas Punggung`: Hanya inventaris

7. **Temukan hasil**
   - Disimpan otomatis ke `GUARDADOS/`
   - Nama: `KINGDOM_results_YYYYMMDD_HHMMSS.txt`

## 📸 Cara Mengambil Tangkapan Layar

### Dari PC (Direkomendasikan)

✅ **Cara benar:**
- Buka game dalam mode jendela
- Ambil tangkapan layar jendela Sumber Daya dengan jelas
- Pastikan angka tidak terpotong
- Gambar harus tajam tanpa bayangan

![Tangkapan dari PC](../../images/app/Foto-desde-PC.png)

**Tips:**
- Gunakan alat tangkapan layar Windows (Win + Shift + S)
- Sertakan hanya dialog sumber daya
- Angka dan label harus terbaca

### Dari Mobile

⚠️ **Penting:**
1. Ambil tangkapan layar di ponsel
2. **Transfer ke PC** (USB, Google Drive, Telegram, dll.)
3. Hindari foto miring atau buram
4. Tangkapan harus tajam dan jelas

![Tangkapan dari Mobile](../../images/app/Foto-desde-Movil.png)

**Rekomendasi:**
- Gunakan screenshot asli ponsel (lebih baik dari foto)
- Pencahayaan baik
- Tidak ada pantulan atau bayangan
- Transfer tanpa kompresi

## 🔢 Format Masukan

### Nomor Awal dan Nomor Akhir

- **Hanya angka**: `1` hingga `30` (misalnya mulai=1, akhir=30)
- **Harus bilangan bulat positif**
- **Jumlah gambar harus cocok** dengan akun yang valid

### Nomor Diblokir (Opsional)

**Dua format yang diizinkan:**

**Format 1: Rentang**
```
1-10      → 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
3-5       → 3, 4, 5
```

**Format 2: Daftar**
```
1,3,5,7   → 1, 3, 5, 7
3, 5, 8   → 3, 5, 8 (spasi diizinkan)
```

**Format 3: Campuran**
```
1-5,8,10-15  → 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 14, 15
```

### Contoh Praktis

| Kolom | Nilai | Hasil |
|-------|-------|-------|
| Awal | 1 | Akun 1 |
| Akhir | 10 | Akun 10 |
| Diblokir | 3,5 | Memproses: 1,2,4,6,7,8,9,10 |
| Gambar | 8 | ✅ Valid (cocok) |

⚠️ Jika jumlah gambar ≠ akun yang valid, Anda akan melihat kesalahan.

### Level

- `Level Kota` (Pasar): 1-25
- `Level Gudang` (Penyimpanan): 1-25



## 🎯 Tombol dan Fungsi

### Tambah Gambar
- Membuka selektor file
- Pilih beberapa tangkapan layar
- Ditambahkan ke daftar pemrosesan

### Tambah Folder
- Memuat semua gambar valid dari satu folder
- Lebih cepat untuk batch besar
- Direkomendasikan saat memproses banyak akun

### Hapus Gambar
- Menghapus satu gambar terpilih dari daftar
- Berguna untuk memperbaiki tangkapan yang salah tanpa mengosongkan semua
- Membantu validasi batch akhir sebelum diproses

### Bersihkan Daftar
- Mengosongkan semua gambar yang dimuat
- Menghapus data sementara
- Berguna untuk memulai batch baru

### Jendela Baru
- Membuka instance aplikasi lain
- Berguna untuk beberapa tugas

### Perbarui Data
- Mengunduh `kingdoms/` dan `Iconos/` terbaru dari sumber pembaruan
- Menimpa data lokal
- Jika menggunakan .exe, menampilkan halaman release untuk installer baru

### Sumber Daya Total
- Memproses gambar untuk setiap akun
- Menyimpan: Makanan, Kayu, Batu, Emas
- Menampilkan total per akun
- Berguna untuk pelacakan inventaris

### Sumber Daya Akun
- Menghitung sumber daya bersih (total - inventaris)
- Mengurangi item tas punggung
- Menunjukkan sumber daya akun nyata
- Lebih baik untuk manajemen akun

### Sumber Daya Tas Punggung
- Menampilkan hanya item inventaris
- Mengekstrak nilai "dari objek"
- Berguna untuk analisis tas punggung

## 💾 Hasil dan File Tersimpan

### Lokasi File

```
GUARDADOS/
├── KINGDOM_results_20260602_143022.txt
├── KINGDOM_results_20260602_145015.txt
└── KINGDOM_results_20260603_101530.txt
```

### Format File

```
Nickname: Account_1
Level Kota: 15
Level Gudang: 18
Makanan: 45.0K
Kayu: 32.5K
Batu: 28.7K
Emas: 5.6K
---
Nickname: Account_2
Level Kota: 15
Level Gudang: 18
Makanan: 41.2K
Kayu: 35.1K
Batu: 26.8K
Emas: 6.1K
---
```

### Cara Menggunakan Hasil

1. Buka file `.txt` di editor
2. Salin data yang Anda butuhkan
3. Tempelkan ke alat manajemen Anda
4. Nickname dibuat otomatis

---

## 🆘 Pemecahan Masalah

### "Tidak dapat mendeteksi 4 nilai"
- Masalah kualitas tangkapan layar - coba gambar lebih jelas
- Angka harus terbaca jelas
- Coba potong ulang atau ambil ulang tangkapan layar
- Sesuaikan kecerahan jika angka gelap

### "Error: X gambar dipilih tetapi Y akun valid"
- Jumlah gambar tidak cocok dengan akun valid
- Periksa nomor awal/akhir dan angka diblokir
- Gunakan rumus: (akhir - awal + 1) - diblokir = total yang dibutuhkan
- Tambahkan atau hapus gambar agar cocok

### "Error pembaruan"
- Periksa koneksi internet
- Coba lagi dalam beberapa menit
- Restart aplikasi jika error berlanjut
- Periksa pengaturan firewall

### Gambar tidak diproses
- Verifikasi kerajaan telah dipilih
- Periksa semua kolom angka terisi
- Pastikan jumlah gambar cocok dengan akun yang diharapkan
- Coba pratinjau gambar untuk memeriksa kualitas OCR

### "Tidak dapat membuka jendela"
- Kemungkinan ada instance lain yang sedang berjalan
- Tutup jendela yang ada dan coba lagi
- Coba jalankan sebagai Administrator

---

## 🔄 Sistem Pembaruan

### Otomatis
- Aplikasi **memeriksa versi baru saat startup**
- Jika pembaruan tersedia, notifikasi muncul
- Unduhan otomatis dari server yang dikonfigurasi
- Instalasi tanpa intervensi

### Manual
- Jalankan `actualizar.bat` di folder instalasi
- Ini memperbarui langsung dari sumber yang dikonfigurasi

### Apa yang Diperbarui
- `kingdoms/` → template baru
- `Iconos/` → ikon baru
- versi .exe → dari Releases

---

## 📋 Tingkat yang Tersedia

### Level Kota (Pasar)
- Rentang: 1 sampai 25
- Berlaku untuk semua sumber daya
- Disimpan dalam hasil



### Level Gudang (Penyimpanan)
- Rentang: 1 sampai 25
- Penyimpanan tersedia
- Disimpan dalam hasil



### Teknologi Maksimal
- Mempengaruhi kapasitas sumber daya
- Referensi dalam aplikasi



---

## 🎯 Contoh Lengkap

**Skenario:** Anda memiliki 5 akun, Anda ingin sumber daya total

1. **Siapkan tangkapan layar**
   - Ambil 5 tangkapan layar (satu per akun)
   - Transfer ke PC
   - Simpan di folder yang dapat diakses

2. **Konfigurasikan aplikasi**
   - Tambah Gambar → pilih 5
   - Kerajaan → pilih yang benar
   - Nomor awal: 1
   - Nomor akhir: 5
   - Nomor diblokir: (kosong)
   - Level Kota: 15
   - Level Gudang: 18

3. **Proses**
   - Klik `Sumber Daya Total`
   - Tunggu hingga selesai
   - Anda akan melihat kemajuan dalam %

4. **Hasil**
   - File disimpan otomatis
   - Buka `GUARDADOS/REINO_results_*.txt`
   - Salin data ke alat Anda
