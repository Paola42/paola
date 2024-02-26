from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.proveedor import Proveedores
from app import db

bp = Blueprint('proveedor', __name__)

@bp.route('/Proveedores')
def index():
    data = Proveedores.query.all()
    return render_template('proveedor/index.html', data=data)

@bp.route('/proveedor/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreProveedor= request.form['nombreProveedor']
        documentoProveedor = request.form['documentoProveedor']
        celularProveedor  = request.form['celularProveedor']
        correo       = request.form['correo']
        new_proveedor= Proveedores(nombreProveedor=nombreProveedor , documentoProveedor=documentoProveedor, celularProveedor=celularProveedor, correo= correo)
        db.session.add(new_proveedor)
        db.session.commit()
        
        return redirect(url_for('proveedor.index'))

    return render_template('proveedor/add.html')

@bp.route('/proveedor/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    proveedor = Proveedores.query.get_or_404(id)

    if request.method == 'POST':
        proveedor.nombreProveedor = request.form['nombreProveedor']
        proveedor.documentoProveedor = request.form['documentoProveedor']
        proveedor.celularProveedor = request.form['celularProveedor']
        proveedor.correo = request.form['correo']
    
        db.session.commit()
        return redirect(url_for('proveedor.index'))

    return render_template('proveedor/edit.html',proveedor=proveedor)
    

@bp.route('/proveedor/delete/<int:id>')
def delete(id):
    proveedor = Proveedores.query.get_or_404(id)
    
    db.session.delete(proveedor)
    db.session.commit()

    return redirect(url_for('proveedor.index'))
