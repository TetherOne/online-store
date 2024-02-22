from pydantic import ConfigDict
from pydantic import BaseModel


class ProductBase(BaseModel):

    name: str
    description: str
    count: int
    price: int


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductCreate):
    pass


class ProductUpdatePartial(ProductCreate):

    name: str | None = None
    description: str | None = None
    count: int | None = None
    price: int | None = None