from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.administrador import Administrador
from app import db

bp = Blueprint('administrador', __name__)

@bp.route('/Administrador')
def index():
    data = Administrador.query.all()
    return render_template('administrador/index.html', data=data)

@bp.route('/Administrador/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombreAdministrador = request.form['nombreAdministrador']
        documentoAdministrador = request.form['documentoAdministrador']
        direccion    = request.form['direccion']
        telefono     =request.form['telefono']
        correo       = request.form['correo']
        contraseña = request.form['contraseña']
        new_administrador= Administrador(nombreAdministrador=nombreAdministrador, documentoAdministrador=documentoAdministrador, direccion=direccion, telefono=telefono, correo=correo, contraseña=contraseña)
        db.session.add(new_administrador)
        db.session.commit()
        
        return redirect(url_for('administrador.index'))

    return render_template('administrador/add.html')

@bp.route('/administrador/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    administrador = Administrador.query.get_or_404(id)

    if request.method == 'POST':
        administrador.nombreAdministrador = request.form['nombre']
        administrador.documentoAdministrador = request.form['documentoAdministrador']
        administrador.direccion = request.form['direccion']
        administrador.telefono = request.form['telefono']
        administrador.correo = request.form['correo']
        administrador.contraseña = request.form['contraseña']
        
    
        db.session.commit()
        return redirect(url_for('administrador.index'))

    return render_template('administrador/edit.html',administrador=administrador)
    

@bp.route('/administrador/delete/<int:id>')
def delete(id):
    administrador = Administrador.query.get_or_404(id)
    
    db.session.delete(administrador)
    db.session.commit()

    return redirect(url_for('administrador.index'))

@bp.route('/admi')
def inicio():
    data = Administrador.query.all()
    return render_template('inicio/index.html', data=data)

