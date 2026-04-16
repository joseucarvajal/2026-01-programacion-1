'''
    Tienda V4

    Qué incluye:
        - Ciclos / repeticiones
        - Soluciones a BUGS
            - 5: El precio admite valores NO numéricos. Sólo debe admitir valores numéricos. El programa debe guiar al usuario: OK
            - 6: El descuento admite valores NO numéricos. Sólo debe admitir valores numéricos. El programa debe guiar al usuario

    Qué problemas tiene (BUG)
        - Es un programa difícil de leer, por lo tanto es difícil de mantener, difícil de hacerle cambios.

'''

total_compra = 0
continuar_con_la_compra = True
while continuar_con_la_compra == True:
    # Input/entrada
    # Solución al BUG #1

    repetir_nombre = True
    while repetir_nombre == True:
        print("Ingrese el nombre del producto: ")
        nombre_producto = input()
        if nombre_producto == '':
            print("ERROR: El nombre del producto no puede ser vacío")
        else:
            repetir_nombre = False

    # Input/entrada
    # Solución al BUG #2
    repetir_precio = True
    while repetir_precio == True:
        print("Ingrese el precio del producto: ")
        precio_del_producto = input()
        if precio_del_producto == '':
            print("ERROR: El precio del producto no puede ser vacío")
        else:
            try:
                precio_del_producto = float(precio_del_producto)
            except:
                print("ERROR: El precio del producto debe ser un valor numérico válido")
                continue
        
        if precio_del_producto < 0:
            print("ERROR: El precio del producto debe ser un valor positivo")
        else:
            repetir_precio = False
        
    print("Ingrese el descuento del producto: ")
    descuento_producto = input()
    if descuento_producto == '':
        descuento_producto = 0
    else:
        try:
            descuento_producto = float(descuento_producto)
            if descuento_producto < 0:
                print("ERROR: El descuento del producto no puede ser negativo")
            else:
                if(descuento_producto > precio_del_producto):
                    print("ERROR: El descuento del producto no puede ser superior a su precio")
                else:
                    costo_total_producto = precio_del_producto - descuento_producto
                    total_compra = total_compra + costo_total_producto

                    # Output/salida
                    print(f"El producto es: {nombre_producto} y cuesta: {costo_total_producto}")
                quiere_continuar = input("Quiere continuar si (s) / No (n): ")
            if(quiere_continuar == "n"):
                continuar_con_la_compra = False
        except:
            print("ERROR: El descuento debe ser un valor numérico válido")

print(f"El valor total de la compra es: {total_compra}")
