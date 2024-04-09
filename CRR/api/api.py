import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

# Define a Pydantic model for the Customer data
class Customer(BaseModel):
    FullName: str
    EmailAddress: str
    Age: int
    PhoneNumber: str
    Address: str
    Married: str

# Load the data
data = pd.read_csv('CRR/api/Customer.csv')

# Create FastAPI app instance
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_info/{ID}")
async def get_info(ID: int):
    """Retrieve information for a customer by their ID."""
    info = data[data['CustomerID'] == ID].to_dict('records')
    if not info:
        raise HTTPException(status_code=404, detail="Customer not found")
    return info[0]

@app.post("/add_info", response_model=Dict[str, int])
async def add_info(customer: Customer):
    """Add a new customer to the database."""
    global data
    customer_dict = customer.dict()
    customer_dict['CustomerID'] = data['CustomerID'].max() + 1
    new_row = pd.DataFrame([customer_dict])
    data = data.append(new_row, ignore_index=True)
    # Persist changes
    data.to_csv('CRR/api/Customer.csv', index=False)
    return {"message": "Customer added successfully", "CustomerID": customer_dict['CustomerID']}

@app.put("/update_info/{ID}", response_model=Dict[str, str])
async def update_info(ID: int, update_fields: Dict[str, str]):
    """Update information for an existing customer."""
    global data
    if ID not in data['CustomerID'].values:
        raise HTTPException(status_code=404, detail="Customer not found")
    data.loc[data['CustomerID'] == ID, list(update_fields.keys())] = list(update_fields.values())
    # Persist changes
    data.to_csv('CRR/api/Customer.csv', index=False)
    return {"message": "Customer information updated successfully"}

@app.delete("/delete_info/{ID}", response_model=Dict[str, str])
async def delete_info(ID: int):
    """Delete a customer from the database."""
    global data
    if ID not in data['CustomerID'].values:
        raise HTTPException(status_code=404, detail="Customer not found")
    data = data[data['CustomerID'] != ID]
    # Persist changes
    data.to_csv('CRR/api/Customer.csv', index=False)
    return {"message": "Customer deleted successfully"}