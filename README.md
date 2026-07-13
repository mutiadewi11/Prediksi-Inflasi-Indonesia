# Prediksi Inflasi Indonesia — Dashboard Streamlit

Dashboard hasil penelitian skripsi: perbandingan model VAR, VECM, dan Random Forest
untuk prediksi inflasi Indonesia.

## Cara menjalankan secara lokal

```bash
pip install -r requirements.txt
streamlit run Home.py
```

## Sebelum dijalankan, pastikan:

1. Folder `dataset/` sudah berisi file hasil export dari Colab:
   - data_historis.csv
   - hasil_evaluasi.csv
   - hasil_perbandingan_model.csv
   - prediksi_mei_agustus_2026.csv
   - statistik_deskriptif.csv
   - korelasi.csv
   - feature_importance.csv
   - informasi_penelitian.json
   - aktual_2026.csv (opsional — berisi Tanggal & Aktual (%) untuk bulan yang datanya sudah dirilis BI)
2. Folder `assets/` sudah berisi:
   - `metode_penelitian.png` (gambar alur penelitian)
   - `foto_mutia-bgred.png` (foto profil bulat di sidebar)
3. Isi NPM dan nama dosen pembimbing di `Home.py` (cari tanda `[isi ...]`).
4. Tombol "Deploy" saat run lokal sudah disembunyikan lewat `.streamlit/config.toml`
   (otomatis hilang juga setelah di-deploy ke Streamlit Cloud).

## Struktur folder

```
SKRIPSI_STREAMLIT/
├── Home.py                    # Halaman Home (entry point)
├── utils.py                   # Helper load CSS, sidebar profil, & data
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml            # Sembunyikan tombol Deploy, atur tema warna
├── dataset/                   # CSV & JSON hasil export dari Colab
├── assets/
│   ├── metode_penelitian.png
│   └── foto_mutia-bgred.png
├── styles/
│   └── style.css
└── pages/
    ├── 2_Tentang_Penelitian.py
    ├── 3_Visualisasi_Data.py
    ├── 4_Perbandingan_Model.py
    └── 5_Prediksi_2026.py
```

## Deploy ke Streamlit Community Cloud

1. Push seluruh folder ini (termasuk folder `.streamlit/`) ke repository GitHub.
2. Buka https://share.streamlit.io, login dengan akun GitHub.
3. Klik "New app" → pilih repo ini → main file `Home.py` → Deploy.