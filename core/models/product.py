from sqlalchemy.orm import Mapped, relationship
from typing_extensions import TYPE_CHECKING

from core.models import order_product_association_table
from core.models.base import Base


if TYPE_CHECKING:
    from .order import Order


class Product(Base):

    name: Mapped[str]
    description: Mapped[str]
    count: Mapped[int]
    price: Mapped[int]
    orders: Mapped[list['Order']] = relationship(
        secondary=order_product_association_table,
        back_populates='products',
    )