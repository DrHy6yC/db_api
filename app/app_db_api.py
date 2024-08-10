from icecream import ic
from fastapi import FastAPI

from contextlib import asynccontextmanager

from api.router import router as tasks_router


@asynccontextmanager
async def lifespan(apps: FastAPI):

    ic("Api запущен")
    yield
    ic("Api выключен")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


@app.get("/")
async def hello():
    return {"Message": "HI!"}
