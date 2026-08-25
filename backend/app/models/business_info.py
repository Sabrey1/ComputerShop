from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func
from app.database import Base


class BusinessInfo(Base):
    __tablename__ = "business_info"

    id = Column(Integer, primary_key=True, index=True)
    bussiness_name = Column(String(100), nullable=False, unique=True)
    logo = Column(String(255), nullable=True)
    phone_number_1 = Column(String(100), nullable=True)
    phone_number_2 = Column(String(100), nullable=True)
    address = Column(String(100), nullable=True)
    status = Column(Boolean, default=True, nullable=False)

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