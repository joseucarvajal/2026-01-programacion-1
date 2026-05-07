from tienda import Tienda
from producto import Producto
from producto_electronico import ProductoElectronico

tienda = Tienda()
tienda.nombre = "Tienda de la esquina"
tienda.agregar_producto_a_venta()
tienda.agregar_producto_electronico_a_venta()
tienda.agregar_producto_alimenticio_a_venta()
tienda.calcular_total_ventas()
print(f"El total de ventas es: {tienda.total_ventas}")