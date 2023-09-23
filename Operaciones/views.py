from datetime import datetime
from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Tarifa, Empresa, Clientes, Zona, Operaciones, TiposCar, UsuarioEmpresa, Placas, Conductores, Propietarios
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .forms import ClientesForm, ConductoresForm, OperacionesForm, PlacasForm, PropietariosForm, TarifasForm, TiposCarForm, ZonasForm

from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User

# Create your views here.

def inicio(request):
    return redirect("/")

def exit(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request, 'inicio.html',{'empresa':'1'})
   # tarifas  = Tarifa.objects.all() #lista de Tarifas
   # messages.success(request,'!Tarifas Listadas¡')
   # return render(request, "gestionTarifas.html", {"tarifa":tarifas})

@login_required
def tarifas(request):
    usuario = request.user
    empresa= UsuarioEmpresa.objects.get(username= usuario)
    tarifas = Tarifa.objects.filter(empresa=empresa.id)
    return render(request, "gestionTarifas.html", {"tarifa":tarifas})

def registrarTarifa(request):
    codigo=request.POST['txtcodigo']
    #cliente=request.POST['txtcliente']
    #zona=request.POST['txtzona']
    tipo_carro=request.POST['txttipo_carro']
    valor_cobrar=request.POST['txtcobrar']
    valor_pagar=request.POST['txtpagar']

    tarifa=Tarifa.objects.create(codigo=codigo, Cliente=cliente,zona=zona,tipo_carro=tipo_carro, valor_cobrar=valor_cobrar, valor_pagar=valor_pagar)
    
    tarifa.Cliente = Clientes.objects.get(nombre = request.POST['txtcliente'])
    tarifa.zona =Zona.objects.get(zona= request.POST['txtzona'])
    tarifa.tipo_carro = TiposCar.objects.get(tipo_carro=tipo_carro, empresa=empresa)
    messages.success(request,'!Tarifa Creada¡')
    return redirect('/')

def eliminarTarifa(request, codigo):
    tarifa = Tarifa.objects.get(codigo=codigo)
    tarifa.delete()
    messages.success(request,'!Tarifas Eliminada¡')
    return redirect('/')

def edicionTarifa(request, codigo):
    tarifa = Tarifa.objects.get(codigo=codigo)
    return render(request,"edicionTarifa.html", {"tarifa":tarifa})

def editarTarifa(request, empresa):
    codigo=request.POST['txtcodigo']
    cliente=request.POST['txtcliente']
    zona=request.POST['txtzona']
    tipo_carro=request.POST['txttipo_carro']
    valor_cobrar=request.POST['txtcobrar']
    valor_pagar=request.POST['txtpagar']

    tarifa = Tarifa.objects.get(codigo=codigo)
    tarifa.Cliente= Clientes.objects.get(nit=cliente)
    tarifa.zona = Zona.objects.get(zona=zona, empresa=empresa)
    tarifa.tipo_carro = TiposCar.objects.get(tipo_carro=tipo_carro, empresa=empresa)
    tarifa.valor_cobrar = valor_cobrar
    tarifa.valor_pagar = valor_pagar
    tarifa.save()
    messages.success(request,'!Tarifas Actualizada¡')
    return redirect('/')

# Manejo de Empresas
@login_required
def empresa(request):
    empresas  = Empresa.objects.all() #lista de Empresas
    messages.success(request,'!Empresas Listadas¡')
    return render(request, "gestionEmpresas.html", {"empresas":empresas})

def crearEmpresa(request):
    id=request.POST['txtid']
    nombre=request.POST['txtnombre']
    nit=request.POST['txtnit']
    email=request.POST['txtemail']
    telefono=request.POST['txttelefono']
    observacion=request.POST['txtobservacion']
    estado=request.POST['txtestado']

    #fechacrea=models.DateField()
    #fechaupdate=models.DateField(auto_now=True)
    #usuariocrea= request.POST['txtnombre'] Pendiente enviar el usuario logueado

    empresa=Empresa.objects.create(id=id, nombre=nombre,nit=nit,email=email, telefono=telefono, observacion=observacion, estado=estado)
    messages.success(request,'!Empresa Creada¡')
    return redirect('/empresas/')

