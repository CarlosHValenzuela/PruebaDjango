# Generated by Django 4.0.1 on 2022-06-03 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_Cliente', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de cliente')),
                ('nom_Usuario', models.CharField(max_length=100, verbose_name='Nombre de usuario')),
                ('pass_Usuario', models.CharField(max_length=50, verbose_name='PassWord de usuario')),
                ('email_Usuario', models.CharField(max_length=100, verbose_name='Correo del usuario')),
                ('dir_Usuario', models.CharField(max_length=100, verbose_name='Dirrecion del usuario')),
            ],
        ),
    ]
