from tienda import Tienda
from producto import Producto
from producto_electronico import ProductoElectronico

tienda = Tienda()
tienda.nombre = "Tienda de la esquina"
tienda.agregar_producto_a_venta()
tienda.agregar_producto_a_venta()
print(f"El total de ventas es: {tienda.total_ventas}")