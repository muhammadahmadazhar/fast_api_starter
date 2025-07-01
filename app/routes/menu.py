# TODO: Implement menu endpoints
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.MenuItemOut)
def create_menu_item(menu_item: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    db_item = models.MenuItem(**menu_item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/available/", response_model=List[schemas.MenuItemOut])
def get_available_menu_items(db: Session = Depends(get_db)):
    items = db.query(models.MenuItem).filter(models.MenuItem.is_available == True).all()
    return items