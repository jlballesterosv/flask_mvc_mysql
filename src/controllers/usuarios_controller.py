from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.usuarios import Usuarios

class UsuariosController(FlaskController):
    @app.route("/usuarios")
    def usuarios():
        usuarios = Usuarios.obtener_todos()
        return render_template('usuarios.html', titulo="Lista de Usuarios", usuarios=usuarios)    
    
    @app.route("/usuarios/<id>")
    def usuario_por_id(id):
        usuario = Usuarios.obtener_por_id(id)        
        return usuario

    @app.route("/agregar_usuario", methods=['GET','POST'])
    def agregar_usuario():
        if request.method == 'POST':
            nombre = request.form.get('nombre')
            usuario = request.form.get('usuario')
            contrasena = request.form.get('contrasena')
            rol = request.form.get('rol')
            
            if not nombre:
                flash('El nombre es un campo obligatorio')        
            elif not usuario:
                flash('El usuario es un campo obligatorio')   
            elif not contrasena:
                flash('La contraseña es un campo obligatorio') 
            elif not rol:
                flash('El rol en stock es un campo obligatorio')   
            else:          
                usuario = Usuarios(nombre,usuario,contrasena,rol)
                Usuarios.agregar(usuario)
                return redirect(url_for('usuarios'))    
        return render_template('formulario_usuario.html', titulo="Formulario de Usuario")