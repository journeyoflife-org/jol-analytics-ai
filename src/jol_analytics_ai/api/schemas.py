"""Pydantic schemas for API request/response validation."""

from typing import Any

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health check response."""

    status: str = "healthy"


class InferenceRequest(BaseModel):
    """ML inference request."""

    model_name: str
    model_version: str = "latest"
    features: dict[str, Any] = Field(default_factory=dict)


class InferenceResponse(BaseModel):
    """ML inference response."""

    model_name: str
    predictions: list[Any] = Field(default_factory=list)
    message: str = ""


class RAGQueryRequest(BaseModel):
    """RAG query request."""

    query: str = Field(min_length=3, max_length=2000)
    top_k: int = Field(default=5, ge=1, le=20)
    filters: dict[str, Any] = Field(default_factory=dict)


class RAGQueryResponse(BaseModel):
    """RAG query response."""

    query: str
    results: list[dict[str, Any]] = Field(default_factory=list)
    message: str = ""


class ModelInfo(BaseModel):
    """Model metadata for listing."""

    model_name: str
    version: str
    status: str
    approved: bool
