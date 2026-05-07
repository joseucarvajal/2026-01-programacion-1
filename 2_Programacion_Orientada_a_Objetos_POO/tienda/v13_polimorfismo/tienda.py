from producto import Producto
from producto_electronico import ProductoElectronico
from producto_alimenticio import ProductoAlimenticio

class Tienda:
    nombre: str
    total_ventas: float
    producto_en_venta: Producto

    def __init__(self):
        self.total_ventas = 0.0

    def agregar_producto_a_venta(self):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        tipo_producto = input("Ingrese el tipo de producto electronico (e), alimenticio (a): ")
        if tipo_producto == "e":
            garantia = int(input("Ingrese la garantía del producto electrónico (en meses): "))
            self.producto_en_venta = ProductoElectronico(nombre, precio, garantia)
        elif tipo_producto == "a":
            fecha_de_vencimiento = input("Ingrese la fecha de vencimiento del producto alimenticio (en formato dd/mm/yyyy): ")
            self.producto_en_venta = ProductoAlimenticio(nombre, precio, fecha_de_vencimiento)
        self.producto_en_venta.solicitar_descuento()
        self.total_ventas = self.total_ventas + self.producto_en_venta.total_producto()
