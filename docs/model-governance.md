# Model Governance

## Overview

All production ML models must be documented, versioned, approved, and tested for fairness before deployment. This aligns with GDPR Art. 22, the EU AI Act, and SOC 2 CC8.

## Model Lifecycle

1. **Development** — Training with anonymised data, fairness testing
2. **Review** — Model card creation, peer review, compliance check
3. **Approval** — Registered in model registry with approval record
4. **Deployment** — Versioned artifact deployed to inference endpoint
5. **Monitoring** — Drift detection, periodic fairness re-evaluation
6. **Deprecation** — Archived with retention per data policy

## Model Cards

Every production model requires a model card (`model_cards/TEMPLATE.md`) documenting:
- Model type, architecture, intended use
- Training data provenance and PII audit status
- Evaluation metrics
- Fairness and bias assessment
- Ethical considerations and Art. 22 applicability

## Fairness Testing

Mandatory tests before deployment:
- **Demographic parity** across protected attributes
- **Equalized odds** (TPR/FPR parity)
- Results documented in model card and `compliance/audit/evidence-index.md`

## Versioning

- Model artifacts stored in `artifacts/models/`
- Registry index maintained in `ml.registry.ModelRegistry`
- Each version records: metrics, training data hash, approval status

## Change Management

Model changes require:
1. Updated model card
2. Re-run of fairness tests
3. New registry entry (never overwrite)
4. GitHub issue using `model_change.yml` template
