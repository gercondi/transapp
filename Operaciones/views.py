from datetime import datetime
from django.shortcuts import render, redirect
from .models import Tarifa, Empresa, Clientes, Zona, Operaciones, TiposCar, UsuarioEmpresa
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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
    UsuarioEmpresa.empresa = UsuarioEmpresa.objects.get(username= usuario)
    tarifas = Tarifa.objects.filter(empresa=empresa)
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
def cliente(request, empresa):
    clientes= Clientes.objects.filter(empresa=empresa)
    messages.success(request,'!Clientes Listados¡')
    return render(request, "gestionClientes.html", {"clientes":clientes})

@login_required
def zona(request, empresa):
    zonas= Zona.objects.filter(empresa=empresa)
    messages.success(request,'!Zonas Listadas¡')
    return render(request, "gestionZonas.html", {"zonas":zonas})

@login_required
def Operacion(request, empresa):
    operaciones= Operaciones.objects.filter(empresa=empresa, fecha=datetime.now())
    messages.success(request,'!Operaciones Listadas¡')
    return render(request, "gestionOperaciones.html", {"operaciones":operaciones})

# creamos la funcion que carga la informacion necesaria para el formulario de Servicios
def cargarServicio(request, empresa):
    clientes=Clientes.objects.filter(empresa=empresa)
    return render(request, "crearServicio.html", {"clientes":clientes})

# Funcion que recibe la informacion de la pagina y crea el servicio en la base de datos
def crearServicio(request):

    messages.success(request, 'Servicio Creado!')
    return redirect('/gestionOperaciones/') 