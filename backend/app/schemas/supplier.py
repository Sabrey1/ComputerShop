from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SupplierCreate(BaseModel):
    name: str
    contact_person : str | None = None
    phone : str | None = None
    email : str | None = None
    address  : str | None = None
    status: bool = True


class SupplierUpdate(BaseModel):
    name: str | None = None
    contact_person: str | None = None
    phone: str | None = None
    email: str | None = None
    address: str | None = None
    status: bool | None = None


class SupplierResponse(BaseModel):
    id: int
    name: str
    contact_person: str
    phone: str
    email: str | None
    address: str | None
    status: bool
    created_at: datetime
    updated_at: datetime

class SupplierSample(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)