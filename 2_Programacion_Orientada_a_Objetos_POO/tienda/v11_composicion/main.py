from tienda import Tienda


tienda = Tienda()
tienda.nombre = "Tienda de la esquina"
tienda.agregar_producto_a_venta()
tienda.agregar_producto_a_venta()
tienda.agregar_producto_a_venta()
print(f"El total de ventas es: {tienda.total_ventas}")