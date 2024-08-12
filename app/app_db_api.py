from icecream import ic
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends

from auth.models import User
from auth.schemas import UserCreate, UserRead
from auth.utils import create_db_and_tables, auth_backend, fastapi_users_param, current_active_user
from tasks.router import router as tasks_router


@asynccontextmanager
async def lifespan(apps: FastAPI):
    await create_db_and_tables()
    ic("Api запущен")
    yield
    ic("Api выключен")


app = FastAPI(lifespan=lifespan, title="Api DB")

app.include_router(tasks_router, dependencies=[Depends(current_active_user)])


@app.get("/", tags=["Greetings"])
async def hello():
    return {"Message": "HI!"}


app.include_router(
    fastapi_users_param.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Authorization"]
)
app.include_router(
    fastapi_users_param.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Authorization"],
)


@app.get("/authenticated-route", tags=["Authenticated"])
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}
