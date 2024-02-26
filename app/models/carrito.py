from app.models.producto import Productos

class Carritos:
    def __init__(self):
        self.carrito = []

    def agregar_producto(self, producto_id, cantidad):
        producto = Productos.query.get(producto_id)
        if producto:
            item = {'producto': producto, 'cantidad': cantidad}
            self.carrito.append(item)

    def calcular_total(self):
        return sum(item['producto'].precioProductocompra * item['cantidad'] for item in self.carrito)
    
    def tamañoD(self):   
        return len(self.carrito)

    def getItems(self):
        return self.carrito
    
    def eliminarItem(self,item):
        self.carrito.remove(item)
    
    def vaciarcarrito(self):
        self.carrito = []
