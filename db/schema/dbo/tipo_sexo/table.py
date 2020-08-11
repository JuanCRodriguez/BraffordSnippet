from pypika import Table


class TipoSexoTable(Table):
    id: int
    descripcion: str

    def __init__(self):
        super().__init__('tipo_sexo')
