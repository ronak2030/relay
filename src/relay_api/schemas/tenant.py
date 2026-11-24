from pydantic import BaseModel, Field
from uuid import UUID

class Tenant(BaseModel):
    id: UUID
    name: str = Field(min_length=1)