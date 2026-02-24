import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("data/PRSA_Data_Aotizhongxin_20130301-20170228.csv")
    df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    df['PM2.5'] = df['PM2.5'].interpolate(method='linear', limit_direction='both')
    return df

df = load_data()

st.title("☁️ Air Quality Data Dashboard: Aotizhongxin Station")
st.markdown("Dashboard ini menampilkan hasil analisis kualitas udara dengan fokus pada PM2.5 dan Ozon.")

# Sidebar untuk filter tahun
st.sidebar.header("Filter Waktu")
min_date = df['datetime'].min().date()
max_date = df['datetime'].max().date()

start_date, end_date = st.sidebar.date_input(
    label='Rentang Waktu',
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

# Filter data based on date input
main_df = df[(df["datetime"].dt.date >= start_date) & 
             (df["datetime"].dt.date <= end_date)]

# Row 1: Metrik Utama
col1, col2 = st.columns(2)
with col1:
    st.metric("Rata-rata PM2.5", value=f"{main_df['PM2.5'].mean():.2f} µg/m³")
with col2:
    st.metric("Rata-rata Suhu (TEMP)", value=f"{main_df['TEMP'].mean():.2f} °C")

# Row 2: Visualisasi Tren PM2.5
st.subheader("Tren Tingkat PM2.5")
fig, ax = plt.subplots(figsize=(16, 6))
main_df_monthly = main_df.set_index('datetime').resample('M').mean(numeric_only=True).reset_index()
sns.lineplot(data=main_df_monthly, x='datetime', y='PM2.5', marker='o', color='red', ax=ax)
ax.set_ylabel("PM2.5")
ax.set_xlabel("Waktu")
st.pyplot(fig)

# Row 3: Visualisasi Korelasi
st.subheader("Korelasi Suhu (TEMP) vs Ozon (O3)")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=main_df, x='TEMP', y='O3', alpha=0.5, color='orange', ax=ax2)
ax2.set_ylabel("Ozon (O3)")
ax2.set_xlabel("Suhu (TEMP)")
st.pyplot(fig2)

st.caption("Proyek Analisis Data © 2026")
