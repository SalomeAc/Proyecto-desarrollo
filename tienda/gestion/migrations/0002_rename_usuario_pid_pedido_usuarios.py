# Generated by Django 4.2.14 on 2024-10-11 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='usuario_pid',
            new_name='usuarios',
        ),
    ]
