"""Vector store access controls for RAG (CC6 logical access)."""

from typing import Any

from jol_analytics_ai.logging import get_logger
from jol_analytics_ai.security.access_control import Permission, Role, check_access

logger = get_logger(__name__)


class VectorAccessController:
    """Enforce role-based access to vector store operations."""

    @staticmethod
    def check_read(role: Role) -> bool:
        """Check if role can read from the vector store."""
        decision = check_access(role, Permission.ACCESS_RAG)
        if not decision.allowed:
            logger.warning("Vector store READ denied for role '%s'", role.value)
        return decision.allowed

    @staticmethod
    def check_write(role: Role) -> bool:
        """Check if role can write to the vector store."""
        decision = check_access(role, Permission.WRITE_DATA)
        if not decision.allowed:
            logger.warning("Vector store WRITE denied for role '%s'", role.value)
        return decision.allowed

    @staticmethod
    def filter_by_tenant(
        results: list[dict[str, Any]], tenant_id: str
    ) -> list[dict[str, Any]]:
        """Filter retrieval results by tenant for multi-tenant isolation."""
        return [
            r for r in results if r.get("metadata", {}).get("tenant_id") == tenant_id
        ]
