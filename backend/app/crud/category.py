from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate


def create_category(
    db: Session,
    category_data: CategoryCreate,
):
    stmt = select(Category).where(Category.name == category_data.title)
    existing_category = db.execute(stmt).scalar()

    if existing_category:
        raise HTTPException(status_code=400, detail="Category already exists")

    new_category = Category(name = category_data.title)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category

def delete_category(db: Session, category_id: int):
    stmt = select(Category).where(Category.id == category_id)

    category = db.execute(stmt).scalar_one_or_none()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()

def get_category(db: Session, category_id: int):
    stmt = select(Category).where(Category.id == category_id)
    category = db.execute(stmt).scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

def get_categories(db: Session):
    stmt = select(Category)
    categories = db.execute(stmt).scalars().all()
    if not categories:
        raise HTTPException(status_code=404, detail="Categories not found")
    return categories

def update_category(db: Session, category_id: int, category_data: CategoryCreate):
    stmt = select(Category).where(Category.id == category_id)
    category = db.execute(stmt).scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    category.name = category_data.title

    db.commit()
    db.refresh(category)
    return category