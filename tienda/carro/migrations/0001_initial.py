# Generated by Django 5.1.1 on 2024-11-29 23:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito_compra',
            fields=[
                ('id_carrito', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('cantidad_total_productos', models.IntegerField()),
                ('monto_carrito', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='CarritoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_producto_carrito', models.IntegerField()),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carro.carrito_compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producto')),
            ],
        ),
        migrations.AddField(
            model_name='carrito_compra',
            name='productos',
            field=models.ManyToManyField(through='carro.CarritoProducto', to='products.producto'),
        ),
    ]