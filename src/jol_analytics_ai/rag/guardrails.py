"""RAG output guardrails: PII filtering and content safety."""

from jol_analytics_ai.logging import get_logger
from jol_analytics_ai.security.pii_redaction import detect_pii, redact_pii

logger = get_logger(__name__)


def apply_guardrails(text: str, redact: bool = True) -> str:
    """Apply output guardrails to RAG-generated text.

    - Detects and optionally redacts PII
    - Logs any detected PII for audit
    """
    findings = detect_pii(text)
    if findings:
        logger.warning(
            "Guardrails: detected %d PII instances in RAG output",
            len(findings),
        )
        if redact:
            text = redact_pii(text)
            logger.info("Guardrails: PII redacted from output")
    return text


def validate_input(query: str) -> tuple[bool, str]:
    """Validate user input before RAG retrieval."""
    if not query or len(query.strip()) < 3:
        return False, "Query too short"
    if len(query) > 2000:
        return False, "Query exceeds maximum length"
    return True, ""
