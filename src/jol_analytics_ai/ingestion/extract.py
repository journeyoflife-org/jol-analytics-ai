"""Data extraction from external sources with lineage tracking."""

from pathlib import Path
from typing import Any

import pandas as pd

from jol_analytics_ai.logging import get_logger

logger = get_logger(__name__)


def extract_csv(file_path: str | Path) -> pd.DataFrame:
    """Extract data from a CSV file with logging."""
    logger.info("Extracting CSV: %s", file_path)
    df = pd.read_csv(file_path)
    logger.info("Extracted %d rows, %d columns", len(df), len(df.columns))
    return df


def extract_json(file_path: str | Path) -> list[dict[str, Any]]:
    """Extract data from a JSON file."""
    import json

    logger.info("Extracting JSON: %s", file_path)
    with open(file_path, encoding="utf-8") as f:
        data: list[dict[str, Any]] = json.load(f)
    logger.info("Extracted %d records", len(data))
    return data


def extract_sql(query: str, connection_string: str) -> pd.DataFrame:
    """Extract data via SQL query with parameterised connection."""
    from sqlalchemy import create_engine, text

    logger.info("Extracting SQL data")
    engine = create_engine(connection_string)
    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)
    logger.info("Extracted %d rows via SQL", len(df))
    return df
