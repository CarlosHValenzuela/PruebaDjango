from dataclasses import field
from django import forms
from django.forms import ModelForm
from .models import Cliente,Carrito

class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields = ['id_Cliente','nom_Usuario','pass_Usuario','email_Usuario','dir_usuario']

class CarritoForm(ModelForm):
    class Meta:
        model = Carrito
        fields = ['dir_Carrito','precio_Carrito']