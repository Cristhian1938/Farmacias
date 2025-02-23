# Generated by Django 5.1.5 on 2025-01-28 00:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmaciasS', '0002_delete_detallepedido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='fecha_pedido',
            new_name='fecha_creacion',
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='opcion_entrega',
            field=models.CharField(choices=[('retiro', 'Retiro en sucursal'), ('envio', 'Envío a sucursal')], default='retiro', max_length=20),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='FarmaciasS.cliente'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En proceso'), ('enviado', 'Enviado'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=15),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='sucursal_destino',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pedidos_destino', to='FarmaciasS.sucursal'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='sucursal_origen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pedidos_origen', to='FarmaciasS.sucursal'),
        ),
        migrations.CreateModel(
            name='PedidoInventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('inventario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FarmaciasS.inventario')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FarmaciasS.pedido')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='inventarios',
            field=models.ManyToManyField(through='FarmaciasS.PedidoInventario', to='FarmaciasS.inventario'),
        ),
    ]
