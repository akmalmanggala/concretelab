# Acceptance Test Matrix — ConcreteLab

> **Owner:** Person 4 (QA, Deployment & Presentation Lead) — Task `P4-02`, `P4-04`

## Golden Sample
*(Diisi bersama P1 & P2 setelah artifact final dibekukan)*
- **Payload:** `{ "Cement": ..., "Slag": ..., "FlyAsh": ..., "Water": ..., "Superplasticizer": ..., "CoarseAgg": ..., "FineAgg": ..., "Age": ... }`
- **Expected Output (MPa):** `...`

## Minimal Test Matrix (TC01–TC12)

| ID | Test Case | Expected Result | Owner | Status | Catatan |
| :---: | :--- | :--- | :---: | :---: | :--- |
| TC01 | Semua 8 input valid | Result float MPa dan bukan nilai mock | P2+P4 | [ ] | |
| TC02 | Input sama ke service dan Streamlit | Prediksi sama sesuai pembulatan yang ditampilkan | P1+P4 | [ ] | |
| TC03 | Missing input / field tidak valid | Pesan validasi jelas, tidak crash | P2+P4 | [ ] | |
| TC04 | String / NaN / Inf pada service | Ditolak dengan controlled error | P2 | [ ] | |
| TC05 | Nilai bahan negatif | Ditolak dengan penjelasan | P2+P3 | [ ] | |
| TC06 | `Age <= 0` atau non-integer | Ditolak / dibatasi dengan jelas | P2+P3 | [ ] | |
| TC07 | `Slag` / `FlyAsh` / `Superplasticizer` = 0 | Tetap diterima bila input lain valid | P1+P2 | [ ] | |
| TC08 | Reset form | Kembali ke nilai contoh | P3+P4 | [ ] | |
| TC09 | Model artifact hilang | App menampilkan error terbaca, tidak raw traceback | P2+P4 | [ ] | |
| TC10 | Fresh clone / restart | Run sesuai README, tanpa retraining | P4 | [ ] | |
| TC11 | Demo tanpa internet | Fallback lokal dapat dijalankan | P4 | [ ] | |
| TC12 | Pernyataan batasan | Aplikasi tidak menjanjikan kelayakan konstruksi | P1+P3 | [ ] | |
