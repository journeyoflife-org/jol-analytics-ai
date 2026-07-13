"""RAG retrieval from vector store with access control."""

from typing import Any

from jol_analytics_ai.config import settings
from jol_analytics_ai.logging import get_logger
from jol_analytics_ai.rag.embeddings import EmbeddingService

logger = get_logger(__name__)


class RetrievalService:
    """Semantic retrieval from ChromaDB vector store."""

    def __init__(
        self,
        embedding_service: EmbeddingService | None = None,
        collection_name: str | None = None,
    ) -> None:
        self.embedding_service = embedding_service or EmbeddingService()
        self.collection_name = collection_name or settings.chroma_collection
        self._client: Any = None
        self._collection: Any = None

    def _get_collection(self) -> Any:
        import chromadb

        if self._collection is None:
            self._client = chromadb.HttpClient(
                host=settings.chroma_host, port=settings.chroma_port
            )
            self._collection = self._client.get_or_create_collection(
                self.collection_name
            )
        return self._collection

    def retrieve(self, query: str, top_k: int = 5) -> list[dict[str, Any]]:
        """Retrieve top-k relevant documents for a query."""
        query_embedding = self.embedding_service.embed_single(query)
        collection = self._get_collection()
        results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
        documents = []
        if results and results.get("documents"):
            for i, doc in enumerate(results["documents"][0]):
                metadata = (
                    results["metadatas"][0][i] if results.get("metadatas") else {}
                )
                documents.append({"content": doc, "metadata": metadata})
        logger.info("Retrieved %d documents for query", len(documents))
        return documents

    def add_documents(
        self, documents: list[str], metadatas: list[dict[str, Any]], ids: list[str]
    ) -> None:
        """Add documents to the vector store."""
        embeddings = self.embedding_service.embed(documents)
        collection = self._get_collection()
        collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids,
        )
        logger.info("Added %d documents to vector store", len(documents))
