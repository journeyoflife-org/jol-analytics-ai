"""Text chunking strategies for RAG document ingestion."""

from jol_analytics_ai.logging import get_logger

logger = get_logger(__name__)


def chunk_text(
    text: str,
    chunk_size: int = 512,
    overlap: int = 64,
) -> list[str]:
    """Split text into overlapping chunks by character count."""
    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    logger.info(
        "Chunked text into %d chunks (size=%d, overlap=%d)",
        len(chunks),
        chunk_size,
        overlap,
    )
    return chunks


def chunk_by_paragraphs(text: str, min_length: int = 50) -> list[str]:
    """Split text by paragraphs, filtering short ones."""
    paragraphs = [p.strip() for p in text.split("\n\n") if len(p.strip()) >= min_length]
    logger.info(
        "Paragraph chunking: %d chunks (min_length=%d)",
        len(paragraphs),
        min_length,
    )
    return paragraphs
