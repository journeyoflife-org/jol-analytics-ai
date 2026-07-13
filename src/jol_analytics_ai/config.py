"""Application configuration with GDPR-compliant defaults."""

from pathlib import Path
from typing import Any

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Central configuration loaded from environment / .env file."""

    # Application
    app_name: str = "jol-analytics-ai"
    environment: str = "development"
    debug: bool = False
    log_level: str = "INFO"

    # Database
    database_url: str = "postgresql://localhost:5432/jol_analytics"

    # Security
    secret_key: str = "CHANGE_ME"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # ML
    model_registry_path: Path = Path("./artifacts/models")
    model_version: str = "1.0.0"

    # RAG
    chroma_host: str = "localhost"
    chroma_port: int = 8000
    chroma_collection: str = "jol_documents"
    embedding_model: str = "all-MiniLM-L6-v2"

    # GDPR
    anonymization_k_value: int = 5
    pii_detection_enabled: bool = True
    data_retention_days: int = 365

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    allowed_origins: list[str] = []

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        if self.environment != "development" and self.secret_key == "CHANGE_ME":
            raise ValueError(
                "SECRET_KEY must be set to a non-default value in "
                f"'{self.environment}' environment"
            )


settings = Settings()
