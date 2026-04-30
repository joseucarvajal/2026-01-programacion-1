#clase (molde)
class Producto:

    #atributos, propiedades o características (variables o las cosas que tiene el molde)
    nombre: str
    precio: float
    descuento: float

    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio
        self.descuento = 0.0