from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.image_slide import ImageSlide
from app.schemas.image_slide import (
    ImageSlideCreate,
    ImageSlideResponse,
    ImageSlideUpdate,
)

router = APIRouter(
    prefix="/api/image_slide",
    tags=["ImageSlide"]
)

# CREATE
@router.post(
    "/",
    response_model=ImageSlideResponse,
    status_code=201
)
def create_image_slide(
    image_slide: ImageSlideCreate,
    db: Session = Depends(get_db)
):
    existing = (
        db.query(ImageSlide)
        .filter(ImageSlide.title == image_slide.title)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="ImageSlide already exists"
        )

    new_image_slide = ImageSlide(
        title=image_slide.title,
        image=image_slide.image,
        sort_order=image_slide.sort_order,
        enable=image_slide.enable
    )

    db.add(new_image_slide)
    db.commit()
    db.refresh(new_image_slide)

    return new_image_slide


# READ ALL
@router.get(
    "/",
    response_model=list[ImageSlideResponse]
)
def get_image_slides(
    db: Session = Depends(get_db)
):
    return db.query(ImageSlide).all()


# READ ONE
@router.get(
    "/{image_slide_id}",
    response_model=ImageSlideResponse
)
def get_image_slide(
    image_slide_id: int,
    db: Session = Depends(get_db)
):
    image_slide = (
        db.query(ImageSlide)
        .filter(ImageSlide.id == image_slide_id)
        .first()
    )

    if not image_slide:
        raise HTTPException(
            status_code=404,
            detail="ImageSlide not found"
        )

    return image_slide


# UPDATE
@router.put(
    "/{image_slide_id}",
    response_model= ImageSlideResponse
)
def update_image_slide(
    image_slide_id: int,
    image_slide_data: ImageSlideUpdate,
    db: Session = Depends(get_db)
):
    image_slide = (
        db.query(ImageSlide)
        .filter(ImageSlide.id == image_slide_id)
        .first()
    )

    if not image_slide:
        raise HTTPException(
            status_code=404,
            detail="ImageSlide not found"
        )

    if image_slide_data.title is not None:
        image_slide.title = image_slide_data.title

    if image_slide_data.image is not None:
        image_slide.image = image_slide_data.image

    if image_slide_data.sort_order is not None:
        image_slide.sort_order = image_slide_data.sort_order

    if image_slide_data.enable is not None:
        image_slide.enable = image_slide_data.enable

    db.commit()
    db.refresh(image_slide)

    return image_slide


# DELETE
@router.delete(
    "/{image_slide_id}",
)
def delete_image_slide(
    image_slide_id: int,
    db: Session = Depends(get_db)
):
    image_slide = (
        db.query(ImageSlide)
        .filter(ImageSlide.id == image_slide_id)
        .first()
    )

    if not image_slide:
        raise HTTPException(
            status_code=404,
            detail="Image Slide not found"
        )

    db.delete(image_slide)
    db.commit()

    return {
        "message": "Image Slide deleted successfully",
        "id": image_slide_id
    }