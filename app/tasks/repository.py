from icecream import ic
from sqlalchemy import select

from db.engine import async_session_sql_connect
from schema import STaskAdd, STask
from ORM import TaskOrm


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with async_session_sql_connect() as session:
            task_dict = data.model_dump()
            ic(task_dict)
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            ic()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]:
        async with async_session_sql_connect() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_schemas
