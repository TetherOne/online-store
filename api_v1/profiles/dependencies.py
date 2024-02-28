from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper

from fastapi import HTTPException
from fastapi import Depends
from fastapi import status
from fastapi import Path

from api_v1.profiles import crud

from core.models import Profile

from typing import Annotated


async def profile_by_id(
    profile_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Profile:

    profile = await crud.get_profile(
        session=session,
        profile_id=profile_id,
    )

    if profile is not None:
        return profile

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Profile {profile_id} not found!",
    )