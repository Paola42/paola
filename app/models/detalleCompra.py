from app import db
from sqlalchemy.orm import relationship

class DetalleCompras(db.Model):
    __tablename__ = 'detalleCompra'
    idDetalleCompra = db.Column(db.Integer, primary_key=True)
    descripcionDC= db.Column(db.String(255), nullable=False)
    cantidad =db.Column(db.Integer,nullable=False)
    idProducto = db.Column(db.Integer, db.ForeignKey('producto.idProducto'))
    idCompra= db.Column(db.Integer, db.ForeignKey('compra.idCompra'))
    