from producto import Producto
from tienda import Tienda


nombre = input("Ingrese el nombre del producto 1: ")
precio = float(input("Ingrese el precio del producto 1: "))
producto1 = Producto(nombre, precio)
producto1.descuento = float(input("Ingrese el descuento del producto 1: "))

nombre = input("Ingrese el nombre del producto 2: ")
precio = float(input("Ingrese el precio del producto 2: "))
producto2 = Producto(nombre, precio)
#Problema: el descuento puede ser negativo o puede ser mayor al precio, lo cual no tiene sentido, porque un descuento no puede ser negativo ni puede ser mayor al precio del producto
producto2.descuento = float(input("Ingrese el descuento del producto 2: "))

nombre = input("Ingrese el nombre del producto 3: ")
precio = float(input("Ingrese el precio del producto 3: "))
producto3 = Producto(nombre, precio)
producto3.descuento = float(input("Ingrese el descuento del producto 3: "))

total_compra = (producto1.precio - producto1.descuento) + (producto2.precio - producto2.descuento) + (producto3.precio - producto3.descuento)

if(producto1.precio < producto2.precio and producto1.precio < producto3.precio):
    print(f"El producto más barato es: {producto1.nombre}")

print(f"El valor total de la compra es: {total_compra}")