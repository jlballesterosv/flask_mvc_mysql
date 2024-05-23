from flask import Flask, request, redirect
from flask.templating import render_template
from src.models import Base , engine
from flask_controller import FlaskControllerRegister



 
app = Flask(__name__)
app.secret_key = 'llave_para_sesion'
app.debug = True

register = FlaskControllerRegister(app)

register.register_package('src.controllers')


Base.metadata.create_all(engine)

    
if __name__ == '__main__':
    app.run(debug=True)