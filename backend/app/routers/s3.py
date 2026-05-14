import uuid

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.crud.receipt import update_receipt_image_key, get_receipt
from app.db.dependencies import get_db
from app.services.s3 import upload_receipt_image, generate_receipt_image_url

router = APIRouter(
    prefix="/upload",
    tags=["upload"],
)


@router.post("/receipt/{receipt_id}/image")
async def upload_receipt_image_route(
    receipt_id: uuid.UUID,
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    object_key = upload_receipt_image(image)

    receipt = update_receipt_image_key(
        db=db,
        receipt_id=receipt_id,
        object_key=object_key,
    )

    return {
        "message": "Receipt image uploaded successfully",
        "receipt_id": receipt.id,
        "receipt_image_key": receipt.receipt_image_key,
    }

