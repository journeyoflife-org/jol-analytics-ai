"""Data loading to storage targets with audit logging."""

from pathlib import Path

import pandas as pd

from jol_analytics_ai.logging import get_logger

logger = get_logger(__name__)


def load_csv(df: pd.DataFrame, output_path: str | Path) -> Path:
    """Write DataFrame to CSV with audit log entry."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    logger.info("Loaded %d rows to %s", len(df), path)
    return path


def load_sql(df: pd.DataFrame, table_name: str, connection_string: str) -> None:
    """Load DataFrame to SQL table."""
    from sqlalchemy import create_engine

    logger.info("Loading %d rows to table '%s'", len(df), table_name)
    engine = create_engine(connection_string)
    df.to_sql(table_name, engine, if_exists="append", index=False)
    logger.info("SQL load complete: %s", table_name)
