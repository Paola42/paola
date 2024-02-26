from app import db
from sqlalchemy.orm import relationship

class DetalleVentas(db.Model):
    __tablename__ = 'detalleventa'
    idDetalleVenta = db.Column(db.Integer, primary_key=True)
    cantidad =db.Column(db.Integer,nullable=False)
    idProducto = db.Column(db.Integer, db.ForeignKey('producto.idProducto'))
    idVenta= db.Column(db.Integer, db.ForeignKey('venta.idVenta'))
    subTotal =db.Column(db.Integer,nullable=False)

    producto = db.relationship('Productos')