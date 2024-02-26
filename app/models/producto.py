from app import db


class Productos(db.Model):
    __tablename__ = 'producto'
    idProducto = db.Column(db.Integer, primary_key=True)
    nombreProducto = db.Column(db.String(255), nullable=False)
    precioProductocompra= db.Column(db.Integer, nullable=False)
    precioProductoventa= db.Column(db.Integer, nullable=False)
    imagen = db.Column(db.String(255), nullable=True)
    vent = db.relationship("Ventas", secondary="detalleventa", back_populates="productos", single_parent=False)
