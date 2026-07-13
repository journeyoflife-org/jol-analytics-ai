"""Validation utilities for anonymisation compliance."""

from dataclasses import dataclass

import pandas as pd

from jol_analytics_ai.anonymization.k_anonymity import (
    compute_k_anonymity,
)
from jol_analytics_ai.config import settings
from jol_analytics_ai.logging import get_logger

logger = get_logger(__name__)


@dataclass
class AnonymisationReport:
    """Report on the anonymisation status of a dataset."""

    k_value: int
    k_required: int
    k_valid: bool
    quasi_identifiers: list[str]
    row_count: int
    equivalence_classes: int


def generate_anonymisation_report(
    df: pd.DataFrame,
    quasi_identifiers: list[str],
    k: int | None = None,
) -> AnonymisationReport:
    """Generate a comprehensive anonymisation compliance report."""
    k = k or settings.anonymization_k_value
    k_value = compute_k_anonymity(df, quasi_identifiers)
    groups = (
        df.groupby(quasi_identifiers).size()
        if quasi_identifiers
        else pd.Series([len(df)])
    )

    return AnonymisationReport(
        k_value=k_value,
        k_required=k,
        k_valid=k_value >= k,
        quasi_identifiers=quasi_identifiers,
        row_count=len(df),
        equivalence_classes=len(groups),
    )
