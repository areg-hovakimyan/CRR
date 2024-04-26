from faker import Faker
import random

fake = Faker()

def generate_age():
    # Generate age based on a skewed distribution
    age = int(random.normalvariate(35, 10))
    return max(18, min(age, 70))  # Ensure age is within a realistic range

def generate_customer(customer_id):
    return {
        "CustomerID": customer_id,
        "FullName": fake.name(),
        "EmailAddress": fake.email(),
        "Age": generate_age(),
        "PhoneNumber": fake.phone_number(),
        "Address": fake.address(),
        "Married": fake.random_element(elements=("Yes", "No"))
    }

def generate_product(product_id):
    # Different price ranges for different types of products
    price_range = (20, 1000) if product_id % 3 == 0 else (5, 100) if product_id % 3 == 1 else (1, 50)
    return {
        "ProductID": product_id,
        "ProductName": fake.word().capitalize(),
        "Price": round(random.uniform(*price_range), 2)
    }

def generate_order(order_id, customer_id, product_id, order_date, quantity):
    return {
        "OrderID": order_id,
        "CustomerID": customer_id,
        "OrderDate": order_date,
        "ProductID": product_id,
        "Quantity": quantity
    }

