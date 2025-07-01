import time
from fastapi import FastAPI, Request
from app.routes import menu, order

app = FastAPI()

@app.middleware("http")
async def log_request_path_and_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    print(f"[LOG] {request.method} {request.url.path} - {duration:.4f} seconds")
    return response

app.include_router(menu.router, prefix="/menu", tags=["Menu"])
app.include_router(order.router, prefix="/order", tags=["Order"])

