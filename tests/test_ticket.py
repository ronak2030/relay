from datetime import datetime, timezone
from uuid import UUID

import pytest
from pydantic import ValidationError

from relay_api.schemas.ticket import Ticket, TicketStatus


def valid_ticket_data() -> dict[str, object]:
    return {
        "id": "123e4567-e89b-42d3-a456-426614174000",
        "tenant_id": "123e4567-e89b-42d3-a456-426614174001",
        "created_by": "123e4567-e89b-42d3-a456-426614174002",
        "title": "Login issue",
        "status": "open",
        "priority": 3,
        "created_at": "2026-11-23T10:00:00+00:00",
    }


def test_ticket_accepts_valid_data() -> None:
    ticket = Ticket.model_validate(valid_ticket_data())

    assert ticket.id == UUID("123e4567-e89b-42d3-a456-426614174000")
    assert ticket.tenant_id == UUID("123e4567-e89b-42d3-a456-426614174001")
    assert ticket.created_by == UUID("123e4567-e89b-42d3-a456-426614174002")
    assert ticket.title == "Login issue"
    assert ticket.status is TicketStatus.OPEN
    assert ticket.priority == 3
    assert ticket.created_at == datetime(2026, 11, 23, 10, 0, tzinfo=timezone.utc)


def test_ticket_rejects_empty_title() -> None:
    data = valid_ticket_data()
    data["title"] = ""

    with pytest.raises(ValidationError):
        Ticket.model_validate(data)


def test_ticket_rejects_unknown_status() -> None:
    data = valid_ticket_data()
    data["status"] = "pending"

    with pytest.raises(ValidationError):
        Ticket.model_validate(data)


@pytest.mark.parametrize("priority", [0, 6])
def test_ticket_rejects_priority_outside_range(priority: int) -> None:
    data = valid_ticket_data()
    data["priority"] = priority

    with pytest.raises(ValidationError):
        Ticket.model_validate(data)


def test_ticket_rejects_naive_created_at() -> None:
    data = valid_ticket_data()
    data["created_at"] = "2026-11-23T10:00:00"

    with pytest.raises(ValidationError):
        Ticket.model_validate(data)
