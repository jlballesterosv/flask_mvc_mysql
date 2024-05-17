from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("mysql+pymysql://root@localhost/factura01?charset=utf8mb4")

# Establish a connection
connection = engine.connect()

# Create a base class for declarative class definitions
Base = declarative_base()
Base.metadata.bind = engine

# Create a session to interact with the database
Session = sessionmaker(bind=engine)

session = Session()