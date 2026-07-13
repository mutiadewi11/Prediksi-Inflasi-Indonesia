import matplotlib.pyplot as plt
import streamlit as st

from utils import load_all_data, load_css, render_sidebar_profile

st.set_page_config(page_title="Perbandingan Model", page_icon="📈", layout="wide")
load_css()
render_sidebar_profile()
data = load_all_data()

hasil_eval = data["hasil_eval"]
hasil_perbandingan = data["hasil_perbandingan"]
info = data["info"]

st.title("Perbandingan Model")
st.caption(f"Periode evaluasi: {info['periode']} (data uji: {info['jumlah_data_uji']} observasi)")


def highlight_best(row):
    is_best = row["Model"] == info["model_terbaik"]
    style = "background-color:#FADCD9; font-weight:bold;" if is_best else ""
    return [style for _ in row]


st.subheader("Tabel Evaluasi Model")
st.dataframe(
    hasil_eval.style.apply(highlight_best, axis=1).format(
        {"RMSE": "{:.6f}", "MAE": "{:.6f}", "MAPE": "{:.2f}%"}
    ),
    use_container_width=True,
)
st.success(f"🏆 Model dengan performa terbaik: **{info['model_terbaik']}**")

st.subheader("Grafik Perbandingan Metrik Evaluasi")
warna = ["#F4A9A8", "#E8837D", "#C97C74"]
fig, axes = plt.subplots(1, 3, figsize=(14, 4))
fig.patch.set_facecolor("#FFF7F3")
for ax, metric in zip(axes, ["RMSE", "MAE", "MAPE"]):
    ax.set_facecolor("#FFF7F3")
    ax.bar(hasil_eval["Model"], hasil_eval[metric], color=warna)
    ax.set_title(metric, color="#5C4742")
    ax.tick_params(axis="x", rotation=15)
st.pyplot(fig)

st.subheader("Grafik Aktual vs Prediksi (Data Uji)")
chart_df = hasil_perbandingan.set_index("Tanggal")
st.line_chart(chart_df)

st.subheader("Feature Importance — Random Forest")
feature_importance = data["feature_importance"].sort_values("Importance")
fig2, ax2 = plt.subplots(figsize=(8, 4))
fig2.patch.set_facecolor("#FFF7F3")
ax2.set_facecolor("#FFF7F3")
ax2.barh(feature_importance["Feature"], feature_importance["Importance"], color="#E8837D")
ax2.set_xlabel("Importance")
st.pyplot(fig2)
st.caption(
    "Variabel **Inflasi (%)_lag1** (nilai inflasi satu bulan sebelumnya) memiliki "
    "kontribusi paling dominan dalam prediksi Random Forest, jauh lebih besar "
    "dibandingkan BI Rate maupun harga minyak dunia (log_oil)."
)

st.subheader("Kesimpulan")
st.write(
    """
    Berdasarkan hasil evaluasi menggunakan metrik RMSE, MAE, dan MAPE, model
    **Random Forest** menunjukkan performa prediksi terbaik dibandingkan VAR dan
    VECM, dengan tingkat kesalahan prediksi paling rendah pada data pengujian.
    Meskipun demikian, model **VECM** tetap relevan digunakan untuk menganalisis
    hubungan jangka panjang antarvariabel melalui mekanisme *Error Correction
    Term* (ECT) yang tidak dimiliki oleh Random Forest maupun VAR.
    """
)