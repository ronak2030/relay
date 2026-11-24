from uuid import UUID

import pytest
from pydantic import ValidationError

from relay_api.schemas.identity import Membership, Role


def test_model_validate_accepts_string_uuids_and_role() -> None:
    membership = Membership.model_validate(
        {
            "user_id": "123e4567-e89b-42d3-a456-426614174000",
            "tenant_id": "123e4567-e89b-42d3-a456-426614174001",
            "role": "agent",
        }
    )

    assert membership.user_id == UUID("123e4567-e89b-42d3-a456-426614174000")
    assert membership.tenant_id == UUID("123e4567-e89b-42d3-a456-426614174001")
    assert membership.role is Role.AGENT


def test_unknown_role_is_rejected() -> None:
    with pytest.raises(ValidationError):
        Membership.model_validate(
            {
                "user_id": "123e4567-e89b-42d3-a456-426614174000",
                "tenant_id": "123e4567-e89b-42d3-a456-426614174001",
                "role": "owner",
            }
        )


def test_malformed_uuid_is_rejected() -> None:
    with pytest.raises(ValidationError):
        Membership.model_validate(
            {
                "user_id": "not-a-uuid",
                "tenant_id": "123e4567-e89b-42d3-a456-426614174001",
                "role": "agent",
            }
        )


def test_user_can_have_different_roles_in_different_tenants() -> None:
    user_id = "123e4567-e89b-42d3-a456-426614174000"
    tenant_a = Membership.model_validate(
        {
            "user_id": user_id,
            "tenant_id": "123e4567-e89b-42d3-a456-426614174001",
            "role": "admin",
        }
    )
    tenant_b = Membership.model_validate(
        {
            "user_id": user_id,
            "tenant_id": "123e4567-e89b-42d3-a456-426614174002",
            "role": "agent",
        }
    )

    assert tenant_a.user_id == tenant_b.user_id
    assert tenant_a.tenant_id != tenant_b.tenant_id
    assert tenant_a.role is Role.ADMIN
    assert tenant_b.role is Role.AGENT
