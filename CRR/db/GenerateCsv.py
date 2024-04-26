from data_generator import generate_customer, generate_product, generate_order
import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()

def modify_order_dates(customer_id, num_customers):
    """Modify order dates to introduce recency variation."""
    if customer_id <= num_customers // 3:
        return '-30d', 'today'
    elif customer_id <= 2 * num_customers // 3:
        return '-90d', 'today'
    else:
        return '-1y', 'today'

def adjust_order_quantity(customer_id, num_customers):
    """Adjust order quantities based on customer spending habits."""
    return random.randint(1, 5) if customer_id <= num_customers // 2 else random.randint(5, 10)

num_customers = 500
customers = [generate_customer(i) for i in range(1, num_customers + 1)]
customer_df = pd.DataFrame(customers)

num_products = 50
products = [generate_product(i) for i in range(1, num_products + 1)]
product_df = pd.DataFrame(products)

num_orders = 2000
orders = []
for i in range(1, num_orders + 1):
    customer_id = random.choice(range(1, num_customers + 1))
    product_id = random.choice(range(1, num_products + 1))
    start_date, end_date = modify_order_dates(customer_id, num_customers)
    order_date = fake.date_between(start_date=start_date, end_date=end_date)
    quantity = adjust_order_quantity(customer_id, num_customers)
    order = generate_order(i, customer_id, product_id, order_date, quantity)
    orders.append(order)
order_df = pd.DataFrame(orders)

# Save data to CSV
customer_df.to_csv("Customer.csv", index=False)
product_df.to_csv("Product.csv", index=False)
order_df.to_csv("Order.csv", index=False)
