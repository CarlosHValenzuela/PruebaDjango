# Generated by Django 4.0.4 on 2022-06-09 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=150,verbose_name='Nombre del producto')),
                ('precioProducto', models.CharField(max_length=6, verbose_name='Precio del producto')),
                ('cantidadProducto', models.CharField(max_length=6, verbose_name='Cantidad')),
            ],
        ),
    ]
