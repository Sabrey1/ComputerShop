from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CustomerCreate(BaseModel):
    name: str
    phone: str | None = None
    address: str | None = None
    status: bool = True


class CustomerUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    address: str | None = None
    status: bool | None = None


class CustomerResponse(BaseModel):
    id: int
    name: str
    phone: str
    address: str | None
    status: bool
    created_at: datetime
    updated_at: datetime

class BrandSample(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)