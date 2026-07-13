# Contributing to jol-analytics-ai

Thank you for contributing to the Journey Of Life analytics platform.

## Development Setup

```bash
git clone https://github.com/journeyoflife-org/jol-analytics-ai.git
cd jol-analytics-ai
python -m venv .venv
source .venv/bin/activate
make dev
```

## Code Standards

- **Formatting:** Black (88 chars)
- **Linting:** Ruff
- **Type checking:** mypy (strict)
- **Pre-commit hooks:** Enabled via `make dev`

## Pull Request Process

1. Create a feature branch from `main`
2. Write tests for new functionality
3. Ensure `make lint` and `make test` pass
4. Submit PR with description following the PR template

## GDPR & Compliance Requirements

All contributors must ensure:

- **No PII** in code, tests, or fixtures
- **Data anonymisation** (k ≥ 5) for any ML training data
- **Model cards** created for all production models
- **DPIA review** triggered for AI/automated decision features
- **Access controls** reviewed for new endpoints

## Code Review

- All PRs require at least one approval
- Security-sensitive changes require security team review (see CODEOWNERS)
- ML model changes require data science team review
- Compliance changes require compliance team review

## Issue Templates

- **Bug Report:** Standard bug reporting
- **Feature Request:** Includes GDPR impact assessment
- **Model Change:** Requires model card and fairness updates
- **DPIA Review:** For high-risk AI processing (Art. 35)
