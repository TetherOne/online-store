from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from sqlalchemy.ext.asyncio import AsyncSession

from ..config import async_session_maker

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped

from core.models.base import Base

from typing import AsyncGenerator
from typing import TYPE_CHECKING

from sqlalchemy import String

from fastapi import Depends


if TYPE_CHECKING:
    from .profile import Profile


class User(Base, SQLAlchemyBaseUserTable[int]):

    username: Mapped[str] = mapped_column(String(30))
    profile: Mapped['Profile'] = relationship(back_populates='user', cascade='all,delete')


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:

    session = None

    try:
        async with async_session_maker() as s:

            session = s
            yield session

    except GeneratorExit:

        if session:
            await session.close()

        raise


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)