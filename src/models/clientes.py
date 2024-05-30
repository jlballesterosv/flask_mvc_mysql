from sqlalchemy import Column, Integer, String
from src.models import session, Base
from sqlalchemy_serializer import SerializerMixin

class Clientes(Base, SerializerMixin):    
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
        
    def obtener_por_id(id):
        cliente = session.query(Clientes).get(id)
        return cliente.to_dict()
    
    def agregar(cliente):
        cliente = session.add(cliente)        
        session.commit()
        return cliente