from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional, Annotated
import random
from src.password.models import Password as passwordmodel

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.password.schemas import Password

router = APIRouter(prefix='/pass')


@router.get('/random_passwords')
async def generate_five_random_passwords(length: Annotated[int, Query(ge=4)] = 7,
                                         uppercase_chars: Optional[bool] = False,
                                         digits: Optional[bool] = False,
                                         special_chars: Optional[bool] = False, hard_mode: Optional[bool] = False):
    generated_password_1 = ""
    generated_password_2 = ""
    generated_password_3 = ""
    generated_password_4 = ""
    generated_password_5 = ""
    initial = list("abcdefghijklmnopqrstuvwxyz")
    if uppercase_chars:
        initial.extend(list("ABCDEFGHIJKLMNOPQRSUVWXYZ"))
    if digits:
        initial.extend(list("1234567890"))
    if special_chars:
        initial.extend((list("!@#$%^&*")))
    if hard_mode:
        initial.extend(list(r"~()_-+={[}]|\:;><.?/"))
    for i in range(length):
        generated_password_1 += random.choice(initial)
        generated_password_2 += random.choice(initial)
        generated_password_3 += random.choice(initial)
        generated_password_4 += random.choice(initial)
        generated_password_5 += random.choice(initial)

    return {'Your pass_1 is ready': generated_password_1,
            'Your pass_2 is ready': generated_password_2,
            'Your pass_3 is ready': generated_password_3,
            'Your pass_4 is ready': generated_password_4,
            'Your pass_5 is ready': generated_password_5}


@router.get("")
async def get_a_list_of_pass_from_db(id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(passwordmodel).where(passwordmodel.c.id == id)
        res = await session.execute(query)
        return {"status": "success", "data": res.mappings().first(), "details": None}
    except Exception:
        raise HTTPException(status_code=500, detail={"status": "error", "data": None, "details": None})


@router.post("")
async def insert_my_pass_to_db(pas: Password, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(passwordmodel).values(**pas.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "201 success"}
