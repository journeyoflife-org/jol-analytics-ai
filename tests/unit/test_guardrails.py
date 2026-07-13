"""Unit tests for RAG guardrails."""

from jol_analytics_ai.rag.guardrails import apply_guardrails, validate_input


class TestGuardrails:
    def test_redacts_pii_in_output(self) -> None:
        text = "User email is admin@jol.org and phone is 555-123-4567"
        result = apply_guardrails(text, redact=True)
        assert "admin@jol.org" not in result

    def test_clean_text_unchanged(self) -> None:
        text = "This is a clean response with no PII"
        result = apply_guardrails(text)
        assert result == text


class TestValidateInput:
    def test_valid_query(self) -> None:
        valid, msg = validate_input("What is the meaning of life?")
        assert valid is True

    def test_short_query_rejected(self) -> None:
        valid, msg = validate_input("ab")
        assert valid is False

    def test_empty_query_rejected(self) -> None:
        valid, msg = validate_input("")
        assert valid is False
