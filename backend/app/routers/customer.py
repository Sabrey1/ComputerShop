from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.customer import Customer
from app.schemas.customer import (
    CustomerCreate,
    CustomerResponse,
    CustomerUpdate,
)

router = APIRouter(
    prefix="/api/customer",
    tags=["Customer"]
)


# CREATE
@router.post(
    "/",
    response_model=CustomerResponse,
    status_code=201
)
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    existing = (
        db.query(Customer)
        .filter(Customer.name == customer.name)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Customer already exists"
        )

    new_customer = Customer(
        name=customer.name,
        phone=customer.phone,
        
        address=customer.address,
        status=customer.status
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


# READ ALL
@router.get(
    "/",
    response_model=list[CustomerResponse]
)
def get_customers(
    db: Session = Depends(get_db)
):
    return db.query(Customer).all()


# READ ONE
@router.get(
    "/{customer_id}",
    response_model=CustomerResponse
)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = (
        db.query(Customer)
        .filter(Customer.id == customer_id)
        .first()
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


# UPDATE
@router.put(
    "/{customer_id}",
    response_model= CustomerResponse
)
def update_customer(
    customer_id: int,
    customer_data: CustomerUpdate,
    db: Session = Depends(get_db)
):
    customer = (
        db.query(Customer)
        .filter(Customer.id == customer_id)
        .first()
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    if customer_data.name is not None:
        customer.name = customer_data.name

    if customer_data.phone is not None:
        customer.phone = customer_data.phone
 

    if customer_data.address is not None:
        customer.address = customer_data.address

    if customer_data.status is not None:
        customer.status = customer_data.status

    db.commit()
    db.refresh(customer)

    return customer


# DELETE
@router.delete(
    "/{customer_id}"
)
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = (
        db.query(Customer)
        .filter(Customer.id == customer_id)
        .first()
    )

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    db.delete(customer)
    db.commit()

    return {
        "message": "Customer deleted successfully",
        "id": customer_id
    }