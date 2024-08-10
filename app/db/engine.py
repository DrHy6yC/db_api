from sqlalchemy.orm import DeclarativeBase

from database import DBAPP
from config_db import DB_ECHO


class ModelORM(DeclarativeBase):
    pass


db_app = DBAPP()
is_echo_db = DB_ECHO

sql_async_engine = db_app.get_async_engine(is_echo_db)
async_session_sql_connect = db_app.get_async_sessionmaker(is_echo_db)


async def create_tables(model: ModelORM):
    async with sql_async_engine.begin() as conn:
        await conn.run_sync(model.metadata.create_all)


async def delete_tables(model: ModelORM):
    async with sql_async_engine.begin() as conn:
        await conn.run_sync(model.metadata.drop_all)
