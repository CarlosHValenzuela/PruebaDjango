from django.db import models

# Create your models here.


class Cliente(models.Model):
    id_Cliente =models.IntegerField(primary_key=True, verbose_name='Id de cliente')
    nom_Usuario =models.CharField(max_length=100, verbose_name='Nombre de usuario')
    pass_Usuario =models.CharField(max_length=50, verbose_name='PassWord de usuario')
    email_Usuario =models.CharField(max_length=100, verbose_name='Correo del usuario')
    dir_usuario =models.CharField(max_length=110, verbose_name='Dirrecion del usuario')

    def __str__(self):
        return self.nom_Usuario


class Carrito(models.Model):
    dir_Carrito =models.CharField(max_length=150,verbose_name='Dirrecion del Carrito')
    precio_Carrito =models.CharField(max_length=100, verbose_name='Precio del Carrito')

    def __str__(self):
        return self.dir_Carrito