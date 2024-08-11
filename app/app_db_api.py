from icecream import ic
from fastapi import FastAPI, Depends

from contextlib import asynccontextmanager

from tasks.router import router as tasks_router
from auth.users import create_db_and_tables, auth_backend, fastapi_users \
    , UserRead, UserCreate, User, current_active_user


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
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Authorization"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Authorization"],
)
# app.include_router(
#     fastapi_users.get_reset_password_router(),
#     prefix="/auth",
#     tags=["Authorization"],
# )
# app.include_router(
#     fastapi_users.get_verify_router(UserRead),
#     prefix="/auth",
#     tags=["Authorization"],
# )


@app.get("/authenticated-route", tags=["Authenticated"])
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}
