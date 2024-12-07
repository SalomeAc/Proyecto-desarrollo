from django.db import models
from productos.models import Producto

class Carrito_compra(models.Model):
    productos=models.ManyToManyField(Producto,through='CarritoProducto')
    id_carrito=models.CharField(max_length=10, unique=True,primary_key=True)
    cantidad_total_productos=models.IntegerField()
    monto_carrito=models.DecimalField(max_digits=10, decimal_places=2)
    
 
    


class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito_compra, on_delete=models.CASCADE)
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto_carrito=models.IntegerField()
