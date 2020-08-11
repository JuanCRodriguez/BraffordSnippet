import pytest
from factory.contacto.email import EmailFactory
from factory.tipos.perfil import PerfilFactory
from factory.usuario import UsuarioFactory

# params:
# {
#     "UN": TiposPerfil,
# }
@pytest.fixture()
def usuarios(context, cabaña, request):
    if not request.param:
        raise Exception("Invalid param")
    aux = dict()
    perfil_factory = PerfilFactory(context.db)
    user_factory = UsuarioFactory(context.db)
    email_factory = EmailFactory(context.db)
    for key, role in request.param.items():
        aux[key] = user_factory.create(
            cabaña,
            email_factory.create(),
            perfil_factory.get(role)
        )
    context.db.commit()
    return aux