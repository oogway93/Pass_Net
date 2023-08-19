import time

from fastapi import APIRouter
from fastapi_cache.decorator import cache

router = APIRouter(prefix="/operation")


@router.get("/long_operation")
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return {"msg": "Too long...", "details": "check redis"}
