from fastapi import APIRouter

from src.tasks.tasks import send_email_greetings

router = APIRouter(prefix='/task')


@router.get("/greetings")
async def get_greetings_bue_email(username: str):
    send_email_greetings.delay(username)
    return {"status": "200 success", "data": "Receive u email", "details": None}
