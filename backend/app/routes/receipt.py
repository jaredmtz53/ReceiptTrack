from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.receipt import get_receipt, get_receipts, create_receipt, update_receipt, delete_receipt
from app.db.dependencies import get_db
from app.schemas.receipt import ReceiptCreate

router = APIRouter()


@router.get("/receipt/{receipt_id}")
def get_receipt_route(receipt_id: int, db: Session = Depends(get_db)):
    return get_receipt(db, receipt_id)


@router.get("/receipt")
def get_all_receipt_route(db: Session = Depends(get_db)):
    return get_receipts(db)


@router.post("/receipt")
def create_receipt_route(receipt_data: ReceiptCreate, db: Session = Depends(get_db)):
    return create_receipt(db, receipt_data)


@router.put("/receipt/{receipt_id}")
def update_receipt_route(receipt_id: int, receipt_data: ReceiptCreate, db: Session = Depends(get_db), ):
    return update_receipt(db, receipt_id, receipt_data)


@router.delete("/receipt/{receipt_id}")
def delete_receipt_route(receipt_id: int, db: Session = Depends(get_db)):
    return delete_receipt(db, receipt_id)
