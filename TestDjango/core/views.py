from django.shortcuts import render


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
    return render(request,'core/FormRegistrate.html')

def MetodoPago(request):
    return render(request,'core/MetodoPago.html')

def Suscribirte(request):
    return render(request,'core/Suscribirte.html')

def PaginaPrincipal(request):
    return render(request, 'core/PaginaPrincipal.html')
