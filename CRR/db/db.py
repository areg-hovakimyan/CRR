from sqlalchemy import create_engine, Column, Integer, String, REAL, ForeignKey, Float
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

    CustomerID = Column(String, primary_key=True)
    FullName = Column(String, nullable=False)
    EmailAddress = Column(String, nullable=False)
    Age = Column(Integer)
    PhoneNumber = Column(String)
    Address = Column(String)
    Married = Column(String)

# Define the Product table
class Product(Base):
    __tablename__ = 'Product'

    ProductID = Column(String, primary_key=True)
    ProductName = Column(String, nullable=False)
    Price = Column(REAL)

# Define the Order table
class Order(Base):
    __tablename__ = 'Order'

    OrderID = Column(String, primary_key=True)
    CustomerID = Column(Integer, ForeignKey('Customer.CustomerID'))
    OrderDate = Column(String)
    ProductID = Column(Integer, ForeignKey('Product.ProductID'))
    Quantity = Column(Integer)

class Modeling(Base):
    __tablename__ = 'Modeling'
    
    CustomerID = Column(String, ForeignKey('Customer.CustomerID'), primary_key=True)
    Recency = Column(Float)
    Frequency = Column(Float)
    Monetary = Column(Float)
    R_Score = Column(Integer)
    F_Score = Column(Integer)
    M_Score = Column(Integer)
    RFM_Score = Column(Float)    
    Cluster = Column(Integer)
    ChurnRiskLevel = Column(String)  

class ChurnRate(Base):
    __tablename__ = 'ChurnRate'

    ChurnRiskLevel = Column(String, primary_key=True)
    ChurnRate = Column(Float)

def create_engine_db(db_path='sqlite:///DB.db'):
    engine = create_engine(db_path)
    return engine

def initialize_database(engine):
    Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
def get_session(engine):
    DBSession = sessionmaker(bind=engine)
    return DBSession()



# Function to view the table content using SQLAlchemy
def push_data_to_db(session, df, table_class):
    valid_columns = {c.name for c in table_class.__table__.columns}
    df = df.loc[:, df.columns.intersection(valid_columns)]
    
    for index, row in df.iterrows():
        row_dict = row.to_dict()
        for key, value in row_dict.items():
            if pd.isna(value):
                row_dict[key] = None
            else:
                col_type = type(getattr(table_class, key).type).__name__
                if col_type == 'Integer':
                    row_dict[key] = int(value)
                elif col_type == 'Float':
                    row_dict[key] = float(value)
                elif col_type == 'String':
                    row_dict[key] = str(value)

        table_instance = table_class(**row_dict)
        session.add(table_instance)
    session.commit()

# Function to view the table content
def view_table(session, table_class):
    for instance in session.query(table_class).all():
        print(instance.__dict__)
