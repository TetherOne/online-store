from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper

from fastapi import HTTPException
from fastapi import Depends
from fastapi import status
from fastapi import Path

from core.models import Product

from typing import Annotated

from . import crud


async def product_by_id(
    product_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Product:

    product = await crud.get_product(session=session, product_id=product_id)

    if product is not None:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_id} not found!",
    )