from pypika import Table


class TipoCuernoTable(Table):
    id: int
    descripcion: str

    def __init__(self):
        super().__init__('tipo_cuerno')
