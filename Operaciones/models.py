from django.db import models

# Create your models here.
class Empresa(models.Model):
    id=models.PositiveIntegerField(null=False, primary_key=True)
    nombre=models.CharField(max_length=60, null=False)
    nit=models.CharField(max_length=20,null=False)
    email=models.EmailField()
    telefono=models.CharField(max_length=20)
    observacion=models.TextField(verbose_name='Observaciones')
    # Este compo establece el estado del cliente Activo(1) inactivo(0)
    estado=models.CharField(max_length=1, null=False, default='1')

    fechacrea=models.DateField(auto_now_add=True)
    fechaupdate=models.DateField(auto_now=True)
    usuariocrea=models.CharField(max_length=10, default='')

    def __str__(self):
        texto = "{0},{1},{2},{3}"
        return texto.format(self.nombre,self.email,self.nit, self.telefono)

class UsuarioEmpresa(models.Model):
    id=models.PositiveSmallIntegerField(primary_key=True)
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE)
    username=models.CharField(max_length=150, null=False)
    def __str__(self):
        texto = "{0},{1}"
        return texto.format(self.empresa,self.username)


class Zona(models.Model):
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE)
    id_zona=models.PositiveSmallIntegerField(primary_key=True, null=False)
    zona=models.CharField(max_length=15, null=False)
    
    def __str__(self):
        texto = "{0}"
        return texto.format(self.zona)

class Clientes(models.Model):
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, default=0)
    nit=models.PositiveIntegerField(primary_key=True, null=False)
    nombre=models.CharField(max_length=60, null=False)
    email=models.EmailField()
    contacto=models.CharField(max_length=100) #Persona de contacto
    telefono=models.CharField(max_length=20)
    fechacrea=models.DateField(auto_now_add=True)
    fechaupdate=models.DateField(auto_now=True)
    usuariocrea=models.CharField(max_length=10, default='')

    def __str__(self):
        texto = "{0}, {1}"
        return texto.format(self.nit, self.nombre)

class TiposCar(models.Model):
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, default=0)
    id=models.PositiveIntegerField(primary_key=True)
    tipo_carro=models.CharField(max_length=50, null=False)
    observacion=models.CharField(max_length=200)
    fechacrea=models.DateField(auto_now_add=True)
    fechaupdate=models.DateField(auto_now=True)
    usuariocrea=models.CharField(max_length=10, default='')

    def __str__(self) :
        texto= "{0}, {1}"
        return texto.format(self.tipo_carro, self.observacion)      

class Tarifa(models.Model):
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, default=0)
    codigo=models.PositiveSmallIntegerField(primary_key=True)
    Cliente=models.ForeignKey(Clientes, on_delete=models.CASCADE, default=1)
    #zona=models.CharField(max_length=50)
    zona=models.ForeignKey(Zona, on_delete=models.CASCADE)
    origendestino=models.CharField(max_length=200, null=True ,default='') # almacena la informacion de lugar de origen o destino del servicio para calcular la tarifa
    tipo_carro=models.ForeignKey(TiposCar,on_delete=models.CASCADE)
    valor_cobrar=models.PositiveBigIntegerField(null=False)
    valor_pagar=models.PositiveBigIntegerField(null=False)
    comentarios=models.TextField(default='')
    fechacrea=models.DateField(auto_now_add=True)
    fechaupdate=models.DateField(auto_now=True)
    usuariocrea=models.CharField(max_length=10, default='')

    def __str__(self):
        texto = "{0}, {1}, {2}"
        return texto.format(self.Cliente, self.zona, self.tipo_carro)
    
class Propietarios(models.Model):
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, default=0)
    id_propietario=models.PositiveSmallIntegerField(primary_key=True, null=False)
    nombre=models.CharField(max_length=60, null=False)
    email=models.EmailField()
    telefono=models.CharField(max_length=20)
    fechacrea=models.DateField(auto_now_add=True)
    fechaupdate=models.DateField(auto_now=True)
    usuariocrea=models.CharField(max_length=10,default='')

    def __str__(self):
        texto = "{0}, {1}"
        return texto.format(self.id_propietario, self.nombre)

class Conductores(models.Model):
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, default=0)
    cedula=models.PositiveIntegerField(primary_key=True, null=False)
    nombre=models.CharField(max_length=60, null=False)
    email=models.EmailField()
    telefono=models.CharField(max_length=20)
    fechacrea=models.DateField(auto_now_add=True)
    fechaupdate=models.DateField(auto_now=True)
    usuariocrea=models.CharField(max_length=10, default='')

    def __str__(self):
        texto = "{0}, {1}"
        return texto.format(self.cedula, self.nombre)

  
    
class Placas(models.Model):
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, default=0)
    placa=models.CharField(max_length=6, null=False, primary_key=True)
    tipo_carro=models.ForeignKey(TiposCar, on_delete=models.CASCADE)
    capacidad=models.PositiveSmallIntegerField(default=4, null=False)
    id_propietario=models.ForeignKey(Propietarios, on_delete=models.CASCADE)
    conductor=models.ForeignKey(Conductores, on_delete=models.CASCADE)
    fechacrea=models.DateField(auto_now_add=True)
    fechaupdate=models.DateField(auto_now=True)
    usuariocrea=models.CharField(max_length=10, default='')
    
    def __str__(self):
        texto = "{0}"
        return texto.format(self.placa)

class Operaciones(models.Model):
    opc_SERVICIOS=(
        (0, 'ENTRADA'),
        (1, 'SALIDA'),
        (2, 'OTROS')
    )
    opc_ESTADOS=(
        (0,'PENDIENTE'),
        (1,'ASIGNADO'),
        (2,'EJECUTADO'),
        (3,'CANCELADO')
    )
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, default=0)
    id=models.PositiveIntegerField(primary_key=True, null=False)
    fecha=models.DateField()
    hora=models.DateTimeField(null=False)
    tipo_servicio=models.CharField(choices=opc_SERVICIOS, max_length=50)
    estado=models.CharField(choices=opc_ESTADOS,max_length=20, default='PENDIENTE')
    placa=models.ForeignKey(Placas, on_delete=models.CASCADE)
    cliente=models.ForeignKey(Clientes, on_delete=models.CASCADE)
    origen=models.CharField(max_length=200)
    destino=models.CharField(max_length=200)
    usuarios=models.TextField(null=False)
    zona=models.ForeignKey(Zona, on_delete=models.CASCADE)
    comentario=models.TextField()

    fechacrea=models.DateField(auto_now_add=True)
    fechaupdate=models.DateField(auto_now=True)
    usuariocrea=models.CharField(max_length=10, default='')
    
    def __str__(self):
        texto = "{0},{1},{2},{3},{4},{5},{6},{7}"
        return texto.format(self.tipo_servicio,self.fecha, self.hora,self.placa,self.cliente,self.origen,self.destino,self.usuarios)

