from pathlib import Path

import streamlit as st

from utils import load_all_data, load_css, render_sidebar_profile

st.set_page_config(page_title="Tentang Penelitian", page_icon="📈", layout="wide")
load_css()
render_sidebar_profile()
data = load_all_data()
info = data["info"]

st.title("Tentang Penelitian")

st.subheader("Latar Belakang")
st.write(
    """
    Inflasi merupakan fenomena kenaikan harga barang dan jasa secara umum yang
    berlangsung terus-menerus dalam jangka waktu tertentu. Pergerakan inflasi di
    Indonesia dipengaruhi oleh berbagai faktor, di antaranya BI Rate sebagai
    instrumen kebijakan moneter dan harga minyak dunia yang memengaruhi biaya
    produksi serta distribusi barang.
    """
)

st.subheader("Tujuan Penelitian")
st.write(
    """
    Mengimplementasikan dan membandingkan performa model **VAR**, **VECM**, dan
    **Random Forest** dalam memprediksi inflasi di Indonesia berdasarkan metrik
    evaluasi RMSE, MAE, dan MAPE, kemudian menyajikan hasil prediksi periode
    Mei&ndash;Agustus 2026 melalui aplikasi berbasis Streamlit.
    """
)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Variabel Penelitian")
    st.markdown(
        """
        - Inflasi (%) — variabel dependen
        - BI Rate (%) — variabel independen
        - Harga Minyak Dunia (log_oil) — variabel independen
        """
    )
with col2:
    st.subheader("Model yang Digunakan")
    daftar_model_md = "\n".join(f"- {m}" for m in info["model"])
    st.markdown(daftar_model_md)

st.subheader("Alur Penelitian")
img_path = Path(__file__).parent.parent / "assets" / "metode_penelitian.png"
if img_path.exists():
    st.image(str(img_path), use_container_width=True)
else:
    st.info(
        "📌 Tambahkan gambar alur penelitian di assets/metode_penelitian.png "
        "agar tampil di sini."
    )

col1, col2 = st.columns(2)
with col1:
    st.subheader("Tools yang Digunakan")
    st.markdown(
        """
        - Python
        - statsmodels
        - scikit-learn
        - Streamlit
        """
    )
with col2:
    st.subheader("Sumber Data")
    st.markdown(
        """
        - [Bank Indonesia (BI)](https://www.bi.go.id/id/default.aspx)
        - [U.S. Energy Information Administration (EIA) — Europe Brent Spot Price](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=pet&s=rbrte&f=m)
        """
    )

st.markdown(
    f"""
    <p style='font-size:16px; color:#5C4742; margin-top:8px;'>
    <b>Periode data:</b> {info['periode']} ({info['jumlah_observasi']} observasi bulanan)
    — data latih {info['jumlah_data_latih']} observasi,
    data uji {info['jumlah_data_uji']} observasi.
    </p>
    """,
    unsafe_allow_html=True,
)