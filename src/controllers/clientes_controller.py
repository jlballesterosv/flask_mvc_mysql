from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.clientes import Clientes

class ClientesController(FlaskController):
    @app.route("/clientes")
    def clientes():
        clientes = Clientes.obtener_todos()
        return render_template('clientes.html', titulo="Lista de Clientes", clientes=clientes)

    @app.route("/agregar_cliente", methods=['GET','POST'])
    def agregar_cliente():
        if request.method == 'POST':
            nombre = request.form.get('nombre')
            print(nombre)
            identificacion = request.form.get('identificacion')
            direccion = request.form.get('direccion')
            telefono = request.form.get('telefono')
            email = request.form.get('email')
            if not nombre:
                flash('El nombre es un campo obligatorio')        
            elif not identificacion:
                flash('La identificación es un campo obligatorio')   
            elif not direccion:
                flash('La dirección es un campo obligatorio') 
            elif not telefono:
                flash('El teléfono en stock es un campo obligatorio')    
            elif not email:
                flash('El email es un campo obligatorio')  
            else:          
                cliente = Clientes(nombre,identificacion,direccion,telefono,email)
                Clientes.agregar(cliente)
                return redirect(url_for('clientes'))    
        return render_template('formulario_cliente.html', titulo="Formulario de Cliente")