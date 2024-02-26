from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        from .models.administrador import Administrador
        return Administrador.query.get(int(user_id))

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        from .models.cliente import Clientes
        return Clientes.query.get(int(user_id))
    
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    from app.routes import (cliente_routes, administrador_routes, producto_routes,proveedor_routes, compra_routes,
                            detalleCompra_routes,venta_routes, detalleVenta_routes,auth,carrito_routes)

    app.register_blueprint(cliente_routes.bp)
    app.register_blueprint(administrador_routes.bp)
    app.register_blueprint(producto_routes.bp)
    app.register_blueprint(proveedor_routes.bp)
    app.register_blueprint(compra_routes.bp)
    app.register_blueprint(detalleCompra_routes.bp)
    app.register_blueprint(venta_routes.bp)
    app.register_blueprint(detalleVenta_routes.bp)
    app.register_blueprint(carrito_routes.bp) 
   
    
    return app