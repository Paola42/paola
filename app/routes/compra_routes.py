from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.compra import Compras
from app.models.administrador import Administrador
from app.models.proveedor import Proveedores
from app import db

bp = Blueprint('compra', __name__)

@bp.route('/compra')
def index():
    data = Compras.query.all()
     
    return render_template('compra/index.html', data=data)
    #return data

@bp.route('/compras/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        descripcionCompra = request.form['descripcionCompra']
        fechaFacturac =request.form['fechaFacturac']
        totalCompra =request.form['totalCompra']
        idAdministrador =request.form['idAdministrador']
        idProveedor =request.form['idProveedor']
        
        
        new_compra = Compras(descripcionCompra=descripcionCompra,fechaFacturac=fechaFacturac, totalCompra=totalCompra, idAdministrador=idAdministrador,
        idProveedor=idProveedor)
        db.session.add(new_compra)
        db.session.commit()
        
        return redirect(url_for('compra.index'))
    
    data = Proveedores.query.all()
    data1 = Administrador.query.all()

    return render_template('compra/add.html', data=data, data1=data1)

@bp.route('/compra/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    compra = Compras.query.get_or_404(id)

    if request.method == 'POST':
        #return "entra al if"
        compra.descripcionCompra = request.form['descripcionCompra']
        compra.fechaFacturac =request.form['fechaFacturac']
        compra.totalCompra =request.form['totalCompra']
        compra.idAdministrador = request.form['idAdministrador']
        compra.idProveedor= request.form['idProveedor']
        
        db.session.commit()
        
        return redirect(url_for('compra.index'))

    return render_template('compra/edit.html', compra=compra)

@bp.route('/compra/delete/<int:id>')
def delete(id):
    compra = Compras.query.get_or_404(id)
    
    db.session.delete(compra)
    db.session.commit()

    return redirect(url_for('compra.index'))
