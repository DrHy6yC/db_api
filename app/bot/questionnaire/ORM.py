import datetime
from typing import Annotated

from sqlalchemy import BigInteger, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from db.engine import ModelORM


int_pk = Annotated[int, mapped_column(primary_key=True)]
big_int = Annotated[int, mapped_column(BigInteger)]
big_int_uniq = Annotated[int, mapped_column(BigInteger, unique=True)]
int_serv_def_0 = Annotated[int, mapped_column(server_default='0')]
int_serv_def_1 = Annotated[int, mapped_column(server_default='1')]

date_now = Annotated[datetime.datetime, mapped_column(server_default=func.now())]

txt = Annotated[str, mapped_column(Text)]

str_512 = Annotated[str, mapped_column(String(512))]
str_256 = Annotated[str, mapped_column(String(256))]
str_50 = Annotated[str, mapped_column(String(50))]


class QuestionnaireOrm(ModelORM):
    __tablename__ = "questionnaire"

    id: Mapped[int_pk]
    questionnaire_name: Mapped[str_50] = mapped_column(unique=True)
    questionnaire_description: Mapped[str_256]
    create_time: Mapped[date_now]
