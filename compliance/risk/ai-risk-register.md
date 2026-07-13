# AI Risk Register

## Risk Entries

| ID | Risk | Likelihood | Impact | Score | Mitigation | Owner | Status |
|----|------|-----------|--------|-------|-----------|-------|--------|
| R1 | Biased model outputs | Medium | High | Medium | Fairness testing, monitoring | ML Team | Open |
| R2 | PII in training data | Medium | Critical | High | PII audit, k-anonymity | Data Team | Open |
| R3 | Unauthorised model access | Low | High | Medium | RBAC, JWT auth | Security | Open |
| R4 | Training data breach | Low | Critical | High | Encryption, access control | Security | Open |
| R5 | Non-compliance with Art. 22 | Medium | Critical | High | DPIA, model cards | Compliance | Open |
| R6 | Model drift | Medium | Medium | Medium | Monitoring, retraining | ML Team | Open |
| R7 | RAG PII leakage | Medium | High | High | Output guardrails | RAG Team | Open |

## Risk Scoring Matrix

| | Low Impact | Medium Impact | High Impact | Critical Impact |
|---|-----------|--------------|-------------|----------------|
| **High Likelihood** | Medium | High | Critical | Critical |
| **Medium Likelihood** | Low | Medium | High | High |
| **Low Likelihood** | Low | Low | Medium | High |
