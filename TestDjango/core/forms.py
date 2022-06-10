from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import *

class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields = ['id_Cliente','nom_Usuario','pass_Usuario','email_Usuario','dir_usuario']

class CarritoForm(ModelForm):
    class Meta:
        model = Carrito
        fields = ['nombreProducto','precioProducto','cantidadProducto']

class Pedidos(ModelForm):
    class Meta:
        model = Pedidos
        fields = ['idProducto','direccion','diasTranscurridos','nombreProducto','nom_Usuario','precioProducto','cantidadProducto']

class MetodoPagoForm(ModelForm):
    class Meta:
        model = MetodoPago
        fields = ['nombreTitular','numeroTarjeta','ccvTarjeta','fecha_ven']