"""
Paquete: modelos
Agrupa las clases que representan las entidades del sistema
(Producto y Cliente). Se exponen aquí para poder importarlas
directamente desde el paquete, por ejemplo:
    from modelos import Producto, Cliente
"""

from modelos.producto import Producto
from modelos.cliente import Cliente

# __all__ define explícitamente qué nombres se exportan al hacer
# "from modelos import *", siguiendo buenas prácticas de Python.
__all__ = ["Producto", "Cliente"]
