from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    id_usuario=models.CharField(max_length=10, primary_key=True)
    nombre=models.CharField(max_length = 30)
    direccion=models.CharField
    email=models.EmailField()
    tfno=models.CharField(max_length=10)
    contrasena=models.CharField(max_length = 10)
    foto= models.ImageField(upload_to='usuarios/', null=True, blank=True)
    
class Cliente(models.Model):
    usuario_cid = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
class Administrador(models.Model):
    reporte = models.CharField(max_length = 100)
    usuario_aid = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Pedido(models.Model):
    id_compra=models.CharField(max_length=10, primary_key=True)
    cliente_pid = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    metodo_pago=models.CharField(max_length=30)
    monto_pedido= models.DecimalField(max_digits=10, decimal_places=2)
    hora_pedido=models.TimeField(auto_now_add=True)
    estado_pedido=models.BooleanField()
    fecha_pedido =models.DateField()
    
class CarritoCompra(models.Model):
    id_carrito=models.CharField(max_length=10, primary_key=True)
    cantidad_total_productos=models.IntegerField()
    monto_carrito=models.DecimalField(max_digits=10, decimal_places=2)
    
class Categoria(models.Model):
    id_categoria=models.CharField(max_length=10, primary_key=True)
    nombre_categoria=models.CharField(max_length=10)
    descripcion_categoria=models.CharField(max_length=100)

class Producto(models.Model):
    
    id_producto=models.CharField(max_length=10, primary_key=True)
    carrito_pid = models.ForeignKey(CarritoCompra, on_delete=models.CASCADE)
    admin_pid = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    pedido_pid = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    categoria_pid = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    estado_producto=models.BooleanField()
    nombre_producto=models.CharField(max_length=30)
    precio_producto= models.DecimalField(max_digits=10, decimal_places=2)
    descripcion_producto=models.CharField(max_length=50)
    foto_producto=models.ImageField(upload_to='productos/', null=True, blank=True)
    cantidad_producto=models.IntegerField()
    
    cantidad_padmin = models.IntegerField()
    cantidad_ppedido = models.IntegerField()
    cantidad_pcarrito = models.IntegerField()
    
    
""" class ClienteProducto(models.Model):
    cliente_cpid = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto_cpid = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto_usuario=models.IntegerField()

class CarritoProducto(models.Model):
    carrito_cppid = models.ForeignKey(CarritoCompra, on_delete=models.CASCADE)
    producto_cppid = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto_carrito=models.IntegerField()
    
class PedidoProducto(models.Model):
    pedido_ppid = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto_ppid = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_producto_carrito=models.IntegerField()
     """

   

# Create your models here.
