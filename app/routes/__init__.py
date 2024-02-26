from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import cliente_routes, administrador_routes, producto_routes, proveedor_routes, compra_routes, detalleCompra_routes, venta_routes,detalleVenta_routes,carrito_routes,auth
