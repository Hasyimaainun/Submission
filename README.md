# 🚲 Bike Rental Analysis Dashboard

Aplikasi **Bike Rental Analysis Dashboard** adalah sebuah alat analisis berbasis Streamlit untuk mengeksplorasi data penyewaan sepeda harian dan per jam. Dashboard ini dirancang untuk memberikan insight mendalam melalui visualisasi data, perhitungan metrik penting, dan tren penyewaan berdasarkan waktu, musim, dan tahun.

---

## 🚀 Fitur Utama
1. **Statistik Harian**:  
   - Total penyewaan oleh pengguna kasual (Casual User).  
   - Total penyewaan oleh pengguna terdaftar (Registered User).  
   - Total penyewaan keseluruhan (Total User).  

2. **Eksplorasi Dataset**:  
   - Menampilkan data mentah dari dataset harian (`day.csv`) dan per jam (`hour.csv`).  
   - Statistik deskriptif, seperti rata-rata, standar deviasi, nilai minimum, dan maksimum.  

3. **Visualisasi Data**:
   - **Heatmap Korelasi**: Mengidentifikasi hubungan antar variabel dalam dataset.  
   - **Histogram**: Menampilkan distribusi variabel dalam dataset harian.  
   - **Tren Waktu dan Musim**: Analisis penyewaan sepeda berdasarkan jam, musim, dan tahun.  

4. **Insight Dinamis**:  
   - Jam puncak penyewaan sepeda.  
   - Musim dengan penyewaan tertinggi dan perbandingan antara tahun 2011 dan 2012.  

---

## 📋 Prasyarat

Sebelum menjalankan dashboard, pastikan Anda telah memenuhi persyaratan berikut:  

1. **Python**: Versi 3.8 atau lebih baru.  
2. **Library Python**:  
   Pastikan Anda menginstal library berikut:  
   - `streamlit`
   - `pandas`
   - `seaborn`
   - `matplotlib`

---

## 📦 Instalasi dan Cara Menjalankan

Ikuti langkah-langkah berikut untuk menjalankan aplikasi:  

### **1. Clone Repository**  
Clone repository ke komputer lokal Anda:  
```bash
git clone [https://github.com/Hasyimaainun/Submission/blob/main/dashboard.py]
```

### **2. Instal Dependensi**
Instal semua dependensi yang diperlukan menggunakan pip dan file requirements.txt:
```bash
pip install -r requirements.txt
```

Jika file requirements.txt belum tersedia, buat file tersebut dengan daftar berikut:
```bash
streamlit
pandas
seaborn
matplotlib
```

### **3. Jalankan Dashboard**
```bash
streamlit run app.py
