from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.category import get_category, create_category, update_category, delete_category, get_categories
from app.db.dependencies import get_db
from app.schemas.category import CategoryCreate

router = APIRouter()


@router.get("/category/{category_id}")
def get_category_route(category_id: int, db: Session = Depends(get_db)):
    return get_category(db, category_id)


@router.get("/categories")
def get_categories_route(db: Session = Depends(get_db)):
    return get_categories(db)


@router.post("/category")
def create_category_route(category_data: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category_data)


@router.put("/category/{category_id}")
def update_category_route(category_id: int, category_data: CategoryCreate, db: Session = Depends(get_db)):
    return update_category(db, category_id, category_data)


@router.delete("/category/{category_id}")
def delete_category_route(category_id: int, db: Session = Depends(get_db)):
    return delete_category(db, category_id)
