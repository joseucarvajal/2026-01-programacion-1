#clase (molde)
from producto import Producto


class ProductoAlimenticio(Producto):
    fecha_de_vencimiento: str

    def __init__(self, nombre: str, precio: float, fecha_de_vencimiento: str):
        super().__init__(nombre, precio)
        self.fecha_de_vencimiento = fecha_de_vencimiento

    def aplicar_costos_adicionales(self):
        descuento_subsidio = self.precio * 0.1
        return descuento_subsidio * -1

