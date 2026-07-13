# Controls Matrix

## Control Mapping

| Control ID | Control | Standard | Implementation | Evidence | Status |
|-----------|---------|----------|---------------|----------|--------|
| C1 | Data anonymisation | GDPR minimisation | `anonymization/k_anonymity.py` (k≥5) | `verify-k-anonymity.py` | Planned |
| C2 | Model transparency | GDPR Art. 22 | Model cards for all production models | `model_cards/` | Planned |
| C3 | Access control | ISO A.5.15 | RBAC in `security/access_control.py` | `access-review-log.md` | Planned |
| C4 | Data lineage | GDPR Art. 30 | dbt models + lineage export | `data-lineage.md` | Planned |
| C5 | PII audit | GDPR | `scripts/run-pii-audit.py` | Audit reports | Planned |
| C6 | RAG access control | CC6 | `rag/vector_access.py` | Access logs | Planned |
| C7 | Inference auth | CC6.1 | JWT in `security/auth.py` | API logs | Planned |
| C8 | DPIA | GDPR Art. 35 | `compliance/dpia/ai-dpia.md` | DPIA docs | Planned |
| C9 | Fairness testing | EU AI Act | `ml/fairness.py` | Test results | Planned |
| C10 | Model versioning | SOC 2 CC8 | `ml/registry.py` | Registry index | Planned |
