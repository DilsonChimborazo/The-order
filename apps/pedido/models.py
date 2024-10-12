from django.db import models

# Create your models here.

class Pedidos(models.Model):
    estados=[('En espera', 'En espera'),
            ('En preparación', 'En preparación'),
            ('Terminado', 'Terminado')
            ]
    llevar=[('si', 'si'),
            ('no', 'no')
            ]
    nombre_Pedido = models.CharField(max_length=100)
    para_llevar = models.CharField(max_length=10, choices=llevar, default='no')
    estado = models.CharField(max_length=20, choices=estados, default='En espera')
    
    def __str__(self):
        return self.nombre_Pedido
