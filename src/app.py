from flask import Flask, request, redirect
from flask.templating import render_template
from src.models import Base , engine
from flask_controller import FlaskControllerRegister

from flask_cors import CORS, cross_origin


 
app = Flask(__name__)


cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.secret_key = 'llave_para_sesion'
app.debug = True

register = FlaskControllerRegister(app)

register.register_package('src.controllers')


Base.metadata.create_all(engine)

    
if __name__ == '__main__':
    app.run(debug=True)