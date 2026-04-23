'''
    Tienda V6

    Qué incluye:
        - Ciclos / repeticiones
        - Soluciones a BUGS
            - Es un programa difícil de leer, por lo tanto es difícil de mantener, difícil de hacerle cambios.
            
    Solución:
        - Trabajar con funciones / rutinas, de esta forma el código se vuelve más legible, más fácil de mantener y de hacerle cambios.
    
       

'''

from funciones.solicitar_nombre_producto import solicitar_nombre_producto
from funciones.solicitar_precio_producto import solicitar_precio_producto
from funciones.solicitar_descuento_producto import solicitar_descuento_producto
from funciones.solicitar_si_quiere_continuar import solicitar_si_quiere_continuar

total_compra = 0
continuar_con_la_compra = True

print("Versión 6.1: Funciones / Rutinas")

while continuar_con_la_compra == True:

    nombre_producto = solicitar_nombre_producto()
    precio_del_producto = solicitar_precio_producto()
    descuento_producto = solicitar_descuento_producto(precio_del_producto)

    costo_total_producto = precio_del_producto - descuento_producto
    total_compra = total_compra + costo_total_producto

    print(f"El producto es: {nombre_producto} y cuesta: {costo_total_producto}")

    continuar_con_la_compra = solicitar_si_quiere_continuar()


print(f"El valor total de la compra es: {total_compra}")
