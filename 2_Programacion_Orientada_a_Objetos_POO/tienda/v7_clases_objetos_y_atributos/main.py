from producto import Producto
from tienda import Tienda


#objeto (copia del molde): instancia de una clase
producto1 = Producto()
producto1.nombre = input("Ingrese el nombre del producto 1: ")
producto1.precio = float(input("Ingrese el precio del producto 1: "))
producto1.descuento = float(input("Ingrese el descuento del producto 1: "))

# Problema 1: Yo puedo crear un producto sin nombre, sin precio o sin descuento, 
# lo cual no tiene sentido, porque un producto siempre debería tener un nombre, un precio y un descuento (aunque sea 0)
producto2 = Producto()
#producto2.precio = float(input("Ingrese el precio del producto 2: "))
producto2.nombre = input("Ingrese el nombre del producto 2: ")
producto2.descuento = float(input("Ingrese el descuento del producto 2: "))

producto3 = Producto()
producto3.nombre = input("Ingrese el nombre del producto 3: ")
producto3.precio = float(input("Ingrese el precio del producto 3: "))
producto3.descuento = float(input("Ingrese el descuento del producto 3: "))   

total_compra = (producto1.precio - producto1.descuento) + (producto2.precio - producto2.descuento) + (producto3.precio - producto3.descuento)

if(producto1.precio < producto2.precio and producto1.precio < producto3.precio):
    print(f"El producto más barato es: {producto1.nombre}")

print(f"El valor total de la compra es: {total_compra}")