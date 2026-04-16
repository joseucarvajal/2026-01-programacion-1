'''
    Tienda V3

    Qué incluye:
        - Condicionales
        - Soluciónes a BUGS
            - 3: El nombre del producto puede ser vacío: OK
            - 4: El precio del producto puede ser vacío: OK
            - 7: El precio del producto permite valores negativos. Sólo debe permitir valores positivos: OK
            - 8: El valor del descuento permite valores negativos. Sólo debe permitir valores positivos: OK
            - 9: El valor del descuento no debe superar el precio del producto: OK
            - 10: El valor del descuento no se procesa adecuadamente. Se debe aplicar la siguiente regla: OK
                - Si el descuento es vacío entonces se asume que el descuento debe ser igual a 0

    Qué problemas tiene (BUG)
        - 5: El precio admite valores NO numéricos. Sólo debe admitir valores numéricos. El programa debe guiar al usuario
        - 6: El descuento admite valoes NO numéricos. Sólo debe admitir valores numéricos. El programa debe guiar al usuario
        - 11: El sistemas SÓLO permite registrar 1 producto. El sistema debería permitir registrar varios productos y mostrar el total de toda la compra.
        - 12: El sistema no es capaz de recuperarse de los errores. Cuando hay un error el sistema debería repetir la pregunta del dato que causó el error
        hasta que este dato se digite bien.

'''

# Input/entrada
# Solución al BUG #1
print("Ingrese el nombre del producto: ")
nombre_producto = input()
if nombre_producto == '':
    print("ERROR: El nombre del producto no puede ser vacío")
else:
    # Input/entrada
    # Solución al BUG #2
    print("Ingrese el precio del producto: ")
    precio_del_producto = input()
    if precio_del_producto == '':
        print("ERROR: El precio del producto no puede ser vacío")
    else:
        precio_del_producto = float(precio_del_producto)
        
        if precio_del_producto < 0:
            print("ERROR: El precio del producto debe ser un valor positivo")
        else:
            print("Ingrese el descuento del producto: ")
            descuento_producto = input()
            if descuento_producto == '':
                descuento_producto = 0
            else:
                descuento_producto = float(descuento_producto)

            if descuento_producto < 0:
                print("ERROR: El descuento del producto no puede ser negativo")
            else:
                if(descuento_producto > precio_del_producto):
                    print("ERROR: El descuento del producto no puede ser superior a su precio")
                else:
                    costo_total_producto = precio_del_producto - descuento_producto

                    # Output/salida
                    print(f"El producto es: {nombre_producto} y cuesta: {costo_total_producto}")

