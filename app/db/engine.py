from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base

from database import DBAPP
from config_db import DB_ECHO

Base = declarative_base()


class ModelORM(DeclarativeBase):
    pass


db_app = DBAPP()
is_echo_db = DB_ECHO
dns_sql = db_app.get_async_dsn()

sql_async_engine = db_app.get_async_engine(is_echo_db)
async_session_sql_connect = db_app.get_async_sessionmaker(is_echo_db)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_sql_connect() as session:
        yield session
