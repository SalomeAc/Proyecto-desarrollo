# Generated by Django 4.2.14 on 2024-10-11 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=10, verbose_name='Nombre de la categoría')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo_pago', models.CharField(max_length=30, verbose_name='Método de pago')),
                ('monto_pedido', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cantidad pedida')),
                ('hora', models.TimeField(auto_now_add=True)),
                ('estado_pedido', models.BooleanField(verbose_name='Envíado')),
                ('fecha', models.DateField()),
            ],
            options={
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('tfno', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('contrasena', models.CharField(max_length=10, verbose_name='Contraseña')),
                ('foto', models.ImageField(null=True, upload_to='usuarios/', verbose_name='Foto de perfil')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_producto', models.BooleanField(verbose_name='Disponible')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción')),
                ('foto_producto', models.ImageField(blank=True, null=True, upload_to='productos/', verbose_name='Foto del producto')),
                ('cantidad_producto', models.IntegerField(verbose_name='Cantidad')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_cid', to='gestion.categoria', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
        migrations.CreateModel(
            name='PedidoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_producto_carrito', models.IntegerField()),
                ('pedido_ppid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.pedido')),
                ('producto_ppid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.producto')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='productos',
            field=models.ManyToManyField(through='gestion.PedidoProducto', to='gestion.producto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario_pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_pid', to='gestion.usuario', verbose_name='Id del usuario'),
        ),
        migrations.CreateModel(
            name='CarritoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_producto_carrito', models.IntegerField()),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.carrito_compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.producto')),
            ],
        ),
        migrations.AddField(
            model_name='carrito_compra',
            name='productos',
            field=models.ManyToManyField(through='gestion.CarritoProducto', to='gestion.producto'),
        ),
    ]
