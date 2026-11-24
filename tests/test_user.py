from uuid import UUID

import pytest
from pydantic import ValidationError

from relay_api.schemas.user import User


def test_user_accepts_valid_data() -> None:
    user = User.model_validate(
        {
            "id": "123e4567-e89b-42d3-a456-426614174000",
            "email": "ronak@example.com",
            "display_name": "Ronak",
        }
    )

    assert user.id == UUID("123e4567-e89b-42d3-a456-426614174000")
    assert user.email == "ronak@example.com"
    assert user.display_name == "Ronak"


def test_user_rejects_malformed_email() -> None:
    with pytest.raises(ValidationError):
        User.model_validate(
            {
                "id": "123e4567-e89b-42d3-a456-426614174000",
                "email": "not-an-email",
                "display_name": "Ronak",
            }
        )


def test_user_rejects_empty_display_name() -> None:
    with pytest.raises(ValidationError):
        User.model_validate(
            {
                "id": "123e4567-e89b-42d3-a456-426614174000",
                "email": "ronak@example.com",
                "display_name": "",
            }
        )
