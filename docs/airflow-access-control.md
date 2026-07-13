# Airflow Access Control

## Overview

Airflow DAG access controls implement ISO A.5.15 access control requirements for data pipeline orchestration.

## Policy Framework

Data governance policies are defined in `airflow.policies`:

| Policy | Classification | Anonymisation | DPIA |
|--------|---------------|---------------|------|
| Standard ETL | Internal | No | No |
| PII Processing | Restricted | Yes | Yes |

## Role-Based Access

| Role | DAG Access |
|------|-----------|
| Viewer | Read-only DAG status |
| Analyst | Trigger standard DAGs |
| Data Scientist | Trigger all DAGs except PII |
| Admin | Full DAG management |

## DAG Requirements

Every DAG must:
1. Declare its data classification via `DataPolicy`
2. Validate the executing user has appropriate role
3. Log all executions with policy metadata
4. Enforce retention policies on generated data
