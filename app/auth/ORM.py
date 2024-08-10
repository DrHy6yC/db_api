from typing import List

from fastapi_users.db import (
    SQLAlchemyBaseOAuthAccountTableUUID,
    SQLAlchemyBaseUserTableUUID
)

from sqlalchemy.orm import Mapped, relationship

from db.engine import ModelORM, async_session_sql_connect


class OAuthAccount(SQLAlchemyBaseOAuthAccountTableUUID, ModelORM):
    pass


class User(SQLAlchemyBaseUserTableUUID, ModelORM):
    oauth_accounts: Mapped[List[OAuthAccount]] = relationship(
        "OAuthAccount", lazy="joined"
    )


connect = async_session_sql_connect
