from app import db


class Ventas(db.Model):
    __tablename__ = 'venta'
    idVenta = db.Column(db.Integer, primary_key=True)
    descripcionVenta = db.Column(db.String(255), nullable=False)
    fechaV=db.Column(db.Date,nullable=True)
    totalV = db.Column(db.String(255), nullable=False)
    idCliente = db.Column(db.Integer, db.ForeignKey('cliente.idCliente'))
    idAdministrador = db.Column(db.Integer, db.ForeignKey('administrador.idAdministrador'))
    productos = db.relationship("Productos", secondary="detalleventa", back_populates="vent")
    clientes = db.relationship('Clientes')