# RAG Security

## Overview

The RAG (Retrieval-Augmented Generation) system processes potentially sensitive documents. Security controls ensure data isolation, access control, and PII protection.

## Access Controls (CC6)

- **Authentication**: JWT required for all RAG endpoints
- **Authorisation**: Role-based via `rag.vector_access.VectorAccessController`
- **Tenant isolation**: Results filtered by `tenant_id` metadata
- **Write access**: Restricted to `analyst` role and above

## PII Protection

- **Input validation**: Query length and format checked (`rag.guardrails.validate_input`)
- **Output guardrails**: PII detection and redaction on all RAG responses (`rag.guardrails.apply_guardrails`)
- **Document ingestion**: PII should be redacted before indexing

## Vector Store Security

- ChromaDB instance runs on internal network
- Collection-level access controls planned
- Embedding model version tracked in config

## Audit Logging

All RAG operations are logged:
- Query text (PII-redacted in logs)
- Result count
- User/role
- Timestamp
