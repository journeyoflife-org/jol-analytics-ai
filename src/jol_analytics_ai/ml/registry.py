"""Model registry with versioning for SOC 2 CC8 change management."""

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from pydantic import BaseModel

from jol_analytics_ai.logging import get_logger

logger = get_logger(__name__)


class ModelRecord(BaseModel):
    """Metadata record for a registered model version."""

    model_name: str
    version: str
    artifact_path: str
    metrics: dict[str, float] = {}
    training_data_hash: str = ""
    created_at: str = ""
    approved: bool = False
    approved_by: str = ""
    model_card_path: str = ""


class ModelRegistry:
    """File-based model registry with version tracking."""

    def __init__(self, registry_dir: str | Path) -> None:
        self.registry_dir = Path(registry_dir)
        self.registry_dir.mkdir(parents=True, exist_ok=True)
        self._index_path = self.registry_dir / "registry.json"

    def _load_index(self) -> list[dict[str, Any]]:
        if self._index_path.exists():
            return json.loads(self._index_path.read_text())  # type: ignore[no-any-return]
        return []

    def _save_index(self, index: list[dict[str, Any]]) -> None:
        self._index_path.write_text(json.dumps(index, indent=2))

    def register(self, record: ModelRecord) -> None:
        """Register a new model version."""
        if not record.created_at:
            record.created_at = datetime.now(UTC).isoformat()
        index = self._load_index()
        index.append(record.model_dump())
        self._save_index(index)
        logger.info("Registered model '%s' v%s", record.model_name, record.version)

    def get_latest(self, model_name: str) -> ModelRecord | None:
        """Get the latest registered version of a model."""
        index = self._load_index()
        matches = [r for r in index if r["model_name"] == model_name]
        if not matches:
            return None
        return ModelRecord(**matches[-1])

    def list_models(self) -> list[ModelRecord]:
        """List all registered models."""
        return [ModelRecord(**r) for r in self._load_index()]
