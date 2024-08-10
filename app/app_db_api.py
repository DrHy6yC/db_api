from icecream import ic
from fastapi import FastAPI

from contextlib import asynccontextmanager

from tasks.router import router as tasks_router
# from auth.users import (
#     SECRET,
#     auth_backend,
#     current_active_user,
#     fastapi_users,
#     google_oauth_client,
# )


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

#
# app.include_router(
#     fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
# )
# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["auth"],
# )
# app.include_router(
#     fastapi_users.get_reset_password_router(),
#     prefix="/auth",
#     tags=["auth"],
# )
# app.include_router(
#     fastapi_users.get_verify_router(UserRead),
#     prefix="/auth",
#     tags=["auth"],
# )
# app.include_router(
#     fastapi_users.get_users_router(UserRead, UserUpdate),
#     prefix="/users",
#     tags=["users"],
# )
# app.include_router(
#     fastapi_users.get_oauth_router(google_oauth_client, auth_backend, SECRET),
#     prefix="/auth/google",
#     tags=["auth"],
# )
#
#
# @app.get("/authenticated-route")
# async def authenticated_route(user: User = Depends(current_active_user)):
#     return {"message": f"Hello {user.email}!"}
