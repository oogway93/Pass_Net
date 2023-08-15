from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Optional, Annotated
import random
import re
from src.password.models import Password

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.password.schemas import Password as PasswordSchema

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
        query = select(Password).where(Password.id == id)
        result = await session.execute(query)
        return {"status": "success", "data": result.mappings().first(), "details": None}
    except Exception:
        raise HTTPException(status_code=500, detail={"status": "error", "data": None, "details": None})


@router.post("")
async def insert_my_pass_to_db(pas: PasswordSchema, session: AsyncSession = Depends(get_async_session)):
    flag = True
    while True:
        if len(pas.password) <= 8:
            flag = False
            break
        elif not re.search("[a-z]", pas.password):
            flag = False
            break
        elif not re.search("[A-Z]", pas.password):
            flag = False
            break
        elif not re.search("[0-9]", pas.password):
            flag = False
            break
        elif re.search("\s", pas.password):
            flag = False
            break
        else:
            flag = True
            break

    if flag:
        stmt = insert(Password).values(**pas.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "201 success"}
    else:
        raise HTTPException(status_code=500, detail={"status": "error", "data": None,
                                                     "detail": "The password must contain lowercase chars(a-z), "
                                                               "uppercase chars(A - Z), digits(0 - 9) and be without "
                                                               "symbols: 'tabulation', 'space', 'new line' and etc."})
