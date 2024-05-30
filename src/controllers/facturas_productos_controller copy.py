from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.productos import Productos
from src.models.facturas import Facturas
from src.models.facturas_productos import FacturasProductos
from flask_restful import Api
from src.api.productos_api import ProductosApi
class FacturasProductosController(FlaskController):
    

    
    @app.route("/facturas_productos")
    def facturas_productos():
        facturas_productos = FacturasProductos.obtener_todos()
        return facturas_productos

    @app.route("/agregar_factura_producto", methods=['GET','POST'])
    def agregar_factura_producto():
        if request.method == 'POST':
            descripcion = request.form.get('usuario')
            valor_unitario = request.form.get('valor_unitario')
            unidad_medida = request.form.get('unidad_medida')
            cantidad_stock = request.form.get('cantidad_stock')
            categoria = request.form.get('categoria')
            if not descripcion:
                flash('La descripción es un campo obligatorio')   
            elif not valor_unitario:
                flash('El valor unitario es un campo obligatorio')     
            elif not unidad_medida:
                flash('La unidad de medida es un campo obligatorio')    
            elif not cantidad_stock:
                flash('La cantidad en stock es un campo obligatorio')    
            elif not categoria:
                flash('La categoria es un campo obligatorio')  
            else:          
                producto = Productos(descripcion,valor_unitario,unidad_medida,cantidad_stock,categoria)
                Productos.agregar(producto)
                return redirect(url_for('productos'))     
        categorias = Categorias.obtener_todos()
        return render_template('formulario_producto.html', titulo="Formulario de Producto", categorias=categorias)