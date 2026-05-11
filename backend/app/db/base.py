from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from app.models.category import Category
from app.models.receipt import Receipt
from app.models.receipt_item import ReceiptItem
