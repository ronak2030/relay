from pydantic import EmailStr, BaseModel, Field
from uuid import UUID

class User(BaseModel):
    id: UUID
    email: EmailStr
    display_name: str = Field(min_length=1)