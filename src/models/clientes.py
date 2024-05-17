from sqlalchemy import Column, Integer, String
from src.models import session, Base

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
        clientes = session.query(Clientes).all()
        return clientes