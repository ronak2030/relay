# Relay

Relay is a multi-tenant support-ticketing backend. This repository is separate
from the AI Engineer Learning Journey repository; locally it lives in the
learning workspace at `relay/`.

## Project goals

- Tenant-isolated tickets, users, and roles (`admin`, `agent`, `customer`)
- FastAPI APIs with authentication, authorization, cursor pagination, and
  idempotent writes
- PostgreSQL with row-level security, Redis, and background workers
- Tests, CI, observability, and infrastructure-as-code deployment

## Local development

Setup instructions will be added with the first runnable API slice.

## Project milestones

1. Core API: tenants, users, RBAC, tickets, cursor pagination, idempotency
2. PostgreSQL, migrations, row-level security, indexes, and search
3. Background jobs, outbox, webhook delivery, and live updates
4. Containerization, CI/CD, Terraform, deployment, and operations
