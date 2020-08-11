from pypika import Table


class TipoColorTable(Table):
    id: int
    descripcion: str

    def __init__(self):
        super().__init__('tipo_color')
