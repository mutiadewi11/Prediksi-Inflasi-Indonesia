import streamlit as st

from utils import load_all_data, load_css, render_sidebar_profile

st.set_page_config(
    page_title="Prediksi Inflasi Indonesia",
    page_icon="📈",
    layout="wide",
)
load_css()
render_sidebar_profile()

data = load_all_data()
info = data["info"]

st.markdown(
    "<h1 style='text-align:center;'>📈 Prediksi Inflasi Indonesia</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    f"<h4 style='text-align:center; color:#C97C74;'>{info['judul']}</h4>",
    unsafe_allow_html=True,
)

st.write("")

_, col2, _ = st.columns([1, 2, 1])
with col2:
    st.markdown(
        """
        <div class="kartu-peach">
            <p>👩‍🎓 <b>Disusun oleh:</b> Mutia Dewi Prameswari</p>
            <p>🆔 <b>NPM:</b> 51422181</p>
            <p>👩‍🏫 <b>Dosen Pembimbing:</b> Dr. Elfitrin Syahrul, ST., MT.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
st.markdown(
    """
    <div style='text-align:center; max-width:720px; margin:auto; line-height:1.7;'>
    Website ini menyajikan hasil penelitian mengenai prediksi inflasi di Indonesia
    menggunakan tiga pendekatan model: <b>Vector Autoregression (VAR)</b>,
    <b>Vector Error Correction Model (VECM)</b>, dan <b>Random Forest</b>, dengan
    variabel BI Rate dan harga minyak dunia sebagai variabel penjelas. Jelajahi hasil
    analisis dan prediksi inflasi periode Mei&ndash;Agustus 2026 melalui menu di sisi kiri.
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
_, col2, _ = st.columns([1, 1, 1])
with col2:
    if st.button("Mulai →", use_container_width=True):
        st.switch_page("pages/2_Tentang_Penelitian.py")