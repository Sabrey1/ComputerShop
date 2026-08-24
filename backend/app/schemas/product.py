from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

from app.schemas.category import CategorySample
from app.schemas.brand import BrandSample


class ProductCreate(BaseModel):
    name: str
    category_id: int
    brand_id: int
    description: str
    cost_price: int
    selling_price: int
    stock_quantity: int
    min_quantity: int
    image: str
    status: bool = True


class ProductUpdate(BaseModel):
    name: str | None = None
    category_id: str | None = None
    brand_id: int | None = None
    description: str | None = None
    cost_price: int | None = None
    selling_price: int | None = None
    stock_quantity: int | None = None
    min_quantity: int | None = None
    image: str | None = None
    status: bool | None = None


class ProductResponse(BaseModel):
    id: int
    name: str
    image: str | None
    category: CategorySample
    brand:  BrandSample | None
    description: str
    cost_price: int
    selling_price: int
    stock_quantity: int
    min_quantity: int
    status: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)