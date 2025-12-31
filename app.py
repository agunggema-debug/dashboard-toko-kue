import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Pro Dashboard Toko Kue", layout="wide")

# Fungsi Load Data
def get_data():
    df = pd.read_csv('retail_toko_kue.csv')
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    return df

try:
    df = get_data()
except FileNotFoundError:
    st.error("File data tidak ditemukan! Jalankan data_generator.py terlebih dahulu.")
    st.stop()

# --- HEADER / KPI ---
st.title("📊 Analisis Retail Toko Kue")
total_revenue = df['Total_Penjualan'].sum()
total_qty = df['Jumlah'].sum()
avg_order = df['Total_Penjualan'].mean()

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Total Omzet", f"Rp {total_revenue:,.0f}")
kpi2.metric("Produk Terjual", f"{total_qty} pcs")
kpi3.metric("Rata-rata Transaksi", f"Rp {avg_order:,.0f}")

st.markdown("---")

# --- VISUALISASI ---
col1, col2 = st.columns([6, 4])

with col1:
    st.subheader("📈 Tren Penjualan Bulanan")
    df_monthly = df.resample('M', on='Tanggal').sum().reset_index()
    fig_line = px.line(df_monthly, x='Tanggal', y='Total_Penjualan', template="plotly_dark")
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.subheader("🥧 Proporsi Kategori")
    fig_pie = px.pie(df, values='Total_Penjualan', names='Kategori', hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

st.subheader("🏆 Top 5 Produk Terlaris")
top_products = df.groupby('Produk')['Total_Penjualan'].sum().sort_values(ascending=False).head(5).reset_index()
fig_bar = px.bar(top_products, x='Total_Penjualan', y='Produk', orientation='h', color='Produk')
st.plotly_chart(fig_bar, use_container_width=True)

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