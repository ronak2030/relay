from datetime import datetime
from uuid import UUID

import pytest
from fastapi.testclient import TestClient

from relay_api.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_tickets() -> None:
    app.state.tickets = []


def test_create_ticket_returns_validated_request() -> None:
    response = client.post(
        "/tickets",
        json={"title": "Login issue", "priority": 2},
    )

    assert response.status_code == 201
    ticket = response.json()
    assert ticket["title"] == "Login issue"
    assert ticket["priority"] == 2
    ticket_id = UUID(ticket["id"])
    assert str(ticket_id) == ticket["id"]
    created_at = datetime.fromisoformat(ticket["created_at"])
    assert created_at.tzinfo is not None
    assert created_at.utcoffset() is not None


def test_create_ticket_uses_default_priority() -> None:
    response = client.post("/tickets", json={"title": "Login issue"})

    assert response.status_code == 201
    assert response.json()["priority"] == 3


def test_create_ticket_rejects_invalid_request() -> None:
    response = client.post(
        "/tickets",
        json={"title": "", "priority": 2},
    )

    assert response.status_code == 422
    assert client.get("/tickets").json() == []


def test_list_tickets_returns_tickets_created_during_app_lifetime() -> None:
    first_response = client.post(
        "/tickets",
        json={"title": "Login issue", "priority": 2},
    )
    second_response = client.post(
        "/tickets",
        json={"title": "Billing question"},
    )

    response = client.get("/tickets")

    assert response.status_code == 200
    tickets = response.json()
    assert len(tickets) == 2
    assert [ticket["title"] for ticket in tickets] == [
        "Login issue",
        "Billing question",
    ]
    assert tickets[0]["id"] == first_response.json()["id"]
    assert tickets[1]["id"] == second_response.json()["id"]
    assert tickets[0]["id"] != tickets[1]["id"]


def test_list_tickets_is_empty_before_any_tickets_are_created() -> None:
    response = client.get("/tickets")

    assert response.status_code == 200
    assert response.json() == []
