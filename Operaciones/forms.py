from django import forms
from .models import Clientes, Operaciones, Tarifa, TiposCar, UsuarioEmpresa, Zona, Conductores, Propietarios, Placas

class ZonasForm(forms.ModelForm):

    class Meta: 
        model = Zona

        fields=[
            'zona'
        ]
        labels= {
            'zona' : 'Zona'
        }
        widgets ={
            'zona':forms.TextInput(attrs={'class':'form-control'})
        }

class PlacasForm(forms.ModelForm):

    class Meta: 
        model = Placas

        fields=[
            'placa',
            'tipo_carro',
            'capacidad',
            'id_propietario',
            'conductor'
        ]
        labels= {
            'placa' : 'Placa',
            'tipo_carro':'Tipo de Vehiculo',
            'capacidad' : 'Capacidad de Pasajeros',
            'id_propietario' : 'Propietario',
            'conductor' : 'Conductor Asignado'
        }
        widgets ={
            'placa':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_carro':forms.Select(attrs={'class':'form-control'}),
            'capacidad':forms.NumberInput(attrs={'class':'form-control'}),
            'id_propietario':forms.Select(attrs={'class':'form-control'}),
            'conductor':forms.Select(attrs={'class':'form-control'})       
        }
    def __init__(self, user, *args, **kwargs):
        super(PlacasForm, self).__init__(*args, **kwargs)
        # Filtrar los propietarios por la empresa del usuario conectado
        self.fields['id_propietario'].queryset = Propietarios.objects.filter(empresa=user.empresa)
        self.fields['conductor'].queryset = Conductores.objects.filter(empresa=user.empresa)

class ConductoresForm(forms.ModelForm):

    class Meta:
        model = Conductores

        fields=[
            'cedula',
            'nombre',
            'email',
            'telefono'
        ]
        labels= {
            'cedula': 'Numero de Cedula',
            'nombre': 'Nombre y Apellido',
            'email': 'Email',
            'telefono':'Telefono'
        }
        widgets ={
            'cedula': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'})
        }

class PropietariosForm(forms.ModelForm):

    class Meta:
        model = Propietarios

        fields=[
            'nombre',
            'nit',
            'email',
            'telefono'
        ]
        labels= {
            'nombre': 'Nombre y Apellido',
            'nit':'Nit',
            'email': 'Email',
            'telefono':'Telefono'
        }
        widgets ={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'nit' : forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'})
        }




class TarifasForm(forms.ModelForm):

    class Meta:
        model = Tarifa

        fields=[
            'codigo',
            'Cliente',
            'zona',
            'origendestino',
            'tipo_carro',
            'valor_cobrar',
            'valor_pagar',
            'comentarios',
            'estado'
        
        ]
        labels= {
           'codigo':'Codigo Tarifa',
            'Cliente':'Cliente',
            'zona':'Zona',
            'origendestino':'Origen o Destino del Servicio',
            'tipo_carro':'Tipo de Vehiculo',
            'valor_cobrar': 'Valor Tarifa',
            'valor_pagar': 'Costo del Servicio',
            'comentarios': 'Observaciones',
            'estado' : 'Estado'

        }
        widgets ={
            'codigo':forms.TextInput(attrs={'class':'form-control'}),
            'Cliente':forms.Select(attrs={'class':'form-control'}),
            'zona':forms.Select(attrs={'class':'form-control'}),
            'origendestino':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_carro':forms.Select(attrs={'class':'form-control'}),
            'valor_cobrar':forms.NumberInput(attrs={'class':'form-control'}),
            'valor_pagar':forms.NumberInput(attrs={'class':'form-control'}),
            'comentarios':forms.Textarea(attrs={'class':'form-control'}),
            'estado' : forms.CheckboxInput(attrs={'class':'form-control'})
        }
    def __init__(self, user, *args, **kwargs):
        super(TarifasForm, self).__init__(*args, **kwargs)
        # Filtrar las Tarifas, tipo carro y cliente por la empresa del usuario conectado
        self.fields['tipo_carro'].queryset = TiposCar.objects.filter(empresa=user.empresa)
        self.fields['Cliente'].queryset = Clientes.objects.filter(empresa=user.empresa)
        self.fields['zona'].queryset = Zona.objects.filter(empresa=user.empresa)

class TiposCarForm(forms.ModelForm):
    class Meta:
        model=TiposCar

        fields=[
            'tipo_carro',
            'observacion'
        ]
        labels={
            'tipo_carro':'Tipo de Vehiculo',
            'observacion':'Observacion'

        }
        widgets={
            'tipo_carro':forms.TextInput(attrs={'class':'form-control'}),
            'observacion':forms.Textarea(attrs={'class':'form-control'}),

        }

class ClientesForm(forms.ModelForm):

    class Meta:
        model= Clientes

        fields=[
            'nit',
            'nombre',
            'email',
            'contacto',
            'telefono'

        ]

        labels = {
            'nit':'Nit',
            'nombre':'Nombre',
            'email':'Email',
            'contacto':'Persona de Contacto',
            'telefono':'Telefono'

        }

        widgets={
            'nit':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'contacto':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'})
        }

class OperacionesForm(forms.ModelForm):

    class Meta:
        model = Operaciones

        fields=[
            'fecha',
            'hora',
            'tipo_servicio',
            'cliente',
            'zona',
            'placa',
            'origen',
            'destino',
            'usuarios',
            'comentario'
        ]
        labels = {
            'fecha':'Fecha',
            'hora':'Hora',
            'tipo_servicio':'Tipo Servicio',
            'cliente':'Cliente',
            'zona':'Zona',
            'placa':'Placa',
            'origen':'Origen',
            'destino': 'Destino',
            'usuarios': 'Usuarios',
            'comentario':'Observaciones del Servicio'
        }
        widgets ={
            'fecha': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'hora': forms.TimeInput (attrs={'class':'form-control','type':'time'}),
            'tipo_servicio': forms.Select(attrs={'class':'form-control'}),
            'cliente': forms.Select(attrs={'class':'form-control'}),
            'zona': forms.Select(attrs={'class':'form-control'}),
            'placa': forms.Select(attrs={'class':'form-control'}),
            'origen': forms.TextInput(attrs={'class':'form-control'}),
            'destino': forms.TextInput(attrs={'class':'form-control'}),
            'usuarios': forms.Textarea(attrs={'class':'form-control'}),
            'comentario': forms.Textarea(attrs={'class':'form-control'})
        }
    
    def __init__(self, user, *args, **kwargs):
        super(OperacionesForm, self).__init__(*args, **kwargs)
        # Filtrar los propietarios por la empresa del usuario conectado
        self.fields['placa'].queryset = Placas.objects.filter(empresa=user.empresa)
        self.fields['cliente'].queryset = Clientes.objects.filter(empresa=user.empresa)
        self.fields['zona'].queryset = Zona.objects.filter(empresa=user.empresa)
