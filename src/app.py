from flask import Flask, request, redirect
from flask.templating import render_template
from models import Base, engine



 
app = Flask(__name__)
app.debug = True
from controllers import *
Base.metadata.create_all(engine)
    
if __name__ == '__main__':
    app.run(debug=True)