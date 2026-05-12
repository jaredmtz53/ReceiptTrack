import uuid

from sqlalchemy import Integer, Float, ForeignKey, String

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class ReceiptItem(Base):
    __tablename__ = "receipt_item"
    id: Mapped[int] = mapped_column(primary_key=True)
    item_name: Mapped[str] = mapped_column(String)
    quantity: Mapped[int] = mapped_column(Integer)
    item_price: Mapped[float] = mapped_column(Float)
    receipt_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("receipts.id", ondelete="CASCADE"))


    receipt: Mapped["Receipt"] = relationship(
        back_populates="items"
    )