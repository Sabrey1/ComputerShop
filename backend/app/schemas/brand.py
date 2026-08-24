from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BrandCreate(BaseModel):
    name: str
    logo: str | None = None
    status: bool = True


class BrandUpdate(BaseModel):
    name: str | None = None
    logo: str | None = None
    status: bool | None = None


class BrandResponse(BaseModel):
    id: int
    name: str
    logo: str | None
    status: bool
    created_at: datetime
    updated_at: datetime

class BrandSample(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)