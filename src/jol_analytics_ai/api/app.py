"""FastAPI application with GDPR-compliant middleware."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from jol_analytics_ai import __version__
from jol_analytics_ai.api.routes import router
from jol_analytics_ai.config import settings
from jol_analytics_ai.logging import get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifecycle manager."""
    logger.info("Starting jol-analytics-ai v%s", __version__)
    yield
    logger.info("Shutting down jol-analytics-ai")


app = FastAPI(
    title="JOL Analytics AI",
    description="Analytics, ML & RAG Platform for Journey Of Life",
    version=__version__,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
