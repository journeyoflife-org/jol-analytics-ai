"""Role-based access control for API, Airflow, and RAG (ISO A.5.15, CC6)."""

from enum import StrEnum

from pydantic import BaseModel


class Role(StrEnum):
    """System roles with ascending privilege levels."""

    VIEWER = "viewer"
    ANALYST = "analyst"
    DATA_SCIENTIST = "data_scientist"
    ADMIN = "admin"


class Permission(StrEnum):
    """Granular permissions assignable to roles."""

    READ_DATA = "read_data"
    WRITE_DATA = "write_data"
    TRAIN_MODEL = "train_model"
    DEPLOY_MODEL = "deploy_model"
    ACCESS_RAG = "access_rag"
    MANAGE_DAGS = "manage_dags"
    VIEW_PII = "view_pii"
    MANAGE_USERS = "manage_users"


# Default role-permission matrix
_ROLE_PERMISSIONS: dict[Role, set[Permission]] = {
    Role.VIEWER: {Permission.READ_DATA, Permission.ACCESS_RAG},
    Role.ANALYST: {Permission.READ_DATA, Permission.WRITE_DATA, Permission.ACCESS_RAG},
    Role.DATA_SCIENTIST: {
        Permission.READ_DATA,
        Permission.WRITE_DATA,
        Permission.TRAIN_MODEL,
        Permission.ACCESS_RAG,
    },
    Role.ADMIN: set(Permission),  # all permissions
}


class AccessDecision(BaseModel):
    """Result of an access control check."""

    allowed: bool
    role: Role
    permission: Permission
    reason: str = ""


def check_access(role: Role, permission: Permission) -> AccessDecision:
    """Evaluate whether a role has the requested permission."""
    allowed = permission in _ROLE_PERMISSIONS.get(role, set())
    return AccessDecision(
        allowed=allowed,
        role=role,
        permission=permission,
        reason=(
            ""
            if allowed
            else f"Role '{role.value}' lacks permission '{permission.value}'"
        ),
    )


def require_access(role: Role, permission: Permission) -> None:
    """Raise PermissionError if role lacks the requested permission."""
    decision = check_access(role, permission)
    if not decision.allowed:
        raise PermissionError(decision.reason)
