from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *



@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion', 'telefono']
    search_fields = ['nombre']
    list_filter = ['nombre']

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

class PedidoInventarioInline(admin.TabularInline):
    model = PedidoInventario
    extra = 1

@receiver(post_save, sender=PedidoInventario)
def restar_inventario(sender, instance, **kwargs):
    inventario = instance.inventario
    inventario.cantidad -= instance.cantidad
    inventario.save()

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id','sucursal_pedido', 'sucursal_destino', 'estado', 'fecha_creacion',)  # Cambiado de sucursal_origen a sucursal_pedido
    inlines = [PedidoInventarioInline]

@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'medicamento', 'cantidad')
    actions = ['realizar_entrega_desde_admin']
    fields = ('cliente', 'medicamento', 'cantidad', 'opcion_entrega')  # Solo muestra estos campos

    def realizar_entrega_desde_admin(self, request, queryset):
        for entrega in queryset:
            try:
                # Obtener inventario de la sucursal de destino (la sucursal donde se realiza la entrega)
                inventario_destino = Inventario.objects.get(
                    sucursal=entrega.sucursal_destino,  # Sucursal de destino
                    medicamento=entrega.medicamento
                )

                # Verificar si hay suficiente inventario en la sucursal de destino
                if inventario_destino.cantidad >= entrega.cantidad:
                    # Restar la cantidad del inventario de destino
                    inventario_destino.cantidad -= entrega.cantidad
                    inventario_destino.save()  # Guardar los cambios en el inventario de la sucursal de destino

                    # Crear la entrega
                    entrega.save()

                    # Marcar entrega como realizada (opcional: podrías añadir un campo para esto)
                    self.message_user(
                        request, f"Entrega realizada exitosamente: {entrega.id}"
                    )
                else:
                    self.message_user(
                        request,
                        f"No hay suficiente inventario en la sucursal de destino para la entrega {entrega.id}.",
                        level='error'
                    )
            except Inventario.DoesNotExist:
                self.message_user(
                    request,
                    f"El medicamento {entrega.medicamento} no está disponible en la sucursal de destino para la entrega {entrega.id}.",
                    level='error'
                )

    realizar_entrega_desde_admin.short_description = "Realizar entrega para las entregas seleccionadas"



