from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper
from .schemas import ProductCreate
from .schemas import Product

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from . import crud


router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_product(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.get_products(session=session)


@router.post("/")
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}", response_model=Product)
async def get_product(
    product_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    product = await crud.get_product(session=session, product_id=product_id)

    if product is not None:
        return product

    return f"Product {product_id} not found"
