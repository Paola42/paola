from flask import Blueprint, render_template, redirect, url_for, request, flash
from sqlalchemy import func
from app.models.producto import Productos
from app.models.carrito import Carritos
from app.models.venta import Ventas
from app.models.detalleVenta import DetalleVentas
from flask_login import current_user, login_required
from app import db



bp = Blueprint('carritos', __name__)
carrito_compras = Carritos()

@bp.route('/ListarCarrito')
def listar():
    items = carrito_compras.getItems()
    return render_template('producto/listar.html', items=items)

@bp.route('/ListarProductos')
def index():
    productos = carrito_compras
    return render_template('index.html', productos=productos)

@bp.route('/agregar/<int:id>', methods=['POST'])
def agregar_al_carrito(id):
    cantidad = int(request.form.get('cantidad', 1))
   
    #return redirect(url_for('producto.index'))
    items = carrito_compras.getItems()
    for item in items:
        if item['producto'].idProducto == id:
            item['cantidad'] += cantidad
            return redirect(url_for('producto.index1'))
    carrito_compras.agregar_producto(id, cantidad)
    return redirect(url_for("producto.index1"))
    #return "Entra a agregar corrito"



@bp.route('/eliminar/<int:id>', methods=['POST','GET'])
def eliminarItem1(id):
    Items = carrito_compras.getItems()
    for item in Items:
        if  item['producto'].idProducto ==id:
            carrito_compras.eliminarItem(item)
    return render_template('producto/listar.html', items=Items)
    
    #return "Entra a agregar corrito"

@bp.route('/eliminar/<int:id>', methods=['POST','GET'])
def eliminarItem(id):
    items = carrito_compras.getItems()
    for item in items:
        if item['producto'].idProducto== id:
            carrito_compras.eliminarItem(item)
            return redirect(url_for('carritos.listar'))  # Redirigir a la vista del carrito
    return redirect(url_for('carritos.listar'))  # Redirigir a la vista del carrito

@bp.route('/realizar_compra')
@login_required
def realizar_compra():
    total = carrito_compras.calcular_total()
    new_venta = Ventas(fechaV=func.now() ,descripcionVenta="Venta de prodcutos", idCliente=current_user.idCliente, totalV=total)
    db.session.add(new_venta)
    db.session.commit()

    factura =carrito_compras.getItems()

    for producto in factura:
        producto2 = producto['producto']
        detalles = DetalleVentas(cantidad=producto['cantidad'], subTotal=producto2.precioProductoventa, idVenta=new_venta.idVenta, idProducto=producto2.idProducto)
        db.session.add(detalles)

    db.session.commit()
    detalle = DetalleVentas.query.filter_by(idVenta=new_venta.idVenta).all()

    return render_template('carrito/realizar_compra.html', detalles=detalle,new_venta=new_venta)


    #return redirect(url_for('venta.add'))

@bp.route('/generar_compra', methods=['POST'])
def generar_factura():
    total = carrito_compras.calcular_total()
    return redirect(url_for('venta.add'))
    #return render_template('carrito/factura.html', total=total)

@bp.route('/itemscarrito', methods=['GET', 'POST'])
def tCarrito():
    a = carrito_compras.tamañoD()
    print("Entra a carrito rutas", a)
    return f"Entra a carrito {carrito_compras.tamañoD()}"

@bp.route('/vaciar_carrito',methods=["POST"])
def vaciar_carrito():
    carrito_compras.vaciarcarrito()
    return render_template('producto/listar.html')
    