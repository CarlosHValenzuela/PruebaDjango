from django.shortcuts import render
from .forms import ClienteForm
from .models import Cliente

# Create your views here.


def Registro(request):
    return render(request,'core/Registro.html')

def Pedido(request):
    return render(request,'core/Pedido.html')

def InicioSesion(request):
    return render(request,'core/InicioSesion.html')

def Carrito(request):
    return render(request,'core/Carrito.html')

def FormRegistrate(request):
    datos = {
        'form':ClienteForm()
    }
    if request.method=='POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados Correctamente";

    return render(request,'core/FormRegistrate.html',datos)

def MetodoPago(request):
    return render(request,'core/MetodoPago.html')

def Suscribirte(request):
    return render(request,'core/Suscribirte.html')

def PaginaPrincipal(request):
    return render(request, 'core/PaginaPrincipal.html')

def Usuario(request):
    return render (request, 'core/Usuario.html')
