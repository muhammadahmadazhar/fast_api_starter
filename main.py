from fastapi import FastAPI
from app.routes import menu, order

app = FastAPI()

app.include_router(menu.router, prefix="/menu", tags=["Menu"])
app.include_router(order.router, prefix="/order", tags=["Order"])
