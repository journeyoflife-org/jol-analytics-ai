"""Embedding generation for RAG with model versioning."""

from typing import Any

from jol_analytics_ai.config import settings
from jol_analytics_ai.logging import get_logger

logger = get_logger(__name__)


class EmbeddingService:
    """Wraps sentence-transformers for consistent embedding generation."""

    def __init__(self, model_name: str | None = None) -> None:
        self.model_name = model_name or settings.embedding_model
        self._model: Any = None

    def _load_model(self) -> Any:
        from sentence_transformers import SentenceTransformer

        if self._model is None:
            logger.info("Loading embedding model: %s", self.model_name)
            self._model = SentenceTransformer(self.model_name)
        return self._model

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Generate embeddings for a list of texts."""
        model = self._load_model()
        embeddings = model.encode(texts, show_progress_bar=False)
        logger.info("Generated %d embeddings", len(embeddings))
        return embeddings.tolist()  # type: ignore[no-any-return]

    def embed_single(self, text: str) -> list[float]:
        """Generate embedding for a single text."""
        return self.embed([text])[0]