def edicionEmpresa(request, id):
    empresa = Empresa.objects.get(id=id)
    return render(request,"edicionEmpresa.html", {"empresa":empresa})

def editarEmpresa(request):
    id=request.POST['txtid']
    nombre=request.POST['txtnombre']
    nit=request.POST['txtnit']
    email=request.POST['txtemail']
    telefono=request.POST['txttelefono']
    observacion=request.POST['txtobservacion']
    estado=request.POST['txtestado']

    empresa = Empresa.objects.get(id=id)
    empresa.nombre= nombre
    empresa.nit = nit
    empresa.email = email
    empresa.telefono = telefono
    empresa.observacion = observacion
    empresa.estado= estado
    empresa.save()
    messages.success(request,'!Empresa Actualizada¡')
    return redirect('/empresas/')
    
@login_required
def cliente(request):
    usuario = request.user
    empresa= UsuarioEmpresa.objects.get(username= usuario)
    clientes= Clientes.objects.filter(empresa=empresa.id)
    messages.success(request,'!Clientes Listados¡')
    return render(request, "gestionClientes.html", {"clientes":clientes})

@login_required
def zona(request):
    usuario = request.user
    empresa= UsuarioEmpresa.objects.get(username= usuario)
    zonas= Zona.objects.filter(empresa=empresa.id)
    messages.success(request,'!Zonas Listadas¡')
    return render(request, "gestionZonas.html", {"zonas":zonas})

@login_required
def Operacion(request):
    usuario = request.user
    empresa= UsuarioEmpresa.objects.get(username= usuario)
    operaciones= Operaciones.objects.filter(empresa_id=empresa.pk) #, fecha=datetime.now())
    test = empresa.empresa.pk
    messages.success(request,'!Operaciones Listadas¡')
    return render(request, "gestionOperaciones.html", {"operaciones":operaciones, 'registros':test})

# creamos la funcion que carga la informacion necesaria para el formulario de Servicios
def cargarServicio(request):
    usuario = request.user
    empresa= UsuarioEmpresa.objects.get(username= usuario)
    clientes=Clientes.objects.filter(empresa=empresa.id)
    zonas=Zona.objects.filter(empresa=empresa.id)
    placas=Placas.objects.filter(empresa=empresa.id)
    return render(request, "crearServicio.html", {"clientes":clientes, "zonas":zonas, "placas":placas})

def get_vehicle_info(request):
    license_plate = request.GET.get('license_plate')
    try:
        placa = Placas.objects.get(id=license_plate)
        owner_name = placa.id_propietario.nombre
        driver_name = placa.conductor.nombre
    except Placas.DoesNotExist:
        owner_name = 'nada'
        driver_name = 'nada'

    data = {'owner': owner_name, 'driver': driver_name}
    return JsonResponse(data)

# Funcion que recibe la informacion de la pagina y crea el servicio en la base de datos
def crearServicio(request):

    usuario=request.user
    empresausuario=UsuarioEmpresa.objects.get(username= usuario)
    
    fecha= datetime.now #strptime(request.POST['dtfecha'], '%d/%m/%Y')
    hora=request.POST['txthora']
    tiposerv=request.POST['idTiposerv']
    cliente=request.POST['idCliente']
    zona=request.POST['idZona']
    placa=request.POST['idPlacaSelect']
    origen=request.POST['txtorigen']
    destino=request.POST['txtdestino']
    usuarios=request.POST['txtusuarios']
    #al grabar el registro el estado se coloca como Asignado
    estado = "1"
    comentario=request.POST['txtComentrio']
    

    #Guardamos el registro con la informacion recibida del servicio
    Operaciones.empresa = empresausuario.empresa
    Operaciones.placa = Placas.objects.get(id=placa)
    Operaciones.cliente=Clientes.objects.get(id=cliente)
    Operaciones.zona =Zona.objects.get(id=zona)
    Operaciones.objects.create(
                               fecha=fecha,
                                hora=hora,
                                tipo_servicio=tiposerv,
                                origen=origen,
                                destino=destino,
                                placa=placa,
                                usuarios=usuarios,
                                comentario=comentario,
                                estado=estado)
    return redirect('/gestionOperaciones/') 

