from django.db import models
from apps.pedido.models import Pedidos
from apps.productos.models import Productos

# Create your models here.
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Productos, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    observaciones = models.TextField(null=True)

    def __str__(self):
        return self.pedido