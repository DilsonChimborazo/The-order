from django.db import models

class Pedido(models.Model):
        nombre_pedido = models.CharField(max_length=100)
        para_llevar = models.CharField(max_length=20, choices=[
                ('si', 'si'),
                ('no', 'no')
        ], default='no')
        estado = models.CharField(max_length=20, choices=[
                ('En espera', 'En espera'),
                ('En preparación', 'En preparación'),
                ('Terminado', 'Terminado')
        ], default='En espera')

        def __str__(self):
                return self.nombre_pedido

