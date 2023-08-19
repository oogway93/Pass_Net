from typing import Optional

from fastapi import APIRouter, HTTPException
import random
import string

router = APIRouter(prefix="/login")


@router.get("/random_login")
async def generate_random_login(length: int = 8, fluent_log: bool | None = False, nickname: str | None = None):
    if 8 <= length <= 20:
        additions = ['cool', 'awesome', 'master', 'ninja', 'pro', 'gamer', 'hacker', 'star', 'legend', 'expert',
                     'junior', 'profi', 'senior', 'middle', 'sniper', 'pudge', 'lol', 'wow', 'lil']

        if fluent_log and nickname:
            fluent_characters = string.digits
            fluent_login = ''.join(random.choice(fluent_characters) for _ in range(length - len(nickname)))
            return {"fluent login": f"{nickname}{random.choice(additions).capitalize()}{fluent_login}"}
        elif fluent_log:
            raise HTTPException(status_code=500, detail={"status": "error", "data": None,
                                                         "detail": "If you wanna fluent login, you must enter your "
                                                                   "attractive nickname."})
        elif nickname:
            raise HTTPException(status_code=500, detail={"status": "error", "data": None,
                                                         "detail": "If you wanna enter nickname, you must confirm ("
                                                                   "write true) 'fluent log'."})
        else:
            characters = string.ascii_letters + string.digits
            login = ''.join(random.choice(characters) for _ in range(length))
            return {"simple login": login}
    else:
        raise HTTPException(status_code=500, detail={"status": "error", "data": None,
                                                     "detail": "Length must be between 8 and 20."})
