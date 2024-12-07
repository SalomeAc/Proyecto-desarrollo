from rest_framework import serializers
from .models import Categoria, Producto
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ['id','username','email','password']


        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields= '__all__'
        
        

        
