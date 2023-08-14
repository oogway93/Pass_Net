from fastapi import APIRouter
from typing import Optional, Annotated, List
import random

from pydantic import BaseModel

router = APIRouter(prefix='/pass', tags=['PASSWORD'])



@router.get('/password')
async def password(length: int = 7, uppercase_chars: Optional[bool] = False, digits: Optional[bool] = False,
                   special_chars: Optional[bool] = False, hard_mode: Optional[bool] = False):
    generated_password_1 = ''
    generated_password_2 = ''
    generated_password_3 = ''
    generated_password_4 = ''
    generated_password_5 = ''
    initial = list('abcdefghijklmnopqrstuvwxyz')
    if uppercase_chars:
        initial.extend(list('ABCDEFGHIJKLMNOPQRSUVWXYZ'))
    if digits:
        initial.extend(list('1234567890'))
    if special_chars:
        initial.extend((list('!@#$%^&*')))
    if hard_mode:
        initial.extend(list('~()_-+={[}]|\:;><.?/'))
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
