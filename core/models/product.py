from sqlalchemy.orm import Mapped

from core.models.base import Base


class Product(Base):

    name: Mapped[str]
    description: Mapped[str]
    count: Mapped[int]
    price: Mapped[int]
