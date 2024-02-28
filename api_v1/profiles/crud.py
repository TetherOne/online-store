from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.profiles.schemas import ProfileUpdate, ProfileUpdatePartial
from core.models import Profile


async def get_profiles(
    session: AsyncSession,
) -> list[Profile]:

    stmt = select(Profile).order_by(Profile.id)
    result: Result = await session.execute(stmt)
    profiles = result.scalars().all()

    return list(profiles)


async def get_profile(
    session: AsyncSession,
    profile_id: int,
) -> Profile | None:

    return await session.get(Profile, profile_id)


async def update_profile(
    session: AsyncSession,
    profile: Profile,
    profile_update: ProfileUpdate | ProfileUpdatePartial,
    partial: bool = False,
) -> Profile:

    for name, value in profile_update.model_dump(exclude_unset=partial).items():
        setattr(profile, name, value)

    await session.commit()

    return profile