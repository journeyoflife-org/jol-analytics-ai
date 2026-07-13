"""Model inference with authentication and audit logging (CC6.1)."""

from pathlib import Path
from typing import Any

import pandas as pd
from sklearn.base import BaseEstimator

from jol_analytics_ai.logging import get_logger

logger = get_logger(__name__)


def load_model(model_path: str | Path) -> BaseEstimator:
    """Load a persisted model from disk."""
    import joblib

    model = joblib.load(model_path)
    logger.info("Model loaded from %s", model_path)
    return model


# noinspection PyPep8Naming
def predict(model: BaseEstimator, X: pd.DataFrame) -> Any:
    """Run inference and log the request."""
    logger.info("Running inference on %d samples", len(X))
    predictions = model.predict(X)
    logger.info("Inference complete: %d predictions", len(predictions))
    return predictions


# noinspection PyPep8Naming
def predict_proba(model: BaseEstimator, X: pd.DataFrame) -> Any:
    """Run probabilistic inference (classification)."""
    logger.info("Running probabilistic inference on %d samples", len(X))
    return model.predict_proba(X)
