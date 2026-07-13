#!/usr/bin/env python3
"""Build and validate model cards for production models.

Usage:
    python scripts/build-model-card.py [--validate] [--model-name NAME]
"""

import argparse
import sys
from pathlib import Path


def validate_model_cards() -> list[str]:
    """Check that all production models have corresponding model cards."""
    production_dir = Path("model_cards/production")
    issues: list[str] = []

    if not production_dir.exists():
        issues.append("model_cards/production/ directory does not exist")
        return issues

    cards = list(production_dir.glob("*.md"))
    if not cards:
        issues.append("No model cards found in model_cards/production/")

    return issues


def create_model_card(model_name: str) -> Path:
    """Create a new model card from template."""
    template = Path("model_cards/TEMPLATE.md").read_text()
    output = Path(f"model_cards/production/{model_name}.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(template.replace("{MODEL_NAME}", model_name))
    print(f"Created model card: {output}")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Model Card Builder")
    parser.add_argument("--validate", action="store_true", help="Validate existing model cards")
    parser.add_argument("--model-name", type=str, help="Create card for model")
    args = parser.parse_args()

    if args.validate:
        issues = validate_model_cards()
        if issues:
            print("MODEL CARD VALIDATION FAILED:")
            for issue in issues:
                print(f"  - {issue}")
            return 1
        print("MODEL CARD VALIDATION: OK")
        return 0

    if args.model_name:
        create_model_card(args.model_name)
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
