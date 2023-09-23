from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('inicio/', views.inicio, name='inicio'),

    path('tarifas/', views.TarifaListar.as_view()),
    path('registrarTarifa/', views.TarifaCrear.as_view()),
    path('edicionTarifa/<int:pk>', views.TarifaEditar.as_view()),
    #path('editarTarifa/', views.editarTarifa),

    path('eliminarTarifa/<codigo>', views.eliminarTarifa),

    path('empresas/', views.empresa),
    path('crearEmpresa/', views.crearEmpresa),
    path('edicionEmpresa/<id>', views.edicionEmpresa),
    path('editarEmpresa/', views.editarEmpresa),

    path('tiposcar/', views.TiposCarListar.as_view()),
    path('crearTiposcar/', views.TiposCarCrear.as_view()),
    path('edicionTiposcar/<int:pk>', views.TiposCarEditar.as_view()),

    path('conductores/', views.ConductoresListar.as_view()),
    path('crearConductor/', views.ConductoresCrear.as_view()),
    path('edicionConductor/<int:pk>', views.ConductoresEditar.as_view()),

    path('propietarios/', views.PropietariosListar.as_view()),
    path('crearPropietario/', views.PropietariosCrear.as_view()),
    path('edicionPropietario/<int:pk>', views.PropietariosEditar.as_view()),

    path('placas/', views.PlacasListar.as_view()),
    path('crearPlaca/', views.PlacasCrear.as_view()),
    path('edicionPlaca/<int:pk>', views.PlacasEditar.as_view()),

    path('clientes/', views.ClientesListar.as_view()),
    path('crearCliente/', views.ClientesCrear.as_view()),
    path('edicionCliente/<int:pk>', views.ClienteEditar.as_view()),
  #  path('editarCliente/', views.editarCliente),

    path('zona/', views.ZonasList.as_view()),
    path('crearZona/', views.ZonasCreate.as_view()),
    path('edicionZona/<int:pk>', views.ZonaEditar.as_view()),
  #  path('editarZona/', views.editarZona),
  
  path('get_vehicle_info/', views.get_vehicle_info),

 
  path('operacion/', views.ServiciosList.as_view(), name='servicios_listar'),
  #path('cargarServicio/', views.cargarServicio),

  path('edicionServicios/<int:pk>', views.ServiciosEditar.as_view()),
  
  #path('editarServicio/', views.editarServicio),

  path('crearServicio/', views.ServiciosCreate.as_view()),

    path('logout/', views.exit)

]