from models import *


async def create_tables():
    async with sql_async_engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with sql_async_engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
