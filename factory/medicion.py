from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.medicion.handler import MedicionHandler
from dominio.mediciones import Mediciones
from dominio.producto import Denticion


class MedicionFactory:

    def __init__(self, db: MSSQLConnection):
        self._medicion_handler = MedicionHandler(db)

    def create(self, denticion: Denticion) -> Mediciones:
        if not denticion.id:
            raise Exception("Denticion invalida")

        return self._create(denticion)

    # Por el momento, lo unico relevante es la denticion, eventualmente habra que agregar los campos necesarios
    def _create(self, denticion: Denticion) -> Mediciones:
        m = Mediciones(*[None for _ in range(14)], denticion, None, 0, *[None for _ in range(4)])
        m.id = self._medicion_handler.create(m)
        return m
