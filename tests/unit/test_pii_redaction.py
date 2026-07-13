"""Unit tests for PII detection and redaction."""

from jol_analytics_ai.security.pii_redaction import detect_pii, redact_dict, redact_pii


class TestRedactPii:
    def test_redacts_email(self) -> None:
        text = "Contact user@example.com for details"
        result = redact_pii(text)
        assert "user@example.com" not in result
        assert "[REDACTED]" in result

    def test_redacts_ssn(self) -> None:
        text = "SSN: 123-45-6789"
        result = redact_pii(text)
        assert "123-45-6789" not in result

    def test_redacts_phone(self) -> None:
        text = "Call 555-123-4567"
        result = redact_pii(text)
        assert "555-123-4567" not in result

    def test_no_pii_unchanged(self) -> None:
        text = "This is a clean string with no PII"
        assert redact_pii(text) == text


class TestDetectPii:
    def test_detects_email(self) -> None:
        findings = detect_pii("Email: admin@jol.org")
        assert any(f["type"] == "email" for f in findings)

    def test_empty_text(self) -> None:
        assert detect_pii("") == []


class TestRedactDict:
    def test_redacts_nested_dict(self) -> None:
        data = {"user": {"email": "test@test.com", "name": "John"}}
        result = redact_dict(data)
        assert "test@test.com" not in result["user"]["email"]

    def test_preserves_non_string_values(self) -> None:
        data = {"count": 42, "active": True}
        result = redact_dict(data)
        assert result == data
