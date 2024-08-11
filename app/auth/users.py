import uuid
import redis.asyncio

from typing import AsyncGenerator, Optional

from fastapi import Depends, Request
from fastapi_users import schemas, BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    RedisStrategy,
)
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from db.engine import dns_sql

SECRET = "SECRET"
DATABASE_URL = dns_sql

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


cookie_transport = CookieTransport(cookie_max_age=3600)


redis = redis.asyncio.from_url("redis://localhost:6380", decode_responses=True)


def get_redis_strategy() -> RedisStrategy:
    return RedisStrategy(redis, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="api_db_auth",
    transport=cookie_transport,
    get_strategy=get_redis_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
