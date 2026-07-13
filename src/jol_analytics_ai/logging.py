"""Structured logging with PII-safe redaction."""

import logging
import re
import sys

from jol_analytics_ai.config import settings

_EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
_SSN_RE = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
_PII_PATTERNS = [_EMAIL_RE, _SSN_RE]


class PIIRedactingFilter(logging.Filter):
    """Strip obvious PII patterns from log messages before emission."""

    def filter(self, record: logging.LogRecord) -> bool:
        if isinstance(record.msg, str):
            for pattern in _PII_PATTERNS:
                record.msg = pattern.sub("[REDACTED]", record.msg)
        return True


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger with PII redaction."""
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, settings.log_level.upper(), logging.INFO))
    logger.addFilter(PIIRedactingFilter())

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
                datefmt="%Y-%m-%dT%H:%M:%S",
            )
        )
        logger.addHandler(handler)

    return logger
