from sqlalchemy import Column, Integer, String
from src.models import session, Base
from sqlalchemy_serializer import SerializerMixin

class Usuarios(Base, SerializerMixin):    
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(300), nullable=False)
    usuario = Column(String(300), unique=True, nullable=False)    
    contrasena = Column(String(20), nullable=False)    
    rol = Column(String(50), nullable=False)
    
    def __init__(self,nombre, usuario,contrasena,rol):
        self.nombre=nombre
        self.usuario=usuario
        self.contrasena=contrasena
        self.rol=rol
        
    def obtener_todos():
        usuarios = session.query(Usuarios.id, Usuarios.nombre, Usuarios.usuario, Usuarios.rol).all()              
        return usuarios
        
    def obtener_por_id(id):
        usuario = session.query(Usuarios).get(id)
        return usuario.to_dict()

    def agregar(usuario):
        usuario = session.add(usuario)        
        session.commit()
        return usuario