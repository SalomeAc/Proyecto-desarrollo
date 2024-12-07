from django.db import models
from productos.models import Producto

# Create your models here.
class CarritoProducto(models.Model):
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto=models.IntegerField()
