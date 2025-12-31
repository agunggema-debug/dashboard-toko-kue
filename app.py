import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman agar Elegan
st.set_page_config(
    page_title="Dashboard Retail Toko Kue",
    page_icon="🍰",
    layout="wide"
)

# 2. Fungsi Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('retail_toko_kue.csv')
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("File 'retail_toko_kue.csv' tidak ditemukan. Jalankan data_generator.py terlebih dahulu!")
    st.stop()

# --- SIDEBAR: FILTER ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3081/3081913.png", width=100)
st.sidebar.title("Filter Dashboard")

# Filter Rentang Tanggal
min_date = df['Tanggal'].min().to_pydatetime()
max_date = df['Tanggal'].max().to_pydatetime()

date_range = st.sidebar.date_input(
    "Pilih Rentang Waktu",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Filter Pencarian Produk
all_products = df['Produk'].unique()
selected_products = st.sidebar.multiselect("Cari/Pilih Produk", options=all_products, default=all_products)

# Menerapkan Filter ke Data
if len(date_range) == 2:
    start_date, end_date = date_range
    mask = (df['Tanggal'].dt.date >= start_date) & (df['Tanggal'].dt.date <= end_date) & (df['Produk'].isin(selected_products))
    df_filtered = df.loc[mask]
else:
    df_filtered = df[df['Produk'].isin(selected_products)]

# --- MAIN PAGE: METRIK UTAMA ---
st.title("🍰 Dashboard Retail: Analisis Penjualan")
st.markdown(f"Menampilkan data dari **{date_range[0]}** hingga **{date_range[1]}**")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1:
    st.metric("Total Omzet", f"Rp {df_filtered['Total_Penjualan'].sum():,.0f}")
with kpi2:
    st.metric("Produk Terjual", f"{df_filtered['Jumlah'].sum():,.0f} pcs")
with kpi3:
    st.metric("Jumlah Transaksi", f"{len(df_filtered)}")
with kpi4:
    st.metric("Rata-rata Penjualan", f"Rp {df_filtered['Total_Penjualan'].mean():,.0f}")

st.divider()


# --- VISUALISASI ---
col_left, col_right = st.columns([7, 3])

with col_left:
    st.subheader("📈 Grafik Tren Penjualan")
    # Agregasi data harian untuk grafik garis
    daily_sales = df_filtered.groupby('Tanggal')['Total_Penjualan'].sum().reset_index()
    fig_line = px.line(daily_sales, x='Tanggal', y='Total_Penjualan', 
                       line_shape='spline', render_mode='svg')
    fig_line.update_traces(line_color='#FF4B4B')
    st.plotly_chart(fig_line, use_container_width=True)

with col_right:
    st.subheader("🥧 Penjualan per Kategori")
    fig_pie = px.pie(df_filtered, values='Total_Penjualan', names='Kategori', hole=0.5)
    st.plotly_chart(fig_pie, use_container_width=True)

st.subheader("🏆 Top 5 Produk Terlaris")
top_products = df.groupby('Produk')['Total_Penjualan'].sum().sort_values(ascending=False).head(5).reset_index()
fig_bar = px.bar(top_products, x='Total_Penjualan', y='Produk', orientation='h', color='Produk')
st.plotly_chart(fig_bar, use_container_width=True)

# Tabel Data Detail (Dapat diunduh)
st.subheader("📋 Detail Data Transaksi")
st.dataframe(df_filtered, use_container_width=True)

# --- FOOTER ---
st.markdown("---") # Garis pemisah horizontal

# Menggunakan CSS untuk styling footer agar lebih elegan
footer_style = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0E1117;
        color: #FAFAFA;
        text-align: center;
        padding: 10px;
        font-family: 'sans-serif';
        font-size: 14px;
        border-top: 1px solid #4B4B4B;
    }
    </style>
    <div class="footer">
        <p>🍰 <b>Dashboard Toko Kue v1.0</b> | Dikembangkan dengan Python & Streamlit | © 2025 Analisis Retail</p>
    </div>
"""

# Jika ingin footer yang menempel di bawah (fixed), gunakan ini:
# st.markdown(footer_style, unsafe_allow_html=True)

# Atau jika ingin footer biasa yang mengikuti scroll, cukup gunakan markdown sederhana:
st.markdown(
    """
    <div style="text-align: center; color: grey; padding: 20px;">
        <p>Built with ❤️ by agung_gema | <a href="https://github.com/" target="_blank">View on GitHub</a></p>
        <small>Data simulasi ini dibuat untuk keperluan demonstrasi visualisasi retail.</small>
    </div>
    """, 
    unsafe_allow_html=True
)