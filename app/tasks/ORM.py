from typing import Optional
from db.engine import ModelORM


from sqlalchemy.orm import Mapped, mapped_column


class TaskOrm(ModelORM):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
