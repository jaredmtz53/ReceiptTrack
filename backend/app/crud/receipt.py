import uuid

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.receipt import Receipt
from app.models.receipt_item import ReceiptItem
from app.schemas.receipt import ReceiptCreate


def create_receipt(
    db: Session,
    receipt_data: ReceiptCreate
):
    new_receipt = Receipt(
        category_id=receipt_data.category_id,
        store_name= receipt_data.store_name,
        purchase_date= receipt_data.purchase_date,
        subtotal= receipt_data.subtotal,
        tax= receipt_data.tax,
        total= receipt_data.total,
        payment_method= receipt_data.payment_method,
        card_last_four_digits= receipt_data.card_last_four_digits,
        receipt_image_key= receipt_data.receipt_image_key,

    )

    for item_data in receipt_data.items:
        new_item = ReceiptItem(
            item_name=item_data.item_name,
            quantity=item_data.quantity,
            item_price=item_data.item_price,
        )
        new_receipt.items.append(new_item)

    db.add(new_receipt)
    db.commit()
    db.refresh(new_receipt)

    return new_receipt

def get_receipt(db: Session, receipt_id: uuid.UUID):
    stmt = select(Receipt).where(Receipt.id == receipt_id)
    receipt = db.execute(stmt).scalar_one_or_none()
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return receipt

def get_receipts(db: Session):
    stmt = select(Receipt).order_by(Receipt.created_at.desc())
    receipts = db.execute(stmt).scalars().all()
    return receipts

def update_receipt(
    db: Session,
    receipt_id: uuid.UUID,
    receipt_data: ReceiptCreate
):
    stmt = select(Receipt).where(Receipt.id == receipt_id)
    receipt = db.execute(stmt).scalar_one_or_none()
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")

    updated_data = receipt_data.model_dump(exclude={"items"})
    for key, value in updated_data.items():
        setattr(receipt, key, value)

    db.commit()
    db.refresh(receipt)

    return receipt

def delete_receipt(db: Session, receipt_id: uuid.UUID):
    stmt = select(Receipt).where(Receipt.id == receipt_id)
    receipt = db.execute(stmt).scalar_one_or_none()
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    db.delete(receipt)
    db.commit()
    return {"message": "Receipt deleted successfully"}

def update_receipt_image_key(db: Session, receipt_id: uuid.UUID, object_key: str):
    stmt = select(Receipt).where(Receipt.id == receipt_id)
    receipt = db.execute(stmt).scalar_one_or_none()
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    receipt.receipt_image_key = object_key
    db.commit()
    db.refresh(receipt)
    return receipt