# Retention Policy

## Data Retention Schedule

| Data Type | Retention | Deletion Method | Owner |
|-----------|-----------|----------------|-------|
| Raw ingestion data | 365 days | Automated DAG | Data Engineering |
| Anonymised training data | Model lifetime + 1yr | Manual trigger | ML Team |
| Model artifacts | Deprecation + 5yr | Archive | ML Team |
| API request logs | 90 days | Automated | Platform |
| Audit logs | 7 years | Never (legal hold) | Compliance |
| RAG embeddings | Source lifetime | Cascade delete | RAG Team |

## Right to Erasure (Art. 17)

Upon valid erasure request:
1. Identify all data linked to the data subject
2. Delete from raw data stores
3. Pseudonymise in training data (if full deletion impractical)
4. Retrain affected models if necessary
5. Log erasure action in audit trail

## Configuration

- Default retention: `DATA_RETENTION_DAYS=365` in `.env`
- Override per data classification in `airflow.policies`
