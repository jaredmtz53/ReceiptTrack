import datetime

import uuid
from sqlalchemy import UUID, ForeignKey, String, DateTime, Float, Integer

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.category import Category


class Receipt(Base):
    __tablename__ = "receipts"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey('categories.id')

    )
    store_name: Mapped[str] = mapped_column(
        String(100)
    )
    purchase_date: Mapped[datetime.datetime] = mapped_column(
        DateTime
    )
    subtotal: Mapped[float] = mapped_column(
        Float,
        default=0
    )
    tax: Mapped[float] = mapped_column(
        Float,
        default=0
    )
    total: Mapped[float] = mapped_column(
        Float
    )
    payment_method: Mapped[str|None] = mapped_column(
        String,
        nullable=True

    )
    card_last_four_digits: Mapped[str|None] = mapped_column(
        String(4),
        nullable=True
    )
    status: Mapped[str] = mapped_column(
        String(20),
        default="processing"
    )
    receipt_image_url: Mapped[str|None] = mapped_column(
        String,
        nullable=True
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(),
        default=datetime.datetime.now
    )

    category: Mapped["Category"] = relationship(
        back_populates="receipts"
    )

    items: Mapped[list["ReceiptItem"]] = relationship(
        back_populates="receipt",
        cascade="all, delete-orphan"
    )

