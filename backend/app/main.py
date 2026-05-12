from fastapi import FastAPI
from .routers import category, receipt_item, receipt

app = FastAPI()

app.include_router(category.router)
app.include_router(receipt.router)
app.include_router(receipt_item.router)