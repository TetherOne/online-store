from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Order


async def get_orders(
    session: AsyncSession,
) -> list[Order]:

    stmt = select(Order).order_by(Order.id)
    result: Result = await session.execute(stmt)
    orders = result.scalars().all()

    return list(orders)


async def get_order(
    session: AsyncSession,
    order_id: int,
) -> Order | None:

    return await session.get(Order, order_id)