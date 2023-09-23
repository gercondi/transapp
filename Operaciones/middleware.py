from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User
from .models import Empresa, UsuarioEmpresa

class AsignarEmpresaMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            try:
                # Buscar la empresa asociada al usuario a través del modelo UsuarioEmpresa
                usuario_empresa = UsuarioEmpresa.objects.get(username=request.user)
                request.user.empresa = usuario_empresa.empresa
            except UsuarioEmpresa.DoesNotExist:
                # Manejar el caso en el que el usuario no tenga una empresa asignada
                request.user.empresa = None

