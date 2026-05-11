from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.receipt_item import (
    get_receipt_items,
    get_receipt_item,
    update_receipt_item,
    delete_receipt_item,
)
from app.db.dependencies import get_db
from app.schemas.receipt import ReceiptItemCreate

router = APIRouter()


@router.get("/receipt/{receipt_id}/items")
def get_receipt_items_route(
    receipt_id: int,
    db: Session = Depends(get_db)
):
    return get_receipt_items(db, receipt_id)


@router.get("/receipt-item/{receipt_item_id}")
def get_receipt_item_route(
    receipt_item_id: int,
    db: Session = Depends(get_db)
):
    return get_receipt_item(db, receipt_item_id)


@router.put("/receipt-item/{receipt_item_id}")
def update_receipt_item_route(
    receipt_item_id: int,
    receipt_item_data: ReceiptItemCreate,
    db: Session = Depends(get_db)
):
    return update_receipt_item(db, receipt_item_id, receipt_item_data)


@router.delete("/receipt-item/{receipt_item_id}")
def delete_receipt_item_route(
    receipt_item_id: int,
    db: Session = Depends(get_db)
):
    return delete_receipt_item(db, receipt_item_id)