# Panduan Presentasi & Live Demo UAS — ConcreteLab

> **Owner:** Person 4 (QA, Deployment & Presentation Lead) — Task `P4-06`, `P4-07`
> **Durasi:** Maksimal **10 menit presentasi + demo**, dilanjutkan **5 menit Q&A**.
> **Fokus Utama:** Model deployment & live demo aplikasi (modelling/evaluation tidak perlu diulang panjang).

## Pembagian Waktu & Speaker

| Bagian | Durasi | Isi | Speaker |
| :--- | :---: | :--- | :---: |
| 1. Problem & App | 0:45 | Apa yang diprediksi, untuk siapa, mengapa perlu aplikasi | P3 |
| 2. Existing ML -> Artifact | 1:00 | Model existing, joblib serialization, konsistensi preprocessing | P1 |
| 3. Deployment Architecture | 1:00 | Browser -> Streamlit -> inference service -> model artifact | P2 |
| 4. Live Demonstration | 4:00 | Input 8 fitur -> Submit -> Hasil MPa -> Error case -> Reset/Compare | P3 + P2 |
| 5. QA & Operasional | 1:30 | Cara menjalankan, hasil uji TC01–TC12, mitigasi risiko | P4 |
| 6. Limits & Wrap-up | 0:45 | Model hanya estimasi, bukan pengganti uji laboratorium | P1 |
| Buffer | 1:00 | Transisi layar / loading demo | Tim |

## Alur Demo (Single Flow)
1. Perkenalkan ConcreteLab sebagai hasil deployment model UTS.
2. Buka aplikasi Streamlit dan tunjukkan 8 input beserta satuannya.
3. Masukkan contoh golden sample, klik **Prediksi Kuat Tekan**, tampilkan hasil MPa.
4. Uji satu skenario input tidak valid untuk menunjukkan pesan error yang ramah.
5. Reset form (atau tunjukkan fitur compare jika P1 selesai), lalu tutup dengan disclaimer batasan model.

## Fallback Plan
- Jalankan secara lokal (`streamlit run streamlit_app/app.py`) jika koneksi internet bermasalah.
- Siapkan screenshot hasil & rekaman singkat cadangan sebelum hari presentasi.
