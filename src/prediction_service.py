"""Inference and input validation service for ConcreteLab.

Owner: Person 2 (Inference & Validation Engineer)
Tasks: P2-02, P2-03, P2-04, P2-07
"""

from pathlib import Path
from typing import Any

FEATURE_ORDER: list[str] = [
    "Cement",
    "Slag",
    "FlyAsh",
    "Water",
    "Superplasticizer",
    "CoarseAgg",
    "FineAgg",
    "Age",
]

DEFAULT_ARTIFACT_PATH = (
    Path(__file__).resolve().parent.parent / "ml" / "artifacts" / "concrete_pipeline.joblib"
)


def predict_strength(payload: dict[str, Any]) -> float:
    """Predict concrete compressive strength (MPa) from 8 fixed features.

    Args:
        payload: Dictionary containing all 8 required keys in FEATURE_ORDER.

    Returns:
        Predicted compressive strength in MPa as a float.

    Raises:
        ValueError: If required fields are missing or values fail validation.
        FileNotFoundError: If the model artifact is not found.
    """
    raise NotImplementedError(
        "predict_strength() belum diimplementasikan. Dikerjakan oleh P2 (task P2-02 s.d. P2-04)."
    )
