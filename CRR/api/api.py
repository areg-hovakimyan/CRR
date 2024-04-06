from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

# Importing database configurations from db.py
from db import session, engine, Base, Customer, Product, Order

app = FastAPI()

# Dependency to get the database session
def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()

# Pydantic models for request bodies and responses
class CustomerCreate(BaseModel):
    FullName: str
    EmailAddress: str
    Age: int
    PhoneNumber: str = None
    Address: str = None
    Married: str = None

class ProductCreate(BaseModel):
    ProductName: str
    Price: float

class OrderCreate(BaseModel):
    CustomerID: int
    OrderDate: str
    ProductID: int
    Quantity: int

# FastAPI CRUD endpoints for Customer
@app.post("/customers/", response_model=CustomerCreate)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

@app.get("/customers/{customer_id}", response_model=CustomerCreate)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.CustomerID == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

# FastAPI CRUD endpoints for Product
@app.post("/products/", response_model=ProductCreate)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products/{product_id}", response_model=ProductCreate)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.ProductID == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# FastAPI CRUD endpoints for Order
@app.post("/orders/", response_model=OrderCreate)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@app.get("/orders/{order_id}", response_model=OrderCreate)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.OrderID == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

# Run this FastAPI application with Uvicorn:
# uvicorn main:app --reload
# Ensure to replace 'main' with the actual name of the file where this code is saved.
