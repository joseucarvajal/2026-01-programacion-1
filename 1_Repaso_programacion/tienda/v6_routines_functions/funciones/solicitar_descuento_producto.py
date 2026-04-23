def solicitar_descuento_producto(precio_del_producto):
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
                    return descuento_producto
        except:
            print("ERROR: El descuento debe ser un valor numérico válido")
            return 0

