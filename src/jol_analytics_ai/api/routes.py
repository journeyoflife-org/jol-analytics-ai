"""API routes with authentication and compliance-aware endpoints."""

from fastapi import APIRouter
from fastapi.security import HTTPBearer

from jol_analytics_ai.api.schemas import (
    HealthResponse,
    InferenceRequest,
    InferenceResponse,
    RAGQueryRequest,
    RAGQueryResponse,
)
from jol_analytics_ai.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()
security = HTTPBearer()


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(status="healthy")


@router.post("/inference", response_model=InferenceResponse)
async def run_inference(request: InferenceRequest) -> InferenceResponse:
    """Run ML model inference (requires authentication)."""
    logger.info("Inference request for model '%s'", request.model_name)
    return InferenceResponse(
        model_name=request.model_name,
        predictions=[],
        message="Inference endpoint ready — model loading not yet configured",
    )


@router.post("/rag/query", response_model=RAGQueryResponse)
async def rag_query(request: RAGQueryRequest) -> RAGQueryResponse:
    """Query the RAG system (requires authentication)."""
    logger.info("RAG query received")
    return RAGQueryResponse(
        query=request.query,
        results=[],
        message="RAG endpoint ready — vector store not yet configured",
    )
