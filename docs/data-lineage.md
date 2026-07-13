# Data Lineage

## Overview

Data lineage tracking ensures GDPR Art. 30 record-keeping compliance and provides audit trails for all data processing activities.

## Lineage Chain

```
Source → Extract → Transform (PII redaction) → Load → dbt Models → ML Training / RAG Index
```

## Stages

### 1. Source Registration
- All data sources registered in `dbt/sources/`
- Source metadata: origin, owner, classification, lawful basis

### 2. Extraction
- Logged via `ingestion.extract` with timestamps and row counts
- No transformations at extraction stage

### 3. Transformation
- PII redaction applied via `ingestion.transform.redact_pii_columns`
- Anonymisation validated via `anonymization.k_anonymity`
- All transforms logged with before/after statistics

### 4. dbt Models
- dbt models in `dbt/models/` define transformations
- Exposures in `dbt/exposures/` document downstream consumers
- Lineage exported via `scripts/export-lineage.sh`

### 5. ML Training Data
- Training data hash recorded in model registry
- PII audit run via `scripts/run-pii-audit.py` before training
- k-anonymity validated before model fitting

### 6. RAG Document Index
- Documents chunked and embedded with metadata tags
- Access controls enforced per tenant/role

## Audit Trail

All lineage events are logged with:
- Timestamp (UTC)
- Actor (user/service)
- Operation type
- Input/output references
- Data classification
