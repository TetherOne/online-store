from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper

from fastapi import HTTPException
from fastapi import Depends
from fastapi import status
from fastapi import Path

from core.models import User

from typing import Annotated

from . import crud


async def user_by_id(
        user_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User:

    user = await crud.get_user(session=session, user_id=user_id)

    if user is not None:

        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'User {user_id} not found',
    )