def solicitar_nombre_producto():
    repetir_nombre = True
    nombre_producto = ''
    while repetir_nombre == True:
        nombre_producto = input("Ingrese el nombre del producto: ")
        if nombre_producto == '':
            print("ERROR: El nombre del producto no puede ser vacío")
        else:
            repetir_nombre = False
    
    return nombre_producto