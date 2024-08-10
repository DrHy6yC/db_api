from icecream import ic
from fastapi import FastAPI

from contextlib import asynccontextmanager

from tasks.router import router as tasks_router


@asynccontextmanager
async def lifespan(apps: FastAPI):

    ic("Api запущен")
    yield
    ic("Api выключен")


app = FastAPI(lifespan=lifespan, title="Api DB")


@app.get("/", tags=["Greetings"])
async def hello():
    return {"Message": "HI!"}

app.include_router(tasks_router)
