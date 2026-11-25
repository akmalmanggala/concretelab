# ConcreteLab

Aplikasi web berbasis **Streamlit** untuk memprediksi **kuat tekan beton (*Concrete Compressive Strength*, MPa)** berdasarkan 8 parameter komposisi campuran dan umur pengujian. Proyek ini merupakan kelanjutan proyek UTS mata kuliah **Praktikum Penambangan Data (PPD)** — D4 TRPL SV UGM.

> **Disclaimer:** Hasil prediksi dari ConcreteLab bersifat **estimasi berbasis model Machine Learning** untuk keperluan edukasi dan eksplorasi skenario, **bukan pengganti uji laboratorium** maupun alat sertifikasi kelayakan struktur konstruksi.

---

## Arsitektur Aplikasi (3 Lapis)

```text
Browser -> Streamlit UI (streamlit_app/app.py)
        -> Inference & Validation (src/prediction_service.py)
        -> Saved ML Artifact (ml/artifacts/concrete_pipeline.joblib)
```

---

## Struktur Repository

```text
concretelab/
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── inference_contract.md
│   └── UAS_DEMO.md
├── ml/
│   ├── artifacts/                # Menyimpan concrete_pipeline.joblib (P1)
│   ├── notebooks/
│   │   └── implementation1.ipynb # Notebook acuan UTS
│   └── model_card.md             # Dokumentasi audit model & batasan (P1)
├── src/
│   ├── __init__.py
│   └── prediction_service.py     # Kontrak predict_strength() & validasi (P2)
├── streamlit_app/
│   └── app.py                    # Aplikasi web Streamlit (P3)
├── tests/
│   ├── test_acceptance.md        # Matriks QA TC01-TC12 (P4)
│   └── test_prediction_service.py # Unit tests pytest (P2)
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Kontrak 8 Fitur Tetap

| Urutan | Key Python | Label Pengguna | Satuan & Validasi |
| :---: | :--- | :--- | :--- |
| 1 | `Cement` | Semen | kg/m³ (`>= 0`) |
| 2 | `Slag` | Blast furnace slag | kg/m³ (`>= 0`) |
| 3 | `FlyAsh` | Fly ash | kg/m³ (`>= 0`) |
| 4 | `Water` | Air | kg/m³ (`>= 0`) |
| 5 | `Superplasticizer` | Superplasticizer | kg/m³ (`>= 0`) |
| 6 | `CoarseAgg` | Agregat kasar | kg/m³ (`>= 0`) |
| 7 | `FineAgg` | Agregat halus | kg/m³ (`>= 0`) |
| 8 | `Age` | Umur pengujian | hari (integer `> 0`) |

---

## Cara Menjalankan (Local Setup)

### 1. Clone Repository
```bash
git clone https://github.com/akmalmanggala/concretelab.git
cd concretelab
```

### 2. Buat & Aktifkan Virtual Environment
**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi Streamlit
```bash
streamlit run streamlit_app/app.py
```

### 5. Jalankan Automated Tests
```bash
pytest
```

---

## Pembagian Tim & Git Workflow

| Role | PIC | Branch Tugas | Fokus Utama |
| :--- | :--- | :--- | :--- |
| **Person 1** — ML Model Owner | *(isi nama)* | `feat/P1-model-artifact` | Audit notebook, serialize pipeline (`.joblib`), parity test, `model_card.md` |
| **Person 2** — Inference & Validation Engineer | *(isi nama)* | `feat/P2-inference` | Kontrak `predict_strength()`, validasi input, integrasi artifact, unit tests |
| **Person 3** — Streamlit & UX Engineer | *(isi nama)* | `feat/P3-streamlit-ui` | Form 8 input (`st.form`), integrasi service, error handling, UX |
| **Person 4** — QA, Deployment & Presentation Lead | *(isi nama)* | `feat/P4-testing-demo` | Repo setup, test plan (TC01–TC12), manual QA, README, slide & demo 10 menit |

### Aturan Kolaborasi Git
1. Kerjakan tugas pada branch masing-masing (`feat/P1-...`, dst.) — **jangan push langsung ke `main`**.
2. Buat **1 Pull Request (PR)** per task atau kelompok task terkait dengan mengisi template PR.
3. Minimal **1 reviewer** dari anggota lain sebelum merge ke `main`, terutama untuk perubahan kontrak, pipeline, atau alur UI.
4. Jangan commit secrets, `.env`, atau file sementara yang tidak diperlukan.
