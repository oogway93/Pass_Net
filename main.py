import uvicorn
from fastapi import FastAPI
from src.routers.routers import router

app = FastAPI()

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run('main:app')
