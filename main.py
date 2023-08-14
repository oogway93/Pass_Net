import uvicorn
from fastapi import FastAPI

from src.password.routers import router as PasswordRouter

app = FastAPI()

app.include_router(PasswordRouter, tags=['Password'])

if __name__ == '__main__':
    uvicorn.run('main:app')
