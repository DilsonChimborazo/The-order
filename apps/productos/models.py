from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    precio =models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nombre
    