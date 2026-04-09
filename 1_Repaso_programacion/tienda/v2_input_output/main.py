'''
    Tienda V1

    Qué incluye:
        - Variables
        - Input
        - Output
        - Soluciónes a BUGS
            - Bug #1
            - Bug #2
        - Nuevas funcionalidades:
            - Un producto puede tener descuento

    Qué problemas tiene (BUG)
        - 3: El nombre del producto puede ser vacío
        - 4: El precio del producto puede ser vacío
        - 5: El precio admite valores NO numéricos. Sólo debe admitir valores numéricos. El programa debe guiar al usuario
        - 6: El descuento admite valoes NO numéricos. Sólo debe admitir valores numéricos. El programa debe guiar al usuario
        - 7: El precio del producto permite valores negativos. Sólo debe permitir valores positivos.
        - 8: El valor del descuento permite valores negativos. Sólo debe permitir valores positivos.
        - 9: El valor del descuento no debe superar el precio del producto.
        - 10: El valor del descuento no se procesa adecuadamente. Se deben aplicar la siguiente regla:
            - Si el descuento es vacío entonces se asume que el descuento debe ser igual a 0
        - 11: El sistemas SÓLO permite registrar 1 producto. El sistema debería permitir registrar varios productos y mostrar el total de toda la compra.

'''

# Input/entrada
# Solución al BUG #1
print("Ingrese el nombre del producto: ")
nombre_producto = input()

# Input/entrada
# Solución al BUG #2
print("Ingrese el precio del producto: ")
precio_del_producto = input()
precio_del_producto = float(precio_del_producto)

print("Ingrese el descuento del producto: ")
descuento_producto = input()
descuento_producto = float(descuento_producto)

costo_total_producto = precio_del_producto - descuento_producto

# Output/salida
print(f"El producto es: {nombre_producto} y cuesta: {costo_total_producto}")

