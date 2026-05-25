# Tugas-07-BasisData

## Lampiran: Dokumentasi Source Code Antarmuka (Interface)

Sebagai alternatif pengembangan dari contoh dasar PHP yang diberikan, antarmuka (interface) untuk tugas ini dibangun menggunakan bahasa pemrograman Python dengan memanfaatkan framework Streamlit. Pendekatan ini dipilih karena efisiensi dalam menghubungkan logika pemrosesan data secara langsung dengan tampilan web yang interaktif.

**1.Teknologi Pendukung (Tech Stack)**
- Python: Bahasa pemrograman utama untuk mengeksekusi logika query dan memproses data.
- Streamlit: Library Python berkonsep Single Page Application (SPA) yang bertugas merender antarmuka web (UI) secara dinamis tanpa perlu menuliskan kode HTML/CSS secara manual.
- Pandas: Library manipulasi data yang digunakan untuk merapikan hasil query SQL Server menjadi format struktur tabel (Dataframe).
- PyODBC: Driver penghubung antara skrip Python dengan database Microsoft SQL Server.

**2.Persyaratan Sistem (Prerequisites)**
- Sebelum kode dapat dijalankan, pastikan sistem telah terinstal:
- Python versi 3.x.
- ODBC Driver for SQL Server (Versi 17 atau 18) di Windows.
- Library Python yang dibutuhkan. Instalasi dapat dilakukan melalui terminal/CMD dengan perintah:
  ```bash
  pip install streamlit pandas pyodbc
  ```
  
**3.Konfigurasi dan Cara Penggunaan**
1. Penyesuaian Server: Pada bagian fungsi init_connection() di dalam kode, parameter SERVER=LAPTOP-JCGQILKU harus disesuaikan dengan nama server SQL Server yang aktif di komputer host.
2. Eksekusi Program: Buka terminal pada direktori tempat file app.py disimpan, lalu jalankan perintah berikut:
   ```bash
   streamlit run app.py
   ```
3. Akses Antarmuka: Streamlit akan secara otomatis menjalankan local web server dan membuka antarmuka aplikasi melalui browser di alamat http://localhost:8501.

**4.Source Code (app.py)**

Berikut adalah keseluruhan kode program yang digunakan untuk membangun antarmuka ini:

[Lihat Source Code di Sini](app.py)

