"""Fairness and bias testing for EU AI Act compliance."""

from typing import Any

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator

from jol_analytics_ai.logging import get_logger

logger = get_logger(__name__)


# noinspection PyPep8Naming
def demographic_parity(
    model: BaseEstimator,
    X: pd.DataFrame,
    sensitive_column: str,
    positive_class: int = 1,
) -> dict[str, float]:
    """Compute demographic parity ratio across groups of a sensitive attribute.

    Returns dict mapping group value -> positive prediction rate.
    A fair model has approximately equal rates across groups.
    """
    predictions = model.predict(X)
    groups = X[sensitive_column].unique()
    rates: dict[str, float] = {}
    for group in groups:
        mask = X[sensitive_column] == group
        rate = float(np.mean(predictions[mask] == positive_class))
        rates[str(group)] = rate
    logger.info("Demographic parity for '%s': %s", sensitive_column, rates)
    return rates


# noinspection PyPep8Naming
def equalized_odds(
    model: BaseEstimator,
    X: pd.DataFrame,
    y_true: pd.Series,
    sensitive_column: str,
    positive_class: int = 1,
) -> dict[str, dict[str, float]]:
    """Compute equalized odds: TPR and FPR per sensitive group."""
    predictions = model.predict(X)
    groups = X[sensitive_column].unique()
    results: dict[str, dict[str, float]] = {}
    for group in groups:
        mask = X[sensitive_column] == group
        y_g = y_true[mask]
        p_g = predictions[mask]
        tpr = (
            float(np.mean(p_g[y_g == positive_class] == positive_class))
            if (y_g == positive_class).any()
            else 0.0
        )
        fpr = (
            float(np.mean(p_g[y_g != positive_class] == positive_class))
            if (y_g != positive_class).any()
            else 0.0
        )
        results[str(group)] = {"tpr": tpr, "fpr": fpr}
    logger.info("Equalized odds for '%s': %s", sensitive_column, results)
    return results


# noinspection PyPep8Naming
def fairness_report(
    model: BaseEstimator,
    X: pd.DataFrame,
    y_true: pd.Series,
    sensitive_columns: list[str],
) -> dict[str, Any]:
    """Generate a comprehensive fairness report across sensitive attributes."""
    report: dict[str, Any] = {}
    for col in sensitive_columns:
        report[col] = {
            "demographic_parity": demographic_parity(model, X, col),
            "equalized_odds": equalized_odds(model, X, y_true, col),
        }
    return report
