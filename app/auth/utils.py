from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, BearerTransport
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from models import User, Base
from redis_strategy import get_redis_strategy
from user_manager import UserManager
from db.engine import dns_sql_api


DATABASE_URL = dns_sql_api

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


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


bearer_transport = BearerTransport(tokenUrl="auth/login")


auth_backend = AuthenticationBackend(
    name="api_db_auth",
    transport=bearer_transport,
    get_strategy=get_redis_strategy,
)

fastapi_users_param = FastAPIUsers[User, int](get_user_manager, [auth_backend])

current_active_user = fastapi_users_param.current_user(active=True)
