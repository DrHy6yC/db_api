from icecream import ic
from fastapi import FastAPI

from contextlib import asynccontextmanager

from db.engine import create_tables, delete_tables
from api.router import router as tasks_router


@asynccontextmanager
async def lifespan(apps: FastAPI):

    await delete_tables()
    ic("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


@app.get("/")
async def hello():
    return {"Message": "HI!"}
