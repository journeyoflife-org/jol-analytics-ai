#!/usr/bin/env python3
"""Run PII audit on datasets before ML training.

Usage:
    python scripts/run-pii-audit.py [--ci-mode] [--path PATH]
"""

import argparse
import sys
from pathlib import Path


def audit_file(file_path: Path) -> list[dict]:
    """Scan a file for PII patterns."""
    from jol_analytics_ai.security.pii_redaction import detect_pii

    findings = []
    try:
        text = file_path.read_text(encoding="utf-8")
        for line_num, line in enumerate(text.splitlines(), 1):
            line_findings = detect_pii(line)
            for f in line_findings:
                f["file"] = str(file_path)
                f["line"] = line_num
                findings.append(f)
    except (UnicodeDecodeError, PermissionError):
        pass
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="PII Audit Scanner")
    parser.add_argument(
        "--ci-mode", action="store_true", help="Exit with error if PII found"
    )
    parser.add_argument("--path", default="src/", help="Path to scan")
    args = parser.parse_args()

    scan_path = Path(args.path)
    all_findings: list[dict] = []

    for f in scan_path.rglob("*.py"):
        all_findings.extend(audit_file(f))

    if all_findings:
        print(f"PII AUDIT: Found {len(all_findings)} PII instances")
        for f in all_findings:
            print(f"  {f['file']}:{f['line']} - {f['type']}: {f['value']}")
        if args.ci_mode:
            return 1
    else:
        print("PII AUDIT: No PII detected")

    return 0


if __name__ == "__main__":
    sys.exit(main())
