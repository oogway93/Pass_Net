from pydantic import BaseModel, Field


class Password(BaseModel):
    id: int
    password: str = Field(min_length=5)
