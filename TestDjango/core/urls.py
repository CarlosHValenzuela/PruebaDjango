from django.urls import path
from .views import *


urlpatterns =[
    path('', PaginaPrincipal,name="home"),
    path('Pedido',Pedido,name="Pedido"),
    path('InicioSesion',InicioSesion,name="InicioSesion"),
    path('Form-Carrito',FormCarrito,name="Form_Carrito"),
    path('Form-Registrate',FormRegistrate,name="Form_Registrate"),
    path('MetodoPago',MetodoPago,name="MetodoPago"),
    path('Suscribirte',Suscribirte,name="Suscribirte"),
    path('Registro',Registro,name="Registro"),
    path('Usuario',Usuario,name="Usuario"),
]