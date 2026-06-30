"""
Módulo: cliente.py
Contiene la clase Cliente, que representa a una persona registrada
en el sistema del restaurante.
"""

from modelos.producto import Producto
# Nota: aquí se importa directamente desde el módulo (no desde el paquete)
# porque cliente.py forma parte del mismo paquete "modelos" que producto.py.


class Cliente:
    """
    Representa a un cliente del restaurante.

    Atributos:
        nombre_completo (str): Nombre completo del cliente.
        numero_cedula (str): Número de identificación del cliente.
        visitas_realizadas (int): Cantidad de veces que el cliente ha visitado el restaurante.
        es_cliente_frecuente (bool): Indica si el cliente pertenece al programa de fidelidad.
        lista_pedidos (list): Lista de objetos Producto que el cliente ha pedido (tipo de dato compuesto).
    """

    def __init__(self, nombre_completo: str, numero_cedula: str, visitas_realizadas: int = 0,
                 es_cliente_frecuente: bool = False):
        # Constructor: inicializa los datos personales del cliente
        self.nombre_completo: str = nombre_completo
        self.numero_cedula: str = numero_cedula
        self.visitas_realizadas: int = visitas_realizadas
        self.es_cliente_frecuente: bool = es_cliente_frecuente
        self.lista_pedidos: list = []  # Lista (tipo de dato compuesto) que almacena objetos Producto

    def agregar_pedido(self, producto: Producto) -> None:
        """Agrega un producto a la lista de pedidos del cliente."""
        self.lista_pedidos.append(producto)

    def registrar_visita(self) -> None:
        """Incrementa el contador de visitas del cliente en uno."""
        self.visitas_realizadas += 1
        # Si el cliente acumula 5 o más visitas, se considera cliente frecuente
        if self.visitas_realizadas >= 5:
            self.es_cliente_frecuente = True

    def calcular_total_pedido(self) -> float:
        """Calcula el monto total a pagar sumando el precio de todos los productos pedidos."""
        total_a_pagar: float = sum(producto.precio_unitario for producto in self.lista_pedidos)
        return total_a_pagar

    def __str__(self) -> str:
        # Representación legible del cliente como texto
        cantidad_pedidos: int = len(self.lista_pedidos)
        condicion_frecuente: str = "Sí" if self.es_cliente_frecuente else "No"
        return (f"Cliente: {self.nombre_completo} | Cédula: {self.numero_cedula} | "
                f"Visitas: {self.visitas_realizadas} | Frecuente: {condicion_frecuente} | "
                f"Pedidos: {cantidad_pedidos} | Total a pagar: ${self.calcular_total_pedido():.2f}")
