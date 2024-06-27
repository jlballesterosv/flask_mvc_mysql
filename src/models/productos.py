from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import session, Base
from src.models.categorias import Categorias
from sqlalchemy_serializer import SerializerMixin

class Productos(Base, SerializerMixin):    
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
        productos = session.query(Productos).join(Categorias).all()   
        print(productos[0].to_dict())           
        return productos

    def agregar(producto):
        producto = session.add(producto)        
        session.commit()
        return producto

