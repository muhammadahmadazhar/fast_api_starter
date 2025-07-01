from pydantic import BaseModel
from typing import List
from datetime import datetime

class MenuItemCreate(BaseModel):
    name: str
    price: float
    is_available: bool = True

class MenuItemOut(BaseModel):
    id: int
    name: str
    price: float
    is_available: bool
    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    customer_name: str
    item_ids: List[int]

class OrderOut(BaseModel):
    id: int
    customer_name: str
    created_at: datetime
    items: List[MenuItemOut]
    class Config:
        orm_mode = True
