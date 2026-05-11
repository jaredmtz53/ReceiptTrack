from datetime import datetime

from pydantic import BaseModel

class ReceiptItemCreate(BaseModel):
    item_name: str
    quantity: int
    item_price: float

class ReceiptCreate(BaseModel):
    category_id: int
    store_name: str
    purchase_date: datetime
    subtotal: float
    tax: float
    total: float
    payment_method: str | None = None
    card_last_four_digits: str | None = None
    receipt_image_url: str | None = None
    items: list[ReceiptItemCreate] 

class ResponseReceipt(BaseModel):
    receipt_id: int
    status: str
    created_at: datetime




