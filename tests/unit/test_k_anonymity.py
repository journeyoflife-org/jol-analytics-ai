"""Unit tests for k-anonymity validation."""

import pandas as pd

from jol_analytics_ai.anonymization.k_anonymity import (
    compute_k_anonymity,
    validate_k_anonymity,
)


class TestKAnonymity:
    def test_computes_k_correctly(self) -> None:
        df = pd.DataFrame(
            {
                "age": [25, 25, 25, 30, 30, 30],
                "city": ["A", "A", "A", "B", "B", "B"],
            }
        )
        k = compute_k_anonymity(df, ["age", "city"])
        assert k == 3

    def test_validates_passing_k(self) -> None:
        df = pd.DataFrame(
            {
                "age": [25] * 10,
                "city": ["A"] * 10,
            }
        )
        assert validate_k_anonymity(df, ["age", "city"], k=5) is True

    def test_validates_failing_k(self) -> None:
        df = pd.DataFrame(
            {
                "age": [25, 25, 30, 35],
                "city": ["A", "A", "B", "C"],
            }
        )
        assert validate_k_anonymity(df, ["age", "city"], k=5) is False

    def test_empty_quasi_identifiers(self) -> None:
        df = pd.DataFrame({"x": [1, 2, 3]})
        k = compute_k_anonymity(df, [])
        assert k == 3
