import uvicorn
from fastapi import FastAPI

from src.password.routers import router as PasswordRouter
from src.pin_code.routers import router as PinCodeRouter

app = FastAPI()

app.include_router(PasswordRouter, tags=['Password'])
app.include_router(PinCodeRouter, tags=['Pin-Code'])

if __name__ == '__main__':
    uvicorn.run('main:app')
