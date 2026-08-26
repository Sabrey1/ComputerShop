from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.business_info import BusinessInfo
from app.schemas.business_info import (
    BussinessInfoCreate,
    BussinessInfoResponse,
    BussinessInfoUpdate,
)

router = APIRouter(
    prefix="/api/business_info",
    tags=["BusinessInfo"]
)


# CREATE
@router.post(
    "/",
    response_model=BussinessInfoResponse,
    status_code=201
)
def create_bussiness_info(
    bussiness_info: BussinessInfoCreate,
    db: Session = Depends(get_db)
):
    existing = (
        db.query(BusinessInfo)
        .filter(BusinessInfo.bussiness_name == bussiness_info.bussiness_name)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Business Info already exists"
        )

    new_bussiness = BusinessInfo(
        bussiness_name=bussiness_info.bussiness_name,
        logo=bussiness_info.logo,
        phone_number_1=bussiness_info.phone_number_1,
        phone_number_2=bussiness_info.phone_number_2,
        address=bussiness_info.address,
        status=bussiness_info.status
    )

    db.add(new_bussiness)
    db.commit()
    db.refresh(new_bussiness)

    return new_bussiness


# READ ALL
@router.get(
    "/",
    response_model=list[BussinessInfoResponse]
)
def get_bussiness_info(
    db: Session = Depends(get_db)
):
    return db.query(BusinessInfo).all()


# READ ONE
@router.get(
    "/{business_info_id}",
    response_model=BussinessInfoResponse
)
def get_business_info(
    business_info_id: int,
    db: Session = Depends(get_db)
):
    business_info = (
        db.query(BusinessInfo)
        .filter(BusinessInfo.id == business_info_id)
        .first()
    )

    if not business_info:
        raise HTTPException(
            status_code=404,
            detail="Bussiness Info not found"
        )

    return business_info


# UPDATE
@router.put(
    "/{bussiness_info_id}",
    response_model= BussinessInfoResponse
)
def update_business_info(
    business_info_id: int,
    bussiness_info_data: BussinessInfoUpdate,
    db: Session = Depends(get_db)
):
    bussiness_info = (
        db.query(BusinessInfo)
        .filter(BusinessInfo.id == business_info_id)
        .first()
    )

    if not bussiness_info:
        raise HTTPException(
            status_code=404,
            detail="Bussiness Info not found"
        )

    if bussiness_info_data.bussiness_name is not None:
        bussiness_info.bussiness_name = bussiness_info_data.bussiness_name

    if bussiness_info_data.logo is not None:
        bussiness_info.logo = bussiness_info_data.logo

    if bussiness_info_data.phone_number_1 is not None:
        bussiness_info.phone_number_1 = bussiness_info_data.phone_number_1

    if bussiness_info_data.phone_number_2 is not None:
        bussiness_info.phone_number_2 = bussiness_info_data.phone_number_2

    if bussiness_info_data.address is not None:
        bussiness_info.address = bussiness_info_data.address

    if bussiness_info_data.status is not None:
        bussiness_info.status = bussiness_info_data.status

    db.commit()
    db.refresh(bussiness_info)

    return bussiness_info


# DELETE
@router.delete(
    "/{bussiness_info_id}"
)
def delete_business_info(
    bussiness_info_id: int,
    db: Session = Depends(get_db)
):
    bussiness_info = (
        db.query(BusinessInfo)
        .filter(BusinessInfo.id == bussiness_info_id)
        .first()
    )

    if not bussiness_info:
        raise HTTPException(
            status_code=404,
            detail="Bussiness Info not found"
        )

    db.delete(bussiness_info)
    db.commit()

    return {
        "message": "Bussiness Info deleted successfully",
        "id": bussiness_info_id
    }