from enum import Enum


class TiposPerfil(Enum):

    PRODUCTOR = 'Productor'
    GESTOR = 'Gestión ABA'
    SUPERVISOR = 'Supervisor ABA'


class TiposSexo(Enum):

    MACHO = "Macho"
    HEMBRA = "Hembra"

class TiposVariedad(Enum):

    NO_INFORMADO = "NO INFORMADO"
    MEDIO = "1/2"
    CUARTO = "1/4"
    TRES_CUARTOS = "3/4"
    TRES_OCTAVOS = "3/8"
    CINCO_OCTAVOS = "5/8"
    BRAFORD = "Braford"

class TiposRaza(Enum):
    BRAFORD = "Braford"
    BRAHMAN = "Brahman"
    HEREFORD = "Hereford"
    NELORE = "Nelore"

class TiposDenticion(Enum):
    NO_INFORMADO = "N/I"
    DL = "DL"
    _2D = "2D"
    _4D = "4D"
    _6D = "6D"
    _8D = "8D"
    BLL = "BLL"

class TiposColor(Enum):
    NO_INFORMADO = "NO INFORMADO"
    TIPICO_CLARO = "Tipico de la raza claro"
    TIPICO_OSCURO = "Tipico de la raza oscuro"
    BARCINO = "Barcino"
    HOSCO_BARCINO = "Hosco - Barcino"
    COLORADO = "Colorado"
    TIPICO = "Tipico de la raza"

class TiposRegistro(Enum):
    BRAFORD_ORIGEN = "Braford de origen" # 1
    PREPARATORIO = "Preparatorio" # 2
    CONTROLADO = "Controlado" # 3
    REGISTRADO = "Registrado" # 4
    AVANZADO = "Avanzado" # 5
    DEFINITIVO = "Definitivo" # 6

class OrdenRegistro:
    BRAFORD_ORIGEN = 1
    PREPARATORIO = 2
    CONTROLADO = 3
    REGISTRADO = 4
    AVANZADO = 5
    DEFINITIVO = 6

class TiposParto(Enum):
    NO_INFORMADO = "NO INFORMADO"
    NORMAL = "Normal"
    AYUDA_MENOR = "Ayuda menor"
    AYUDA_MAYOR = "Ayuda mayor/traccion"
    CESAREA = "Cesarea"
    ABORTO = "Aborto"


class TiposPompe(Enum):

    SIN_ANALISIS = "Sin Análisis"
    POSITIVO = "Positivo"
    NEGATIVO = "Negativo"

class TiposCuerno(Enum):

    NO_INFORMADO = "NO INFORMADO"
    ASTADO = "Astado"
    MOCHO = "Mocho"
    TOCO = "Toco"

class TiposServicio(Enum):

    COLECTIVO_CON_ID = "Colectivo con identificación"
    FLUSHING = "Flushing"
    IMPLANTE_EMBRIONARIO = "Implante embrionario"
    INSEMINACION_ARTIFICIAL = "Inseminación artificial"
    INDIVIDUAL = "Individual"
    COLECTIVO_SIN_ID = "Colectivo sin identificación"
    FERTILIZACION_IN_VITRO = "Fertilización in vitro"
    NO_INFORMADO = "NO INFORMADO"