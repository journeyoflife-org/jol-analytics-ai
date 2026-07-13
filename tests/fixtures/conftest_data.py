"""Shared pytest fixtures."""

import pandas as pd
import pytest


@pytest.fixture
def sample_dataframe() -> pd.DataFrame:
    """Return a sample DataFrame for testing."""
    return pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Charlie"],
            "email": ["alice@test.com", "bob@test.com", "charlie@test.com"],
            "age": [30, 25, 35],
            "city": ["London", "Paris", "Berlin"],
        }
    )


@pytest.fixture
def sample_pii_text() -> str:
    """Return text containing various PII types."""
    return (
        "Contact John Doe at john.doe@example.com or call 555-123-4567. "
        "SSN: 123-45-6789. Credit card: 4111-1111-1111-1111."
    )
