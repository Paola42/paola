from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.detalleCompra import DetalleCompras
from app.models.producto import Productos
from app.models.compra import Compras
from app import db

bp = Blueprint('detalleCompra', __name__)

@bp.route('/detalleCompra')
def index():
    data = DetalleCompras.query.all()
     
    return render_template('detalleCompra/index.html', data=data)
    #return data

@bp.route('/detalleCompra/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        descripcionDC = request.form['descripcionDC']
        cantidad  =request.form['cantidad']
        idProducto =request.form['idProducto']
        idCompra =request.form['idCompra']
        
        
        new_detalleCompra = DetalleCompras(descripcionDC=descripcionDC, cantidad =cantidad ,idProducto=idProducto,idCompra=idCompra)
        db.session.add(new_detalleCompra)
        db.session.commit()
        
        return redirect(url_for('detalleCompra.index'))
    
    datas = Productos.query.all()
    dat = Compras.query.all()

    return render_template('detalleCompra/add.html', datas=datas, dat=dat)

@bp.route('/detalleCompra/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    detalleCompra = DetalleCompras.query.get_or_404(id)

    if request.method == 'POST':
        #return "entra al if"
        detalleCompra.descripcionDC = request.form['descripcionDC']
        detalleCompra.cantidad  =request.form['cantidad']
        detalleCompra.idAdministrador = request.form['idAdministrador']
        detalleCompra.idCompra= request.form['idCompra']
        
        db.session.commit()
        
        return redirect(url_for('detalleCompra.index'))

    return render_template('detalleCompra/edit.html', detalleCompra=detalleCompra)

@bp.route('/detalleCompra/delete/<int:id>')
def delete(id):
   detalleCompra = DetalleCompras.query.get_or_404(id)
   db.session.delete(detalleCompra)
   db.session.commit() 
    

   return redirect(url_for('detalleCompra.index'))
