from ORM import *
from engine import sql_async_engine


async def create_tables():
    async with sql_async_engine.begin() as conn:
        await conn.run_sync(ModelORM.metadata.create_all)


async def delete_tables():
    async with sql_async_engine.begin() as conn:
        await conn.run_sync(ModelORM.metadata.drop_all)
