# Generated by Django 4.2.16 on 2024-11-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_remove_pedido_monto_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre_categoria',
            field=models.CharField(max_length=30, verbose_name='Nombre de la categoría'),
        ),
    ]
