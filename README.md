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

From this directory, install the locked project dependencies:

```sh
uv sync
```

Run the tests:

```sh
uv run pytest -q
```

Start the development server:

```sh
uv run uvicorn relay_api.main:app --reload
```

The health endpoint is available at <http://127.0.0.1:8000/health>.

## Current API slice

- `POST /tickets` validates a title and optional priority (default `3`), then
  returns a server-generated UUID and timezone-aware creation timestamp.
- `GET /tickets` returns tickets created since the application started.

Ticket data is currently held in application memory and is lost on restart.
Persistence, tenant ownership, authentication, and idempotency are later
milestones.

## Project milestones

1. Core API: tenants, users, RBAC, tickets, cursor pagination, idempotency
2. PostgreSQL, migrations, row-level security, indexes, and search
3. Background jobs, outbox, webhook delivery, and live updates
4. Containerization, CI/CD, Terraform, deployment, and operations
