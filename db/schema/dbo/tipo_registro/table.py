from pypika import Table


class TipoRegistroTable(Table):
    id: int
    descripcion: str
    orden: int

    def __init__(self):
        super().__init__('tipo_registro')
