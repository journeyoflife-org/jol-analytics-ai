"""Security tests: PII must not appear in logs or outputs without redaction."""

from jol_analytics_ai.security.pii_redaction import detect_pii, redact_pii


class TestPIIInOutputs:
    def test_all_pii_types_redacted(self) -> None:
        text = (
            "User john@doe.com with SSN 123-45-6789 and "
            "card 4111-1111-1111-1111 called 555-867-5309"
        )
        result = redact_pii(text)
        assert "john@doe.com" not in result
        assert "123-45-6789" not in result
        assert "4111-1111-1111-1111" not in result
        assert "555-867-5309" not in result


class TestPIIDetection:
    def test_detects_all_types(self) -> None:
        text = "email: a@b.com, ssn: 111-22-3333, cc: 4444-5555-6666-7777"
        findings = detect_pii(text)
        types_found = {f["type"] for f in findings}
        assert "email" in types_found
        assert "ssn" in types_found
        assert "credit_card" in types_found
