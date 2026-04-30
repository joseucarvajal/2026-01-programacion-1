from producto import Producto
from tienda import Tienda


nombre = input("Ingrese el nombre del producto 1: ")
precio = float(input("Ingrese el precio del producto 1: "))
producto1 = Producto(nombre, precio)
producto1.solicitar_descuento()

nombre = input("Ingrese el nombre del producto 2: ")
precio = float(input("Ingrese el precio del producto 2: "))
producto2 = Producto(nombre, precio)
producto2.solicitar_descuento()

nombre = input("Ingrese el nombre del producto 3: ")
precio = float(input("Ingrese el precio del producto 3: "))
producto3 = Producto(nombre, precio)
producto3.solicitar_descuento()

total_compra = producto1.total_producto() + producto2.total_producto() + producto3.total_producto()

if(producto1.precio < producto2.precio and producto1.precio < producto3.precio):
    print(f"El producto más barato es: {producto1.nombre}")

print(f"El valor total de la compra es: {total_compra}")