from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False
    )

    brand_id = Column(
        Integer,
        ForeignKey("brands.id"),
        nullable=False
    )
    description = Column(Text, nullable=True)
    status = Column(Boolean, default=True, nullable=False)
    cost_price = Column(Integer, nullable=False)
    selling_price = Column(Integer, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    min_quantity = Column(Integer, nullable=False)
    image = Column(String(100), nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    category = relationship("Category", back_populates="products")
    brand = relationship("Brand", back_populates="products")