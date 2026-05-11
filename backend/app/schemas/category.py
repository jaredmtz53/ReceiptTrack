from pydantic import BaseModel

class CategoryCreate(BaseModel):
    title: str

class CategoryResponse(BaseModel):
    category_id: int
    title: str
