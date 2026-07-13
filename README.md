# jol-analytics-ai

Analytics, ML & RAG Platform for [Journey Of Life](https://journeyoflife.org) — serving ~400,000 religious institution websites across 27 EU countries.

## Overview

jol-analytics-ai delivers:

- **Analytics** — Data ingestion, transformation, and insights via ETL pipelines
- **Machine Learning** — Model training, evaluation, fairness testing, and versioned registry
- **RAG** — Retrieval-Augmented Generation with semantic search, PII guardrails, and access control
- **Compliance** — GDPR (Art. 22, 30, 35), EU AI Act, SOC 2, and ISO 27001 controls built in

## Quick Start

```bash
git clone https://github.com/journeyoflife-org/jol-analytics-ai.git
cd jol-analytics-ai
python -m venv .venv
source .venv/bin/activate
make dev
cp .env.example .env
# Edit .env with your configuration
```

Run the API:

```bash
uvicorn jol_analytics_ai.api.app:app --reload
```

## Project Structure

```
src/jol_analytics_ai/
├── config.py              # Central configuration
├── logging.py             # PII-safe structured logging
├── security/              # Auth, PII redaction, RBAC
├── ingestion/             # ETL: extract, transform, load
├── anonymization/         # k-anonymity, pseudonymisation
├── airflow/               # DAG orchestration + policies
├── dbt/                   # Data transformation models
├── ml/                    # Train, evaluate, infer, fairness, registry
├── model_cards/           # GDPR Art. 22 transparency
├── rag/                   # Embeddings, retrieval, guardrails
└── api/                   # FastAPI endpoints
```

## Compliance

| Area | Implementation | Standard |
|------|---------------|----------|
| Data anonymisation | k-anonymity (k ≥ 5) | GDPR minimisation |
| Model transparency | Model cards | GDPR Art. 22 |
| Access control | RBAC | ISO A.5.15, CC6 |
| Data lineage | dbt + export scripts | GDPR Art. 30 |
| DPIA | Template + screening | GDPR Art. 35 |
| Fairness testing | Demographic parity, equalized odds | EU AI Act |
| Model versioning | File-based registry | SOC 2 CC8 |
| Authentication | JWT | CC6.1 |

## Testing

```bash
make test       # All tests with coverage
make lint       # Ruff + mypy + Black
```

## Documentation

- [Architecture](docs/architecture.md)
- [Model Governance](docs/model-governance.md)
- [RAG Security](docs/rag-security.md)
- [DPIA Template](docs/DPIA-template.md)
- [Data Lineage](docs/data-lineage.md)

## License

[Apache License 2.0](LICENSE)
