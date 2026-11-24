from uuid import UUID

from pydantic import AwareDatetime, BaseModel, Field


class TicketResponse(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    priority: int = Field(ge=1, le=5)
    created_at: AwareDatetime
