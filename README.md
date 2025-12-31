# 🍰 Dashboard Retail: Analisis Penjualan
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://your-app-url.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📌 Deskripsi Proyek
Dashboard ini dirancang untuk memberikan wawasan mendalam (insights) bagi pemilik toko kue retail. Proyek ini memvisualisasikan data transaksi harian, tren penjualan bulanan, serta performa produk secara interaktif tanpa memerlukan lisensi berbayar seperti Power BI Pro.

Aplikasi ini dibangun menggunakan **Python** dengan library **Streamlit** untuk antarmuka web yang modern dan **Plotly** untuk grafik yang responsif.

## 🚀 Fitur Utama
* **KPI Metrics:** Ringkasan instan mengenai Total Omzet, Jumlah Produk Terjual, dan Rata-rata Transaksi.
* **Filter Interaktif:** * *Date Range Filter*: Memungkinkan analisis performa pada periode tertentu.
    * *Product Search*: Memfilter data berdasarkan produk spesifik.
* **Visualisasi Data:**
    * Grafik Tren Penjualan (Line Chart) untuk melihat fluktuasi omzet.
    * Proporsi Kategori (Pie Chart) untuk memahami segmentasi pasar.
    * Top 5 Produk Terlaris (Bar Chart).
* **Data Table:** Akses langsung ke detail data mentah yang dapat diurutkan.

## 🛠️ Teknologi yang Digunakan
- **Bahasa Pemrograman:** Python
- **Library Utama:** - `Streamlit` (Web Framework)
  - `Pandas` (Data Manipulation)
  - `Plotly` (Interactive Visualization)
- **Deployment:** GitHub Pages & Streamlit Community Cloud

## 📂 Struktur Folder
```text
.
├── app.py                # File utama aplikasi Streamlit
├── data_generator.py     # Script untuk membuat data simulasi (2000+ transaksi)
├── retail_toko_kue.csv   # Dataset (dihasilkan dari script generator)
├── requirements.txt      # Daftar library yang diperlukan
└── README.md             # Dokumentasi proyek
