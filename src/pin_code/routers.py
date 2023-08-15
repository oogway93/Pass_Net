import random
from typing import Annotated

from fastapi import APIRouter, Query, Depends

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.pin_code.models import PinCode
from src.pin_code.schemas import Pin_code

router = APIRouter(prefix='/pin_code')


@router.get("/random_pin-code")
async def generate_random_pin_code(pin: Annotated[int, Query(ge=4, le=6)] = 4):
    pin_code = ""
    for i in range(pin):
        pin_code += random.choice("0123456789")
    return {"pin_code": pin_code}


@router.post("")
async def insert_pin_code_to_db(pin: Pin_code,
                                session: AsyncSession = Depends(get_async_session)):
    stmt = insert(PinCode).values(**pin.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "201 created"}


