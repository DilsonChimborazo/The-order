from django.db import models
from apps.pedido.models import Pedido
from apps.detalles.models import DetallePedido
from apps.Datos_restaurante.models import Configuracion

# Create your models here.
class Facturacion(models.Model):
    restaurante = models.ForeignKey(Configuracion, on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    detalle = models.ForeignKey(DetallePedido, on_delete=models.SET_NULL, null=True)

    def total_a_pagar(self):
        return self.detalle.cantidad * self.detalle.producto.precio

    def __str__(self):
        return f"Factura:{self.restaurante}, {self.pedido.nombre_pedido}, Total: {self.total_a_pagar()}"