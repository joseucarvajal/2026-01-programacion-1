#clase (molde)
class Producto:

    #atributos, propiedades o características (variables o las cosas que tiene el molde)
    nombre: str
    _precio: float
    _descuento: float

    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio
        self._descuento = 0.0

    # Proteger el descuento
    # El encapsulamiento es para proteger, se basa en una idea muy simple: a todo valor se le puede hacer dos cosas
    # 1. Leerlo: obtener su valor, mostrarlo, es decir: get: getter
    # 2. Modificarlo: cambiar su valor, es decir: set: setter

    @property
    def descuento(self):
        return self._descuento
    
    @descuento.setter
    def descuento(self, valor: float):
        try:
            valor = float(valor)
        except ValueError:
            raise ValueError(f"ERROR: El descuento del producto {self.nombre} debe ser un número")
        if valor < 0:
            raise ValueError(f"ERROR: El descuento del producto {self.nombre} no puede ser negativo")
        elif valor > self.precio:
            raise ValueError(f"ERROR: El descuento del producto {self.nombre} no puede ser mayor al precio del producto")
        else:
            self._descuento = valor

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, valor: float):
        try:
            valor = float(valor)
        except ValueError:
            raise ValueError(f"ERROR: El precio del producto {self.nombre} debe ser un número")
        if valor < 0:
            raise ValueError(f"ERROR: El precio del producto {self.nombre} no puede ser negativo")
        else:
            self._precio = valor

    def solicitar_descuento(self):
        while True:
            try:
                descuento = input(f"Ingrese el descuento del producto {self.nombre}: ") 
                self.descuento = descuento
                break
            except ValueError as e:
                print(e)

    def total_producto(self):
        return self.precio - self.descuento