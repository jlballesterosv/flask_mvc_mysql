from sqlalchemy import Column, Integer, DateTime, ForeignKey
from src.models import session, Base

class Facturas(Base):    
    __tablename__ = 'facturas'
    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime,nullable=False)
    cliente = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    
    def __init__(self,fecha, cliente,usuario):
        self.fecha=fecha
        self.cliente=cliente
        self.usuario=usuario
        
    def obtener_todos():
        facturas = session.query(Facturas).all()              
        return facturas

    def agregar(factura):
        factura = session.add(factura)        
        session.commit()
        return factura
