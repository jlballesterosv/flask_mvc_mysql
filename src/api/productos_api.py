from flask_restful import Resource
from flask import request

from flask_cors import cross_origin

from src.models.productos import Productos
from src.models.categorias import Categorias

class ProductosApi(Resource):  
    
    @cross_origin()   
    def post(self):
        producto = Productos(descripcion=request.json["descripcion"]
                             , valor_unitario=request.json["valor_unitario"]
                             , unidad_medida=request.json["unidad_medida"]
                             , cantidad_stock=request.json["cantidad_stock"]
                             , categoria=request.json["categoria"])
        try:
            Productos.agregar(producto)
        except Exception:
            return "Error al almacenar el producto", 409
        return "Producto almacenado correctamente"
    
    def get(self):
        productos = Productos.obtener_todos()
        productos_result = []
        for producto in productos:
            productos_result.append(producto.to_dict())            
        return productos_result