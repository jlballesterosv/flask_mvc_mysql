from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController

class ClientesController(FlaskController):
    @app.route("/clientes")
    def clientes():
        return render_template('clientes.html', titulo="Lista de Clientes")

    @app.route("/formulario_cliente")
    def form_cliente():
        return render_template('formulario_cliente.html', titulo="Formulario de Cliente")