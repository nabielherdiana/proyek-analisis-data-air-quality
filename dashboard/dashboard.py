import pandas as pd
import plotly.express as px
import streamlit as st

# Set config web
st.set_page_config(page_title="Air Quality Insights", page_icon="🌬️", layout="wide")

# --- CUSTOM CSS  ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    h1, h2, h3 {
        color: #2c3e50;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv("data/PRSA_Data_Aotizhongxin_20130301-20170228.csv")
    df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    cols_to_interpolate = ['PM2.5', 'TEMP', 'O3']
    for col in cols_to_interpolate:
        df[col] = df[col].interpolate(method='linear', limit_direction='both')
    return df

df = load_data()

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3313/3313888.png", width=100)
    st.title("Air Quality: Aotizhongxin")
    st.markdown("Cek kualitas udara dan korelasinya dengan cuaca di sini.")
    st.divider()
    
    min_date = df['datetime'].min().date()
    max_date = df['datetime'].max().date()
    
    start_date, end_date = st.date_input(
        label='Pilih Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter Data
main_df = df[(df["datetime"].dt.date >= start_date) & 
             (df["datetime"].dt.date <= end_date)]

# --- MAIN CONTENT ---
st.title("🌬️ Air Quality Insights Dashboard")
st.markdown("**Proyek Analisis Data | Nabiel Alfallah Herdiana**")
st.divider()

# --- METRICS LAYER ---
col1, col2, col3 = st.columns(3)
col1.metric("☁️ Rata-rata PM2.5", f"{main_df['PM2.5'].mean():.1f} µg/m³")
col2.metric("🌡️ Rata-rata Suhu", f"{main_df['TEMP'].mean():.1f} °C")
col3.metric("💨 Rata-rata Ozon (O3)", f"{main_df['O3'].mean():.1f} µg/m³")

st.markdown("<br>", unsafe_allow_html=True)

# --- VISUALIZATION LAYER ---
st.subheader("📈 Tren Tingkat PM2.5 Bulanan")
main_df_monthly = main_df.set_index('datetime').resample('M').mean(numeric_only=True).reset_index()

# Plotly Line Chart
fig_pm = px.line(
    main_df_monthly, 
    x='datetime', 
    y='PM2.5', 
    markers=True, 
    line_shape='spline', 
    color_discrete_sequence=['#E74C3C'] 
)
fig_pm.update_layout(xaxis_title="Waktu", yaxis_title="Konsentrasi PM2.5", plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_pm, use_container_width=True)


st.divider()


st.subheader("🔥 Suhu Udara vs 💨 Ozon (O3)")
# Plotly Scatter Chart
fig_corr = px.scatter(
    main_df, 
    x='TEMP', 
    y='O3', 
    opacity=0.4,
    color='O3', 
    color_continuous_scale='Tealrose'
)
fig_corr.update_layout(xaxis_title="Suhu Udara (°C)", yaxis_title="Konsentrasi Ozon (O3)", plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_corr, use_container_width=True)

# Footer
st.markdown("<p style='text-align: center; color: grey; font-size: 12px;'>Dibuat menggunakan Streamlit & Plotly | © 2026</p>", unsafe_allow_html=True)
