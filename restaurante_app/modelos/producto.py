"""
Módulo: producto.py
Contiene la clase Producto, que representa un plato, bebida o
producto disponible en el menú del restaurante.
"""


class Producto:
    """
    Representa un producto (plato o bebida) ofrecido por el restaurante.

    Atributos:
        nombre_producto (str): Nombre del producto (ej. "Ceviche de camarón").
        categoria (str): Categoría a la que pertenece (ej. "Plato fuerte", "Bebida").
        precio_unitario (float): Precio unitario del producto.
        esta_disponible (bool): Indica si el producto está disponible para la venta.
    """

    def __init__(self, nombre_producto: str, categoria: str, precio_unitario: float, esta_disponible: bool = True):
        # Constructor: inicializa los atributos básicos del producto
        # Se aplican identificadores descriptivos y anotaciones de tipo según cada dato
        self.nombre_producto: str = nombre_producto
        self.categoria: str = categoria
        self.precio_unitario: float = precio_unitario
        self.esta_disponible: bool = esta_disponible

    def cambiar_disponibilidad(self, nuevo_estado: bool) -> None:
        """Actualiza si el producto está disponible o no en el menú."""
        self.esta_disponible = nuevo_estado

    def aplicar_descuento(self, porcentaje_descuento: float) -> None:
        """
        Aplica un descuento porcentual al precio del producto.
        Por ejemplo, aplicar_descuento(10) reduce el precio en un 10%.
        """
        if 0 < porcentaje_descuento < 100:
            self.precio_unitario = self.precio_unitario - (self.precio_unitario * porcentaje_descuento / 100)

    def __str__(self) -> str:
        # Representación legible del objeto como texto
        estado_texto: str = "Disponible" if self.esta_disponible else "No disponible"
        return (f"{self.nombre_producto} | Categoría: {self.categoria} | "
                f"Precio: ${self.precio_unitario:.2f} | {estado_texto}")
