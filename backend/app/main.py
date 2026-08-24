from fastapi import FastAPI
from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

from app.routers.category import router as category_router
from app.routers.brand import router as brand_router
from app.routers.product import router as product_router
from app.routers.supplier import router as supplier_router
from app.routers.customer import router as customer_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(category_router)
app.include_router(brand_router)
app.include_router(product_router)
app.include_router(supplier_router)
app.include_router(customer_router)


@app.get("/")
def home():
    return {"message": "FastAPI + SQLite"}