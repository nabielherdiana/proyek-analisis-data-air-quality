# ☁️ Proyek Analisis Data: Air Quality Dataset

Proyek ini adalah *submission* akhir untuk kelas **Belajar Analisis Data dengan Python** di Dicoding.

Di dalam proyek ini, saya menganalisis dataset kualitas udara dari stasiun **Aotizhongxin** (Beijing) pada periode Maret 2013 – Februari 2017. Analisis ini berfokus pada eksplorasi polutan PM2.5 dan pola pengaruh faktor meteorologi (suhu udara) terhadap pembentukan gas Ozon (O3).

## 📌 Pertanyaan Bisnis (S.M.A.R.T)
1. Bagaimana tren tingkat polusi PM2.5 di stasiun Aotizhongxin selama periode 2013–2017?
2. Bagaimana pola pengaruh perubahan suhu udara (TEMP) terhadap tingkat konsentrasi gas Ozon (O3) di stasiun Aotizhongxin sepanjang periode observasi?

## 💡 Insight Utama
- Konsentrasi PM2.5 sangat fluktuatif dan memiliki pola musiman. Polusi cenderung memburuk pada periode akhir dan awal tahun (musim dingin), lalu membaik di pertengahan tahun.
- Terdapat korelasi positif yang signifikan antara suhu udara dengan kadar O3. Cuaca panas (>25°C) memicu lonjakan pembentukan gas ozon di atmosfer secara drastis.
- Rata-rata PM2.5 selama periode pengamatan berada di angka **82.54 µg/m³**, yang masuk dalam kategori kualitas udara tidak sehat.

## 🛠️ Teknologi yang Digunakan
- **Bahasa:** Python
- **Library Analisis:** Pandas, NumPy
- **Library Visualisasi:** Matplotlib, Seaborn, Plotly
- **Dashboard:** Streamlit
- **Environment:** Jupyter Notebook

---

## 🚀 Cara Menjalankan Dashboard secara Lokal

Untuk menjalankan *dashboard* interaktif ini di komputer lokal, silakan ikuti langkah-langkah *setup environment* berikut:

### 1. Clone Repository
Buka terminal/Command Prompt dan jalankan perintah berikut untuk mengunduh *repository*:
```bash
git clone [https://github.com/nabielherdiana/proyek-analisis-data-air-quality.git](https://github.com/nabielherdiana/proyek-analisis-data-air-quality.git)
cd proyek-analisis-data-air-quality
