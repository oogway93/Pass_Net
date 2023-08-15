import uvicorn
from fastapi import FastAPI

from src.password.routers import router as PasswordRouter
from src.pin_code.routers import router as PinCodeRouter
from src.login.routers import router as LoginRouter
from src.secret_key.routers import router as SecretKeyRouter

app = FastAPI()

app.include_router(PasswordRouter, tags=['Password'])
app.include_router(PinCodeRouter, tags=['Pin-Code'])
app.include_router(LoginRouter, tags=['Login'])
app.include_router(SecretKeyRouter, tags=['Secret Key'])

if __name__ == '__main__':
    uvicorn.run('src.main:app')
