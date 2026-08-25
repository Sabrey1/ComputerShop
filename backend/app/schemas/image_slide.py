from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ImageSlideCreate(BaseModel):
    title: str
    image: str | None = None
    sort_order: int
    enable: bool = True


class ImageSlideUpdate(BaseModel):
    title: str | None = None
    image: str | None = None
    sort_order: int | None = None
    enable: bool | None = None


class ImageSlideResponse(BaseModel):
    id: int
    title: str
    image: str
    sort_order: int
    enable: bool