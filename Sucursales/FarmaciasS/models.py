from django.db import models
from django.contrib.auth.models import User

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.medicamento.nombre} - {self.sucursal.nombre}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    sucursal_pedido = models.ForeignKey('Sucursal', on_delete=models.SET_NULL, null=True, related_name='pedidos_pedido')  # Cambiado de sucursal_origen a sucursal_pedido
    sucursal_destino = models.ForeignKey('Sucursal', on_delete=models.SET_NULL, null=True, related_name='pedidos_destino')
    estado = models.CharField(
        max_length=15,
        choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En proceso'), ('enviado', 'Enviado'), ('entregado', 'Entregado')],
        default='pendiente'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    opcion_entrega = models.CharField(
        max_length=20,
        choices=[('retiro', 'Retiro en sucursal'), ('envio', 'Envío a sucursal')],
        default='retiro'
    )

    def __str__(self):
        return f"Pedido {self.id} - {self.sucursal_pedido.nombre} a {self.sucursal_destino.nombre}"


class PedidoInventario(models.Model):
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    inventario = models.ForeignKey('Inventario', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.inventario.medicamento.nombre} ({self.inventario.sucursal.nombre}) x{self.cantidad} (Pedido {self.pedido.id})"

class Entrega(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    medicamento = models.ForeignKey('Medicamento', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    sucursal_destino = models.ForeignKey('Sucursal', on_delete=models.CASCADE)
    fecha_entrega = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Entrega de {self.medicamento.nombre} a {self.cliente.nombre}"

    def save(self, *args, **kwargs):
        # Lógica para restar inventario de la sucursal de destino
        try:
            inventario_destino = Inventario.objects.get(
                sucursal=self.sucursal_destino,
                medicamento=self.medicamento
            )

            # Verificar si hay suficiente inventario
            if inventario_destino.cantidad >= self.cantidad:
                inventario_destino.cantidad -= self.cantidad
                inventario_destino.save()
            else:
                raise ValueError("No hay suficiente inventario en la sucursal de destino.")

        except Inventario.DoesNotExist:
            raise ValueError(f"El medicamento {self.medicamento.nombre} no está disponible en la sucursal de destino.")

        # Guardar la entrega
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Entrega"
        verbose_name_plural = "Entregas"



