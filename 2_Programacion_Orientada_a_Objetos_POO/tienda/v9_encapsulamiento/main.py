from producto import Producto
from tienda import Tienda


nombre = input("Ingrese el nombre del producto 1: ")
precio = float(input("Ingrese el precio del producto 1: "))
producto1 = Producto(nombre, precio)

error_descuento = True
while error_descuento == True:
    try:
         producto1.descuento = input("Ingrese el descuento del producto 1: ")
         error_descuento = False
    except ValueError as e:
        print(e)


nombre = input("Ingrese el nombre del producto 2: ")
precio = float(input("Ingrese el precio del producto 2: "))
producto2 = Producto(nombre, precio)
#Problema: Si quiero validar el descuento con repetición (while), tendría qeu repetir el mismo código para cada producto, 
# lo cual no es eficiente ni escalable, porque si tengo 100 productos, tendría que repetir el mismo código 100 veces, 
# lo cual no tiene sentido
# y para esto se crea la versión 10 con métodos
producto2.descuento = input("Ingrese el descuento del producto 2: ")


nombre = input("Ingrese el nombre del producto 3: ")
precio = float(input("Ingrese el precio del producto 3: "))
producto3 = Producto(nombre, precio)
producto3.descuento = input("Ingrese el descuento del producto 3: ")


total_compra = (producto1.precio - producto1.descuento) + (producto2.precio - producto2.descuento) + (producto3.precio - producto3.descuento)

if(producto1.precio < producto2.precio and producto1.precio < producto3.precio):
    print(f"El producto más barato es: {producto1.nombre}")

print(f"El valor total de la compra es: {total_compra}")