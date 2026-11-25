# Model Card — ConcreteLab

> **Owner:** Person 1 (ML Model Owner) — Task `P1-01`, `P1-02`, `P1-06`

## 1. Ringkasan Model
- **Nama Model / Pipeline:** *(diisi P1 setelah audit)*
- **Artifact Path:** `ml/artifacts/concrete_pipeline.joblib`
- **Versi Library:** `scikit-learn == ...`, `joblib == ...`, `numpy == ...`, `pandas == ...`
- **Sumber Notebook:** `ml/notebooks/implementation1.ipynb`

## 2. Audit Cepat & Keputusan Kandidat Final (Decision Log)
- **Dataset:** Concrete Compressive Strength (UCI ID 165, I.-C. Yeh 1998)
- **Jumlah Fitur Final:** 8 fitur tetap (`Cement`, `Slag`, `FlyAsh`, `Water`, `Superplasticizer`, `CoarseAgg`, `FineAgg`, `Age`)
- **Catatan Audit (8 vs 13 fitur):** *(diisi P1 — pastikan tidak mencampur versi fitur/metrik)*
- **Strategi Scaling:** *(diisi P1 — wajib dibungkus dalam satu `Pipeline` jika menggunakan MLP/model sensitif skala)*
- **Alasan Pemilihan Kandidat Final:** *(diisi P1)*

## 3. Evaluasi & Parity Check
- **Metrik Evaluasi (Test Set):**
  - R²: `...`
  - MAE: `... MPa`
  - RMSE: `... MPa`
- **Golden Sample Parity Test (Before vs After `joblib.load`):**
  - Sample Input: `{...}`
  - Prediksi Notebook: `... MPa`
  - Prediksi Artifact: `... MPa`
  - Selisih: `...` (Pass jika dalam toleransi floating point)

## 4. Batasan & Penggunaan yang Diizinkan
- Model ini menghasilkan **estimasi** kuat tekan beton (MPa) berdasarkan pola data historis.
- **Tidak boleh** digunakan sebagai pengganti uji tekan laboratorium maupun dasar sertifikasi keselamatan struktur konstruksi.
- Input di luar rentang data latih berpotensi menghasilkan extrapolasi yang kurang akurat.
