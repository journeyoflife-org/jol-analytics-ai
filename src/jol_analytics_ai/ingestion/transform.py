"""Data transformation with PII-aware processing."""

import pandas as pd

from jol_analytics_ai.logging import get_logger
from jol_analytics_ai.security.pii_redaction import redact_pii

logger = get_logger(__name__)


def clean_nulls(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """Drop columns with null ratio above threshold, fill remaining nulls."""
    null_ratios = df.isnull().mean()
    drop_cols = null_ratios[null_ratios > threshold].index.tolist()
    logger.info("Dropping %d columns with >%s null ratio", len(drop_cols), threshold)
    df = df.drop(columns=drop_cols)
    return df.ffill().bfill()


def redact_pii_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Redact PII from specified string columns."""
    df = df.copy()
    for col in columns:
        if col in df.columns and df[col].dtype == object:
            df[col] = df[col].apply(lambda x: redact_pii(str(x)) if pd.notna(x) else x)
    logger.info("PII redaction applied to columns: %s", columns)
    return df


def normalize_text(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Lowercase and strip whitespace from text columns."""
    df = df.copy()
    for col in columns:
        if col in df.columns and df[col].dtype == object:
            df[col] = df[col].str.strip().str.lower()
    return df
