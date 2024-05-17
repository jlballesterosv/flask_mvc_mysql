from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController

class HomeController(FlaskController):
    @app.route("/")
    def index():
        return render_template('index.html', titulo="App Facturación")