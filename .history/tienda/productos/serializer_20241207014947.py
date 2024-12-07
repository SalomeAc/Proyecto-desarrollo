from rest_framework import serializers
from .models import Categoria, Producto
from django.contrib.auth.models import User


        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields= '__all__'
        
        

        
