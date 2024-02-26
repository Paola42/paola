from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.cliente import Clientes
from app import db

bp = Blueprint('cliente', __name__)

@bp.route('/cliente')
def index():
    data = Clientes.query.all()
    return render_template('cliente/index.html', data=data)

@bp.route('/Cliente/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreCliente = request.form['nombreCliente']
        documentoCliente = request.form['documentoCliente']
        direccion    = request.form['direccion']
        telefono     =request.form['telefono']
        correo       = request.form['correo']
        contraseña   = request.form['contraseña']
        new_cliente = Clientes(nombreCliente=nombreCliente, documentoCliente=documentoCliente, direccion=direccion, telefono=telefono, correo=correo,contraseña =contraseña )
        db.session.add(new_cliente)
        db.session.commit()
        
        return render_template('login/login.html')
    return render_template('cliente/add.html')

@bp.route('/cliente/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cliente = Clientes.query.get_or_404(id)

    if request.method == 'POST':
        cliente.nombreCliente = request.form['nombre']
        cliente.documentoCliente = request.form['documentoCliente']
        cliente.direccion = request.form['direccion']
        cliente.telefono = request.form['telefono']
        cliente.correo = request.form['correo']
        cliente.contraseña= request.form['contraseña']
        db.session.commit()
        return redirect(url_for('cliente.index'))

    return render_template('cliente/edit.html',cliente=cliente)
    

@bp.route('/cliente/delete/<int:id>')
def delete(id):
    Cliente = Clientes.query.get_or_404(id)
    
    db.session.delete(Cliente)
    db.session.commit()

    return redirect(url_for('cliente.index'))



