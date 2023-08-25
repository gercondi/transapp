from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('inicio/', views.inicio, name='inicio'),

    path('tarifas/', views.tarifas),
    path('registrarTarifa/<empresa>', views.registrarTarifa),
    path('edicionTarifa/<codigo>', views.edicionTarifa),
    path('editarTarifa/<empresa>', views.editarTarifa),

    path('eliminarTarifa/<codigo>', views.eliminarTarifa),

    path('empresas/', views.empresa),
    path('crearEmpresa/', views.crearEmpresa),
    path('edicionEmpresa/<id>', views.edicionEmpresa),
    path('editarEmpresa/', views.editarEmpresa),

    path('clientes/<empresa>', views.cliente),
  #  path('crearClientes/', views.crearCliente),
  #  path('edicionCliente/<id>', views.edicionCliente),
  #  path('editarCliente/', views.editarCliente),

    path('zona/<empresa>', views.zona),
  #  path('crearZona/', views.crearZona),
  #  path('edicionZona/<id>', views.edicionZona),
  #  path('editarZona/', views.editarZona),

  path('operacion/<empresa>', views.Operacion),
    path('cargarServicio/<empresa>', views.cargarServicio),
  #  path('edicionZona/<id>', views.edicionZona),
  #  path('editarZona/', views.editarZona),

    path('logout/', views.exit)

]