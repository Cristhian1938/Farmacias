# Generated by Django 5.1.5 on 2025-01-28 01:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmaciasS', '0005_entrega'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrega',
            name='sucursal_origen',
        ),
        migrations.AlterField(
            model_name='entrega',
            name='sucursal_destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FarmaciasS.sucursal'),
        ),
    ]
