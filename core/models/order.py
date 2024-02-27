from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing_extensions import TYPE_CHECKING

from core.models import Base, order_product_association_table

if TYPE_CHECKING:
    from .product import Product


class Order(Base):

    promocode: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now,
    )
    products: Mapped[list['Product']] = relationship(
        secondary=order_product_association_table,
        back_populates='orders',
    )