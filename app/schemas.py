from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class MenuItemCreate(BaseModel):
    name: str = Field(..., example="Chicken Biryani")
    price: float = Field(..., example=450.0)
    is_available: bool = Field(default=True, example=True)

class MenuItemOut(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="Chicken Biryani")
    price: float = Field(..., example=450.0)
    is_available: bool = Field(..., example=True)

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    customer_name: str = Field(..., example="Ali")
    item_ids: List[int] = Field(..., example=[1, 2])

class OrderOut(BaseModel):
    id: int = Field(..., example=1)
    customer_name: str = Field(..., example="Ali")
    created_at: datetime = Field(..., example="2025-07-01T10:30:00")
    items: List[MenuItemOut]

    class Config:
        orm_mode = True

