from django.contrib import admin
from .models import Tarifa, Zona, UsuarioEmpresa, Empresa, Clientes, Conductores, Propietarios,Placas, TiposCar, Operaciones

# Register your models here.
admin.site.register(Tarifa)
admin.site.register(Zona)
admin.site.register(UsuarioEmpresa)
admin.site.register(Empresa)
admin.site.register(Clientes)
admin.site.register(Conductores)
admin.site.register(Propietarios)
admin.site.register(Placas)
admin.site.register(TiposCar)
admin.site.register(Operaciones)