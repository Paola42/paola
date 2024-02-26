from app import db


class Proveedores(db.Model):
    __tablename__ = 'proveedor'
    idProveedor = db.Column(db.Integer, primary_key=True)
    nombreProveedor = db.Column(db.String(255), nullable=False)
    documentoProveedor= db.Column(db.String(255), nullable=False)
    celularProveedor = db.Column(db.String(255), nullable=False)
    correo = db.Column(db.String(255), nullable=False)