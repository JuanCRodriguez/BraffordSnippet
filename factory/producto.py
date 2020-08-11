from datetime import datetime
from random import randint

from db.conn.mssql.conn import MSSQLConnection
from db.schema.dbo.producto.handler import ProductoHandler, ProductoCabañaRelationBuilder, \
    ProductoEstablecimientoRelationBuilder
from dominio.cabaña import Cabaña
from dominio.establecimiento import Establecimiento
from dominio.mediciones import Mediciones
from dominio.producto import Producto, Raza, Registro, Color, Cuerno, Variedad, Parto, Pompe, Sexo


class ProductoFactory:

    def __init__(self, db: MSSQLConnection):
        self._producto_handler = ProductoHandler(db)
        self._producto_cabaña_relation = ProductoCabañaRelationBuilder(db)
        self._producto_establecimiento_relation = ProductoEstablecimientoRelationBuilder(db)

    def create(self,
               cabaña: Cabaña,
               establecimiento: Establecimiento,
               mediciones: Mediciones,
               raza: Raza,
               registro: Registro,
               color: Color,
               cuerno: Cuerno,
               variedad: Variedad,
               parto: Parto,
               pompe: Pompe,
               sexo: Sexo) -> Producto:

        if not cabaña.id:
            raise Exception("Cabaña invalida")

        if not establecimiento.id:
            raise Exception("Establecimiento invalido")

        if not mediciones.id:
            raise Exception("Medicioens invalidas")

        if not raza.id:
            raise Exception("Raza invalida")

        if not registro.id:
            raise Exception("Registro invalido")

        if not color.id:
            raise Exception("Color invalido")

        if not cuerno.id:
            raise Exception("Cuerno invalido")

        if not variedad.id:
            raise Exception("Variedad invalida")

        if not parto.id:
            raise Exception("Parto invalido")

        if not pompe.id:
            raise Exception("Pompe invalido")

        if not sexo.id:
            raise Exception("Sexo invalido")

        return self._create(cabaña, establecimiento, mediciones,
                            raza, registro, color,
                            cuerno, variedad, parto,
                            pompe, sexo)

    def _create(self,
                cabaña: Cabaña,
                establecimiento: Establecimiento,
                mediciones: Mediciones,
                raza: Raza,
                registro: Registro,
                color: Color,
                cuerno: Cuerno,
                variedad: Variedad,
                parto: Parto,
                pompe: Pompe,
                sexo: Sexo) -> Producto:
        n = randint(1, 500)
        p = Producto("RP", f"{sexo.nombre} {n}", "Apodo2", "tat",
                    raza, registro, color, cuerno,
                    variedad, sexo, 12545 + n, pompe, mediciones, None,
                    datetime.now(), parto, establecimiento)
        p.id = self._producto_handler.create(p)
        self._producto_cabaña_relation.create(cabaña, p)
        self._producto_establecimiento_relation.create(p, establecimiento)
        return p
