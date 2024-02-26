from app import db
from sqlalchemy.orm import relationship

class Compras(db.Model):
    __tablename__ = 'compra'
    idCompra = db.Column(db.Integer, primary_key=True)
    descripcionCompra= db.Column(db.String(255), nullable=False)
    fechaFacturac=db.Column(db.Date,nullable=True)
    totalCompra =db.Column(db.Integer,nullable=False)
    idAdministrador = db.Column(db.Integer, db.ForeignKey('administrador.idAdministrador'))
    idProveedor = db.Column(db.Integer, db.ForeignKey('proveedor.idProveedor'))
    