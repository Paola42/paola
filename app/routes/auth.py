from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.administrador import Administrador
from app.models.cliente import Clientes
import random

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        
        administrador = Administrador.query.filter_by(correo=correo, contraseña=contraseña).first()

        if administrador:
            login_user(administrador)
            flash("Login successful!", "success")

            return render_template("inicio/index.html")
        
        cliente = Clientes.query.filter_by(correo=correo, contraseña=contraseña).first()
        
        if cliente:

            login_user(cliente)
            print(current_user.nombreCliente)
            return redirect(url_for("producto.index1"))
       
        flash('Invalid credentials. Please try again.', 'danger')
    
        

    
    return render_template("login/login.html")

@auth_bp.route('/dashboard')
@login_required
def dashboard():
    return f'Welcome, {current_user.correo}! This is your dashboard Es una bolita muy brillante como el sol.'

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/')
def index():
    backgrounds = ['florBlanca.jpg','bonsai.jpg', 'florManzana.jpg']
    random_background = random.choice(backgrounds)
    return  render_template('principal/index.html', random_background=random_background)
    

