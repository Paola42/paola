from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.venta import Ventas
from app.models.cliente import Clientes
from app.models.administrador import Administrador
from app.models.detalleVenta import DetalleVentas
from app.routes.carrito_routes import carrito_compras
from app import db

bp = Blueprint('venta', __name__)

@bp.route('/venta')
def index():
    data = Ventas.query.all()
     
    return render_template('venta/index.html', data=data)
    #return data

@bp.route('/venta/add', methods=['GET', 'POST'])
def add():
    pass
    # descripcionVenta = "descripcion"
    # fechaV = "2024-02-12"
    # totalV = "12132131"
    # idCliente = 1
    # idAdministrador = 1
    
    
    # new_venta = Ventas(descripcionVenta=descripcionVenta,fechaV=fechaV, totalV=totalV, idCliente=idCliente, idAdministrador=1)
    # db.session.add(new_venta)
    # db.session.commit()
    # return redirect(url_for('detalleVenta.add',id=new_venta.idVenta))
    #return redirect(url_for('venta.index'))
    
    #data = Clientes.query.all()
    #data3 = Administrador.query.all()

    #return render_template('venta/add.html', data=data, data3=data3)


@bp.route('/adddetalle/<int:id>', methods=['GET', 'POST'])  
def addDetalle(id):  
    for item in carrito_compras.getItems():
        idproducto = item["producto"].idproducto        
        detalleVenta = DetalleVentas(idVenta=id,idproducto=idproducto)
        db.session.add(detalleVenta)
        db.session.commit() 
    carrito_compras.vaciarcarrito()
    
    return redirect(url_for('producto.index'))


@bp.route('/venta/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    venta = Ventas.query.get_or_404(id)

    if request.method == 'POST':
        #return "entra al if"
        venta.descripcionVenta = request.form['descripcionVenta']
        venta.fechaV =request.form['fechaV']
        venta.totalV =request.form['totalV']
        venta.idCliente= request.form['idCliente']
        venta.idAdministrador = request.form['idAdministrador']
        
        db.session.commit()
        
        return redirect(url_for('venta.index'))

    return render_template('venta/edit.html', venta=venta)


@bp.route('/venta/delete/<int:id>')
def delete(id):
    venta = Ventas.query.get_or_404(id)
    
    db.session.delete(venta)
    db.session.commit()

    return redirect(url_for('venta.index'))
