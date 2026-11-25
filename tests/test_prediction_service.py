"""Unit tests for src.prediction_service.

Owner: Person 2 (Inference & Validation Engineer) — Task P2-05
"""

import pytest

from src.prediction_service import FEATURE_ORDER, predict_strength


def test_feature_order_has_eight_fixed_keys() -> None:
    assert FEATURE_ORDER == [
        "Cement",
        "Slag",
        "FlyAsh",
        "Water",
        "Superplasticizer",
        "CoarseAgg",
        "FineAgg",
        "Age",
    ]


@pytest.mark.skip(reason="Akan diaktifkan setelah P2 mengimplementasikan predict_strength()")
def test_predict_strength_placeholder() -> None:
    sample = {
        "Cement": 540.0,
        "Slag": 0.0,
        "FlyAsh": 0.0,
        "Water": 162.0,
        "Superplasticizer": 2.5,
        "CoarseAgg": 1040.0,
        "FineAgg": 676.0,
        "Age": 28,
    }
    result = predict_strength(sample)
    assert isinstance(result, float)
