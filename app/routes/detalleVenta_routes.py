from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.detalleVenta import DetalleVentas
from app.models.producto import Productos
from app.models.venta import Ventas
from app.routes.carrito_routes import carrito_compras
from app import db

bp = Blueprint('detalleVenta', __name__)

@bp.route('/detalleVenta')
def index():
    data = DetalleVentas.query.all()
     
    return render_template('detalleVenta/index.html', data=data)
    #return data

@bp.route('/detalleVenta/add/<int:id>', methods=['GET', 'POST'])
def add(id):
    print(id)
    descripcionDV = "Descripcion"
    idVenta = id
    
    for item in carrito_compras.getItems():
        cantidad = item["cantidad"]
        producto = item["producto"]
        new_detalleVenta = DetalleVentas( cantidad = cantidad , idProducto=producto.idProducto,idVenta=idVenta)
        db.session.add(new_detalleVenta)
        db.session.commit()
     #return "Detalle inseratado"
        
        
    factura = Ventas.query.get_or_404(id)
    detalles = DetalleVentas.query.filter_by(idVenta=factura.idVenta)

    return render_template('orquidea/factura.html', factura=factura, detalles=detalles)

    
    ata = Ventas.query.all()
    datas = Productos.query.all()
 

    return render_template('detalleVenta/add.html', data=data, datas=datas)


 #@bp.route('/detalleVenta/add/<int:id>', methods=['GET', 'POST'])
 #def add2():
@bp.route('/detalleVenta/add', methods=['GET', 'POST'])
def add2():
    if request.method == 'POST':
        cantidad  =request.form['cantidad ']
        idProducto =request.form['idProducto']
        idVenta =request.form['idVenta']
        subTotal = request.form['subTotal']
        
        new_detalleVenta = DetalleVentas( cantidad =cantidad ,idProducto=idProducto,idVenta=idVenta,subTotal=subTotal)
        db.session.add(new_detalleVenta)
        db.session.commit()
        
        return redirect(url_for('detalleVenta.index'))
    
    datas = Productos.query.all()
    dat = Ventas.query.all()

    return render_template('detalleVenta/add.html', datas=datas, dat=dat)

@bp.route('/detalleVenta/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    detalleVenta = DetalleVentas.query.get_or_404(id)

    if request.method == 'POST':
        #return "entra al if"
        detalleVenta.cantidad =request.form['cantidad']
        detalleVenta.subTotal =request.form['subTotal']
        detalleVenta.idAdministrador = request.form['idAdministrador']
        detalleVenta.idVenta = request.form['idVenta']
        
        db.session.commit()
        
        return redirect(url_for('detalleVenta.index'))

    return render_template('detalleVenta/edit.html', detalleVenta=detalleVenta)

@bp.route('/detalleVenta/delete/<int:id>')
def delete(id):
   detalleVenta = DetalleVentas.query.get_or_404(id)
   
   db.session.delete(detalleVenta)
   db.session.commit() 
    

   return redirect(url_for('detalleVenta.index'))
