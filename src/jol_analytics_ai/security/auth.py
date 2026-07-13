"""JWT-based authentication for API and inference endpoints (CC6.1)."""

from datetime import UTC, datetime, timedelta
from typing import Any

from jose import JWTError, jwt
from passlib.context import CryptContext

from jol_analytics_ai.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


_BCRYPT_MAX_BYTES = 72


def _validate_password_length(password: str) -> None:
    """Raise ValueError if password exceeds bcrypt's 72-byte limit."""
    if len(password.encode("utf-8")) > _BCRYPT_MAX_BYTES:
        raise ValueError(f"Password exceeds bcrypt's {_BCRYPT_MAX_BYTES}-byte limit.")


def hash_password(password: str) -> str:
    """Hash a plaintext password."""
    _validate_password_length(password)
    return pwd_context.hash(password)  # type: ignore[no-any-return]


def verify_password(plain: str, hashed: str) -> bool:
    """Verify a plaintext password against its hash."""
    _validate_password_length(plain)
    return pwd_context.verify(plain, hashed)  # type: ignore[no-any-return]


def create_access_token(
    data: dict[str, Any],
    expires_delta: timedelta | None = None,
) -> str:
    """Create a signed JWT access token."""
    to_encode = data.copy()
    expire = datetime.now(UTC) + (
        expires_delta or timedelta(minutes=settings.access_token_expire_minutes)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)  # type: ignore[no-any-return]


def decode_access_token(token: str) -> dict[str, Any] | None:
    """Decode and validate a JWT token. Returns payload or None."""
    try:
        payload: dict[str, Any] = jwt.decode(
            token, settings.secret_key, algorithms=[settings.algorithm]
        )
        return payload
    except JWTError:
        return None
