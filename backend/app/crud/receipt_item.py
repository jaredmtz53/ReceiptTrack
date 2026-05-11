from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import receipt_item
from app.models.receipt_item import ReceiptItem
from app.schemas.receipt import ReceiptItemCreate


def get_receipt_items(db: Session, receipt_id: int):
    stmt = select(ReceiptItem).where(ReceiptItem.receipt_id == receipt_id)
    receipt_items = db.execute(stmt).scalars().all()
    return receipt_items

def get_receipt_item(db: Session, receipt_item_id: int):
    stmt = select(ReceiptItem).where(
        ReceiptItem.id == receipt_item_id
    )

    receipt_item = db.execute(stmt).scalar_one_or_none()

    if not receipt_item:
        raise HTTPException(
            status_code=404,
            detail="Receipt item not found"
        )

    return receipt_item

def update_receipt_item(db: Session, receipt_item_id: int, receipt_item_data: ReceiptItemCreate):
    stmt = select(ReceiptItem).where(ReceiptItem.id == receipt_item_id)
    receipt_item = db.execute(stmt).scalar_one_or_none()
    if not receipt_item:
        raise HTTPException(
            status_code=404,
            detail="Receipt item not found"
        )

    updated_data = receipt_item_data.model_dump()
    for key, val in updated_data.items():
        setattr(receipt_item, key, val)
    db.commit()
    db.refresh(receipt_item)
    return receipt_item

def delete_receipt_item(db: Session, receipt_item_id: int):
    stmt = select(ReceiptItem).where(ReceiptItem.id == receipt_item_id)
    receipt_item = db.execute(stmt).scalar_one_or_none()
    if not receipt_item:
        raise HTTPException(
            status_code=404,
            detail="Receipt item not found"
        )
    db.delete(receipt_item)
    db.commit()
    return receipt_item