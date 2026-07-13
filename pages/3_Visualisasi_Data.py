import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from utils import load_all_data, load_css, render_sidebar_profile

st.set_page_config(page_title="Visualisasi Data", page_icon="📈", layout="wide")
load_css()
render_sidebar_profile()
data = load_all_data()
df = data["data_historis"]

st.title("Visualisasi Data")

# ---------- LINE CHART PER VARIABEL ----------
st.subheader("Time Series per Variabel")
variabel = st.selectbox("Pilih variabel:", df.columns.tolist())

fig, ax = plt.subplots(figsize=(10, 4))
fig.patch.set_facecolor("#FFF7F3")
ax.set_facecolor("#FFF7F3")
ax.plot(df.index, df[variabel], color="#E8837D", linewidth=2)
ax.set_title(f"Time Series: {variabel}", color="#5C4742")
ax.set_xlabel("Periode")
ax.set_ylabel(variabel)
ax.grid(alpha=0.25)
st.pyplot(fig)

with st.expander("Lihat ketiga variabel dalam satu grafik"):
    st.line_chart(df)

# ---------- HEATMAP KORELASI ----------
st.subheader("Heatmap Korelasi Antarvariabel")
corr = data["korelasi"]

fig2, ax2 = plt.subplots(figsize=(6, 5))
fig2.patch.set_facecolor("#FFF7F3")
sns.heatmap(corr, annot=True, cmap="RdPu", fmt=".2f", ax=ax2, cbar=True)
st.pyplot(fig2)

st.markdown(
    """
    <p style='font-size:15px; color:#5C4742; max-width:750px;'>
    Nilai korelasi antarvariabel di atas tergolong <b>rendah</b> (0,12&ndash;0,18),
    yang berarti hubungan <i>linear searah waktu</i> antara Inflasi, BI Rate, dan
    harga minyak dunia tidak terlalu kuat. Hal ini <b>tidak bertentangan</b> dengan
    hasil uji kointegrasi Johansen pada Bab 4, karena korelasi Pearson hanya
    mengukur hubungan linear yang terjadi pada periode yang sama, sedangkan
    kointegrasi menangkap hubungan jangka panjang yang melibatkan lag dan proses
    penyesuaian bertahap (Error Correction Term) antarvariabel.
    </p>
    """,
    unsafe_allow_html=True,
)

# ---------- STATISTIK DESKRIPTIF ----------
st.subheader("Statistik Deskriptif")
st.dataframe(data["statistik"].style.format("{:.4f}"), use_container_width=True)