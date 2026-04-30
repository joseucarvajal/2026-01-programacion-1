from producto import Producto

class Tienda:
    nombre: str
    total_ventas: float
    producto_en_venta: Producto

    def __init__(self):
        self.total_ventas = 0.0

    def agregar_producto_a_venta(self):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        self.producto_en_venta = Producto(nombre, precio)
        self.producto_en_venta.solicitar_descuento()
        self.total_ventas = self.total_ventas + self.producto_en_venta.total_producto()

    