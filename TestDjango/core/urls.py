from django.urls import path
from .views import Registro,Pedido,InicioSesion,Carrito,Registrate,MetodoPago,Suscribirte

urlpatterns =[
    path('', Registro,name="home"),
    path('Pedido',Pedido,name="Pedido"),
    path('InicioSesion',InicioSesion,name="InicioSesion"),
    path('Carrito',Carrito,name="Carrito"),
    path('Registrate',Registrate,name="Registrate"),
    path('MetodoPago',MetodoPago,name="MetodoPago"),
    path('Suscribirte',Suscribirte,name="Suscribirte"),
]