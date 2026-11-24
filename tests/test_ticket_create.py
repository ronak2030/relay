import pytest
from pydantic import ValidationError

from relay_api.schemas.ticket_create import CreateTicketRequest


def test_create_ticket_request_accepts_valid_input() -> None:
    request = CreateTicketRequest.model_validate(
        {"title": "Login issue", "priority": 2}
    )

    assert request.title == "Login issue"
    assert request.priority == 2


def test_create_ticket_request_defaults_priority_to_three() -> None:
    request = CreateTicketRequest.model_validate({"title": "Login issue"})

    assert request.priority == 3


def test_create_ticket_request_rejects_empty_title() -> None:
    with pytest.raises(ValidationError):
        CreateTicketRequest.model_validate({"title": ""})


@pytest.mark.parametrize("priority", [0, 6])
def test_create_ticket_request_rejects_priority_outside_range(
    priority: int,
) -> None:
    with pytest.raises(ValidationError):
        CreateTicketRequest.model_validate(
            {"title": "Login issue", "priority": priority}
        )
