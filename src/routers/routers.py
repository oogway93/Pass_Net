from fastapi import APIRouter
from typing import Optional
import random

router = APIRouter(prefix='/pass')


@router.get('/password')
async def password(length: int, uppercase_chars: Optional[bool], digits: Optional[bool], special_chars: Optional[bool]):
    generated_password = ''
    initial = list('abcdefghijklmnopqrstuvwxyz')
    if uppercase_chars:
        initial.extend(list('ABCDEFGHIJKLMNOPQRSUVWXYZ'))
    if digits:
        initial.extend(list('1234567890'))
