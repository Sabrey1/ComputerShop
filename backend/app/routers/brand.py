from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.brand import Brand
from app.schemas.brand import (
    BrandCreate,
    BrandResponse,
    BrandUpdate,
)

router = APIRouter(
    prefix="/api/brand",
    tags=["Brand"]
)


# CREATE
@router.post(
    "/",
    response_model=BrandResponse,
    status_code=201
)
def create_brand(
    brand: BrandCreate,
    db: Session = Depends(get_db)
):
    existing = (
        db.query(Brand)
        .filter(Brand.name == brand.name)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Brand already exists"
        )

    new_brand = Brand(
        name=brand.name,
        logo=brand.logo,
        status=brand.status
    )

    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)

    return new_brand


# READ ALL
@router.get(
    "/",
    response_model=list[BrandResponse]
)
def get_brands(
    db: Session = Depends(get_db)
):
    return db.query(Brand).all()


# READ ONE
@router.get(
    "/{brand_id}",
    response_model=BrandResponse
)
def get_brand(
    brand_id: int,
    db: Session = Depends(get_db)
):
    brand = (
        db.query(Brand)
        .filter(Brand.id == brand_id)
        .first()
    )

    if not brand:
        raise HTTPException(
            status_code=404,
            detail="Brand not found"
        )

    return brand


# UPDATE
@router.put(
    "/{brand_id}",
    response_model= BrandResponse
)
def update_brand(
    brand_id: int,
    brand_data: BrandUpdate,
    db: Session = Depends(get_db)
):
    brand = (
        db.query(Brand)
        .filter(Brand.id == brand_id)
        .first()
    )

    if not brand:
        raise HTTPException(
            status_code=404,
            detail="Brand not found"
        )

    if brand_data.name is not None:
        brand.name = brand_data.name

    if brand_data.logo is not None:
        brand.logo = brand_data.logo

    if brand_data.status is not None:
        brand.status = brand_data.status

    db.commit()
    db.refresh(brand)

    return brand


# DELETE
@router.delete(
    "/{brand_id}"
)
def delete_brand(
    brand_id: int,
    db: Session = Depends(get_db)
):
    brand = (
        db.query(Brand)
        .filter(Brand.id == brand_id)
        .first()
    )

    if not brand:
        raise HTTPException(
            status_code=404,
            detail="Brand not found"
        )

    db.delete(brand)
    db.commit()

    return {
        "message": "Brand deleted successfully",
        "id": brand_id
    }