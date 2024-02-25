from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.users.schemas import UserCreate, UserUpdatePartial, UserUpdate

from sqlalchemy import Result
from sqlalchemy import select

from core.models import User


async def get_users(session: AsyncSession) -> list[User]:

    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()

    return list(users)


async def get_user(
    session: AsyncSession,
    user_id: int,
) -> User | None:

    return await session.get(User, user_id)


async def create_user(
    session: AsyncSession,
    product_in: UserCreate,
) -> User:

    user = User(**product_in.model_dump())

    session.add(user)
    await session.commit()

    return user


async def update_user(
    session: AsyncSession,
    user: User,
    user_update: UserUpdate | UserUpdatePartial,
    partial: bool = False,
) -> User:

    for name, value in user_update.model_dump(exclude_unset=partial).items():
        setattr(user, name, value)
    await session.commit()

    return user


async def delete_user(
    session: AsyncSession,
    user: User,
) -> None:

    await session.delete(user)
    await session.commit()