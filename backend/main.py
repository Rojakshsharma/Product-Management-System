from fastapi import Depends ,  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import SessionLocal , engine
import model
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)
model.Base.metadata.create_all(bind = engine)

@app.get("/")
def greet():
    return "Welcome to fast api project"

data = [
    Product(
        id=1,
        name="Shirt",
        description="Blue cotton shirt",
        price=200,
        quantity=4
    ),
    Product(
        id=2,
        name="Jeans",
        description="Slim fit blue jeans",
        price=1200,
        quantity=10
    ),
    Product(
        id=3,
        name="Shoes",
        description="Black running shoes",
        price=2500,
        quantity=6
    ),
    Product(
        id=4,
        name="Jacket",
        description="Warm winter jacket",
        price=3500,
        quantity=3
    ),
    Product(
        id=5,
        name="Cap",
        description="Black cotton cap",
        price=500,
        quantity=8
    )
]

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

def init_db():
    db = SessionLocal()

    count = db.query(model.Product).count()

    if count == 0 :
        for product in data:
            db.add(model.Product(**product.model_dump()))
        db.commit()

init_db()


@app.get("/products")
def get_all_products(db : Session = Depends(get_db)):

    db_products = db.query(model.Product).all()
    return db_products

@app.get("/products/{id}")
def get_product_by_id(id:int  , db : Session = Depends(get_db)):

    db_product = db.query(model.Product).filter(model.Product.id == id).first()
    if db_product:
            return db_product
    return "Product not found"

@app.post("/products")
def add_product(product : Product , db : Session = Depends(get_db)):
    db.add(model.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id : int , product : Product , db : Session = Depends(get_db)):
    db_product = db.query(model.Product).filter(model.Product.id == id).first()

    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()

        return "Product updated"
    else:
        return "Not found"

@app.delete("/products/{id}")
def delete_product(id:int , db : Session = Depends(get_db)):
    db_product = db.query(model.Product).filter(model.Product.id == id).first()

    if db_product:
            db.delete(db_product)
            db.commit()
            return "Product Deleted"
    else:
        return "Not found"