from aiocache.serializers import PickleSerializer

from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper

from fastapi_cache.decorator import cache

from .schemas import ProfileUpdatePartial
from .schemas import ProfileUpdate
from .schemas import Profile

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from config import REDIS_PORT

from .dependencies import profile_by_id

from api_v1.profiles import crud

from aiocache import cached
from aiocache import Cache


router = APIRouter(tags=["Profiles"])


cache = Cache(
    Cache.REDIS,
    endpoint="redis-store",
    port=REDIS_PORT,
    namespace="store",
)


@router.get(
    "/",
    response_model=list[Profile],
    status_code=status.HTTP_200_OK,
)
@cached(
    ttl=60,
    cache=Cache.REDIS,
    key="profiles",
    serializer=PickleSerializer(),
    namespace="store",
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
@cached(
    ttl=60,
    cache=Cache.REDIS,
    key="profiles",
    serializer=PickleSerializer(),
    namespace="store",
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

    await cache.delete("profiles")

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

    await cache.delete("profiles")

    return await crud.update_profile(
        session=session,
        profile=profile,
        profile_update=profile_update,
        partial=True,
    )
