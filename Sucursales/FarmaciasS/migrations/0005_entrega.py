# Generated by Django 5.1.5 on 2025-01-28 01:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmaciasS', '0004_remove_pedido_fecha_actualizacion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('fecha_entrega', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FarmaciasS.cliente')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FarmaciasS.medicamento')),
                ('sucursal_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entregas_destino', to='FarmaciasS.sucursal')),
                ('sucursal_origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entregas_origen', to='FarmaciasS.sucursal')),
            ],
            options={
                'verbose_name': 'Entrega',
                'verbose_name_plural': 'Entregas',
            },
        ),
    ]
