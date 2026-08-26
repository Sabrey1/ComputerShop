from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BussinessInfoCreate(BaseModel):
    bussiness_name: str
    logo: str | None = None
    phone_number_1: str | None = None
    phone_number_2: str | None = None
    address: str | None = None
    status: bool = True


class BussinessInfoUpdate(BaseModel):
    bussiness_name: str | None = None
    logo: str | None = None
    phone_number_1: str | None = None
    phone_number_2: str | None = None
    address: str | None = None
    status: bool | None = None


class BussinessInfoResponse(BaseModel):
    id: int
    bussiness_name: str
    logo: str
    phone_number_1: str
    phone_number_2: str
    address: str
    status: bool