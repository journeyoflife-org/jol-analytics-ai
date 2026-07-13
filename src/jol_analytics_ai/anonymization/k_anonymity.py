"""k-Anonymity validation (GDPR data minimisation; minimum k=5)."""

import pandas as pd

from jol_analytics_ai.config import settings
from jol_analytics_ai.logging import get_logger

logger = get_logger(__name__)


def compute_k_anonymity(df: pd.DataFrame, quasi_identifiers: list[str]) -> int:
    """Compute the minimum equivalence class size for quasi-identifier columns.

    Returns the smallest group size — must be >= k (default 5) for compliance.
    """
    if not quasi_identifiers:
        return len(df)
    groups = df.groupby(quasi_identifiers).size()
    k = int(groups.min()) if not groups.empty else 0
    logger.info("k-anonymity value: %d (quasi-identifiers: %s)", k, quasi_identifiers)
    return k


def validate_k_anonymity(
    df: pd.DataFrame,
    quasi_identifiers: list[str],
    k: int | None = None,
) -> bool:
    """Return True if the dataset satisfies k-anonymity for the given k."""
    k = k or settings.anonymization_k_value
    actual_k = compute_k_anonymity(df, quasi_identifiers)
    is_valid = actual_k >= k
    if not is_valid:
        logger.warning(
            "k-anonymity VIOLATION: k=%d < required %d for %s",
            actual_k,
            k,
            quasi_identifiers,
        )
    else:
        logger.info("k-anonymity PASS: k=%d >= %d", actual_k, k)
    return is_valid
