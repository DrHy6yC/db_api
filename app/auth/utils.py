from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase

from ORM import User, OAuthAccount, connect


async def get_user_db(session: AsyncSession = Depends(connect)):
    yield SQLAlchemyUserDatabase(session, User, OAuthAccount)
