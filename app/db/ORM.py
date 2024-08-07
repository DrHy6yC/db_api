from typing import Optional


from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class ModelORM(DeclarativeBase):
    pass


class TaskOrm(ModelORM):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
