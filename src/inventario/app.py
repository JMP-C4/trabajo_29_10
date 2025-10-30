from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination, get_page_args

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///inventario.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from inventario.routes.productos import productos_bp
    app.register_blueprint(productos_bp, url_prefix="/api/productos")

    with app.app_context():
        db.create_all()

    return app
