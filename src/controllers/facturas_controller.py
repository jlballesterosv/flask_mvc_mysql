from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.facturas import Facturas
from src.models.clientes import Clientes
from src.models.usuarios import Usuarios
import datetime
class FacturasProductosController(FlaskController):
    

    
    @app.route("/facturas")
    def facturas():
        facturas = Facturas.obtener_todos()
        return render_template('facturas.html', titulo="Lista de Facturas", facturas=facturas)

    @app.route("/agregar_factura", methods=['GET','POST'])
    def agregar_factura():
        if request.method == 'POST':
            fecha = request.form.get('fecha')
            cliente = request.form.get('cliente')
            usuario = request.form.get('usuario')
            if not fecha:
                flash('La fecha es un campo obligatorio')   
            elif not cliente:
                flash('El cliente es un campo obligatorio')     
            elif not usuario:
                flash('El usuario es un campo obligatorio')     
            else:          
                factura = Facturas(fecha,cliente,usuario)
                Facturas.agregar(factura)
                return redirect(url_for('facturas'))    
        fecha =  datetime.datetime.now()
        clientes = Clientes.obtener_todos()
        usuarios = Usuarios.obtener_todos()
        return render_template('formulario_factura.html', titulo="Facturar", fecha=fecha, clientes=clientes, usuarios=usuarios)