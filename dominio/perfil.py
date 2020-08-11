


class Perfil:

    def __init__(self, nombre, id):
        self.id = id
        self.nombre = nombre


    def __eq__(self, other):
        return self.id == other.id and self.nombre == other.tipo