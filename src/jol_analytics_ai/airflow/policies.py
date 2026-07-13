"""Data governance policies enforced via Airflow DAG policies."""

from dataclasses import dataclass, field
from datetime import timedelta
from enum import StrEnum


class DataClassification(StrEnum):
    """Data sensitivity classification levels."""

    PUBLIC = "public"
    INTERNAL = "internal"
    CONFIDENTIAL = "confidential"
    RESTRICTED = "restricted"


@dataclass
class DataPolicy:
    """Policy definition for data pipeline governance."""

    name: str
    classification: DataClassification
    retention_days: int = 365
    requires_anonymisation: bool = False
    requires_dpia: bool = False
    allowed_roles: list[str] = field(default_factory=lambda: ["admin"])
    max_execution_time: timedelta = timedelta(hours=2)

    def validate(self) -> list[str]:
        """Return list of policy violations."""
        issues: list[str] = []
        if self.classification in (
            DataClassification.CONFIDENTIAL,
            DataClassification.RESTRICTED,
        ):
            if not self.requires_anonymisation:
                issues.append(
                    f"Policy '{self.name}': " "classified data requires anonymisation"
                )
            if (
                self.classification == DataClassification.RESTRICTED
                and not self.requires_dpia
            ):
                issues.append(f"Policy '{self.name}': restricted data requires DPIA")
        return issues


# Pre-defined policies
PII_POLICY = DataPolicy(
    name="pii_processing",
    classification=DataClassification.RESTRICTED,
    requires_anonymisation=True,
    requires_dpia=True,
    allowed_roles=["admin", "data_scientist"],
)

STANDARD_POLICY = DataPolicy(
    name="standard_etl",
    classification=DataClassification.INTERNAL,
)
