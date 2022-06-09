from django.shortcuts import render
from .forms import ClienteForm,CarritoForm
from .models import Cliente,Carrito,metodoPago,Pedidos

# Create your views here.


def Registro(request):
    return render(request,'core/Registro.html')

def Pedido(request):
    pedidos= Pedidos.objects.all()
    datos = {
        'pedidos': pedidos
    }
    return render(request,'core/Pedido.html', datos)

def InicioSesion(request):
    return render(request,'core/InicioSesion.html')

def FormCarrito(request):
    datos = {
        'form':CarritoForm()
    }
    if request.method=='POST':
        formulario = CarritoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados Correctamente"

    return render(request,'core/FormCarrito.html',datos)

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
