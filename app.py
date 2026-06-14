import streamlit as st
import pandas as pd
import numpy as np

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Dashboard Analisis Data Nutrisi", layout="wide")

st.title("	Dashboard Analisis Faktor Risiko Nutrisi & Tumbuh Kembang")
st.write("Aplikasi ini menganalisis hubungan antara asupan nutrisi dan kategori pertumbuhan anak.")

# 2. Membuat Dataset Tiruan (Agar langsung jalan tanpa file luar)
np.random.seed(42)
n_samples = 100
data = {
    'Usia_Bulan': np.random.randint(6, 60, n_samples),
    'Asupan_Protein_Gram': np.random.uniform(10, 50, n_samples),
    'Tinggi_Badan_Cm': np.random.uniform(60, 110, n_samples),
}
df = pd.DataFrame(data)

# Logika penentuan status (simplifikasi untuk visualisasi)
df['Status_Gizi'] = np.where(df['Asupan_Protein_Gram'] < 22, 'Risiko Kurang Gizi', 'Gizi Baik')

# 3. Sidebar untuk Filter Interaktif
st.sidebar.header("Filter Data")
status_filter = st.sidebar.multiselect(
    "Pilih Status Gizi:",
    options=df['Status_Gizi'].unique(),
    default=df['Status_Gizi'].unique()
)

filtered_df = df[df['Status_Gizi'].isin(status_filter)]

# 4. Menampilkan Metrik Ringkasan
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Sampel Diarsip", len(filtered_df))
with col2:
    st.metric("Rata-rata Protein (g)", f"{filtered_df['Asupan_Protein_Gram'].mean():.2f}")
with col3:
    st.metric("Rata-rata Tinggi (cm)", f"{filtered_df['Tinggi_Badan_Cm'].mean():.2f}")

st.markdown("---")

# 5. Visualisasi Data
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Hubungan Usia vs Tinggi Badan")
    st.scatter_chart(data=filtered_df, x='Usia_Bulan', y='Tinggi_Badan_Cm', color='Status_Gizi')

with col_right:
    st.subheader("Distribusi Asupan Protein")
    st.bar_chart(filtered_df['Asupan_Protein_Gram'])

# 6. Menampilkan Tabel Data
st.subheader("Data Mentah")
st.dataframe(filtered_df)