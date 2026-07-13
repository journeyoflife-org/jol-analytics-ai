# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 0.1.x   | Yes       |

## Reporting a Vulnerability

**Do NOT open a public issue for security vulnerabilities.**

1. Email: security@journeyoflife.org
2. Include: description, impact assessment, reproduction steps
3. Expected response: within 48 hours

## Security Controls

### Authentication
- JWT-based for all API endpoints (`security/auth.py`)
- Bcrypt password hashing
- Configurable token expiry

### Authorisation
- Role-based access control (`security/access_control.py`)
- Granular permissions per operation type
- Quarterly access reviews (ISO A.5.15)

### Data Protection
- PII detection and redaction (`security/pii_redaction.py`)
- k-Anonymity validation (k ≥ 5) for ML training data
- Pseudonymisation via HMAC-SHA256

### Compliance
- GDPR Art. 22 transparency via model cards
- DPIA required for all AI features (Art. 35)
- EU AI Act fairness testing before deployment

### Incident Response
See `docs/incident-response-ai.md`

## Dependencies

- Monitored via Dependabot (weekly)
- CodeQL analysis on all PRs
- Qodana static analysis
