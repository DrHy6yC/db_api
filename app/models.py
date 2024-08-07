from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from engine import sql_async_engine


class Model(DeclarativeBase):
    pass


class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]


async def create_tables():
    async with sql_async_engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with sql_async_engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
