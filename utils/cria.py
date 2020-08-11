from dominio.enums.tipos import TiposRegistro, OrdenRegistro
from dominio.producto import Producto


def cria_suceptible_ga(madre: Producto):
    return madre.registro.orden >= OrdenRegistro.CONTROLADO
