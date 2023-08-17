from typing import Optional

from fastapi import APIRouter
import random
import string
import hashlib
import secrets

router = APIRouter(prefix="/key")


@router.get("/hash_key")
async def generate_hash_key(bytes: int = 16):
    random_string = secrets.token_hex(bytes)
    hash_key = hashlib.sha256(random_string.encode()).hexdigest()
    return {"hash key": hash_key, "info": "A length of string depends on bytes. For example: 10 bytes = 20 symbols"}


@router.get("")
async def create_secret_keys_and_tokens_for_some_platforms(git: Optional[bool] = False, django: Optional[bool] = False):
    if git:
        random_string = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(36))
        return {"git token": f"ghp_{random_string}"}
    if django:
        allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
        random_string = ''.join(random.choice(allowed_chars) for i in range(50))
        return {"django's secret key": f"django-insecure-{random_string}"}


@router.get("/personal_key")
async def create_personal_key_for_different_situations():
    key = ''.join(random.choice(string.digits + string.ascii_letters) for i in range(20))
    return {"personal key": key}
