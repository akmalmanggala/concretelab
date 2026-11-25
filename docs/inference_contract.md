# Inference Contract — ConcreteLab

> **Owner:** Person 2 (bersama P1 & P3) — Task `P2-01`

## Function Signature
```python
predict_strength(payload: dict) -> float
```

## Input Keys (Urutan Wajib Sesuai Training)
1. `Cement` — float (`>= 0`, kg/m³)
2. `Slag` — float (`>= 0`, kg/m³; nilai `0` valid)
3. `FlyAsh` — float (`>= 0`, kg/m³; nilai `0` valid)
4. `Water` — float (`>= 0`, kg/m³)
5. `Superplasticizer` — float (`>= 0`, kg/m³; nilai `0` valid)
6. `CoarseAgg` — float (`>= 0`, kg/m³)
7. `FineAgg` — float (`>= 0`, kg/m³)
8. `Age` — int (`> 0`, hari)

## Output
- `float`: Estimasi kuat tekan beton dalam satuan **MPa**.

## Error Handling Rules
- Missing key -> `ValueError` dengan nama field yang kurang.
- Non-numeric / `NaN` / `Inf` -> `ValueError` dengan pesan ramah.
- Nilai bahan `< 0` -> `ValueError`.
- `Age <= 0` atau bukan bilangan bulat -> `ValueError`.
- Artifact tidak ditemukan -> `FileNotFoundError` dengan pesan jelas (UI tidak boleh menampilkan raw traceback).
