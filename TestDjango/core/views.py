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

def Registrate(request):
    return render(request,'core/Registrate.html')

def MetodoPago(request):
    return render(request,'core/MetodoPago.html')

def Suscribirte(request):
    return render(request,'core/Suscribirte.html')
