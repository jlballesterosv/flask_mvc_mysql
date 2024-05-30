from sqlalchemy import Column, Integer, Float, ForeignKey
from src.models import session, Base

class FacturasProductos(Base):    
    __tablename__ = 'facturas_productos'
    id = Column(Integer, primary_key=True)
    factura = Column(Integer, ForeignKey('facturas.id'), nullable=False)
    producto = Column(Integer, ForeignKey('productos.id'), nullable=False)    
    cantidad = Column(Float, nullable=False)
    valor_unitario = Column(Float, nullable=False)
    
    def __init__(self,factura, producto, cantidad, valor_unitario):
        self.factura=factura
        self.producto=producto
        self.cantidad=cantidad
        self.valor_unitario=valor_unitario
        
    def obtener_todos():
        facturas_productos = session.query(FacturasProductos).all()              
        return facturas_productos

    def agregar(factura_producto):
        factura_producto = session.add(factura_producto)        
        session.commit()
        return factura_producto
