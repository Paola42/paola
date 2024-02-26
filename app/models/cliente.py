from flask_login import UserMixin

from app import db


class Clientes(db.Model, UserMixin):
    __tablename__ = 'cliente'
    idCliente = db.Column(db.Integer, primary_key=True)
    nombreCliente = db.Column(db.String(255), nullable=False)
    documentoCliente = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False)
    contraseña= db.Column(db.String(255), nullable=False)
    vent = db.relationship("Ventas", backref='cliente', lazy=True)


    def get_id(self):
        return str(self.idCliente)