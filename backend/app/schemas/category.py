from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CategoryCreate(BaseModel):
    name: str
    description: str | None = None
    status: bool = True


class CategoryUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    status: bool | None = None


class CategoryResponse(BaseModel):
    id: int
    name: str
    description: str | None
    status: bool
    created_at: datetime
    updated_at: datetime

class CategorySample(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)