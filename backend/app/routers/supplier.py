from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.supplier import Supplier
from app.schemas.supplier import (
    SupplierCreate,
    SupplierResponse,
    SupplierUpdate,
)

router = APIRouter(
    prefix="/api/supplier",
    tags=["Supplier"]
)


# CREATE
@router.post(
    "/",
    response_model=SupplierResponse,
    status_code=201
)
def create_supplier(
    supplier: SupplierCreate,
    db: Session = Depends(get_db)
):
    existing = (
        db.query(Supplier)
        .filter(Supplier.name == supplier.name)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Supplier already exists"
        )

    new_supplier = Supplier(
        name=supplier.name,
        contact_person=supplier.contact_person,
        phone=supplier.phone,
        email=supplier.email,
        address=supplier.address,
        status=supplier.status
    )

    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)

    return new_supplier


# READ ALL
@router.get(
    "/",
    response_model=list[SupplierResponse]
)
def get_suppliers(
    db: Session = Depends(get_db)
):
    return db.query(Supplier).all()


# READ ONE
@router.get(
    "/{supplier_id}",
    response_model=SupplierResponse
)
def get_supplier(
    supplier_id: int,
    db: Session = Depends(get_db)
):
    supplier = (
        db.query(Supplier)
        .filter(Supplier.id == supplier_id)
        .first()
    )

    if not supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    return supplier


# UPDATE
@router.put(
    "/{supplier_id}",
    response_model=SupplierResponse
)
def update_supplier(
    supplier_id: int,
    supplier_data: SupplierUpdate,
    db: Session = Depends(get_db)
):
    supplier = (
        db.query(Supplier)
        .filter(Supplier.id == supplier_id)
        .first()
    )

    if not supplier:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    if supplier_data.name is not None:
        supplier.name = supplier_data.name

    if supplier_data.contact_person is not None:
        supplier.contact_person = supplier_data.contact_person

    if supplier_data.phone is not None:
        supplier.phone = supplier_data.phone

    if supplier_data.email is not None:
        supplier.email = supplier_data.email

    if supplier_data.address is not None:
        supplier.address = supplier_data.address

    if supplier_data.status is not None:
        supplier.status = supplier_data.status

    db.commit()
    db.refresh(supplier)

    return supplier


# DELETE
@router.delete(
    "/{supplier_id}"
)
def delete_supplier(
    supplier_id: int,
    db: Session = Depends(get_db)
):
    supplier = (
        db.query(Supplier)
        .filter(Supplier.id == supplier_id)
        .first()
    )

    if not supplier:
        raise HTTPException(
            status_code=404,
            detail="Supplier not found"
        )

    db.delete(supplier)
    db.commit()

    return {
        "message": "Supplier deleted successfully",
        "id": supplier_id
    }