from producto import Producto
from producto_electronico import ProductoElectronico
from producto_alimenticio import ProductoAlimenticio

class Tienda:
    nombre: str
    total_ventas: float
    producto_en_venta: Producto
    agregar_producto_electronico_en_venta: ProductoElectronico
    agregar_producto_alimenticio_en_venta: ProductoAlimenticio

    def __init__(self):
        self.total_ventas = 0.0

    def agregar_producto_a_venta(self):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        self.producto_en_venta = Producto(nombre, precio)
        self.producto_en_venta.solicitar_descuento()

    def agregar_producto_electronico_a_venta(self):
        nombre = input("Ingrese el nombre del producto electrónico: ")
        precio = float(input("Ingrese el precio del producto electrónico: "))
        garantia = int(input("Ingrese la garantía del producto electrónico (en meses): "))
        self.producto_electronico = ProductoElectronico(nombre, precio, garantia)
        self.producto_electronico.cobrar_impuesto()

    def agregar_producto_alimenticio_a_venta(self):
        nombre = input("Ingrese el nombre del producto alimenticio: ")
        precio = float(input("Ingrese el precio del producto alimenticio: "))
        fecha_de_vencimiento = input("Ingrese la fecha de vencimiento del producto alimenticio (en formato dd/mm/yyyy): ")
        self.producto_alimenticio = ProductoAlimenticio(nombre, precio, fecha_de_vencimiento)
        self.producto_alimenticio.aplicar_subsidio()


    def calcular_total_ventas(self):
        self.total_ventas = self.total_ventas + self.producto_en_venta.total_producto()
        self.total_ventas = self.total_ventas + self.producto_electronico.total_producto()
        self.total_ventas = self.total_ventas + self.producto_alimenticio.total_producto()