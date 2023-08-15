from fastapi import APIRouter, HTTPException
import random
import string

router = APIRouter(prefix="/login")


@router.get("/random_login")
async def generate_random_login(length: int = 8):
    if 8 <= length <= 20:
        characters = string.ascii_letters + string.digits
        login = ''.join(random.choice(characters) for _ in range(length))
        return login
    else:
        raise HTTPException(status_code=500, detail={"status": "error", "data": None,
                                                     "detail": "Length must be between 8 and 20."})
