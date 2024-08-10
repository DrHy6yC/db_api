from ORM import *
from database import DBAPP
from config_db import DB_ECHO

db_app = DBAPP()
is_echo_db = DB_ECHO
sql_async_engine = db_app.get_async_engine(is_echo_db)
async_session_sql_connect = db_app.get_async_sessionmaker(is_echo_db)


# async def test_connection():
#     try:


async def create_tables():
    async with sql_async_engine.begin() as conn:
        await conn.run_sync(ModelORM.metadata.create_all)


async def delete_tables():
    async with sql_async_engine.begin() as conn:
        await conn.run_sync(ModelORM.metadata.drop_all)
