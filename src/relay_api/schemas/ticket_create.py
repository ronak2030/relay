from pydantic import BaseModel, Field


class CreateTicketRequest(BaseModel):
    title: str = Field(min_length=1)
    priority: int = Field(default=3, ge=1, le=5)
