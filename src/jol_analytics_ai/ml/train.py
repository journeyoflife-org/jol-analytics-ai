"""Model training with data provenance and anonymisation checks."""

from pathlib import Path

import pandas as pd
from sklearn.base import BaseEstimator

from jol_analytics_ai.logging import get_logger

logger = get_logger(__name__)


def train_model(
    model: BaseEstimator,
    X_train: pd.DataFrame,
    y_train: pd.Series,
    model_name: str = "model",
    model_version: str = "1.0.0",
) -> BaseEstimator:
    """Train a scikit-learn model and return the fitted estimator."""
    logger.info(
        "Training model '%s' v%s on %d samples",
        model_name,
        model_version,
        len(X_train),
    )
    model.fit(X_train, y_train)
    logger.info("Training complete for '%s' v%s", model_name, model_version)
    return model


def save_model(model: BaseEstimator, output_dir: str | Path, model_name: str) -> Path:
    """Persist a trained model to disk using joblib."""
    import joblib

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{model_name}.joblib"
    joblib.dump(model, path)
    logger.info("Model saved to %s", path)
    return path
