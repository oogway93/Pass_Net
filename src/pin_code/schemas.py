from pydantic import BaseModel


class Pin_code(BaseModel):
    id: int
    pin: int
