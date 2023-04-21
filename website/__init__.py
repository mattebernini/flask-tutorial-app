from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

# python3 main.py deploying
try:
    mode = sys.argv[1]
except:
    mode = "development"

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'parola segreta segretissima'    
    if mode == "development":
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    else: # deploying
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@server_ip/nome_db"
    db.init_app(app)

    from .frontend import frontend
    from .privato import privato

    app.register_blueprint(frontend, url_prefix='/')
    app.register_blueprint(privato, url_prefix='/privato')

    with app.app_context():
        db.create_all()
    
    return app

