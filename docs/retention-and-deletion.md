# Retention and Deletion

## Overview

Data retention policies ensure compliance with GDPR storage limitation (Art. 5(1)(e)).

## Retention Schedule

| Data Category | Retention Period | Justification |
|--------------|-----------------|---------------|
| Raw ingestion data | 365 days | Analytics window |
| Anonymised training data | Until model deprecation | ML lifecycle |
| Model artifacts | 5 years after deprecation | Audit trail |
| API logs | 90 days | Operational monitoring |
| Audit logs | 7 years | Legal requirement |
| RAG document embeddings | Until source deletion | Data currency |

## Deletion Procedures

1. **Scheduled deletion**: Automated cleanup via Airflow DAGs
2. **Right to erasure (Art. 17)**: On request, delete all data linked to a data subject
3. **Model retraining**: If training data is deleted, affected models must be retrained

## Implementation

- Retention configured in `.env` via `DATA_RETENTION_DAYS`
- Deletion logged in audit trail
- Verification via `compliance/audit/access-review-log.md`
