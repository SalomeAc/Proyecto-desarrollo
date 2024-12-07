from django.db import models
from categorias.models import Categoria


    
class Producto(models.Model):
    
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_cid', verbose_name="Categoría")
    estado_producto=models.BooleanField(verbose_name="Disponible")
    nombre=models.CharField(max_length=30)
    precio= models.DecimalField(max_digits=10, decimal_places=2)
    descripcion=models.CharField(max_length=50, verbose_name="Descripción")
    foto_producto=models.ImageField(upload_to='productos/', null=True, blank=True, verbose_name="Foto del producto")
    cantidad_producto=models.IntegerField(verbose_name="Cantidad")
    
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        
    def __str__(self):
        return self.nombre
    

    
 

