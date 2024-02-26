from flask_login import UserMixin
from app import db


class Administrador(db.Model,UserMixin):
    __tablename__ = 'administrador'
    idAdministrador = db.Column(db.Integer, primary_key=True)
    nombreAdministrador = db.Column(db.String(255), nullable=False)
    documentoAdministrador= db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False)
    contraseña= db.Column(db.String(255), nullable=False)
    venta = db.relationship("Ventas", backref="administrador", lazy=True)

    def get_id(self):
        return str(self.idAdministrador)