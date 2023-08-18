import time

from fastapi import APIRouter
from fastapi_cache.decorator import cache

route = APIRouter(prefix="/operation")


@route.get("/long_operation")
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "Too long..."
