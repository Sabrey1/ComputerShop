from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.product import Product
from app.schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductUpdate,
)

router = APIRouter(
    prefix="/api/product",
    tags=["Product"]
)

# CREATE
@router.post(
    "/",
    response_model=ProductResponse,
    status_code=201
)
def create_prodcut(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    existing = (
        db.query(Product)
        .filter(Product.name == product.name)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Product already exists"
        )

    new_product = Product(
        name=product.name,
        category_id=product.category_id,
        brand_id=product.brand_id,
        cost_price=product.cost_price,
        selling_price=product.selling_price,
        stock_quantity=product.stock_quantity,
        min_quantity=product.min_quantity,
        image=product.image,
        description=product.description,
        status=product.status
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

# READ ALL
@router.get(
    "/",
    response_model=list[ProductResponse]
)
def get_products(
    db: Session = Depends(get_db)
):
    return db.query(Product).all()

# READ ONE
@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product

# UPDATE
@router.put(
    "/{product_id}",
    response_model= ProductResponse
)
def update_product(
    product_id: int,
    product_data: ProductUpdate,
    db: Session = Depends(get_db)
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if product_data.name is not None:
        product.name = product_data.name

    if product_data.category_id is not None:
        product.category_id = product_data.category_id

    if product_data.brand_id is not None:
        product.brand_id = product_data.brand_id

    if product_data.description is not None:
        product.description = product_data.description

    if product_data.cost_price is not None:
        product.cost_price = product_data.cost_price

    if product_data.selling_price is not None:
        product.selling_price = product_data.selling_price

    if product_data.stock_quantity is not None:
        product.stock_quantity = product_data.stock_quantity

    if product_data.min_quantity is not None:
        product.min_quantity = product_data.min_quantity

    if product_data.status is not None:
        product.status = product_data.status

    db.commit()
    db.refresh(product)

    return product

# DELETE
@router.delete(
    "/{product_id}"
)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db.delete(product)
    db.commit()

    return {
        "message": "Product deleted successfully",
        "id": product_id
    }