from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import ProfileUpdatePartial
from .schemas import ProfileUpdate
from .schemas import Profile

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from core.models.db_helper import db_helper

from .dependencies import profile_by_id

from api_v1.profiles import crud


router = APIRouter(tags=["Profiles"])


@router.get(
    "/",
    response_model=list[Profile],
    status_code=status.HTTP_200_OK,
)
@cache(namespace='store', expire=60)
async def get_profiles(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.get_profiles(session=session)


@router.get(
    "/{profile_id}",
    response_model=Profile,
    status_code=status.HTTP_200_OK,
)
@cache(namespace='store', expire=60)
async def get_product(
    profile: Profile = Depends(profile_by_id),
):

    return profile


@router.put("/{profile_id}")
async def update_product(
    profile_update: ProfileUpdate,
    profile: Profile = Depends(profile_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    await FastAPICache.clear(namespace='store')

    return await crud.update_profile(
        session=session,
        profile=profile,
        profile_update=profile_update,
    )


@router.patch("/{profile_id}")
async def update_product_partial(
    profile_update: ProfileUpdatePartial,
    profile: Profile = Depends(profile_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    await FastAPICache.clear(namespace='store')

    return await crud.update_profile(
        session=session,
        profile=profile,
        profile_update=profile_update,
        partial=True,
    )