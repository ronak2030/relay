from uuid import UUID

import pytest
from pydantic import ValidationError

from relay_api.schemas.tenant import Tenant


def test_tenant_accepts_valid_data() -> None:
    tenant = Tenant.model_validate(
        {
            "id": "123e4567-e89b-42d3-a456-426614174000",
            "name": "Acme",
        }
    )

    assert tenant.id == UUID("123e4567-e89b-42d3-a456-426614174000")
    assert tenant.name == "Acme"


def test_tenant_rejects_empty_name() -> None:
    with pytest.raises(ValidationError):
        Tenant.model_validate(
            {
                "id": "123e4567-e89b-42d3-a456-426614174000",
                "name": "",
            }
        )
