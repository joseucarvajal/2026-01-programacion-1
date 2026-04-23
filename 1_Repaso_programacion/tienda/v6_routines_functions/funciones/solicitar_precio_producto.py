
def solicitar_precio_producto():
    repetir_precio = True
    precio_del_producto = 0
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
    return precio_del_producto