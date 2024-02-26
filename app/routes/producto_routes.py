from flask import Blueprint, render_template, request, redirect, url_for, jsonify,flash
from flask_login import login_required
from app.models.producto import Productos
from app.routes.carrito_routes import carrito_compras
from app import db
import os
from flask_login import current_user


bp = Blueprint('producto', __name__)

@bp.route('/producto2')
def index():
    data = Productos.query.all()
    return render_template('producto/index.html', data=data, t =carrito_compras.tamañoD())

@bp.route('/producto')
@login_required
def index1():
    data = Productos.query.all()
    return render_template('principal/index.html', data=data)

@bp.route('/producto1')
def vista():
    data = Productos.query.all()
    return render_template('principal/index1.html', data=data)

@bp.route('/produ')
def ideales():
    data = Productos.query.all()
    return render_template('servicios/index.html', data=data)

@bp.route('/producto/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreProducto = request.form['nombreProducto']
        precioProductocompra = request.form['precioProductocompra']
        precioProductoventa    = request.form['precioProductoventa']
        imagen = request.files['imagenProducto']
        
        new_producto = Productos(nombreProducto=nombreProducto, precioProductocompra=precioProductocompra, precioProductoventa=precioProductoventa, imagen=imagen.filename)
       
        guardarImagen(imagen)
        
        

        db.session.add(new_producto)
        db.session.commit()
        


        return redirect(url_for('producto.index'))

    return render_template('producto/add.html')

@bp.route('/producto/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    producto = Productos.query.get_or_404(id)

    if request.method == 'POST':
        producto.nombreProducto = request.form['nombreProducto']
        producto.precioProductocompra = request.form['productoPreciocompra']
        producto.precioProductoventa= request.form['productoPrecioventa']
        


        db.session.commit()
        return redirect(url_for('producto.index'))

    return render_template('producto/edit.html',producto=producto)
    

@bp.route('/producto/delete/<int:id>')
def delete(id):
    producto= Productos.query.get_or_404(id)
    
    try:
        db.session.delete(producto)
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        flash('el producto no se puede eliminar', 'danger')
    
    return redirect(url_for('producto.index'))


def guardarImagen(imagen):
    from run import app
    carpetaDestino = os.path.join(app.root_path, "static" ,"imagenes")
    imagen.save(os.path.join(carpetaDestino, imagen.filename))




def eliminar(idProducto):
    from run import app
    producto = producto.query.get_or_404(idProducto)
    ruta_imagen = os.path.join(app.root_path, "static" ,"imagenes", producto.imagen)

    if os.path.exists(ruta_imagen):
        os.remove(ruta_imagen)