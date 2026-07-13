"""Unit tests for JWT authentication."""

from jol_analytics_ai.security.auth import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)


class TestPasswordHashing:
    def test_hash_and_verify(self) -> None:
        password = "secure_password_123"
        hashed = hash_password(password)
        assert verify_password(password, hashed) is True

    def test_wrong_password_fails(self) -> None:
        hashed = hash_password("correct_password")
        assert verify_password("wrong_password", hashed) is False


class TestJWT:
    def test_create_and_decode(self) -> None:
        data = {"sub": "user123", "role": "analyst"}
        token = create_access_token(data)
        decoded = decode_access_token(token)
        assert decoded is not None
        assert decoded["sub"] == "user123"

    def test_invalid_token(self) -> None:
        result = decode_access_token("invalid.token.here")
        assert result is None
