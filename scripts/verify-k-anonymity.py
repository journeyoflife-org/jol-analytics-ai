#!/usr/bin/env python3
"""Verify k-anonymity compliance on training datasets.

Usage:
    python scripts/verify-k-anonymity.py [--check] [--k VALUE] [--file PATH]
"""

import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="k-Anonymity Verifier")
    parser.add_argument(
        "--check",
        action="store_true",
        help="CI mode: exit with error if non-compliant",
    )
    parser.add_argument(
        "--k", type=int, default=5, help="Required k value (default: 5)"
    )
    parser.add_argument("--file", type=str, help="CSV file to check")
    args = parser.parse_args()

    if not args.file:
        print(f"k-Anonymity check mode: k={args.k}")
        print("No file specified — skipping (use --file PATH to check a dataset)")
        return 0

    import pandas as pd

    from jol_analytics_ai.anonymization.k_anonymity import validate_k_anonymity

    df = pd.read_csv(args.file)
    # Use all columns as quasi-identifiers by default
    quasi_ids = list(df.select_dtypes(include=["object", "int64"]).columns)

    if not quasi_ids:
        print("No quasi-identifier columns found")
        return 0

    is_valid = validate_k_anonymity(df, quasi_ids, k=args.k)

    if is_valid:
        print(f"k-ANONYMITY: PASS (k ≥ {args.k})")
        return 0
    else:
        print(f"k-ANONYMITY: FAIL (k < {args.k})")
        if args.check:
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
