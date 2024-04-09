from sqlalchemy import create_engine, Column, Integer, String, REAL, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define base
Base = declarative_base()

# Define the Customer table
class Customer(Base):
    __tablename__ = 'Customer'

    CustomerID = Column(Integer, primary_key=True)
    FullName = Column(String, nullable=False)
    EmailAddress = Column(String, nullable=False)
    Age = Column(Integer)
    PhoneNumber = Column(String)
    Address = Column(String)
    Married = Column(String)

# Define the Product table
class Product(Base):
    __tablename__ = 'Product'

    ProductID = Column(Integer, primary_key=True)
    ProductName = Column(String, nullable=False)
    Price = Column(REAL)

# Define the Order table
class Order(Base):
    __tablename__ = 'Order'

    OrderID = Column(Integer, primary_key=True)
    CustomerID = Column(Integer, ForeignKey('Customer.CustomerID'))
    OrderDate = Column(String)
    ProductID = Column(Integer, ForeignKey('Product.ProductID'))
    Quantity = Column(Integer)

# Create an engine that stores data in the local directory's DB.db file.
engine = create_engine('sqlite:///DB.db')

# Create all tables by issuing CREATE TABLE commands to the DB.
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
DBSession = sessionmaker(bind=engine)

# Create a DBSession() instance to establish all conversations with the database
session = DBSession()

# Function to view the table content using SQLAlchemy
def view_table(table_class):
    for instance in session.query(table_class).all():
        print(instance.__dict__)


orders_df = pd.read_csv("/Users/karensahakyan/Desktop/group_project/CRR/db/Order.csv")
customers_df = pd.read_csv("/Users/karensahakyan/Desktop/group_project/CRR/db/Customer.csv")
products_df = pd.read_csv("/Users/karensahakyan/Desktop/group_project/CRR/db/Product.csv")

def push_data_to_db(df, table_class):
    for index, row in df.iterrows():
        # Convert the row to a dictionary, handling NaN values as None
        row_dict = row.to_dict()
        for key, value in row_dict.items():
            if pd.isna(value):
                row_dict[key] = None  # Convert NaN to None for database compatibility

        # Create an instance of the table class with the row's data
        table_instance = table_class(**row_dict)
        
        # Add the new instance to the session
        session.add(table_instance)
    
    # Commit all the added instances to the database
    session.commit()

push_data_to_db(customers_df, Customer)
push_data_to_db(products_df, Product)
push_data_to_db(orders_df, Order)

engine = create_engine('sqlite://///Users/karensahakyan/Desktop/group_project/DB.db') 

Session = sessionmaker(bind=engine)
session = Session()


# Assuming your session is already created and is named 'session'
# and you have a model class 'Customer'

customers = session.query(Customer).all()  # Fetch all records from the Customer table

for customer in customers:
    print(f"ID: {customer.CustomerID}, Name: {customer.FullName}, Email: {customer.EmailAddress}")
    # Add more fields as needed

