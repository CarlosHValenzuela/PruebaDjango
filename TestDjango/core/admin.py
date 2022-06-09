from django.contrib import admin
from .models import Carrito, Cliente, Pedidos
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Carrito)
admin.site.register(Pedidos)
