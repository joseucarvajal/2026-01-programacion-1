#clase (molde)
from producto import Producto

# Producto es la clase base / superclase
# ProductoElectronico es la clase hija / derivada, que hereda de Producto
# ProductoElectronico es una especialización de Producto, es decir, es un tipo de producto que tiene características adicionales a las de un producto común,
# como la garantía.
class ProductoElectronico(Producto):

    #atributos, propiedades o características (variables o las cosas que tiene el molde)
    _garantia: int

    def __init__(self, nombre: str, precio: float, garantia: int):
        super().__init__(nombre, precio)
        self._garantia = garantia

    @property
    def garantia(self):
        return self._garantia
    
    @garantia.setter
    def garantia(self, valor: int):
        if valor == "":
            self._garantia = 0
            return
        try:
            valor = int(valor)
        except ValueError:
            raise ValueError(f"ERROR: La garantía del producto {self.nombre} debe ser un número entero")
        if valor < 0:
            raise ValueError(f"ERROR: La garantía del producto {self.nombre} no puede ser negativa")
        else:
            self._garantia = valor

    def cobrar_impuesto(self):
        impuesto = self.precio * 0.1
        self.precio = self.precio + impuesto