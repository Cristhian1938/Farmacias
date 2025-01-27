from django.contrib import admin
from .models import *

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion', 'telefono']
    search_fields = ['nombre']
    list_filter = ['nombre']

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio']
    search_fields = ['nombre']
    list_filter = ['nombre']

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ['sucursal', 'medicamento', 'cantidad']
    list_filter = ['sucursal']


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'direccion', 'telefono']
    search_fields = ['usuario']
    list_filter = ['usuario']


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'fecha_pedido', 'sucursal_origen', 'sucursal_destino', 'estado']
    search_fields = ['cliente']
    list_filter = ['cliente']


