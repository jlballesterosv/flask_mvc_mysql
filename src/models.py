
from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine("mysql+pymysql://root@localhost/factura13?charset=utf8mb4")

# Establish a connection
connection = engine.connect()

# Create a base class for declarative class definitions
Base = declarative_base()
Base.metadata.bind = engine

# Create a session to interact with the database
Session = sessionmaker(bind=engine)


class Productos(Base):    
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(300), unique=True, nullable=False)
    valor_unitario = Column(Float(10,8))
    unidad_medida = Column(String(3), nullable=False)
    cantidad_stock = Column(Float(10,8))
    categoria = Column(Integer, ForeignKey('categorias.id'), nullable=False)
    
    def __init__(self,descripcion, valor_unitario,unidad_medida,cantidad_stock,categoria):
        self.descripcion=descripcion
        self.valor_unitario=valor_unitario
        self.unidad_medida=unidad_medida
        self.cantidad_stock=cantidad_stock
        self.categoria=categoria
        
    def obtener_todos():
        session = Session()
        productos = session.query(Productos).all()              
        return productos

    def agregar_producto(producto):
        session = Session()
        producto = session.add(producto)        
        session.commit()
        return producto

class Categorias(Base):    
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    categoria = Column(String(128), unique=True, nullable=False)
    
    def __init__(self,categoria):
        self.categoria=categoria   
        
    def obtener_todos():
        session = Session()
        categorias = session.query(Categorias).all()
        return categorias
        
class Clientes(Base):    
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    identificacion = Column(String(20), unique=True, nullable=False)
    direccion = Column(String(300), nullable=False)
    telefono = Column(String(20), nullable=False)
    email = Column(String(300), nullable=True)
    
    def __init__(self,nombre, identificacion,direccion,telefono,email):
        self.nombre=nombre
        self.identificacion=identificacion
        self.direccion=direccion
        self.telefono=telefono
        self.email=email 
        
    def obtener_todos():
        session = Session()
        clientes = session.query(Clientes).all()
        return clientes