def edicionServicios(request, id):
    servicio=Operaciones.objects.get(id=id)
    return redirect('/editarServicio/', {'servicio':servicio}) 

def editarServicio(request):
    if request.method == 'POST':
        form = OperacionesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/operacion/')
    else:
        form = OperacionesForm()
    return render(request,'edicionServicio.html',{'form':form})

#===================== Servicios =====================================

class ServiciosList(LoginRequiredMixin, ListView):
    model=Operaciones
    template_name='gestionOperaciones.html'

    # - Filtramos las Zonas que pertenecen a la empresa del Usuario -----
    def get_queryset(self):
        empresa= UsuarioEmpresa.objects.get(username= self.request.user)
        return Operaciones.objects.filter(empresa=empresa.id) 

class ServiciosEditar(UpdateView):
    model=Operaciones
    form_class= OperacionesForm
    template_name='edicionForm.html'
    success_url=('/edicionTarifa/')

class ServiciosEliminar(DeleteView):
    model=Operaciones
    form_class= OperacionesForm
    template_name='edicionForm.html'

class ServiciosCreate(LoginRequiredMixin, CreateView):
    model=Operaciones
    form_class = OperacionesForm
    template_name ='edicionForm.html'
    success_url= ('/operacion/')

    def get_form_kwargs(self):
        kwargs = super(ServiciosCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pasar el usuario al formulario
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user 
        user = self.request.user #User.objects.get(username = self.request.user)    
        
        Operaciones.objects.create( placa = Placas.objects.get(id=self.request.POST['placa']),
                                    cliente=Clientes.objects.get(id=self.request.POST['cliente']),
                                    zona =Zona.objects.get(id=self.request.POST['zona']),
                                    hora=self.request.POST['hora'],
                                    fecha=self.request.POST['fecha'],                                   
                                    tipo_servicio=self.request.POST['tipo_servicio'],
                                    origen=self.request.POST['origen'],
                                    destino=self.request.POST['destino'],
                                    usuarios=self.request.POST['usuarios'],
                                    comentario =self.request.POST['comentario'],
                                    estado='1',
                                    empresa=UsuarioEmpresa.objects.get(username = user.username).empresa,
                                    usuariocrea=user.username)
        
        return redirect(self.success_url)
    

#=================================== Zona =================================================
class ZonasList(LoginRequiredMixin, ListView):
    model=Zona
    template_name='gestionZonas.html'

    # - Filtramos las Zonas que pertenecen a la empresa del Usuario -----
    def get_queryset(self):
        empresa= UsuarioEmpresa.objects.get(username= self.request.user)
        return Zona.objects.filter(empresa=empresa.id) 

class ZonasCreate(LoginRequiredMixin, CreateView):
    model=Zona
    form_class= ZonasForm
    template_name='edicionForm.html'
    success_url=('/zona/')

    def form_valid(self, form):
        user = User.objects.get(username = self.request.user)
        Zona.objects.create(zona=self.request.POST['zona'], 
                            empresa=UsuarioEmpresa.objects.get(username = user.username).empresa)
        return redirect(self.success_url)
       

class ZonaEditar(UpdateView):
    model=Zona
    fields=['zona']
    template_name= 'edicionForm.html'
    success_url=('/zona/')
    
#========================= Tarifas ====================================================
class TarifaListar(LoginRequiredMixin, ListView):
    model = Tarifa
    template_name='gestionTarifas.html'

    # - Filtramos las Tarifas que pertenecen a la empresa del Usuario -----
    def get_queryset(self):
        empresa= UsuarioEmpresa.objects.get(username= self.request.user)
        return Tarifa.objects.filter(empresa=empresa.id) 

class TarifaCrear(LoginRequiredMixin, CreateView):
    model=Tarifa
    form_class= TarifasForm
    template_name='edicionForm.html'
    success_url=('/tarifas/')

    def get_form_kwargs(self):
        kwargs = super(TarifaCrear, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pasar el usuario al formulario
        return kwargs 

    def form_valid(self, form):
        user = User.objects.get(username = self.request.user)
        Tarifa.objects.create(
                            Cliente=Clientes.objects.get(id=self.request.POST['Cliente']),
                            origendestino=self.request.POST['origendestino'],
                            tipo_carro=TiposCar.objects.get(id=self.request.POST['tipo_carro']),
                            valor_cobrar=self.request.POST['valor_cobrar'],
                            valor_pagar=self.request.POST['valor_pagar'],
                            comentarios=self.request.POST['comentarios'],
                            zona=Zona.objects.get(id=self.request.POST['zona']), 
                            estado=1,
                            empresa=UsuarioEmpresa.objects.get(username = user.username).empresa)
        return redirect(self.success_url)

class TarifaEditar(UpdateView):
    model=Tarifa
    form_class= TarifasForm
    template_name='edicionForm.html'
    success_url=('/tarifas/')

#=================== Conductores ===========================
class ConductoresListar(LoginRequiredMixin, ListView):
    model = Conductores
    template_name = 'gestionConductores.html'

     # - Filtramos las Tarifas que pertenecen a la empresa del Usuario -----
    def get_queryset(self):
        empresa= UsuarioEmpresa.objects.get(username= self.request.user)
        return Conductores.objects.filter(empresa=empresa.id) 

class ConductoresEditar(UpdateView):
    model = Conductores
    form_class= ConductoresForm
    template_name='edicionForm.html'
    success_url=('/conductores/')

class ConductoresCrear(LoginRequiredMixin, CreateView):
    model = Conductores
    form_class= ConductoresForm
    template_name='edicionForm.html'
    success_url=('/conductores/')

    def form_valid(self, form):
        user = User.objects.get(username = self.request.user)
        Conductores.objects.create(
                            nombre=self.request.POST['nombre'],
                            email=self.request.POST['email'],
                            telefono=self.request.POST['telefono'],
                            cedula=self.request.POST['cedula'],
                            
                            empresa=UsuarioEmpresa.objects.get(username = user.username).empresa)
        return redirect(self.success_url)

#=================== Propietarios ===========================
class PropietariosListar(LoginRequiredMixin, ListView):
    model = Propietarios
    template_name = 'gestionPropietarios.html'

     # - Filtramos las Tarifas que pertenecen a la empresa del Usuario -----
    def get_queryset(self):
        empresa= UsuarioEmpresa.objects.get(username= self.request.user)
        return Propietarios.objects.filter(empresa=empresa.id) 


class PropietariosEditar(UpdateView):
    model = Propietarios
    form_class= PropietariosForm
    template_name='edicionForm.html'
    success_url=('/propietarios/')

class PropietariosCrear(LoginRequiredMixin, CreateView):
    model = Propietarios
    form_class= PropietariosForm
    template_name='edicionForm.html'
    success_url=('/propietarios/')

    def form_valid(self, form):
        user = User.objects.get(username = self.request.user)
        empresa = UsuarioEmpresa.objects.get(username = user.username).empresa
        Propietarios.objects.create(
                            nombre=self.request.POST['nombre'],
                            email=self.request.POST['email'],
                            telefono=self.request.POST['telefono'],
                            nit=self.request.POST['nit'],
                            
                            empresa=empresa)
        return redirect(self.success_url)
    
#============================= Placas ===================

class PlacasListar(LoginRequiredMixin, ListView):
    model=Placas
    template_name = 'gestionPlacas.html'

     # - Filtramos las Placas que pertenecen a la empresa del Usuario -----
    def get_queryset(self):
        empresa= UsuarioEmpresa.objects.get(username= self.request.user)
        return Placas.objects.filter(empresa=empresa.id) 

class PlacasEditar(UpdateView):
    model=Placas
    form_class= PlacasForm
    template_name='edicionForm.html'
    success_url=('/placas/')

    def get_form_kwargs(self):
        kwargs = super(PlacasEditar, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pasar el usuario al formulario
        return kwargs


class PlacasCrear(LoginRequiredMixin, CreateView):
    model=Placas
    form_class= PlacasForm
    template_name='edicionForm.html'
    success_url=('/placas/')

    def get_form_kwargs(self):
        kwargs = super(PlacasCrear, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Pasar el usuario al formulario
        return kwargs

    def form_valid(self, form):
        user = User.objects.get(username = self.request.user)
        empresa = UsuarioEmpresa.objects.get(username = user.username).empresa
        Placas.objects.create(
                            placa=self.request.POST['placa'],
                            capacidad = self.request.POST['capacidad'],
                            id_propietario=Propietarios.objects.get(pk=self.request.POST['id_propietario']),
                            conductor=Conductores.objects.get(pk=self.request.POST['conductor']),
                            tipo_carro=TiposCar.objects.get(pk=self.request.POST['tipo_carro']),
                            usuariocrea=user,
                            empresa=empresa)
        return redirect(self.success_url)
    
#==================== CLIENTES ============================
class ClientesListar(LoginRequiredMixin, ListView):
    model=Clientes
    template_name = 'gestionClientes.html'

    # - Filtramos los Clientes que pertenecen a la empresa del Usuario -----
    def get_queryset(self):
        empresa= UsuarioEmpresa.objects.get(username= self.request.user)
        return Clientes.objects.filter(empresa=empresa.id) 

class ClienteEditar(LoginRequiredMixin, UpdateView):
    model=Clientes
    form_class= ClientesForm
    template_name='edicionForm.html'
    success_url=('/clientes/')


class ClientesCrear(LoginRequiredMixin, CreateView):
    model=Clientes
    form_class= ClientesForm
    template_name='edicionForm.html'
    success_url=('/clientes/')
    
    def form_valid(self, form):
        user =  User.objects.get(username = self.request.user)
        empresa = UsuarioEmpresa.objects.get(username = user.username).empresa
        Clientes.objects.create(
                            nit=self.request.POST['nit'],
                            nombre = self.request.POST['nombre'],
                            email=self.request.POST['email'],
                            contacto=self.request.POST['contacto'],
                            telefono=self.request.POST['telefono'],
                            usuariocrea=user,
                            empresa=empresa)
        return redirect(self.success_url)

#==================== TIPOS DE CARRO ============================
class TiposCarListar(LoginRequiredMixin, ListView):
    model=TiposCar
    template_name = 'gestionTiposcar.html'

    # - Filtramos los Clientes que pertenecen a la empresa del Usuario -----
    def get_queryset(self):
        empresa= UsuarioEmpresa.objects.get(username= self.request.user)
        return TiposCar.objects.filter(empresa=empresa.id) 

class TiposCarEditar(LoginRequiredMixin, UpdateView):
    model=TiposCar
    form_class= TiposCarForm
    template_name='edicionForm.html'
    success_url=('/tiposcar/')

class TiposCarCrear(LoginRequiredMixin, CreateView):
    model=TiposCar
    form_class= TiposCarForm
    template_name='edicionForm.html'
    success_url=('/tiposcar/')

    def form_valid(self, form):
        user =  User.objects.get(username = self.request.user)
        empresa = UsuarioEmpresa.objects.get(username = user.username).empresa
        TiposCar.objects.create(
                            tipo_carro=self.request.POST['tipo_carro'],
                            observacion = self.request.POST['observacion'],
                            usuariocrea=user,
                            empresa=empresa)
        return redirect(self.success_url)