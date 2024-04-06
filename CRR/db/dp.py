from sqlalchemy import create_engine, Column, Integer, String, REAL, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
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


