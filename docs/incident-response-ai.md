# Incident Response — AI Systems

## Overview

Incident response procedures for AI-specific incidents including model failures, data breaches involving training data, and biased outputs.

## Incident Categories

| Category | Example | Severity |
|----------|---------|----------|
| Model failure | Inference endpoint errors | High |
| Data breach | Training data exposure | Critical |
| Bias incident | Discriminatory model output | High |
| PII leak | PII detected in RAG output | High |
| Access violation | Unauthorised model access | Medium |

## Response Procedures

### 1. Detection
- Automated monitoring of inference endpoints
- PII detection in outputs (`rag.guardrails`)
- Fairness monitoring on predictions

### 2. Containment
- Disable affected endpoint/DAG
- Revoke compromised access tokens
- Isolate affected model version

### 3. Investigation
- Review audit logs
- Identify affected data subjects
- Assess scope of impact

### 4. Notification
- DPO notified within 24 hours
- Supervisory authority notified within 72 hours (GDPR Art. 33)
- Affected data subjects notified if high risk (Art. 34)

### 5. Remediation
- Patch or rollback model
- Retrain with corrected data if needed
- Update DPIA if processing changes

### 6. Post-Incident
- Root cause analysis
- Update risk register
- Review and update controls
