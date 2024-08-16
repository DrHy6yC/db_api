from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from db.engine import dns_sql_bot, ModelORM


DATABASE_URL = dns_sql_bot

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(ModelORM.metadata.create_all)
