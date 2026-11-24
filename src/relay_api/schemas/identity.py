from enum import Enum
from uuid import UUID

from pydantic import BaseModel


class Role(str, Enum):
    ADMIN = "admin"
    AGENT = "agent"
    CUSTOMER = "customer"


class Membership(BaseModel):
    user_id: UUID
    tenant_id: UUID
    role: Role