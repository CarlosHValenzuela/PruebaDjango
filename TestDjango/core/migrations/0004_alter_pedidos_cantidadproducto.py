# Generated by Django 4.0.4 on 2022-06-09 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_metodopago_pedidos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='cantidadProducto',
            field=models.IntegerField(max_length=6, verbose_name='Cantidad'),
        ),
    ]
