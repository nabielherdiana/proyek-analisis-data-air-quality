# Proyek Analisis Data: Air Quality Dataset

Proyek ini adalah submission akhir untuk kelas **Belajar Fundamental Analisis Data dengan Python** di Dicoding.

Saya menganalisis dataset kualitas udara dari stasiun **Aotizhongxin** (Beijing) periode Maret 2013 – Februari 2017. Dataset ini berisi data per jam yang mencakup berbagai polutan udara dan variabel meteorologi.

## Pertanyaan Bisnis

1. Bagaimana tren tingkat polusi PM2.5 di stasiun Aotizhongxin selama periode 2013–2017?
2. Bagaimana pola pengaruh perubahan suhu udara (TEMP) terhadap tingkat konsentrasi gas Ozon (O3) di stasiun Aotizhongxin sepanjang periode observasi?

## Insight Utama

- Konsentrasi PM2.5 sangat fluktuatif dan memiliki pola musiman. Polusi cenderung memburuk pada periode akhir dan awal tahun (musim dingin), lalu membaik di pertengahan tahun.
- Terdapat korelasi positif yang signifikan antara suhu udara dengan kadar O3. Cuaca panas (>25°C) memicu lonjakan pembentukan gas ozon di atmosfer secara drastis.
- Rata-rata PM2.5 selama periode pengamatan berada di angka **82.54 µg/m³**, yang masuk dalam kategori kualitas udara tidak sehat.

## Teknologi yang Digunakan

- **Bahasa:** Python
- **Library Analisis:** Pandas, NumPy
- **Library Visualisasi:** Matplotlib, Seaborn, Plotly
- **Dashboard:** Streamlit
- **Environment:** Jupyter Notebook

## Cara Menjalankan

1. Clone repository:
   ```bash
   git clone https://github.com/nabielherdiana/proyek-analisis-data-air-quality.git
   cd proyek-analisis-data-air-quality
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan dashboard:
   ```bash
   streamlit run dashboard.py
   ```

Atau buka file `Proyek_Analisis_Data_Nabiel.ipynb` di Jupyter Notebook untuk melihat proses analisis dari awal sampai akhir.
