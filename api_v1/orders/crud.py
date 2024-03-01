from sqlalchemy import select, Result, delete
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Order, order_product_association_table


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


async def delete_order(
    session: AsyncSession,
    order_id: int,
) -> None:

    order = await session.get(Order, order_id)
    if order is None:
        return

    await session.execute(delete(order_product_association_table).where(
        order_product_association_table.c.order_id == order.id
    ))

    await session.delete(order)
    await session.commit()