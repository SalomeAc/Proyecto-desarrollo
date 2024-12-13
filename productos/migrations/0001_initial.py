# Generated by Django 4.2.16 on 2024-12-07 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categorias', '0001_initial'),
    ]

    operations = [
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
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_cid', to='categorias.categoria', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
        migrations.CreateModel(
            name='ProductoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_producto', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]