# TODO: Implement order endpoints

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_, func
from typing import List
from datetime import datetime, date

from app import models, schemas
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.OrderOut)
def place_order(order_data: schemas.OrderCreate, db: Session = Depends(get_db)):
    items = (
        db.query(models.MenuItem)
        .filter(models.MenuItem.id.in_(order_data.item_ids), models.MenuItem.is_available == True)
        .all()
    )

    if len(items) != len(order_data.item_ids):
        raise HTTPException(status_code=400, detail="One or more items are not available or do not exist")

    total_price = sum(item.price for item in items)

    new_order = models.Order(customer_name=order_data.customer_name, items=items)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    # Step 4: Log to file
    timestamp = new_order.created_at.strftime("%Y-%m-%d %H:%M:%S")
    item_ids_str = ",".join(str(i.id) for i in items)
    log_entry = f"{timestamp} | {new_order.customer_name} | {item_ids_str} | {total_price:.2f}\n"

    with open("orders_log.txt", "a") as f:
        f.write(log_entry)

    return new_order


@router.get("/today/", response_model=List[schemas.OrderOut])
def get_todays_orders(db: Session = Depends(get_db)):
    today_start = datetime.combine(date.today(), datetime.min.time())
    today_end = datetime.combine(date.today(), datetime.max.time())

    orders = (
        db.query(models.Order)
        .filter(and_(models.Order.created_at >= today_start, models.Order.created_at <= today_end))
        .all()
    )
    return orders

