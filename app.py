from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db
from routes import *

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    Migrate(app, db)

    
    register_routes(app)

    return app


app = create_app()
