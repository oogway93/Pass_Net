from pydantic import BaseModel, Field


class Pin_code(BaseModel):
    id: int
    pin: str = Field(min_length=4, max_length=6)
