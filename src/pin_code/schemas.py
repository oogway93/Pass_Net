from pydantic import BaseModel, Field


class Pin_code(BaseModel):
    id: int
    pin: int
