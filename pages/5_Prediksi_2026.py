import matplotlib.pyplot as plt
import streamlit as st

from utils import load_all_data, load_css, render_sidebar_profile

st.set_page_config(page_title="Prediksi 2026", page_icon="📈", layout="wide")
load_css()
render_sidebar_profile()
data = load_all_data()
prediksi = data["prediksi_2026"]
aktual = data["aktual_2026"]

st.title("Prediksi Inflasi Mei\u2013Agustus 2026")
st.caption(
    "Prediksi dihasilkan dari model yang telah dilatih ulang menggunakan seluruh "
    "data historis (Agustus 2016 \u2013 April 2026)."
)

if not aktual.empty:
    st.subheader("Data Aktual Terbaru dari Bank Indonesia")
    tabel_aktual = prediksi.copy()
    tabel_aktual = tabel_aktual.merge(
        aktual.set_index("Tanggal"), left_index=True, right_index=True, how="left"
    )
    for model in prediksi.columns:
        tabel_aktual[f"Selisih {model}"] = (
            tabel_aktual["Aktual (%)"] - tabel_aktual[model]
        ).abs()

    tampil = tabel_aktual.copy()
    tampil.index = tampil.index.strftime("%B %Y")
    tampil = tampil.round(2)
    # tampilkan tanda (—) untuk bulan yang aktualnya belum tersedia
    tampil = tampil.fillna("—")
    st.dataframe(tampil, use_container_width=True)
    st.caption(
        "Selisih dihitung sebagai |Aktual \u2212 Prediksi|. Semakin kecil nilainya, "
        "semakin akurat prediksi model pada bulan tersebut."
    )
    st.divider()

pilihan = st.radio(
    "Pilih model yang ingin ditampilkan:",
    ["Semua Model", "VAR", "VECM", "Random Forest"],
    horizontal=True,
)

kolom_dipilih = prediksi.columns.tolist() if pilihan == "Semua Model" else [pilihan]

warna = {"VAR": "#F4A9A8", "VECM": "#E8837D", "Random Forest": "#C97C74"}

st.subheader("Grafik Prediksi")
fig, ax = plt.subplots(figsize=(10, 4))
fig.patch.set_facecolor("#FFF7F3")
ax.set_facecolor("#FFF7F3")
for kolom in kolom_dipilih:
    ax.plot(
        prediksi.index,
        prediksi[kolom],
        marker="o",
        linewidth=2,
        label=kolom,
        color=warna.get(kolom, "#C97C74"),
    )
ax.set_xlabel("Periode")
ax.set_ylabel("Inflasi (%)")
ax.legend()
ax.grid(alpha=0.25)
st.pyplot(fig)

st.subheader("Tabel Prediksi (%)")
st.dataframe(prediksi[kolom_dipilih].round(2), use_container_width=True)

st.subheader("Penjelasan")
penjelasan = {
    "VAR": (
        "Model VAR memprediksi inflasi meningkat secara bertahap dari Mei hingga "
        "Agustus 2026, karena seluruh variabel diproyeksikan secara simultan "
        "berdasarkan hubungan dinamis antarvariabel."
    ),
    "VECM": (
        "Model VECM menunjukkan tren peningkatan yang serupa dengan VAR, namun "
        "dengan nilai yang sedikit lebih rendah karena memperhitungkan koreksi "
        "menuju keseimbangan jangka panjang (Error Correction Term)."
    ),
    "Random Forest": (
        "Model Random Forest menghasilkan pola prediksi yang lebih berfluktuasi "
        "karena menggunakan pendekatan recursive forecasting, yaitu hasil prediksi "
        "satu periode digunakan kembali sebagai input lag untuk periode berikutnya, "
        "sementara BI Rate dan harga minyak diasumsikan tetap."
    ),
}

if pilihan == "Semua Model":
    for m, teks in penjelasan.items():
        st.markdown(f"**{m}:** {teks}")
else:
    st.markdown(f"**{pilihan}:** {penjelasan[pilihan]}")

if not aktual.empty:
    bulan_tersedia = ", ".join(aktual["Tanggal"].dt.strftime("%B %Y"))
    st.caption(
        f"Catatan: nilai aktual inflasi sudah tersedia untuk periode {bulan_tersedia}. "
        "Bulan lainnya akan diperbarui seiring tersedianya data resmi dari Bank Indonesia."
    )
else:
    st.caption(
        "Catatan: nilai aktual inflasi untuk periode di atas akan diperbarui "
        "seiring tersedianya data resmi dari Bank Indonesia."
    )