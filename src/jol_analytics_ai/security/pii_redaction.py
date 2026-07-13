"""PII detection and redaction utilities for GDPR compliance."""

import re
from typing import Any

# Common PII patterns
_EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
_PHONE_RE = re.compile(r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b")
_SSN_RE = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
_CREDIT_CARD_RE = re.compile(r"\b(?:\d{4}[-\s]?){3}\d{4}\b")

_PII_PATTERNS = [
    ("email", _EMAIL_RE),
    ("phone", _PHONE_RE),
    ("ssn", _SSN_RE),
    ("credit_card", _CREDIT_CARD_RE),
]


def redact_pii(text: str, replacement: str = "[REDACTED]") -> str:
    """Replace all detected PII patterns in text."""
    for _, pattern in _PII_PATTERNS:
        text = pattern.sub(replacement, text)
    return text


def detect_pii(text: str) -> list[dict[str, Any]]:
    """Return list of detected PII occurrences with type and position."""
    findings: list[dict[str, Any]] = []
    for pii_type, pattern in _PII_PATTERNS:
        for match in pattern.finditer(text):
            findings.append(
                {
                    "type": pii_type,
                    "start": match.start(),
                    "end": match.end(),
                    "value": match.group(),
                }
            )
    return findings


def redact_dict(
    data: dict[str, Any],
    replacement: str = "[REDACTED]",
) -> dict[str, Any]:
    """Recursively redact PII from all string values in a dict."""
    result: dict[str, Any] = {}
    for key, value in data.items():
        if isinstance(value, str):
            result[key] = redact_pii(value, replacement)
        elif isinstance(value, dict):
            result[key] = redact_dict(value, replacement)
        elif isinstance(value, list):
            result[key] = [
                (
                    redact_dict(item, replacement)
                    if isinstance(item, dict)
                    else (
                        redact_pii(item, replacement) if isinstance(item, str) else item
                    )
                )
                for item in value
            ]
        else:
            result[key] = value
    return result
