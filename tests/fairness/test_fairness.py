"""Fairness tests: verify bias testing framework works correctly."""

import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier

from jol_analytics_ai.ml.fairness import demographic_parity, equalized_odds


class TestFairnessMetrics:
    def setup_method(self) -> None:
        """Create a simple test dataset with a sensitive attribute."""
        np.random.seed(42)
        n = 200
        self.X = pd.DataFrame(
            {
                "feature1": np.random.randn(n),
                "gender": np.random.choice(["M", "F"], size=n),
            }
        )
        self.y = pd.Series(np.random.choice([0, 1], size=n))
        self.model = DummyClassifier(strategy="most_frequent")
        self.model.fit(self.X[["feature1"]], self.y)

    def test_demographic_parity_returns_all_groups(self) -> None:
        rates = demographic_parity(self.model, self.X, "gender")
        assert "M" in rates
        assert "F" in rates

    def test_equalized_odds_returns_tpr_fpr(self) -> None:
        results = equalized_odds(self.model, self.X, self.y, "gender")
        for group_result in results.values():
            assert "tpr" in group_result
            assert "fpr" in group_result

    def test_rates_are_between_0_and_1(self) -> None:
        rates = demographic_parity(self.model, self.X, "gender")
        for rate in rates.values():
            assert 0.0 <= rate <= 1.0
