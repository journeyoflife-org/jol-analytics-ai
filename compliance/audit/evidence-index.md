# Evidence Index

## Audit Evidence Register

| # | Evidence | Location | Standard | Last Verified |
|---|---------|----------|----------|---------------|
| 1 | Model cards | `model_cards/production/` | GDPR Art. 22 | |
| 2 | k-anonymity reports | `scripts/verify-k-anonymity.py` output | GDPR minimisation | |
| 3 | PII audit reports | `scripts/run-pii-audit.py` output | GDPR PII | |
| 4 | Fairness test results | `tests/fairness/` | EU AI Act | |
| 5 | Access control matrix | `security/access_control.py` | ISO A.5.15, CC6 | |
| 6 | Authentication logs | API middleware | CC6.1 | |
| 7 | Model registry | `ml/registry.py` | SOC 2 CC8 | |
| 8 | Data lineage | `docs/data-lineage.md` | GDPR Art. 30 | |
| 9 | DPIA documents | `compliance/dpia/` | GDPR Art. 35 | |
| 10 | Incident response | `docs/incident-response-ai.md` | SOC 2 CC7 | |
