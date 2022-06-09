# Generated by Django 4.0.4 on 2022-06-09 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_carrito'),
    ]

    operations = [
        migrations.CreateModel(
            name='metodoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debito', models.CharField(max_length=150, verbose_name='Debito')),
                ('credito', models.CharField(max_length=150, verbose_name='Credito')),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id del producto')),
                ('direccion', models.CharField(max_length=150, verbose_name='Direccion del producto')),
                ('diasTranscurridos', models.IntegerField(max_length=6, verbose_name='Dias transcurridos')),
                ('nombreProducto', models.CharField(max_length=150, verbose_name='Nombre del producto')),
                ('nom_Usuario', models.CharField(max_length=100, verbose_name='Nombre de usuario')),
                ('precioProducto', models.IntegerField(max_length=6, verbose_name='Precio del producto')),
                ('cantidadProducto', models.IntegerField(max_length=6, verbose_name='Precio del producto')),
            ],
        ),
    ]
