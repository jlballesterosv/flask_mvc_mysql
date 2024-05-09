from flask import render_template, request, redirect, url_for, flash
from app import app
from models import *

@app.route("/")
def index():
    return render_template('index.html', titulo="App Facturación")

@app.route("/clientes")
def clientes():
    return render_template('clientes.html', titulo="Lista de Clientes")

@app.route("/formulario_cliente")
def form_cliente():
    return render_template('formulario_cliente.html', titulo="Formulario de Cliente")

@app.route("/productos")
def productos():
    productos = Productos.obtener_todos()
    return render_template('productos.html', titulo="Lista de Productos", productos=productos)

@app.route("/agregar_producto", methods=['GET','POST'])
def agregar_producto():
    if request.method == 'POST':
        descripcion = request.form.get('descripcion')
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
            Productos.agregar_producto(producto)
            return redirect(url_for('productos'))     
    categorias = Categorias.obtener_todos()
    return render_template('formulario_producto.html', titulo="Formulario de Producto", categorias=categorias)