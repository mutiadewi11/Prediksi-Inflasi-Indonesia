"""
utils.py
Helper untuk memuat CSS tema, sidebar profil, dan seluruh dataset hasil export
dari Colab. Diimpor oleh Home.py dan semua file di folder pages/.
"""

import base64
import json
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT_DIR = Path(__file__).parent
DATASET_DIR = ROOT_DIR / "dataset"
ASSET_DIR = ROOT_DIR / "assets"
STYLE_PATH = ROOT_DIR / "styles" / "style.css"

NAMA_PENULIS = "Mutia Dewi Prameswari"
FOTO_PROFIL = ASSET_DIR / "foto_mutia-bgred.png"


def load_css():
    """Menyuntikkan style.css ke halaman Streamlit yang sedang aktif."""
    if STYLE_PATH.exists():
        with open(STYLE_PATH, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def render_sidebar_profile():
    """Menampilkan foto profil bulat + nama di bagian bawah sidebar.
    Dipanggil di setiap halaman (Home.py dan semua file di pages/) setelah load_css().
    """
    with st.sidebar:
        st.markdown("---")
        if FOTO_PROFIL.exists():
            encoded = base64.b64encode(FOTO_PROFIL.read_bytes()).decode()
            st.markdown(
                f"""
                <div style="text-align:center; margin-top:4px; padding-bottom:12px;">
                    <img src="data:image/png;base64,{encoded}"
                         style="width:88px; height:88px; border-radius:50%;
                                object-fit:cover; border:3px solid #F4A9A8;" />
                    <p style="margin:8px 0 0 0; font-weight:600; color:#6B4C46;
                              font-size:14px;">{NAMA_PENULIS}</p>
                    <p style="margin:2px 0 0 0; font-size:12px; color:#8A6D66;">
                        51422181
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.caption(f"📸 Tambahkan foto di assets/{FOTO_PROFIL.name}")


@st.cache_data
def load_all_data():
    """Membaca seluruh file CSV & JSON hasil export dari Colab (folder dataset/)."""
    data_historis = pd.read_csv(
        DATASET_DIR / "data_historis.csv", index_col=0, parse_dates=True
    )
    hasil_eval = pd.read_csv(DATASET_DIR / "hasil_evaluasi.csv")
    hasil_perbandingan = pd.read_csv(
        DATASET_DIR / "hasil_perbandingan_model.csv", parse_dates=["Tanggal"]
    )
    prediksi_2026 = pd.read_csv(
        DATASET_DIR / "prediksi_mei_agustus_2026.csv", index_col=0, parse_dates=True
    )
    statistik = pd.read_csv(DATASET_DIR / "statistik_deskriptif.csv", index_col=0)
    korelasi = pd.read_csv(DATASET_DIR / "korelasi.csv", index_col=0)
    feature_importance = pd.read_csv(DATASET_DIR / "feature_importance.csv")

    with open(DATASET_DIR / "informasi_penelitian.json", encoding="utf-8") as f:
        info = json.load(f)

    # Data aktual 2026 sifatnya opsional & bertambah seiring waktu (BI merilis
    # bulanan), jadi dibaca dengan aman agar app tidak error jika file belum ada.
    aktual_path = DATASET_DIR / "aktual_2026.csv"
    if aktual_path.exists():
        aktual_2026 = pd.read_csv(aktual_path, parse_dates=["Tanggal"])
    else:
        aktual_2026 = pd.DataFrame(columns=["Tanggal", "Aktual (%)"])

    return {
        "data_historis": data_historis,
        "hasil_eval": hasil_eval,
        "hasil_perbandingan": hasil_perbandingan,
        "prediksi_2026": prediksi_2026,
        "statistik": statistik,
        "korelasi": korelasi,
        "feature_importance": feature_importance,
        "info": info,
        "aktual_2026": aktual_2026,
    }