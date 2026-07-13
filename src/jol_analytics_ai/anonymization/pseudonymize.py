"""Pseudonymisation utilities for GDPR data minimisation."""

from __future__ import annotations

import hashlib
import hmac
from typing import TYPE_CHECKING

from jol_analytics_ai.config import settings
from jol_analytics_ai.logging import get_logger

if TYPE_CHECKING:
    import pandas as pd

logger = get_logger(__name__)


def pseudonymize(value: str, salt: str | None = None) -> str:
    """Generate a deterministic pseudonym using HMAC-SHA256."""
    salt = salt or settings.secret_key
    return hmac.new(salt.encode(), value.encode(), hashlib.sha256).hexdigest()


def pseudonymize_dataframe(
    df: pd.DataFrame,
    columns: list[str],
    salt: str | None = None,
) -> pd.DataFrame:
    """Pseudonymise specified columns in a DataFrame."""
    import pandas as pd  # noqa: PLC0415

    df = df.copy()
    for col in columns:
        if col in df.columns:
            df[col] = df[col].apply(
                lambda x: pseudonymize(str(x), salt) if pd.notna(x) else x
            )
    logger.info("Pseudonymised columns: %s", columns)
    return df
