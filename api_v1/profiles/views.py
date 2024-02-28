from fastapi import APIRouter, Depends
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.profiles import crud
from .dependencies import profile_by_id
from .schemas import Profile, ProfileUpdatePartial, ProfileUpdate
from core.models.db_helper import db_helper

router = APIRouter(tags=["Profiles"])


@router.get(
    "/",
    response_model=list[Profile],
    status_code=status.HTTP_200_OK,
)
async def get_profiles(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.get_profiles(session=session)


@router.get(
    "/{profile_id}",
    response_model=Profile,
    status_code=status.HTTP_200_OK,
)
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

    return await crud.update_profile(
        session=session,
        profile=profile,
        profile_update=profile_update,
        partial=True,
    )