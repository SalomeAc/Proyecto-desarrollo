# Generated by Django 4.2.16 on 2024-11-29 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion', '0004_alter_categoria_nombre_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='usuarios',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_pid', to=settings.AUTH_USER_MODEL, verbose_name='Id del usuario'),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
