from django.db import models

# Create your models here.
class CarritoProducto(models.Model):
   
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto_carrito=models.IntegerField()
