from faker import Faker
import random

fake = Faker()

# Customer Data Model
def generate_customer(customer_id):
    return {
        "CustomerID": customer_id,
        "FullName": fake.name(),
        "EmailAddress": fake.email(),
        "Age": random.randint(18, 70),
        "PhoneNumber": fake.phone_number(),
        "Address": fake.address(),
        "Married": fake.random_element(elements=("Yes", "No"))
    }

# Product Data Model
def generate_product(product_id):
    return {
        "ProductID": product_id,
        "ProductName": fake.word().capitalize(),
        "Price": round(random.uniform(10, 500), 2)
    }

# Order Data Model
def generate_order(order_id, customer_ids, product_ids):
    order_date = fake.date_between(start_date='-2y', end_date='today')
    return {
        "OrderID": order_id,
        "CustomerID": random.choice(customer_ids),
        "OrderDate": order_date,
        "ProductID": random.choice(product_ids),
        "Quantity": random.randint(1, 10)
    }

