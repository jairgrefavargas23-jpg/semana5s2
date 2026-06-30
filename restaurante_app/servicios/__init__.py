"""
Paquete: servicios
Agrupa las clases de servicio que gestionan la lógica principal
del sistema (Restaurante). Se expone aquí para poder importarla
directamente desde el paquete, por ejemplo:
    from servicios import Restaurante
"""

from servicios.restaurante import Restaurante

# __all__ define explícitamente qué nombres se exportan al hacer
# "from servicios import *", siguiendo buenas prácticas de Python.
__all__ = ["Restaurante"]
