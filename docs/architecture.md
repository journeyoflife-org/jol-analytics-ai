# Architecture

## Overview

jol-analytics-ai is a modular platform for analytics, machine learning, and Retrieval-Augmented Generation (RAG) serving ~400,000 religious institution websites across 27 EU countries.

## System Components

### Data Ingestion (ETL)
- **Extract**: CSV, JSON, SQL sources via `ingestion.extract`
- **Transform**: PII-aware cleaning, redaction, normalisation via `ingestion.transform`
- **Load**: CSV and SQL targets via `ingestion.load`

### Anonymisation Layer
- **Pseudonymisation**: HMAC-SHA256 based (`anonymization.pseudonymize`)
- **k-Anonymity**: Validation with configurable k (default k=5) (`anonymization.k_anonymity`)
- **Validators**: Compliance reporting (`anonymization.validators`)

### ML Pipeline
- **Training**: scikit-learn models with provenance tracking (`ml.train`)
- **Evaluation**: Classification and regression metrics (`ml.evaluate`)
- **Inference**: Authenticated prediction endpoints (`ml.infer`)
- **Fairness**: Demographic parity and equalized odds testing (`ml.fairness`)
- **Registry**: Versioned model artifacts with approval workflow (`ml.registry`)

### RAG System
- **Embeddings**: sentence-transformers based (`rag.embeddings`)
- **Chunking**: Configurable text segmentation (`rag.chunking`)
- **Retrieval**: ChromaDB vector store (`rag.retrieval`)
- **Vector Access**: Role-based access control (`rag.vector_access`)
- **Guardrails**: PII detection and redaction on outputs (`rag.guardrails`)

### API Layer
- FastAPI application with JWT authentication
- Health, inference, and RAG query endpoints
- Pydantic-validated request/response schemas

### Orchestration
- Apache Airflow DAGs with data governance policies
- dbt models for data transformation and lineage

## Compliance Architecture

| Layer | Control | Standard |
|-------|---------|----------|
| API | JWT authentication | CC6.1 |
| RAG | Role-based vector access | CC6 |
| ML | Model cards | GDPR Art. 22 |
| Data | k-anonymity ≥ 5 | GDPR minimisation |
| DAGs | Policy enforcement | ISO A.5.15 |
| Models | Versioned registry | SOC 2 CC8 |
