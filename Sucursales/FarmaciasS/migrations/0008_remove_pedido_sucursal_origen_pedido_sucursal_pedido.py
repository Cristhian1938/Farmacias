# Generated by Django 5.1.5 on 2025-01-28 01:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmaciasS', '0007_remove_pedido_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='sucursal_origen',
        ),
        migrations.AddField(
            model_name='pedido',
            name='sucursal_pedido',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pedidos_pedido', to='FarmaciasS.sucursal'),
        ),
    ]
