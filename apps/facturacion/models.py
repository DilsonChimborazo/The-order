from django.db import models
from apps.pedido.models import Pedido
from apps.productos.models import Producto

# Create your models here.
class Facturacion(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.pedido}Total a pagar:{self.cantidad * self.producto}"